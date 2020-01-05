from user_agent import generate_navigator_js


class Configuration(object):
    headless = True
    driver = None
    executable_path = None
    user_agent = None
    debug = False
    binary = None

    def __init__(self, driver="firefox", executable_path="driver/geckodriver",
                 user_agent=generate_navigator_js()["userAgent"], headless=True, debug=False,
                 binary="/usr/bin/firefox"):
        self.driver = driver
        self.executable_path = executable_path
        self.user_agent = user_agent
        self.headless = headless
        self.debug = debug
        self.binary = binary
