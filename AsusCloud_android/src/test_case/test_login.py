# coding:utf-8
__author__ = 'Eki'
'''
description:測試登入
'''

import unittest
from time import sleep
from src.pages.login_page import login
from src.common import driver_configure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.pages.MySyncFolderPage import MySyncFolder
from package import HTMLTestRunner


class test_login(unittest.TestCase):

    def setUp(self):
        dc = driver_configure.driver_configure()
        self.driver = dc.get_driver()

    # 帳密皆正確
    def test_login1(self):
        # 等待app啟動
        sleep(3)
        username = "username"
        password = "password"
        login_page = login(self.driver)
        login_page.first_page_login_butn()
        login_page.login_username(username)
        login_page.login_password(password)
        login_page.second_page_login_butn()
        # 點選"不要備份", #參數傳出去為tuple故需把By.ID,'xxx'再加上一組括號
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, 'xxx:id/btn_close_page'))).click()
        sleep(2)
        # 點選"漢堡多選單"
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//android.widget.ImageButton[@content-desc="向上瀏覽"]'))).click()
        user = str(WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, 'xxx:id/tv_userName'))).text)
        user_id = user.split('：')[1]
        self.assertEqual("eki.hong@asuscloud.com", user_id)
        self.logout()

    # 帳號或密碼錯誤
    def test_login2(self):
        # 等待app啟動
        sleep(3)
        username = "username"
        password = "xxxxxxxx"  #錯誤密碼
        login_page = login(self.driver)
        login_page.first_page_login_butn()
        login_page.login_username(username)
        login_page.login_password(password)
        login_page.second_page_login_butn()
        alert = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, 'android:id/message'))).text
        print(alert)
        self.assertEqual("ASUS Cloud ID或密碼錯誤，請再輸入一次!", alert)


    # 帳號或密碼為空
    def test_login3(self):
        # 等待app啟動
        sleep(3)
        username = ""
        password = ""
        login_page = login(self.driver)
        login_page.first_page_login_butn()
        login_page.login_username(username)
        login_page.login_password(password)
        login_page.second_page_login_butn()
        alert = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, 'android:id/message'))).text
        print(alert)
        self.assertEqual("ASUS Cloud ID或密碼不得為空白!", alert)



    def logout(self):
        MySync = MySyncFolder(self.driver)
        MySync.burger_menu_butn()
        MySync.setting()
        MySync.account_info()
        MySync.logout_butn()
        MySync.confirm_delete()

    def tearDown(self):
        self.driver.quit()


if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(test_login("test_login1"))
    suite.addTest(test_login("test_login2"))
    suite.addTest(test_login("test_login3"))

    #html report output
    file_path = r'D:\AsusCloud_android\report\test_login_result.html'
    fp = open(file_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title="ASUSCLOUD Test Report",
        description="使用者案例執行情況:")
    runner.run(suite)
    fp.close()

