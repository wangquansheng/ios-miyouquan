import unittest
import uuid
from library.core.common.simcardtype import CardType
import time
from preconditions.BasePreconditions import LoginPreconditions
from library.core.TestCase import TestCase
from library.core.utils.applicationcache import current_mobile, current_driver, switch_to_mobile
from library.core.utils.testcasefilter import tags
from pages import *
from pages.contacts.EditContactPage import EditContactPage
from pages.contacts.local_contact import localContactPage
import preconditions
from dataproviders import contact2


REQUIRED_MOBILES = {
    'Android-移动': 'M960BDQN229CH',
    # 'Android-移动': 'single_mobile',
    'IOS-移动': 'iphone',
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


class TagGrouping(TestCase):
    """标签分组"""


    def default_setUp(self):
        """确保每个用例执行前在标签分组页面"""
        Preconditions.make_already_in_message_page()
        time.sleep(2)
        MessagePage().click_contacts()
        time.sleep(2)
        ContactsPage().click_phone_contact()
        ContactsPage().click_label_grouping()

    def default_tearDown(self):
        Preconditions.disconnect_mobile(REQUIRED_MOBILES['IOS-移动'])


    def test_contacts_quxinli_0352(self):
        lg = LabelGroupingPage()
        lg.delete_all_label()
        lg.page_should_contain_text('标签分组')
        lg.page_should_contain_text('新建分组')
        lg.page_should_contain_text('暂无分组')


    @tags('ALL', 'CONTACT', 'CMCC')
    def test_contacts_quxinli_0353(self):
        """新建分组"""
        lg=LabelGroupingPage()
        time.sleep(2)
        lg.click_new_create_group()
        time.sleep(4)
        lg.page_should_contain_text('为你的分组创建一个名称')
        lg.page_should_contain_text('请输入标签分组名称')
        lg.page_should_contain_text('新建分组')
        lg.page_contain_element(text='确定')

    @tags('ALL', 'CONTACT', 'CMCC')
    def test_contacts_quxinli_0355(self):
        """新建分组,标签分组名称输入空格"""
        lg = LabelGroupingPage()
        text = ' '
        lg.click_new_create_group()
        time.sleep(1)
        lg.click_input_box()
        time.sleep(1)
        lg.input_search_text(text)
        lg.click_sure()
        SelectContactsPage().check_if_element_not_exist(text='选择一个群')


    @tags('ALL', 'CONTACT', 'CMCC')
    def test_contacts_quxinli_0356(self):
        """新建分组,标签分组名称输入9个汉字"""
        lg = LabelGroupingPage()
        text = '祝一路顺风幸福美满'
        # GroupListPage().delete_group(name=text)
        lg.click_new_create_group()
        time.sleep(1)
        lg.click_input_box()
        time.sleep(1)
        lg.input_search_text(text)
        lg.click_sure()
        SelectContactsPage().is_element_present(locator='选择一个群')

    @tags('ALL', 'debug', 'CMCC')
    def tearDown_test_contacts_quxinli_0356(self):
        SelectContactsPage().click_back()
        LabelGroupingPage().click_back()
        LabelGroupingPage().delete_label_groups(group='祝一路顺风幸福美满')
        Preconditions.disconnect_mobile(REQUIRED_MOBILES['IOS-移动'])



    @tags('ALL', 'CONTACT', 'CMCC')
    def test_contacts_quxinli_0357(self):
        """新建分组,标签分组名称输入10个汉字"""
        GroupPage = GroupListPage()
        GroupPage.click_new_group()
        GroupPage.click_input_element()
        time.sleep(3)
        GroupPage.input_content(text="祝一路顺风和幸福美满")
        GroupPage.click_sure_element()
        GroupPage.click_allow_button()
        SelectContactsPage().is_element_present(locator='选择一个群')

    def tearDown_test_contacts_quxinli_0357(self):
        SelectContactsPage().click_back()
        LabelGroupingPage().click_back()
        LabelGroupingPage().delete_label_groups(group='祝一路顺风和幸福美满')
        Preconditions.disconnect_mobile(REQUIRED_MOBILES['IOS-移动'])


    @tags('ALL', 'CONTACT', 'CMCC')
    def test_contacts_quxinli_0358(self):
        """新建分组,标签分组名称输入11个汉字"""
        GroupPage = GroupListPage()
        GroupPage.click_new_group()
        GroupPage.click_input_element()
        time.sleep(3)
        GroupPage.input_content(text="祝一路顺风和幸福美满啊")
        GroupPage.click_sure_element()
        GroupPage.click_allow_button()
        SelectContactsPage().is_element_present(locator='选择一个群')

    def tearDown_test_contacts_quxinli_0358(self):
        SelectContactsPage().click_back()
        LabelGroupingPage().click_back()
        LabelGroupingPage().delete_label_groups(group='祝一路顺风和幸福美满')
        Preconditions.disconnect_mobile(REQUIRED_MOBILES['IOS-移动'])

    @tags('ALL', 'CONTACT', 'CMCC')
    def test_contacts_quxinli_0359(self):
        """新建分组,标签分组名称输入29个数字"""
        GroupPage = GroupListPage()
        GroupPage.click_new_group()
        GroupPage.click_input_element()
        time.sleep(3)
        self.group='1'*29
        GroupPage.input_content(text=self.group)
        GroupPage.click_sure_element()
        GroupPage.click_allow_button()
        SelectContactsPage().is_element_present(locator='选择一个群')

    def tearDown_test_contacts_quxinli_0359(self):
        SelectContactsPage().click_back()
        LabelGroupingPage().click_back()
        LabelGroupingPage().delete_label_groups(group=self.group)
        Preconditions.disconnect_mobile(REQUIRED_MOBILES['IOS-移动'])


    @tags('ALL', 'CONTACT', 'CMCC')
    def test_contacts_quxinli_0360(self):
        """新建分组,标签分组名称输入30个数字"""
        GroupPage = GroupListPage()
        GroupPage.click_new_group()
        GroupPage.click_input_element()
        time.sleep(3)
        self.group='1'*30
        GroupPage.input_content(text=self.group)
        GroupPage.click_sure_element()
        GroupPage.click_allow_button()
        SelectContactsPage().is_element_present(locator='选择一个群')

    def tearDown_test_contacts_quxinli_0360(self):
        SelectContactsPage().click_back()
        LabelGroupingPage().click_back()
        LabelGroupingPage().delete_label_groups(group=self.group)
        Preconditions.disconnect_mobile(REQUIRED_MOBILES['IOS-移动'])


    @tags('ALL', 'CONTACT', 'CMCC')
    def test_contacts_quxinli_0361(self):
        """新建分组,标签分组名称输入31个数字"""
        GroupPage = GroupListPage()
        GroupPage.click_new_group()
        GroupPage.click_input_element()
        time.sleep(3)
        self.group='1'*31
        GroupPage.input_content(text=self.group)
        GroupPage.click_sure_element()
        GroupPage.click_allow_button()
        SelectContactsPage().check_if_element_not_exist(text='选择一个群')


    @tags('ALL', 'CONTACT', 'CMCC')
    def test_contacts_quxinli_0362(self):
        """新建分组,标签分组名称输入29个字母"""
        GroupPage = GroupListPage()
        GroupPage.click_new_group()
        GroupPage.click_input_element()
        time.sleep(3)
        self.group='a'*29
        GroupPage.input_content(text=self.group)
        GroupPage.click_sure_element()
        GroupPage.click_allow_button()
        SelectContactsPage().is_element_present(locator='选择一个群')

    def tearDown_test_contacts_quxinli_0362(self):
        SelectContactsPage().click_back()
        LabelGroupingPage().click_back()
        LabelGroupingPage().delete_label_groups(group=self.group)
        Preconditions.disconnect_mobile(REQUIRED_MOBILES['IOS-移动'])



    @tags('ALL', 'CONTACT', 'CMCC')
    def test_contacts_quxinli_0363(self):
        """新建分组,标签分组名称输入30个字母"""
        GroupPage = GroupListPage()
        GroupPage.click_new_group()
        GroupPage.click_input_element()
        time.sleep(3)
        self.group='a'*30
        GroupPage.input_content(text=self.group)
        GroupPage.click_sure_element()
        GroupPage.click_allow_button()
        SelectContactsPage().is_element_present(locator='选择一个群')

    def tearDown_test_contacts_quxinli_0363(self):
        SelectContactsPage().click_back()
        LabelGroupingPage().click_back()
        LabelGroupingPage().delete_label_groups(group=self.group)
        Preconditions.disconnect_mobile(REQUIRED_MOBILES['IOS-移动'])



    @tags('ALL', 'CONTACT', 'CMCC')
    def test_contacts_quxinli_0364(self):
        """新建分组,标签分组名称输入31个字母"""
        GroupPage = GroupListPage()
        GroupPage.click_new_group()
        GroupPage.click_input_element()
        time.sleep(3)
        self.group='a'*31
        GroupPage.input_content(text=self.group)
        GroupPage.click_sure_element()
        GroupPage.click_allow_button()
        SelectContactsPage().check_if_element_not_exist(text='选择一个群')


    @tags('ALL', 'debug', 'CMCC')
    def test_contacts_quxinli_0365(self):
        """新建分组,标签分组名称输入29个字符：汉字、数字、英文字母、空格和特殊字符组合"""
        lg = LabelGroupingPage()
        lg.click_new_create_group()
        time.sleep(1)
        lg.click_input_box()
        time.sleep(1)
        text = 'aa111@@@文 aaa111@@@文 aaaa'
        lg.input_search_text(text)
        lg.click_sure()
        SelectContactsPage().page_should_contain_text('选择联系人')

    @tags('ALL', 'debug', 'CMCC')
    def tearDown_test_contacts_quxinli_0365(self):
        SelectContactsPage().click_back()
        LabelGroupingPage().click_back()
        LabelGroupingPage().delete_label_groups(group='aa111@@@文 aaa111@@@文 aaaa')
        Preconditions.disconnect_mobile(REQUIRED_MOBILES['IOS-移动'])



    @tags('ALL', 'debug', 'CMCC')
    def test_contacts_quxinli_0366(self):
        """新建分组,标签分组名称输入30个字符：汉字、数字、英文字母、空格和特殊字符组合"""
        lg = LabelGroupingPage()
        lg.click_new_create_group()
        time.sleep(1)
        lg.click_input_box()
        time.sleep(1)
        text = 'aa111@@@文 aaa111@@@文 aaaaa'
        lg.input_search_text(text)
        lg.click_sure()
        SelectContactsPage().page_should_contain_text('选择联系人')

    @tags('ALL', 'debug', 'CMCC')
    def tearDown_test_contacts_quxinli_0366(self):
        SelectContactsPage().click_back()
        LabelGroupingPage().click_back()
        LabelGroupingPage().delete_label_groups(group='aa111@@@文 aaa111@@@文 aaaaa')
        Preconditions.disconnect_mobile(REQUIRED_MOBILES['IOS-移动'])


    @tags('ALL', 'CONTACT', 'CMCC')
    def test_contacts_quxinli_0367(self):
        """新建分组,标签分组名称输入31个字符：汉字、数字、英文字母、空格和特殊字符组合"""
        GroupPage = GroupListPage()
        GroupPage.click_new_group()
        GroupPage.click_input_element()
        time.sleep(3)
        self.group='aa111@@@文 aaa111@@@文 aaaaaa'
        GroupPage.input_content(text=self.group)
        GroupPage.click_sure_element()
        GroupPage.click_allow_button()
        SelectContactsPage().check_if_element_not_exist(text='选择一个群')
