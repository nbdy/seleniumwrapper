from selenium import webdriver
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
            d = webdriver.Firefox
            o = webdriver.FirefoxOptions()
            if cfg.profile is None:
                p = webdriver.FirefoxProfile()
            else:
                p = webdriver.FirefoxProfile(cfg.profile)
            p.set_preference("general.useragent.override", cfg.user_agent)
            if cfg.proxy is not None:
                p = cfg.proxy.update_preferences(p)
        elif cfg.driver in WebDriver.CHROME_DRIVER_NAMES:
            d = webdriver.Chrome
            o = webdriver.ChromeOptions()
            o.add_argument("user-agent={0}".format(cfg.user_agent))
            if cfg.proxy is not None:
                o.add_argument("--proxy-server={0}".format(cfg.proxy.for_chrome()))
            p = None
        else:
            raise NotImplementedError

        if fetch_driver:
            Loader.fetch(cfg.executable_path, cfg.debug, cfg.driver)

        o.binary_location = cfg.executable_path
        o.headless = cfg.headless

        if cfg.driver in WebDriver.FIREFOX_DRIVER_NAMES:
            if cfg.proxy is None:
                return d(p, cfg.binary, options=o)
            else:
                return d(p, cfg.binary, options=o, proxy=cfg.proxy)
        elif cfg.driver in WebDriver.CHROME_DRIVER_NAMES:
            if cfg.proxy is None:
                return d(options=o)
            else:
                return d(options=o, proxy=cfg.proxy)
