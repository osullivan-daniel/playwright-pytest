class BrowserConfigs:

    def __init__(self):
        self.browser_dict = {}

    def get_key(self, key):
        return self.browser_dict[key]

    def get_dict(self):
        return self.browser_dict

    def set_dict(self, browser_options):
        for each_browser in browser_options:
            self.browser_dict[each_browser[1] if len(each_browser) > 1 else each_browser[0]] = {
                'browserEngine': each_browser[0],
                'executablePath': each_browser[2] if len(each_browser) > 2 else ''
            }
