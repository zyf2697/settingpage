from base import read_data
from base.base_action import BaseAction
import base


class SettingPage(BaseAction):

    # click_searchid = By.ID, "com.android.settings:id/search"
    # input_src_textid = (By.ID, "android:id/search_src_text")
    # click_backcm = By.CLASS_NAME, "android.widget.ImageButton"

    def __init__(self, driver):
        self.driver = driver
        BaseAction.__init__(self, driver)

    def click_search(self):
        self.click_element(base.click_searchid)
        # self.driver.find_element_by_id("com.android.settings:id/search").click()

    def input_src_text(self,content):
        self.input_element_content(base.input_src_textid,content)
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys("aaa")

    def click_back(self):
        self.click_element(base.click_backcm)
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()

