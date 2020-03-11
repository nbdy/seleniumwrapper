from user_agent import generate_navigator_js


class ProxyTypes:
    SOCKS = 0
    HTTP = 1
    SSL = 2


class Proxy(object):
    type = None
    host = None
    port = None
    version = None
    remote_dns = False

    def __init__(self, _type, host, port, version, remote_dns):
        self.type = _type
        self.host = host
        self.port = port
        self.version = version
        self.remote_dns = remote_dns

    @staticmethod
    def socks(host, port, version=5, remote_dns=True):
        return Proxy(ProxyTypes.SOCKS, host, port, version, remote_dns)

    @staticmethod
    def https(host, port):
        return Proxy(ProxyTypes.SSL, host, port, None, None)

    @staticmethod
    def ssl(host, port):
        return Proxy.https(host, port)

    @staticmethod
    def http(host, port):
        return Proxy(ProxyTypes.HTTP, host, port, None, None)

    def set_proxy(self, profile):
        prefix = "network.proxy."
        profile.set_preference(prefix + ".type", 1)
        if self.type == ProxyTypes.SOCKS:
            profile.set_preference(prefix + ".socks", self.host)
            profile.set_preference(prefix + ".socks_port", self.port)
            if self.version is not None:
                profile.set_preference(prefix + ".socks_version", self.version)
        elif self.type == ProxyTypes.HTTP:
            profile.set_preference(prefix + ".http", self.host)
            profile.set_preference(prefix + ".http_port", self.port)
        elif self.type == ProxyTypes.SSL:
            profile.set_preference(prefix + ".ssl", self.host)
            profile.set_preference(prefix + ".ssl_port", self.port)
        return profile

    def for_chrome(self):
        addr = "{0}:{1}".format(self.host, self.port)
        if self.type == ProxyTypes.SOCKS:
            return "socks{0}://{1}".format(self.version, addr)
        elif self.type == ProxyTypes.HTTP:
            return "http://{0}".format(addr)
        elif self.type == ProxyTypes.SSL:
            return "https://{0}".format(addr)
        else:
            return None


class Configuration(object):
    headless = True
    driver = None
    executable_path = None
    user_agent = None
    debug = False
    binary = None
    proxy = None

    def __init__(self, driver="firefox", executable_path="driver/geckodriver",
                 user_agent=generate_navigator_js()["userAgent"], headless=True, debug=False,
                 binary="/usr/bin/firefox", proxy=None):
        self.driver = driver
        self.executable_path = executable_path
        self.user_agent = user_agent
        self.headless = headless
        self.debug = debug
        self.binary = binary
        self.proxy = proxy
