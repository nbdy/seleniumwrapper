## seleniumwrapper
[![Build Status](http://build.eberlein.io:8080/job/python_seleniumwrapper/badge/icon)](http://build.eberlein.io:8080/job/python_seleniumwrapper/)<br>

downloads drivers<br>
and offers an easier interface
```python
from seleniumwrapper import Configuration, fetch, WebDriver
fetch()  # currently only fetches the chromium webdriver
cfg = Configuration()
cfg.headless = True
driver = WebDriver.build(cfg)
driver.get("https://google.com")
print(driver.title)
```

you can get a prebuild egg/wheel [here](http://build.eberlein.io:8080/job/python_seleniumwrapper/lastSuccessfulBuild/artifact/dist/)

