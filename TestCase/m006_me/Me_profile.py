import random
import re
import time
import unittest
import uuid


from pages.me.MeCallMulti import MeCallMultiPage
from pages.me.MeCardName import MeCardNamePage
from pages.me.MeEditUserProfile import MeEditUserProfilePage
from pages.me.MeViewUserProfile import MeViewUserProfilePage
from pages.me.MeWefare import MeSetWefarePage
from preconditions.BasePreconditions import WorkbenchPreconditions
from preconditions.BasePreconditions import LoginPreconditions

from preconditions.BasePreconditions import LoginPreconditions
from library.core.TestCase import TestCase
from library.core.utils.applicationcache import current_mobile, current_driver, switch_to_mobile
from pages import *
from pages.contacts.EditContactPage import EditContactPage
from library.core.utils.testcasefilter import tags

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


class Meprofile(TestCase):
    """我页面-个人资料"""

    def default_setUp(self):
        Preconditions.make_already_in_message_page()
        MessagePage().open_me_page()
        time.sleep(2)

    def default_tearDown(self):
        Preconditions.disconnect_mobile(REQUIRED_MOBILES['IOS-移动'])


    def test_me_zhangshuli_006(self):
        """进入“编辑资料”界面"""
        me=MePage()
        me.click_view_edit()
        mup = MeViewUserProfilePage()
        mup.click_edit()
        mep = MeEditUserProfilePage()
        mep.wait_for_page_load()
        time.sleep(3)
        # # 4.检验电话不能点击，姓名可以点击
        # self.assertEquals(mep.element_is_click_able("电话"), False)
        # self.assertEquals(mep.element_is_click_able("姓名"), True)
        # 5.检验姓名字符串不超过40个
        name=mep.get_element_text("输入姓名")
        self.assertTrue(len(name) < 41)
        # 6.保存按钮灰色，点击弹框提示
        mep.click_save()
        self.assertTrue(mep.is_on_this_page())
        # 4.点击返回到我的页面
        mep.click_back()
        time.sleep(1)
        mup.click_back()


    @tags('ALL', 'CMCC', 'me_all', 'debug_fk_me1')
    def test_me_zhangshuli_011(self):
        """分享名片-选择一个群"""
        # 0.检验是否跳转到我页面,点击进入查看并编辑资料
        mep = MePage()
        self.assertEquals(mep.is_on_this_page(), True)
        mep.click_view_edit()
        mup = MeViewUserProfilePage()
        time.sleep(2)
        # 1.点击分享名片
        mup.page_up()
        mup.click_share_card()
        scp = SelectContactsPage()
        scp.wait_for_page_load()
        time.sleep(2)
        # 2.点击选择一个群
        scp.click_select_one_group()
        sop = SelectOneGroupPage()
        sop.wait_for_page_load()
        #点击弹框右上角的取消按钮

        # 3.点击第一个群-分享名片
        sop.select_first_group()
        time.sleep(2)
        sop.click_share_card()
        time.sleep(2)


    @tags('ALL', 'CMCC', 'me_all', 'debug_fk_me1')
    def test_me_zhangshuli_012(self):
        """分享名片-选择一个团队联系人"""
        # 0.检验是否跳转到我页面,点击进入查看并编辑资料
        mep = MePage()
        self.assertEquals(mep.is_on_this_page(), True)
        mep.click_view_edit()
        mup = MeViewUserProfilePage()
        time.sleep(2)
        # 1.点击分享名片
        mup.page_up()
        mup.click_share_card()
        scp = SelectContactsPage()
        scp.wait_for_page_load()
        time.sleep(2)

        # 2.点击选择一个团队-分享名片
        scp.click_group_contact()
        time.sleep(2)
        shp = SelectHeContactsPage()
        shp.select_one_team_by_name('ateam7272')
        time.sleep(2)
        sdp = SelectHeContactsDetailPage()
        sdp.wait_for_he_contacts_page_load()
        sdp.select_one_he_contact_by_name('alice')
        time.sleep(1)
        # 点击弹框右上角的取消按钮
        #分享名片
        sdp.click_share_card()
        time.sleep(2)


    @tags('ALL', 'CMCC', 'me_all', 'debug_fk_me1')
    def test_me_zhangshuli_013(self):
        """分享名片-选择团队联系人-通过手机号或姓名搜索团队存在的联系人"""
        # 0.检验是否跳转到我页面,点击进入查看并编辑资料
        mep = MePage()
        self.assertEquals(mep.is_on_this_page(), True)
        mep.click_view_edit()
        mup = MeViewUserProfilePage()
        time.sleep(2)
        # 1.点击分享名片
        mup.page_up()
        mup.click_share_card()
        scp = SelectContactsPage()
        scp.wait_for_page_load()
        time.sleep(2)
        # 2.点击选择一个团队-分享名片
        scp.click_group_contact()
        time.sleep(2)
        shp = SelectHeContactsPage()
        shp.select_one_team_by_name('ateam7272')
        time.sleep(2)
        sdp = SelectHeContactsDetailPage()
        sdp.wait_for_he_contacts_page_load()
        #搜索框输入联系人姓名
        sdp.click_search_box()
        sdp.input_search_text('alice')
        sdp.click_search_result()
        time.sleep(1)
        # 点击弹框右上角的取消按钮
        #点击分享名片
        sdp.click_share_card()
        time.sleep(2)


    @tags('ALL', 'CMCC', 'me_all', 'debug_fk_me1')
    def test_me_zhangshuli_014(self):
        """分享名片-选择团队联系人-通过手机号或姓名搜索我的团队不存在的联系人"""
        # 0.检验是否跳转到我页面,点击进入查看并编辑资料
        mep = MePage()
        self.assertEquals(mep.is_on_this_page(), True)
        mep.click_view_edit()
        mup = MeViewUserProfilePage()
        time.sleep(2)
        # 1.点击分享名片
        mup.page_up()
        mup.click_share_card()
        scp = SelectContactsPage()
        scp.wait_for_page_load()
        time.sleep(2)
        # 2.点击选择一个团队-分享名片
        scp.click_group_contact()
        time.sleep(2)
        shp = SelectHeContactsPage()
        shp.select_one_team_by_name('ateam7272')
        time.sleep(2)
        sdp = SelectHeContactsDetailPage()
        sdp.wait_for_he_contacts_page_load()
        #搜索框输入联系人姓名
        sdp.click_search_box()
        sdp.input_search_text('张无忌')
        sdp.page_down()
        sdp.page_should_contain_text('无搜索结果')
        time.sleep(2)
        # sdp.click_search_result()
        # time.sleep(1)
        # # 点击弹框右上角的取消按钮
        # #点击分享名片
        # sdp.click_share_card()

    @tags('ALL', 'CMCC', 'me_all', 'debug_fk_me1')
    def test_me_zhangshuli_015(self):
        """分享名片-选择团队联系人-通过手机号或姓名搜索我的团队中的自己"""
        # 0.检验是否跳转到我页面,点击进入查看并编辑资料
        mep = MePage()
        self.assertEquals(mep.is_on_this_page(), True)
        mep.click_view_edit()
        mup = MeViewUserProfilePage()
        time.sleep(2)
        # 1.点击分享名片
        mup.page_up()
        mup.click_share_card()
        scp = SelectContactsPage()
        scp.wait_for_page_load()
        time.sleep(2)
        # 2.点击选择一个团队-分享名片
        scp.click_group_contact()
        time.sleep(2)
        shp = SelectHeContactsPage()
        shp.select_one_team_by_name('ateam7272')
        time.sleep(2)
        sdp = SelectHeContactsDetailPage()
        sdp.wait_for_he_contacts_page_load()
        #搜索框输入联系人姓名
        sdp.click_search_box()
        sdp.input_search_text('admin')
        sdp.click_search_result()
        sdp.is_toast_exist('该联系人不可选择')
        # time.sleep(1)
        # # 点击弹框右上角的取消按钮
        # #点击分享名片
        # sdp.click_share_card()

    @tags('ALL', 'CMCC', 'me_all', 'debug_fk_me1')
    def test_me_zhangshuli_016(self):
        """分享名片-选择手机联系人-选择任意联系人（非自己）"""
        # 0.检验是否跳转到我页面,点击进入查看并编辑资料
        mep = MePage()
        self.assertEquals(mep.is_on_this_page(), True)
        mep.click_view_edit()
        mup = MeViewUserProfilePage()
        time.sleep(2)
        # 1.点击分享名片
        mup.page_up()
        mup.click_share_card()
        scp = SelectContactsPage()
        scp.wait_for_page_load()
        time.sleep(2)
        # 2.点击选择一个手机联系人-分享名片
        scp.click_phone_contact()
        time.sleep(2)
        slp=SelectLocalContactsPage()
        slp.swipe_select_one_member_by_name('大佬1')
        time.sleep(2)
        # 点击弹框右上角的取消按钮

        # 分享名片
        slp.click_share_card()
        time.sleep(2)
        self.assertTrue(mup.is_on_this_page())
        time.sleep(2)


    @tags('ALL', 'CMCC', 'me_all', 'debug_fk_me1')
    def test_me_zhangshuli_017(self):
        """分享名片-选择手机联系人-通过姓名关键字或者手机号码搜索在手机通讯录中的联系人（非自己）"""
        # 0.检验是否跳转到我页面,点击进入查看并编辑资料
        mep = MePage()
        self.assertEquals(mep.is_on_this_page(), True)
        mep.click_view_edit()
        mup = MeViewUserProfilePage()
        time.sleep(2)
        # 1.点击分享名片
        mup.page_up()
        mup.click_share_card()
        scp = SelectContactsPage()
        scp.wait_for_page_load()
        time.sleep(2)
        # 2.点击选择一个手机联系人-分享名片
        scp.click_phone_contact()
        time.sleep(2)
        slp=SelectLocalContactsPage()
        slp.click_search_box()
        slp.input_search_keyword('大佬1')
        slp.click_search_result()
        time.sleep(2)
        # 点击弹框右上角的取消按钮

        # 分享名片
        slp.click_share_card()
        time.sleep(2)
        self.assertTrue(mup.is_on_this_page())
        time.sleep(2)

    @tags('ALL', 'CMCC', 'me_all', 'debug_fk_me1')
    def test_me_zhangshuli_018(self):
        """分享名片-选择手机联系人-通过姓名关键字或者手机号码搜索自己"""
        # 0.检验是否跳转到我页面,点击进入查看并编辑资料
        mep = MePage()
        self.assertEquals(mep.is_on_this_page(), True)
        mep.click_view_edit()
        mup = MeViewUserProfilePage()
        time.sleep(2)
        # 1.点击分享名片
        mup.page_up()
        mup.click_share_card()
        scp = SelectContactsPage()
        scp.wait_for_page_load()
        time.sleep(2)
        # 2.点击选择一个手机联系人-分享名片
        scp.click_phone_contact()
        time.sleep(2)
        slp=SelectLocalContactsPage()
        slp.click_search_box()
        slp.input_search_keyword('本机')
        slp.click_search_result()
        time.sleep(2)
        # 点击弹框右上角的取消按钮

        # 分享名片
        slp.is_toast_exist('该联系人不可选择')


    @tags('ALL', 'CMCC', 'me_all', 'debug_fk_me1')
    def test_me_zhangshuli_019(self):
        """分享名片-选择手机联系人-搜索不在本地通讯录的联系人"""
        # 0.检验是否跳转到我页面,点击进入查看并编辑资料
        mep = MePage()
        self.assertEquals(mep.is_on_this_page(), True)
        mep.click_view_edit()
        mup = MeViewUserProfilePage()
        time.sleep(2)
        # 1.点击分享名片
        mup.page_up()
        mup.click_share_card()
        scp = SelectContactsPage()
        scp.wait_for_page_load()
        time.sleep(2)
        # 2.点击选择一个手机联系人-分享名片
        scp.click_phone_contact()
        time.sleep(2)
        slp=SelectLocalContactsPage()
        slp.click_search_box()
        slp.input_search_keyword('张无忌')
        time.sleep(2)
        # 点击弹框右上角的取消按钮

        # 分享名片
        slp.page_down()
        slp.page_should_contain_text('无搜索结果')
        time.sleep(2)











