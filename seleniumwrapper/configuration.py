from user_agent import generate_navigator_js


class IProxy(object):
    host = None
    http_port = None
    ssl_port = None
    socks_port = None
    socks_version = None

    def __init__(self, host, http, ssl, socks, socks_version=5):
        """
        initializes IProxy object
        :param host: str
        :param http: http proxy port
        :param ssl: ssl proxy port
        :param socks: socks proxy port
        :param socks_version: socks proxy version
        """
        self.host = host
        self.http_port = http
        self.ssl_port = ssl
        self.socks_port = socks
        self.socks_version = socks_version

    def update_preferences(self, profile):
        """
        updates profile preferences with proxy settings
        :param profile: selenium profile
        :return: updated profile
        """
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http", self.host)
        profile.set_preference("network.proxy.http_port", self.http_port)
        profile.set_preference("network.proxy.ssl", self.host)
        profile.set_preference("network.proxy.ssl_port", self.ssl_port)
        profile.update_preferences()
        return profile

    def create_options(self):
        """
        creates selenium-wire options
        :return: dict
        """
        return {
            'connection_timeout': 42,
            'proxy': {
                'http': "http://{0}:{1}".format(self.host, self.http_port),
                'https': "https://{0}:{1}".format(self.host, self.ssl_port),
                'no_proxy': "localhost,127.0.0.1"
            },
            'verify_ssl': False,
            'suppress_connection_errors': False
        }


class Configuration(object):
    headless = True
    driver = None
    executable_path = None
    user_agent = None
    debug = False
    binary = None
    proxy = None
    profile = None

    def __init__(self, driver="firefox", executable_path="driver/geckodriver",
                 user_agent=generate_navigator_js()["userAgent"], headless=True, debug=False,
                 binary="/usr/bin/firefox", proxy=None, profile=None):
        """
        initializes Configuration object
        :param driver: str webdriver name (default=firefox)
        :param executable_path: str path to webdriver executable (default=driver/geckodriver)
        :param user_agent: user-agent to use (default=random)
        :param headless: bool (default=True)
        :param debug: bool (default=False)
        :param binary: str path to browser binary (default=/usr/bin/firefox)
        :param proxy: IProxy object (default=None) optional
        :param profile: Profile name (default=None) optional
        """
        self.driver = driver
        self.executable_path = executable_path
        self.user_agent = user_agent
        self.headless = headless
        self.debug = debug
        self.binary = binary
        self.proxy = proxy
        self.profile = profile
