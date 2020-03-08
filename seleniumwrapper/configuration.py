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

    def __init__(self, type, host, port, version):
        self.type = type
        self.host = host
        self.port = port
        self.version = version

    @staticmethod
    def socks(host, port, version=5):
        return Proxy(ProxyTypes.SOCKS, host, port, version)

    def set_proxy(self, proxy_obj):
        addr = "{0}:{1}".format(self.host, self.port)
        if self.type == ProxyTypes.SOCKS:
            proxy_obj.socks_proxy = addr
        elif self.type == ProxyTypes.HTTP:
            proxy_obj.http_proxy = addr
        elif self.type == ProxyTypes.SSL:
            proxy_obj.ssl_proxy = addr
        return proxy_obj

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
