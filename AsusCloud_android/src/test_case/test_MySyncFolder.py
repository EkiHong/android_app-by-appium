# coding:utf-8
__author__ = 'Eki'
'''
description:測試登入
'''
import sys
sys.path.append(r'D:\AsusCloud_android')
sys.path.append(r'C:\Users\Eki\Anaconda3')
import unittest
from time import sleep
from src.pages.login_page import login
from src.common import driver_configure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.pages.MySyncFolderPage import MySyncFolder
from appium.webdriver.common import mobileby
from xmlrunner import xmlrunner
from package import HTMLTestRunner



class test_MySyncFolder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dc = driver_configure.driver_configure()
        cls.driver = dc.get_driver()
        cls.login()

    @classmethod
    def login(cls):
        # 等待app啟動
        sleep(3)
        username = "username"
        password = "password"
        login_page = login(cls.driver)
        login_page.first_page_login_butn()
        login_page.login_username(username)
        login_page.login_password(password)
        login_page.second_page_login_butn()
        # 點選"不要備份", #參數傳出去為tuple故需把By.ID,'xxx'再加上一組括號
        WebDriverWait(cls.driver, 15).until(EC.visibility_of_element_located((By.ID, 'xxx:id/btn_close_page'))).click()
        sleep(3)

    def addnewfolder(self):
        foldername = "test_addnewfolder"
        By = mobileby.MobileBy()
        MySync = MySyncFolder(self.driver)
        MySync.float_blue_butn()
        MySync.addnewfolder(foldername)
        sleep(2)
        addnewfolder_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@text='test_addnewfolder']"))).text
        self.assertEqual(addnewfolder_text, "test_addnewfolder")
        MySync.blue_multiple_butn()
        MySync.multi_select_file()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='test_addnewfolder']"))).click()
        MySync.blue_multiple_butn()
        MySync.blue_multiple_delete_butn()
        MySync.confirm_delete()

    def note(self):
        note_content = "記事本"
        test_note = "測試記事"
        By = mobileby.MobileBy()
        MySync = MySyncFolder(self.driver)
        MySync.float_blue_butn()
        MySync.note(note_content, test_note)
        sleep(8)
        note_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@text='測試記事.txt']"))).text
        self.assertEqual(note_text, "測試記事.txt")
        MySync.blue_multiple_butn()
        MySync.multi_select_file()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='測試記事.txt']"))).click()
        MySync.blue_multiple_butn()
        MySync.blue_multiple_delete_butn()
        MySync.confirm_delete()

    def rename(self):
        foldername = "test_rename"
        rename = "rename"
        MySync = MySyncFolder(self.driver)
        MySync.float_blue_butn()
        MySync.addnewfolder(foldername)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@text="test_rename"]/../../android.widget.RelativeLayout[@resource-id="xxx:id/browse_item_button_group"]'))).click()
        MySync.rename(rename)
        rename_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@text='rename']"))).text
        self.assertEqual(rename_text, "rename")
        MySync.blue_multiple_butn()
        MySync.multi_select_file()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='rename']"))).click()
        MySync.blue_multiple_butn()
        MySync.blue_multiple_delete_butn()
        MySync.confirm_delete()

    def movefolder(self):  #不穩定
        foldername = "movefolder"
        MySync = MySyncFolder(self.driver)
        MySync.float_blue_butn()
        MySync.addnewfolder(foldername)
        MySync.blue_multiple_butn()
        MySync.multi_select_file()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='movefolder']"))).click()
        MySync.blue_multiple_butn()
        MySync.blue_multiple_move_butn()
        blue_addfoldername = "bluefolder"
        MySync.blue_mutiple_addnewfolder_butn(blue_addfoldername)
        MySync.confirm_select_folder_butn()

        sleep(8)
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x*0.5, y*0.25, x*0.5, y*0.75, 2)
        sleep(3)
        print("pass swipeeeeeeeeeeeeeeeeeeee")
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='bluefolder']"))).click()
        movefolder_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@text='movefolder']"))).text
        self.assertEqual(movefolder_text, "movefolder")
        self.driver.back()
        MySync.blue_multiple_butn()
        MySync.multi_select_file()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='bluefolder']"))).click()
        MySync.blue_multiple_butn()
        MySync.blue_multiple_delete_butn()
        MySync.confirm_delete()

    def addmessage(self):
        foldername = "messagefolder"
        MySync = MySyncFolder(self.driver)
        MySync.float_blue_butn()
        MySync.addnewfolder(foldername)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@text="messagefolder"]/../../android.widget.RelativeLayout[@resource-id="xxx:id/browse_item_button_group"]'))).click()
        sleep(2)
        self.driver.swipe(100, 700, 100, 150) #畫面滑動
        message = "test"
        MySync.addmessage_butn(message)
        message_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "xxx:id/message_content"))).text
        print(message_text)
        self.assertEqual(message_text, "test")
        sleep(1)
        self.driver.back()
        MySync.blue_multiple_butn()
        MySync.multi_select_file()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='messagefolder']"))).click()
        MySync.blue_multiple_butn()
        MySync.blue_multiple_delete_butn()
        MySync.confirm_delete()


    @classmethod
    def logout(cls):
        MySync = MySyncFolder(cls.driver)
        MySync.burger_menu_butn()
        MySync.setting()
        MySync.account_info()
        MySync.logout_butn()
        MySync.confirm_delete()

    @classmethod
    def tearDownClass(cls):
        cls.logout()
        cls.driver.quit()

if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(test_MySyncFolder("test_addnewfolder"))
    suite.addTest(test_MySyncFolder("test_note"))
    suite.addTest(test_MySyncFolder("test_rename"))
    suite.addTest(test_MySyncFolder("test_movefolder"))
    suite.addTest(test_MySyncFolder("test_addmessage"))

    # xml report output
    # xmlrunner.XMLTestRunner(output=r'D:\AsusCloud_android\report').run(suite)
    # xmlrunner.XMLTestRunner(output=r'C:\Users\Eki\.jenkins\workspace\ASUSCLOUD_Android\reports').run(suite)  # xml報告存在jenkins目錄下，讓DashBoard可成功輸出

    # html report output
    file_path = r'D:\AsusCloud_android\report\test_MySyncFolder_result.html'
    fp = open(file_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title="ASUSCLOUD Test Report",
        description="使用者案例執行情況:")
    runner.run(suite)
    fp.close()
