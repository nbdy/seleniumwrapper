from seleniumwrapper import fetch, driver, Configuration

if __name__ == '__main__':
    fetch()  # fetches webdrivers
    cfg = Configuration()
    cfg.headless = True
    d = driver(cfg)  # makes a web driver instance based on config
    d.get("https://python.org/")
    print(d.title)
    d.close()
