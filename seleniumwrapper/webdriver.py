from seleniumwire import webdriver as web
from .configuration import Configuration
from .loader import Loader


class WebDriver(object):
    FIREFOX_DRIVER_NAMES = ["f", "firefox"]
    CHROME_DRIVER_NAMES = ["c", "chrom", "chromium"]

    @staticmethod
    def get_default():
        return WebDriver.build(Configuration())

    @staticmethod
    def build(cfg):
        if cfg.driver in WebDriver.FIREFOX_DRIVER_NAMES:
            d = web.Firefox
            o = web.FirefoxOptions()
            p = web.FirefoxProfile()
            p.set_preference("general.useragent.override", cfg.user_agent)
        elif cfg.driver in WebDriver.CHROME_DRIVER_NAMES:
            d = web.Chrome
            o = web.ChromeOptions()
            o.add_argument("user-agent={0}".format(cfg.user_agent))
            p = None
        else:
            raise NotImplementedError

        Loader.fetch(cfg.executable_path, cfg.debug, cfg.driver)

        o.binary_location = cfg.executable_path
        o.headless = cfg.headless

        if cfg.driver in WebDriver.FIREFOX_DRIVER_NAMES:
            return d(p, options=o, firefox_binary=cfg.binary)
        elif cfg.driver in WebDriver.CHROME_DRIVER_NAMES:
            return d(options=o)
