from selenium import webdriver as web


class WebDriver(object):
    FIREFOX_DRIVER_NAMES = ["f", "firefox"]
    CHROME_DRIVER_NAMES = ["c", "chrome"]

    @staticmethod
    def build(cfg):
        d = None
        o = None
        if cfg.driver in WebDriver.FIREFOX_DRIVER_NAMES:
            d = web.Firefox
            o = web.firefox.options.Options()
        elif cfg.driver in WebDriver.CHROME_DRIVER_NAMES:
            d = web.Chrome
            o = web.chrome.options.Options()

        o.headless = cfg.headless
        return d(cfg.executable_path, options=o)
