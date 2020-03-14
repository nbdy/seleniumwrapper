from user_agent import generate_navigator_js


class IProxy(object):
    host = None
    http_port = None
    ssl_port = None
    socks_port = None
    socks_version = None

    def __init__(self, host, http, ssl, socks, socks_version=5):
        self.host = host
        self.http_port = http
        self.ssl_port = ssl
        self.socks_port = socks
        self.socks_version = socks_version

    def update_preferences(self, profile):
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http", self.host)
        profile.set_preference("network.proxy.http_port", self.http_port)
        profile.set_preference("network.proxy.ssl", self.host)
        profile.set_preference("network.proxy.ssl_port", self.ssl_port)
        profile.update_preferences()
        return profile


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
