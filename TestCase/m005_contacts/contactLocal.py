import unittest
import uuid
import time
from preconditions.BasePreconditions import LoginPreconditions
from library.core.TestCase import TestCase
from library.core.utils.applicationcache import current_mobile, current_driver, switch_to_mobile
from library.core.utils.testcasefilter import tags
from pages import *
from pages.contacts.local_contact import localContactPage
import preconditions
from dataproviders import contact2

REQUIRED_MOBILES = {
    'Android-移动': 'M960BDQN229CH',
    # 'Android-移动': 'single_mobile',
    'IOS-移动': 'M960BDQN229CHiphone8',
    'IOS-移动-移动': 'M960BDQN229CHiphone8',
}


class Preconditions(LoginPreconditions):
    """
    分解前置条件
    """
    @staticmethod
    def connect_mobile(category):
        """选择手机手机"""
        client = switch_to_mobile(REQUIRED_MOBILES[category])
        client.connect_mobile()
        return client

    @staticmethod
    def disconnect_mobile(category):
        """选择手机手机"""
        client = switch_to_mobile(category)
        client.disconnect_mobile()
        return client


    @staticmethod
    def create_contacts(name, number):
        """
        导入联系人数据
        :param name:
        :param number:
        :return:
        """
        contacts_page = ContactsPage()
        detail_page = ContactDetailsPage()
        try:
            contacts_page.wait_for_page_load()
            contacts_page.open_contacts_page()
        except:
            Preconditions.make_already_in_message_page(reset=False)
            contacts_page.open_contacts_page()
        # 创建联系人
        contacts_page.click_search_box()
        contact_search = ContactListSearchPage()
        contact_search.wait_for_page_load()
        contact_search.input_search_keyword(name)
        contact_search.click_back()
        contacts_page.click_add()
        create_page = CreateContactPage()
        create_page.hide_keyboard_if_display()
        create_page.create_contact(name, number)
        detail_page.wait_for_page_load()
        detail_page.click_back_icon()

    @staticmethod
    def take_logout_operation_if_already_login():
        """已登录状态，执行登出操作"""
        message_page = MessagePage()
        message_page.wait_for_page_load()
        message_page.open_me_page()

        me = MePage()
        me.scroll_to_bottom()
        me.scroll_to_bottom()
        me.scroll_to_bottom()
        me.click_setting_menu()

        setting = SettingPage()
        setting.scroll_to_bottom()
        setting.click_logout()
        setting.click_ok_of_alert()

    @staticmethod
    def reset_and_relaunch_app():
        """首次启动APP（使用重置APP代替）"""
        app_package = 'com.chinasofti.rcs'
        current_driver().activate_app(app_package)
        current_mobile().reset_app()

    @staticmethod
    def terminate_app():
        """
        强制关闭app,退出后台
        :return:
        """
        app_id = current_driver().desired_capability['appPackage']
        current_mobile().termiate_app(app_id)

    @staticmethod
    def background_app():
        """后台运行"""
        current_mobile().press_home_key()

    @staticmethod
    def activate_app(app_id=None):
        """激活APP"""
        if not app_id:
            app_id = current_mobile().driver.desired_capabilities['appPackage']
        current_mobile().driver.activate_app(app_id)


    @staticmethod
    def create_contacts_if_not_exits(name, number):
        """
        不存在就导入联系人数据
        :param name:
        :param number:
        :return:
        """
        contacts_page = ContactsPage()
        detail_page = ContactDetailsPage()
        try:
            contacts_page.wait_for_page_load()
            contacts_page.open_contacts_page()
        except:
            Preconditions.make_already_in_message_page(reset=False)
            contacts_page.open_contacts_page()
        # 创建联系人
        contacts_page.click_phone_contact()
        contacts_page.click_search_phone_contact()
        contacts_page.input_search_keyword(name)
        if contacts_page.is_contact_in_list():
            contacts_page.click_back()
        else:
            contacts_page.click_add()
            create_page = CreateContactPage()
            create_page.create_contact(name, number)
            time.sleep(2)
            detail_page.click_back_icon()
            contacts_page.click_back()

        #
        # contact_search = ContactListSearchPage()
        # contact_search.wait_for_page_load()
        # contact_search.input_search_keyword(name)
        # if contact_search.is_contact_in_list(name):
        #     contact_search.click_back()
        # else:
        #     contact_search.click_back()
        #     contacts_page.click_add()
        #     create_page = CreateContactPage()
        #     create_page.hide_keyboard_if_display()
        #     create_page.create_contact(name, number)
        #     detail_page.wait_for_page_load()
        #     detail_page.click_back_icon()

class ContactsLocalhigh(TestCase):
    """
    模块：联系-本地联系人
    文件位置：全量/115全量测试用例-联系(1322).xlsx--高等级用例(优先编写)
    表格：通讯录-本地通讯录
    author: 余梦思
    """

    def default_setUp(self):
        """确保每个用例执行前在通讯录页面"""
        Preconditions.make_already_in_message_page()
        MessagePage().wait_for_page_load()
        MessagePage().click_contacts()
        time.sleep(2)
        ContactsPage().click_phone_contact()

    def default_tearDown(self):
        Preconditions.disconnect_mobile(REQUIRED_MOBILES['IOS-移动'])


    @tags('ALL', 'CONTACTS', 'CMCC')
    def test_contacts_chenjixiang_0130(self):
        """测试表单字段，姓名非空校验"""
        ContactsPage().click_add()
        time.sleep(1)
        CreateContactPage().click_input_name()
        CreateContactPage().click_input_number()
        CreateContactPage().is_toast_exist('姓名不能为空，请重新输入')
        time.sleep(2)

    @tags('ALL', 'CONTACTS', 'CMCC')
    def test_contacts_chenjixiang_0137(self):
        """测试表单字段，手机号非空校验"""
        ContactsPage().click_add()
        time.sleep(1)
        creat_contact=CreateContactPage()
        creat_contact.click_input_name()
        creat_contact.input_name('ceshi')
        creat_contact.click_input_number()
        creat_contact.click_input_name()
        creat_contact.is_toast_exist('电话不能为空，请重新输入')
        time.sleep(2)

    @tags('ALL', 'CONTACTS', 'CMCC')
    def test_contacts_chenjixiang_0138(self):
        """测试表单字段，手机号码长度校验，小于3个字符"""
        ContactsPage().click_add()
        time.sleep(1)
        creat_contact=CreateContactPage()
        creat_contact.click_input_name()
        creat_contact.input_name('ceshi')
        creat_contact.click_input_number()
        creat_contact.input_number('12')
        creat_contact.click_save()
        creat_contact.is_toast_exist('号码输入有误，请重新输入')
        time.sleep(2)




if __name__=="__main__":
    unittest.main()
