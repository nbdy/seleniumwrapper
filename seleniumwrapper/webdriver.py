from selenium.webdriver import Firefox, FirefoxProfile, FirefoxOptions, Chrome, ChromeOptions
from .configuration import Configuration
from .loader import Loader


class WebDriver(object):
    FIREFOX_DRIVER_NAMES = ["f", "firefox"]
    CHROME_DRIVER_NAMES = ["c", "chrome", "chromium"]

    @staticmethod
    def get_default():
        return WebDriver.build(Configuration())

    @staticmethod
    def build(cfg, fetch_driver=True):
        if cfg.driver in WebDriver.FIREFOX_DRIVER_NAMES:
            d = Firefox
            o = FirefoxOptions()
            p = FirefoxProfile()
            p.set_preference("general.useragent.override", cfg.user_agent)
            if cfg.proxy is not None:
                p.set_preference("network.proxy.type", 1)
                p.set_preference("network.proxy.socks_version", cfg.proxy.version)
                p.set_preference("network.proxy.socks_remote_dns", True)
                p.set_preference("network.proxy.socks", cfg.proxy.host)
                p.set_preference("network.proxy.socks_port", cfg.proxy.port)
                p.update_preferences()
        elif cfg.driver in WebDriver.CHROME_DRIVER_NAMES:
            d = Chrome
            o = ChromeOptions()
            o.add_argument("user-agent={0}".format(cfg.user_agent))
            if cfg.proxy is not None:
                o.add_argument("--proxy-server={0}".format(cfg.proxy.for_chrome()))
            p = None
        else:
            raise NotImplementedError

        if fetch_driver:
            Loader.fetch(cfg.executable_path, cfg.debug, cfg.driver)

        o.binary_location = cfg.executable_path
        o.set_headless(cfg.headless)

        if cfg.driver in WebDriver.FIREFOX_DRIVER_NAMES:
            return d(p, options=o, firefox_binary=cfg.binary)
        elif cfg.driver in WebDriver.CHROME_DRIVER_NAMES:
            return d(options=o)
