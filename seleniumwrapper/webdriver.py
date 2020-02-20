from seleniumwire import webdriver as web
from .configuration import Configuration
from .loader import Loader
from os.path import isfile, abspath


class WebDriver(object):
    FIREFOX_DRIVER_NAMES = ["f", "firefox"]
    CHROME_DRIVER_NAMES = ["c", "chrom", "chromium"]

    @staticmethod
    def get_default():
        return WebDriver.build(Configuration())

    @staticmethod
    def build(cfg):
        if not isfile(cfg.executable_path):
            Loader.fetch(cfg.executable_path, cfg.debug, cfg.driver)

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

        o.binary_location = abspath(cfg.executable_path)
        o.headless = cfg.headless

        if cfg.driver in WebDriver.FIREFOX_DRIVER_NAMES:
            return d(p, options=o, firefox_binary=cfg.binary, executable_path=cfg.executable_path)
        elif cfg.driver in WebDriver.CHROME_DRIVER_NAMES:
            return d(options=o)
