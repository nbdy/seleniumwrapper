from seleniumwrapper import WebDriver

if __name__ == '__main__':
    d = WebDriver.get_default()  # automatically fetches missing driver
    d.get("https://github.com")
    print(d.title)
    d.close()
