from appium import webdriver
import time

import os, sys
sys.path.append(os.getcwd())
import pytest
from base.base_driver import init_driver
from page.setting_page import SettingPage
from base.read_data import ReadData


def input_data():
    data_list = []
    data_yaml = ReadData().return_data()
    for i in data_yaml.keys():
        data_list.append((i, data_yaml.get(i).get('input_text')))
    return data_list


class TestSitting:
    def setup_class(self):
        self.driver = init_driver()
        self.setting_page = SettingPage(self.driver)


    def teardown_class(self):
        self.driver.quit()

    # @pytest.mark.parametrize('test_id,input_text', input_data())
    # def test_setting(self, test_id, input_text):
    #     sp = SettingPage(self.driver)
    #     print("test_id:", test_id)
    #     sp.input_src_text()

    @pytest.mark.parametrize('content',input_data())
    def test_setting(self, content):
        self.setting_page.click_search()
        self.setting_page.input_src_text(content)
        self.setting_page.click_back()

        # self.driver.find_element_by_id("com.android.settings:id/search").click()
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys("aaa")
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()