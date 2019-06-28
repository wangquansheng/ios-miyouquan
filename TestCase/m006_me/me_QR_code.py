import time
from library.core.TestCase import TestCase
from library.core.utils.applicationcache import current_mobile, current_driver, switch_to_mobile
from pages import *
from preconditions.BasePreconditions import LoginPreconditions
import warnings

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


class MyQRcodePageTest(TestCase):
    """我的二维码页面"""

    def default_setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        Preconditions.make_already_in_message_page()
        MessagePage().open_me_page()
        time.sleep(2)

    def default_tearDown(self):
        Preconditions.disconnect_mobile(REQUIRED_MOBILES['IOS-移动'])

    def test_me_zhangshuli_060(self):
        """我的二维码分享-非手机号码的数字搜索"""
        me = MePage()
        me.click_qr_code_icon()
        # 进入我的二维码界面
        qr_code = MyQRCodePage()
        qr_code.click_forward_qr_code()
        time.sleep(2)
        select=SelectContactsPage()
        time.sleep(2)
        select.page_contain_element(locator='最近聊天')
        select.page_should_contain_text('搜索或输入手机号')
        select.check_if_element_not_exist(text='清空搜索文本')
        # 搜索联系人-有搜索结果
        select.click_search_contact()
        select.input_search_keyword('13800')
        time.sleep(2)
        select.check_if_element_exist(text='清空搜索文本')
        select.check_if_element_exist(text='搜索团队联系人入口')
        select.check_if_element_exist(text='搜索结果列表1')
        self.assertTrue(select.is_keyboard_shown())
        # 无搜索结果时
        select.click_x_icon()
        select.input_search_keyword('张无忌')
        select.check_if_element_exist(text='搜索团队联系人入口')
        select.check_if_element_not_exist(text='搜索结果列表1')


    def test_me_zhangshuli_061(self):
        """我的二维码分享-无本地结果且二次查询无结果"""
        me=MePage()
        me.click_qr_code_icon()
        # 进入我的二维码界面
        qr_code = MyQRCodePage()
        qr_code.click_forward_qr_code()
        time.sleep(2)
        select=SelectContactsPage()
        time.sleep(2)
        select.page_contain_element(locator='最近聊天')
        select.click_search_contact()
        select.input_search_keyword('张无忌')
        select.check_if_element_exist(text='搜索团队联系人入口')
        select.click_element_by_id(text='搜索团队联系人入口')
        time.sleep(2)
        select.page_should_contain_text('无搜索结果')


    def test_me_zhangshuli_062(self):
        """我的二维码分享-搜索未保存在本地的手机号码"""
        me=MePage()
        me.click_qr_code_icon()
        # 进入我的二维码界面
        qr_code = MyQRCodePage()
        qr_code.click_forward_qr_code()
        time.sleep(2)
        select=SelectContactsPage()
        time.sleep(2)
        select.page_contain_element(locator='最近聊天')
        # 顶部搜索框搜索
        select.click_search_contact()
        select.input_search_keyword('19674361585')
        select.check_if_element_exist(text='网络搜索结果')
        # 点击取消发送
        select.click_element_by_id(text='网络搜索结果')
        time.sleep(1)
        select.click_cancel_send()
        time.sleep(2)
        select.check_if_element_not_exist(text='确定发送')
        select.page_contain_element(locator='搜索团队联系人入口')
        # 点击确定发送
        time.sleep(2)
        select.click_element_by_id(text='网络搜索结果')
        select.click_sure_send()
        time.sleep(1)
        self.assertTrue(qr_code.is_on_this_page())



    def test_me_zhangshuli_063(self):
        """我的二维码分享-搜索未保存在本地的手机号码"""
        me=MePage()
        me.click_qr_code_icon()
        # 进入我的二维码界面
        qr_code = MyQRCodePage()
        qr_code.click_forward_qr_code()
        time.sleep(2)
        select=SelectContactsPage()
        time.sleep(2)
        select.page_contain_element(locator='最近聊天')
        select.click_search_contact()
        select.input_search_keyword('19674361585')
        select.check_if_element_exist(text='网络搜索结果')
        # 点击取消发送
        time.sleep(1)
        select.page_down()
        select.click_element_by_id(text='网络搜索结果')
        select.click_cancel_send()
        time.sleep(2)
        select.check_if_element_not_exist(text='确定发送')
        select.page_contain_element(locator='搜索团队联系人入口')
        # 点击确定发送
        select.click_element_by_id(text='网络搜索结果')
        select.click_sure_send()
        time.sleep(1)
        self.assertTrue(qr_code.is_on_this_page())


    def test_me_zhangshuli_064(self):
        """我的二维码分享-手机联系人搜索结果页面顶部搜索"""
        me=MePage()
        me.click_qr_code_icon()
        # 进入我的二维码界面
        qr_code = MyQRCodePage()
        qr_code.click_forward_qr_code()
        time.sleep(2)
        select=SelectContactsPage()
        time.sleep(2)
        select.page_contain_element(locator='最近聊天')
        select.click_search_contact()
        select.input_search_keyword('大佬')
        select.page_down()
        select.check_if_element_exist(text='清空搜索文本')
        select.check_if_element_exist(text='搜索团队联系人入口')
        select.check_if_element_exist(text='搜索结果列表1')
        # 无搜索结果时
        select.click_x_icon()
        select.input_search_keyword('张无忌')
        select.check_if_element_exist(text='搜索团队联系人入口')
        select.check_if_element_not_exist(text='搜索结果列表1')


    def test_me_zhangshuli_065(self):
        """我的二维码分享-搜索字母特殊字符关数字，手机号等关键字有群聊结果"""
        me=MePage()
        me.click_qr_code_icon()
        # 进入我的二维码界面
        qr_code = MyQRCodePage()
        qr_code.click_forward_qr_code()
        time.sleep(2)
        select=SelectContactsPage()
        time.sleep(2)
        select.page_contain_element(locator='最近聊天')
        # 顶部搜索框搜索
        select.click_search_contact()
        select.input_search_keyword('给个红包')
        select.page_down()
        # 搜索结果多余3条
        select.check_if_element_exist(text='清空搜索文本')
        select.check_if_element_exist(text='搜索团队联系人入口')
        select.page_should_contain_text('群聊')
        select.page_contain_element(locator='查看更多')
