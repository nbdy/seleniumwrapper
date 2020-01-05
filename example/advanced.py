from seleniumwrapper import Loader, Configuration, WebDriver, NotSupportedError

if __name__ == '__main__':
    try:
        Loader.fetch(debug=True)  # fetches all drivers for this platform to ./driver/
    except NotSupportedError as e:
        print(e)
        pass

    cfg = Configuration(
        driver="chrome",
        executable_path="drivers/",
        user_agent="seleniumwrapper-0.42",
        headless=False,
        debug=True
    )

    d = WebDriver.build(cfg)
    d.get("https://github.com")
    print(d.title)
    d.close()
