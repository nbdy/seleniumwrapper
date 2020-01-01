from os import system, makedirs
from os.path import isfile, isdir
from sys import platform


class Loader(object):
    class WebDriver(object):
        KEYS = ["linux", "windows", "mac"]

        linux = None
        windows = None
        mac = None

    # https://chromedriver.storage.googleapis.com/index.html
    class Chrome(WebDriver):
        linux = "https://chromedriver.storage.googleapis.com/80.0.3987.16/chromedriver_linux64.zip"
        windows = "https://chromedriver.storage.googleapis.com/80.0.3987.16/chromedriver_win32.zip"
        mac = "https://chromedriver.storage.googleapis.com/80.0.3987.16/chromedriver_mac64.zip"

    drivers = [Chrome]

    # todo method to get drivers by their latest version
    @staticmethod
    def get_for_current_os():
        if platform.startswith("linux"):
            return [Loader.Chrome.linux]
        elif platform.startswith("win"):
            return [Loader.Chrome.windows]
        elif platform.startswith("mac"):
            return [Loader.Chrome.mac]

    @staticmethod
    def download(path, url):
        if not isdir(path):
            makedirs(path)
        z = url.split("/")[-1]
        dn = z.split(".")[0].split("_")[0]
        if not isfile(path + dn):
            c = "cd " + path + ";wget " + url + " >/dev/null 2>&1;unzip " + z + ";rm " + z
            system(c)
            print("downloaded", z, "to ." + path, dn)

    @staticmethod
    def fetch():
        system('if [ ! -d "driver" ]; then mkdir driver/; fi')
        for u in Loader.get_for_current_os():
            Loader.download("driver/", u)

    @staticmethod
    def fetch_all():
        for driver in Loader.drivers:
            for k in driver.KEYS:
                Loader.download("driver/", driver.__dict__[k])
