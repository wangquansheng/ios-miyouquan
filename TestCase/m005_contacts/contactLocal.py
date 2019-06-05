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

    @tags('ALL', 'CONTACTS', 'CMCC')
    def test_contacts_chenjixiang_0140(self):
        """测试表单字段，手机号码长度边界值校验，3个字符"""
        ContactsPage().click_add()
        time.sleep(1)
        creat_contact=CreateContactPage()
        creat_contact.click_input_name()
        creat_contact.input_name('ceshi')
        creat_contact.click_input_number()
        creat_contact.input_number('123')
        creat_contact.click_save()
        time.sleep(2)
        ContactDetailsPage().page_should_contain_text('飞信电话')
        time.sleep(2)

    def tearDown_test_contacts_chenjixiang_0140(self):
        contant_detail = ContactDetailsPage()
        contant_detail.click_edit_contact()
        time.sleep(2)
        contant_detail.hide_keyboard()
        # contant_detail.page_up()
        contant_detail.change_delete_number()
        contant_detail.click_sure_delete()

    @tags('ALL', 'CONTACTS', 'CMCC')
    def test_contacts_chenjixiang_0147(self):
        """测试表单字段，公司边界值校验，输入1个字符"""
        ContactsPage().click_add()
        time.sleep(1)
        creat_contact=CreateContactPage()
        creat_contact.click_input_name()
        creat_contact.input_name('ceshi')
        creat_contact.click_input_number()
        creat_contact.input_number('123')
        creat_contact.click_input_company()
        creat_contact.input_company('a')
        creat_contact.click_save()
        time.sleep(2)
        ContactDetailsPage().page_should_contain_text('飞信电话')
        time.sleep(2)

    def tearDown_test_contacts_chenjixiang_0147(self):
        contant_detail = ContactDetailsPage()
        contant_detail.click_edit_contact()
        time.sleep(2)
        contant_detail.hide_keyboard()
        # contant_detail.page_up()
        contant_detail.change_delete_number()
        contant_detail.click_sure_delete()


    @tags('ALL', 'CONTACTS', 'CMCC')
    def test_contacts_chenjixiang_0154(self):
        """测试表单字段，职位边界值校验，输入1个字符"""
        ContactsPage().click_add()
        time.sleep(1)
        creat_contact=CreateContactPage()
        creat_contact.click_input_name()
        creat_contact.input_name('ceshi')
        creat_contact.click_input_number()
        creat_contact.input_number('123')
        creat_contact.page_up()
        creat_contact.click_input_position()
        creat_contact.input_position('a')
        creat_contact.click_save()
        time.sleep(2)
        ContactDetailsPage().page_should_contain_text('飞信电话')
        time.sleep(2)

    def tearDown_test_contacts_chenjixiang_0154(self):
        contant_detail = ContactDetailsPage()
        contant_detail.click_edit_contact()
        time.sleep(2)
        contant_detail.hide_keyboard()
        contant_detail.change_delete_number()
        contant_detail.click_sure_delete()

    @tags('ALL', 'CONTACTS', 'CMCC')
    def test_contacts_chenjixiang_0161(self):
        """测试表单字段，邮箱边界值校验，输入1个字符"""
        ContactsPage().click_add()
        time.sleep(1)
        creat_contact=CreateContactPage()
        creat_contact.click_input_name()
        creat_contact.input_name('ceshi')
        creat_contact.click_input_number()
        creat_contact.input_number('123')
        creat_contact.page_up()
        creat_contact.click_input_email()
        creat_contact.input_email_address('a')
        creat_contact.click_save()
        time.sleep(2)
        ContactDetailsPage().page_should_contain_text('飞信电话')
        time.sleep(2)

    def tearDown_test_contacts_chenjixiang_0161(self):
        contant_detail = ContactDetailsPage()
        contant_detail.click_edit_contact()
        time.sleep(2)
        contant_detail.hide_keyboard()
        contant_detail.change_delete_number()
        contant_detail.click_sure_delete()


    # @tags('ALL', 'CONTACTS', 'CMCC')
    # def test_contacts_chenjixiang_0166(self):
    #     """测试和飞信新建联系人，名称和本地通讯录联系人一样，手机号码不一样"""
    #     # old_number=ContactsPage().get_all_phone_number()
    #     ContactsPage().click_add()
    #     time.sleep(1)
    #     creat_contact=CreateContactPage()
    #     creat_contact.click_input_name()
    #     input_name='大佬1'
    #     creat_contact.input_name(input_name)
    #     creat_contact.click_input_number()
    #     input_number='12345678901'
    #     creat_contact.input_number(input_number)
    #     creat_contact.click_save()
    #     time.sleep(2)
    #     contact_detail=ContactDetailsPage()
    #     contact_detail.page_should_contain_text('飞信电话')
    #     time.sleep(1)
    #     contact_name1=contact_detail.get_people_name()
    #     contact_number1=contact_detail.get_people_number()
    #     time.sleep(1)
    #     #原本的大佬1
    #     contact_detail.click_back_icon()
    #     time.sleep(1)
    #     ContactsPage().select_contacts_by_number('13800138005')
    #     time.sleep(2)
    #     contact_name2 = contact_detail.get_people_name()
    #     contact_number2 = contact_detail.get_people_number()
    #     #判断新增名称一样,号码与头像不一样
    #     time.sleep(1)
    #     self.assertEqual(contact_name1,contact_name2)
    #     self.assertNotEqual(contact_number1, contact_number2)
    #
    # def tearDown_test_contacts_chenjixiang_0166(self):
    #     Preconditions.make_already_in_message_page()
    #     MessagePage().click_contacts()
    #     contact = ContactsPage()
    #     if contact.is_exit_element_by_text_swipe('12345678901'):
    #         contact.select_contacts_by_number('12345678901')
    #         contant_detail = ContactDetailsPage()
    #         contant_detail.click_edit_contact()
    #         time.sleep(2)
    #         contant_detail.hide_keyboard()
    #         contant_detail.change_delete_number()
    #         contant_detail.click_sure_delete()
    #     else:
    #         pass

    @tags('ALL', 'CONTACTS', 'CMCC')
    def test_contacts_chenjixiang_0175(self):
        """测试页面信息展示，名称正常长度显示"""
        text = '大佬1'
        ContactsPage().select_contacts_by_name(text)
        cdp = ContactDetailsPage()
        time.sleep(2)
        contact_name=cdp.get_people_name(text)
        self.assertEqual(contact_name,text)

    @tags('ALL', 'CONTACTS', 'CMCC')
    def test_contacts_chenjixiang_0177(self,):
        """测试页面信息展示，手机号码正常长度显示"""
        text='大佬1'
        ContactsPage().select_contacts_by_name(text)
        cdp = ContactDetailsPage()
        time.sleep(2)
        number='13800138005'
        contact_number=cdp.get_people_number(number)
        self.assertEqual(contact_number,number)


    @tags('ALL', 'CONTACTS', 'CMCC')
    def test_contacts_chenjixiang_0179(self):
        """测试页面信息展示，未上传头像"""
        ContactsPage().select_contacts_by_name('大佬1')
        cdp = ContactDetailsPage()
        time.sleep(2)
        cdp.page_should_contain_element_first_letter()

    @tags('ALL', 'CONTACTS', 'CMCC')
    def test_contacts_chenjixiang_0180(self):
        """测试页面信息展示，已上传头像"""
        ContactsPage().select_contacts_by_name('测试号码')
        cdp = ContactDetailsPage()
        cdp.wait_for_page_load()
        time.sleep(2)
        cdp.page_contain_contacts_avatar()

    @tags('ALL', 'CONTACTS', 'CMCC')
    def test_contacts_chenjixiang_0181(self):
        """测试点击联系人头像，未上传头像"""
        ContactsPage().select_contacts_by_name('大佬1')
        cdp = ContactDetailsPage()
        cdp.wait_for_page_load()
        time.sleep(2)
        cdp.click_avatar()
        cdp.is_exists_big_avatar()



if __name__=="__main__":
    unittest.main()
