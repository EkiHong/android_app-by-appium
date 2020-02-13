# coding:utf-8
__author__ = 'Eki'
'''
description:UI公共類
'''

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base_page():
    def __init__(self, driver):
        self.driver = driver

    # 顯性等待
    def find_element(self, *loc):
        try:
            return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(loc))
            # return self.driver.find_element(*loc)
        except:
            pass

    # 顯性等待
    def find_elements(self, *loc):
        try:
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(loc))
            # return self.driver.find_elements(*loc)
        except:
            pass
