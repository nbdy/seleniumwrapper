from sys import argv


class Configuration(object):
    headless = True
    driver = "chrome"
    executable_path = "driver/chromedriver"

    @staticmethod
    def help():
        print("usage: python3 Informer.py {arguments}")
        print("\t-h\t--help")
        print("\t-d\t--driver\tsets the webdriver")
        print("\t\tdefault: chrome")
        print("\t\tpossible arguments: chrome, c, firefox, f")
        print("\t-e\t--executable-path\tpath to driver")
        print("\t\tdefault:", Configuration.executable_path)
        print("\t--headless\trun browser headless")
        print("\t\tpossible arguments: none")
        exit()

    class UnexpectedArgumentException(Exception):
        pass

    def __init__(self, **kwargs):
        for k in kwargs.keys():
            if k in ["headless", "driver", "executable_path"]:
                self.__dict__["k"] = kwargs.get(k)
            else:
                raise Configuration.UnexpectedArgumentException("configuration has no variable '", k, "'")

    @staticmethod
    def parse():
        i = 0
        c = Configuration()
        while i < len(argv):
            a = argv[i]
            if a in ["-h", "--help"]:
                Configuration.help()
            elif a in ["-d", "--driver"]:
                c.driver = argv[i + 1]
            elif a in ["--headless"]:
                c.headless = True
            i += 1
        return c
