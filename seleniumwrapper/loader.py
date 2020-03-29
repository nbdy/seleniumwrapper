from os import system, makedirs, chdir
from os.path import isfile, isdir
from sys import platform
from urllib.request import urlretrieve
from subprocess import check_output


class NotSupportedError(Exception):
    @staticmethod
    def throw(exe, version, supported):
        raise NotSupportedError("version '{0}' of '{1}' is either too old or not supported.\n"
                                "currently supported versions:\n\t"
                                "{2}".format(version, exe, supported))


class WebDriver(object):
    exe = None
    os_name = None

    SUPPORTED_VERSIONS = {}

    def get_version(self):
        raise NotImplementedError

    def _get_version(self):
        return check_output([self.exe, "--version"])  # works for chromium and firefox

    def is_supported(self):
        return self.get_version() in self.SUPPORTED_VERSIONS.keys()

    def get_url(self):
        if self.is_supported():
            return self.SUPPORTED_VERSIONS.get(self.get_version()) % self.os_name
        else:
            NotSupportedError.throw(self.exe, self.get_version(), ', '.join(self.SUPPORTED_VERSIONS.keys()))

    @staticmethod
    def decompress(fp, debug=False):  # decompression currently just works under linux
        if platform.startswith("win"):
            raise NotSupportedError.throw("windows", "", "none")
        dc = None
        if fp.endswith(".tar.gz"):
            dc = "tar xf"
        elif fp.endswith(".zip"):
            dc = "unzip"
        cmd = dc + " " + fp
        if not debug:
            cmd += " >/dev/null 2>&1"
        if debug:
            print("executing '{0}'".format(cmd))
        system(cmd)

    def fetch(self, path, debug=False):
        url = self.get_url()
        if not path.endswith("/"):
            path += "/"
        if not isdir(path):
            makedirs(path)
            if debug:
                print("created directory '{0}'".format(path))
        z = url.split("/")[-1]
        dn = z.split("-")[0]
        if not isfile(path + dn):
            chdir(path)
            if debug:
                print("downloading '{0}' to '{1}'".format(url, z))
            urlretrieve(url, z)
            if debug:
                print("decompressing '{0}'".format(z))
            self.decompress(z, debug)
            if not debug:
                system("rm {0}".format(z))
            chdir("..")


# https://chromedriver.storage.googleapis.com/index.html
class Chrome(WebDriver):
    exe = "chromium"

    _79_0_3945_16 = "https://chromedriver.storage.googleapis.com/79.0.3945.16/chromedriver_%s.zip"
    _78_0_3904_70 = "https://chromedriver.storage.googleapis.com/78.0.3904.70/chromedriver_%s.zip"
    _78_0_3904_11 = "https://chromedriver.storage.googleapis.com/78.0.3904.11/chromedriver_%s.zip"
    _78_0_3904_105 = "https://chromedriver.storage.googleapis.com/78.0.3904.105/chromedriver_%s.zip"
    _79_0_3945_36 = "https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_%s.zip"
    _80_0_3987_16 = "https://chromedriver.storage.googleapis.com/80.0.3987.16/chromedriver_%s.zip"

    SUPPORTED_VERSIONS = {
        "79_0_3945_16": _79_0_3945_16,
        "78_0_3904_70": _78_0_3904_70,
        "78_0_3904_11": _78_0_3904_11,
        "78_0_3904_105": _78_0_3904_105,
        "79_0_3945_36": _79_0_3945_36,
        "80_0_3987_16": _80_0_3987_16
    }

    decompressor = "unzip"

    def get_version(self):
        return str(self._get_version().split()[1].replace(b".", b"_"))


class ChromeLinux(Chrome):
    os_name = "linux64"


class ChromeWindows(Chrome):
    os_name = "win32"


class ChromeMac(Chrome):
    os_name = "mac64"


# https://github.com/mozilla/geckodriver/releases
class FireFox(WebDriver):
    exe = "firefox"
    decompressor = "tar xf"

    SUPPORTED_VERSIONS = {
        "60": "https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-%s"
    }

    def get_version(self):
        return self._get_version().split()[2].split(b'.')[0]

    def is_supported(self):
        for k in self.SUPPORTED_VERSIONS:
            if int(self.get_version()) > int(k):
                return True
        return False

    def get_url(self):
        if self.is_supported():
            for k in self.SUPPORTED_VERSIONS:
                if int(self.get_version()) > int(k):
                    return self.SUPPORTED_VERSIONS[k] % self.os_name
        else:
            raise NotSupportedError.throw(self.exe, self.get_version(), ', '.join(self.SUPPORTED_VERSIONS.keys()))


class FireFoxLinux(FireFox):
    os_name = "linux64.tar.gz"


class FireFoxWindows(FireFox):
    os_name = "win64.zip"


class FireFoxMac(FireFox):
    os_name = "macos.tar.gz"


class WebDrivers(object):
    WINDOWS = [FireFoxWindows, ChromeWindows]
    LINUX = [FireFoxLinux, ChromeLinux]
    MAC = [FireFoxMac, ChromeMac]

    @staticmethod
    def get_for_os(os):
        if os.startswith("linux"):
            return WebDrivers.LINUX
        elif os.startswith("win"):
            return WebDrivers.WINDOWS
        elif os.startswith("mac"):
            return WebDrivers.MAC

    @staticmethod
    def get_for_current_os():
        return WebDrivers.get_for_os(platform)


class Loader(object):
    @staticmethod
    def fetch(path="driver", debug=False, driver=None):
        for wd in WebDrivers.get_for_current_os():
            if driver is None:
                wd().fetch(path, debug)
            else:
                if wd.exe.startswith(driver):
                    wd().fetch(path, debug)
        if debug:
            print("done fetching")
