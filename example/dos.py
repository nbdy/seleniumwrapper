from seleniumwrapper.loader import Loader
from seleniumwrapper.webdriver import WebDriver
from seleniumwrapper.configuration import Configuration

if __name__ == '__main__':
    Loader.fetch_all()  # downloads all drivers
    driver = WebDriver.build(Configuration())
    driver.get("https://github.com")
    print(driver.title)
    driver.close()
