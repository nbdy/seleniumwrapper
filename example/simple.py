from seleniumwrapper import Configuration, WebDriver

if __name__ == '__main__':
    cfg = Configuration()
    d = WebDriver.build(cfg)  # automatically fetches missing driver
    d.get("https://github.com")
    print(d.title)
    d.close()
