### seleniumwrapper
[![Build Status](http://build.eberlein.io:8080/job/python_seleniumwrapper/badge/icon)](http://build.eberlein.io:8080/job/python_seleniumwrapper/)<br>

unix only!
#### supports:
- firefox
- chrome(ium) (kinda)

downloads drivers<br>
uses selenium-wire<br>
and offers an easier interface<b>
```python
from seleniumwrapper import WebDriver
d = WebDriver.get_default()  # downloads webdriver
d.get("https://github.com")
print(d.title)
d.close()
```

you can get a prebuild egg/wheel [here](http://build.eberlein.io:8080/job/python_seleniumwrapper/lastSuccessfulBuild/artifact/dist/)

