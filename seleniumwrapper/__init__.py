from seleniumwrapper.loader import Loader
from seleniumwrapper.webdriver import WebDriver
from seleniumwrapper.configuration import Configuration


def fetch():
    Loader.fetch()


def driver(cfg=None):
    if cfg is None:
        cfg = Configuration()
    return WebDriver.build(cfg)
