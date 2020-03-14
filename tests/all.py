from seleniumwrapper import WebDriver, Configuration


def check_output(driver):
    driver.get("https://api.ipify.org/")
    print(driver.page_source)
    driver.close()


d = WebDriver.get_default()
check_output(d)

'''
c = Configuration("chrome", "driver/chromedriver", binary="/usr/bin/chromium")
d = WebDriver.build(c)
check_output(d)
'''

