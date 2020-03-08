from seleniumwrapper import WebDriver, Configuration, Proxy


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

c = Configuration(proxy=Proxy.socks("127.0.0.1", 19340))
d = WebDriver.build(c)
check_output(d)

