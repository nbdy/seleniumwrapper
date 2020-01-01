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
            o = web.FirefoxOptions()
        elif cfg.driver in WebDriver.CHROME_DRIVER_NAMES:
            d = web.Chrome
            o = web.ChromeOptions()

        o.headless = cfg.headless
        o.add_argument("user_agent=%s" % cfg.user_agent)
        print(cfg.__dict__)
        return d(cfg.executable_path, options=o)
