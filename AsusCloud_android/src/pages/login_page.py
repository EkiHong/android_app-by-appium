# coding:utf-8
__author__ = 'Eki'
'''
description:登入頁面
'''
import sys
sys.path.append(r'D:\AsusCloud_android')
sys.path.append(r'C:\Users\Eki\Anaconda3')
sys.path.append(r'C:\Users\Eki\Anaconda3\Lib\site-packages')
from src.common.Base_page import Base_page
from appium.webdriver.common import mobileby

class login(Base_page):
    By = mobileby.MobileBy()
    first_login_butn_loc = (By.ID, "xxx:id/btn_login")
    second_login_butn_loc = (By.ID, "xxx:id/login_rulesave_btn")
    login_username_loc = (By.ID, "xxx:id/username_edit")
    login_password_loc = (By.ID, "xxx:id/password_edit")



    def first_page_login_butn(self):
        self.find_element(*self.first_login_butn_loc).click()

    def second_page_login_butn(self):
        self.find_element(*self.second_login_butn_loc).click()

    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)
