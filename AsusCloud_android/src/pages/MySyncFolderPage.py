# coding:utf-8
__author__ = 'Eki'
'''
description:MySyncFolder頁面操作
'''

from src.common.Base_page import Base_page
from appium.webdriver.common import mobileby

class MySyncFolder(Base_page):
    By = mobileby.MobileBy()
    float_blue_butn_loc = (By.ID, "xxx:id/fab")
    addnewfolder_butn_loc = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout")
    addnewfolder_name_loc = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText")
    addnewfolder_determine_loc = (By.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"建立\")")
    blue_multiple_butn_loc = (By.XPATH, "//*[@resource-id='xxx:id/all_function']")
    multi_select_file_loc = (By.XPATH, "//android.widget.TextView[@text='多選檔案']")
    blue_multiple_delete_butn_loc = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.LinearLayout")
    # 確認鍵
    confirm_loc = (By.XPATH, "//*[@class='android.widget.Button' and @index='1']")
    burger_menu_loc = (By.XPATH, "//android.widget.ImageButton[@content-desc='向上瀏覽']")
    setting_loc = (By.ID, "xxx:id/menu_setting_btn")
    account_info_loc = (By.ID, "xxx:id/go_account_page")
    logout_butn_loc = (By.ID, "xxx:id/account_logout_btn")
    note_butn_loc = (By.XPATH, "//*[@class='android.widget.TextView' and @text='記事']")
    note_content_loc = (By.ID, "xxx:id/note_content")
    note_confirm_loc = (By.ID, "xxx:id/note_confirm")
    rename_inputbox_loc = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText")
    rename_butn_loc = (By.XPATH, "//*[@class='android.widget.TextView' and @text='重新命名']")
    blue_multiple_move_butn_loc = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.LinearLayout")
    blue_multiple_addnewfolder_butn_loc = (By.ID, "xxx:id/menu_operation")
    confirm_select_folder_butn_loc = (By.ID, "xxx:id/confirm_select_folder")
    addmessage_butn_loc = (By.XPATH, "//*[@class='android.widget.TextView' and @text='新增訊息']")
    message_input_loc = (By.ID, "xxx:id/message_input")
    message_confirm_loc = (By.ID, "xxx:id/message_confirm")


    def float_blue_butn(self):
        self.find_element(*self.float_blue_butn_loc).click()

    def addnewfolder(self, foldername):
        self.find_element(*self.addnewfolder_butn_loc).click()
        self.find_element(*self.addnewfolder_name_loc).clear()
        self.find_element(*self.addnewfolder_name_loc).send_keys(foldername)
        self.find_element(*self.addnewfolder_determine_loc).click()

    def blue_multiple_butn(self):
        self.find_element(*self.blue_multiple_butn_loc).click()

    def multi_select_file(self):
        self.find_element(*self.multi_select_file_loc).click()

    def blue_multiple_delete_butn(self):
        self.find_element(*self.blue_multiple_delete_butn_loc).click()

    def confirm_delete(self):
        self.find_element(*self.confirm_loc).click()

    def burger_menu_butn(self):
        self.find_element(*self.burger_menu_loc).click()

    def setting(self):
        self.find_element(*self.setting_loc).click()

    def account_info(self):
        self.find_element(*self.account_info_loc).click()

    def logout_butn(self):
        self.find_element(*self.logout_butn_loc).click()

    def note(self, note_content, test_note):
        self.find_element(*self.note_butn_loc).click()
        self.find_element(*self.note_content_loc).clear()
        self.find_element(*self.note_content_loc).send_keys(note_content)
        self.find_element(*self.note_confirm_loc).click()
        self.find_element(*self.rename_inputbox_loc).clear()
        self.find_element(*self.rename_inputbox_loc).send_keys(test_note)
        self.find_element(*self.confirm_loc).click()

    def rename(self, rename):
        self.find_element(*self.rename_butn_loc).click()
        self.find_element(*self.rename_inputbox_loc).clear()
        self.find_element(*self.rename_inputbox_loc).send_keys(rename)
        self.find_element(*self.confirm_loc).click()

    def blue_multiple_move_butn(self):
        self.find_element(*self.blue_multiple_move_butn_loc).click()

    def blue_mutiple_addnewfolder_butn(self, blue_addfoldername):
        self.find_element(*self.blue_multiple_addnewfolder_butn_loc).click()
        self.find_element(*self.addnewfolder_name_loc).clear()
        self.find_element(*self.addnewfolder_name_loc).send_keys(blue_addfoldername)
        self.find_element(*self.addnewfolder_determine_loc).click()

    def confirm_select_folder_butn(self):
        self.find_element(*self.confirm_select_folder_butn_loc).click()

    def addmessage_butn(self, message):
        self.find_element(*self.addmessage_butn_loc).click()
        self.find_element(*self.message_input_loc).clear()
        self.find_element(*self.message_input_loc).send_keys(message)
        self.find_element(*self.message_confirm_loc).click()





