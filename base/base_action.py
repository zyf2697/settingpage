
class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, loc):
        self.find_element(loc).click()

    def input_element_content(self, loc, content):
        self.find_element(loc).send_keys(content)

    def find_element(self, loc):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(loc[0], loc[1])
