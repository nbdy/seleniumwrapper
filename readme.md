### seleniumwrapper
[![Build Status](http://build.eberlein.io:8080/job/python_seleniumwrapper/badge/icon)](http://build.eberlein.io:8080/job/python_seleniumwrapper/)<br>

#### supports:
- firefox
- chrome(ium)


downloads drivers<br>
and offers an easier interface<br>
uses [selenim-wire](https://github.com/wkeeling/selenium-wire) under the hood<br>
so there are more features<br>
for example: overwriting headers
```python
from seleniumwrapper import WebDriver
d = WebDriver.get_default()  # downloads webdriver
d.get("https://github.com")
print(d.title)
d.close()
```

you can get a prebuild egg/wheel [here](http://build.eberlein.io:8080/job/python_seleniumwrapper/lastSuccessfulBuild/artifact/dist/)

