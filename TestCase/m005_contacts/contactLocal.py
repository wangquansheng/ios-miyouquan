import unittest
import uuid
import time


from library.core.common.simcardtype import CardType
from selenium.common.exceptions import TimeoutException
from library.core.TestCase import TestCase
from library.core.utils.applicationcache import current_mobile, current_driver, switch_to_mobile
from library.core.utils.testcasefilter import tags
from pages import *
from pages.contacts.HeContacts import HeContactsPage
from pages.contacts.official_account import OfficialAccountPage
from pages.contacts.search_official_account import SearchOfficialAccountPage
from pages.contacts.official_account_detail import OfficialAccountDetailPage
from pages.contacts.EditContactPage import EditContactPage
from pages.contacts.components.menu_more import MenuMore
from pages.contacts.local_contact import localContactPage
import preconditions

REQUIRED_MOBILES = {
    'Android-移动': 'M960BDQN229CH',
    'Android-XX': ''  # 用来发短信
}
class Preconditions(object):
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
    def make_already_in_one_key_login_page():
        """
        1、已经进入一键登录页
        :return:
        """
        # 如果当前页面已经是一键登录页，不做任何操作
        one_key = OneKeyLoginPage()
        if one_key.is_on_this_page():
            return

        # 如果当前页不是引导页第一页，重新启动app
        guide_page = GuidePage()
        if not guide_page.is_on_the_first_guide_page():
            current_mobile().launch_app()
            guide_page.wait_for_page_load(20)

        # 跳过引导页
        guide_page.wait_for_page_load(30)
        guide_page.swipe_to_the_second_banner()
        guide_page.swipe_to_the_third_banner()
        guide_page.click_start_the_experience()

        # 点击权限列表页面的确定按钮
        permission_list = PermissionListPage()
        permission_list.click_submit_button()
        one_key.wait_for_page_load(30)

    @staticmethod
    def login_by_one_key_login():
        """
        从一键登录页面登录
        :return:
        """
        # 等待号码加载完成后，点击一键登录
        one_key = OneKeyLoginPage()
        one_key.wait_for_tell_number_load(60)
        login_number = one_key.get_login_number()
        one_key.click_one_key_login()
        one_key.click_read_agreement_detail()

        # 同意协议
        agreement = AgreementDetailPage()
        agreement.click_agree_button()

        # 等待消息页
        message_page = MessagePage()
        message_page.wait_login_success(60)
        return login_number

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
    def create_contacts_if_not_exits(name, number):
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
            Preconditions.make_already_in_message_page(reset_required=False)
            contacts_page.open_contacts_page()
        # 创建联系人
        contacts_page.click_search_box()
        contact_search = ContactListSearchPage()
        contact_search.wait_for_page_load()
        contact_search.input_search_keyword(name)
        if contact_search.is_contact_in_list(name):
            contact_search.click_back()
        else:
            contact_search.click_back()
            contacts_page.click_add()
            create_page = CreateContactPage()
            create_page.hide_keyboard_if_display()
            create_page.create_contact(name, number)
            detail_page.wait_for_page_load()
            detail_page.click_back_icon()


    @staticmethod
    def make_already_in_message_page(reset_required=False):
        """
        前置条件：
        1.已登录客户端
        2.当前在消息页面
        """
        if not reset_required:
            message_page = MessagePage()
            try:
                message_page.wait_until(
                    condition=lambda d: message_page.is_on_this_page(),
                    timeout=3
                )
                return
            except TimeoutException:
                pass
        Preconditions.reset_and_relaunch_app()
        Preconditions.make_already_in_one_key_login_page()
        login_num = Preconditions.login_by_one_key_login()
        return login_num
@unittest.skip("本地调试不执行")
class ContactLocal2(TestCase):
    '''
    通讯录测试记录-陈计祥
    '''
    @classmethod
    def setUpClass(cls):
        # 创建联系人
        fail_time = 0
        import dataproviders

        while fail_time < 3:
            try:
                # 获取需要导入的联系人数据
                required_contacts = dataproviders.get_preset_contacts()

                # 连接手机
                Preconditions.connect_mobile('Android-移动')
                current_mobile().hide_keyboard_if_display()
                # 导入数据
                for name, number in required_contacts:
                    Preconditions.create_contacts_if_not_exits(name, number)

                # 推送resource文件到手机
                dataproviders.push_resource_dir_to_mobile_sdcard(Preconditions.connect_mobile('Android-移动'))
                return
            except:
                fail_time += 1
                import traceback
                msg = traceback.format_exc()
                print(msg)

    @classmethod
    def tearDownClass(cls):
        try:
            Preconditions.connect_mobile('Android-移动')
            current_mobile().hide_keyboard_if_display()
            Preconditions.make_already_in_message_page()
            conts_page = ContactsPage()
            conts_page.open_contacts_page()
            conts_page.click_label_grouping()
            lg = LabelGroupingPage()
            lg.wait_for_page_load()
            lg.delete_all_label()
        except:
            import traceback
            traceback.print_exc()
        try:
            current_mobile().hide_keyboard_if_display()
            Preconditions.make_already_in_message_page()
            cdp = ContactDetailsPage()
            cdp.delete_all_contact()
        except:
            traceback.print_exc()

class ContactLocal(TestCase):
    @staticmethod
    def setUp_test_contacts_0001():
        Preconditions.connect_mobile('Android-移动')
        current_mobile().hide_keyboard_if_display()
        Preconditions.make_already_in_message_page()

    @tags('ALL', 'CONTACTS', 'CMCC')
    def test_contacts_0001(self):
        '''
        搜索输入框校验，通过手机号码搜索，输入数字模糊查询（只搜索一条记录）
        author:yanshunhua

        :return:
        '''
        lcontact=localContactPage()
        GroupPage = GroupListPage()
        GroupPage.open_contacts_page()
        lcontact.click_search_box()
        lcontact.input_search_text()
        lcontact.page_contain_element()
        lcontact.page_contain_element(text='联系人电话')
        lcontact.page_contain_element(text='联系人名字')

    @staticmethod
    def setUp_test_contacts_0002():
        Preconditions.connect_mobile('Android-移动')
        current_mobile().hide_keyboard_if_display()
        Preconditions.background_app()
        time.sleep(3)
        preconditions.launch_app()
        time.sleep(1)

    @tags('ALL', 'CONTACTS', 'CMCC')
    def test_contacts_0002(self):
        '''
        搜索输入框校验，通过手机号码搜索，输入数字模糊查询（搜索多条记录）
        auther:yanshunhua
        :return:
        '''
        lcontact = localContactPage()
        GroupPage = GroupListPage()
        GroupPage.open_contacts_page()
        lcontact.click_search_box()
        time.sleep(1)
        lcontact.input_search_text(text='138')
        time.sleep(1)
        lcontact.hide_keyboard()
        time.sleep(3)
        els=lcontact.get_element_number()
        self.assertTrue(len(els)>1)

    @staticmethod
    def setUp_test_contacts_0003():
        Preconditions.connect_mobile('Android-移动')
        current_mobile().hide_keyboard_if_display()
        Preconditions.background_app()
        time.sleep(3)
        preconditions.launch_app()
        time.sleep(1)

    @tags('ALL', 'CONTACTS', 'CMCC')
    def test_contacts_0003(self):
        '''
        搜索输入框校验，通过手机号码搜索，输入手机号码全匹配查询
        auther:yanshunhua
        :return:
        '''
        lcontact = localContactPage()
        GroupPage = GroupListPage()
        GroupPage.open_contacts_page()
        lcontact.click_search_box()
        time.sleep(1)
        lcontact.input_search_text(text='13800138005')
        time.sleep(1)
        lcontact.hide_keyboard()
        time.sleep(3)
        lcontact.page_contain_element()
        lcontact.page_contain_element(text='联系人电话')
        lcontact.page_contain_element(text='联系人名字')

    @staticmethod
    def setUp_test_contacts_0005():
        Preconditions.connect_mobile('Android-移动')
        current_mobile().hide_keyboard_if_display()
        Preconditions.background_app()
        time.sleep(3)
        preconditions.launch_app()
        time.sleep(1)

    @tags('ALL', 'CONTACTS', 'CMCC')
    def test_contacts_0005(self):
        '''
        搜索输入框校验，通过名称搜索，输入名称模糊查询（搜索多条记录）
        auther:yanshunhua
        :return:
        '''
        lcontact = localContactPage()
        GroupPage = GroupListPage()
        GroupPage.open_contacts_page()
        lcontact.click_search_box()
        time.sleep(1)
        lcontact.input_search_text(text='1-a')
        time.sleep(1)
        lcontact.hide_keyboard()
        time.sleep(3)
        els = lcontact.get_element_number()
        self.assertTrue(len(els) > 1)

    @staticmethod
    def setUp_test_contacts_0006():
        Preconditions.connect_mobile('Android-移动')
        current_mobile().hide_keyboard_if_display()
        Preconditions.background_app()
        time.sleep(3)
        preconditions.launch_app()
        time.sleep(1)

    @tags('ALL', 'CONTACTS', 'CMCC')
    def test_contacts_0006(self):
        '''
        搜索输入框校验，通过名称搜索，输入名称全匹配搜索（搜索多条记录）
        auther:yanshunhua
        :return:
        '''
        lcontact = localContactPage()
        GroupPage = GroupListPage()
        GroupPage.open_contacts_page()
        lcontact.click_search_box()
        time.sleep(1)
        lcontact.input_search_text(text='1-a子')
        time.sleep(1)
        lcontact.hide_keyboard()
        time.sleep(3)
        els = lcontact.get_element_number()
        self.assertTrue(len(els) > 1)

    @staticmethod
    def setUp_test_contacts_0004():
        Preconditions.connect_mobile('Android-移动')
        current_mobile().hide_keyboard_if_display()
        Preconditions.background_app()
        time.sleep(3)
        preconditions.launch_app()
        time.sleep(1)

    @tags('ALL', 'CONTACTS', 'CMCC')
    def test_contacts_0004(self):
        '''
        搜索输入框校验，通过名称（中文）搜索，输入名称模糊查询（搜索多条记录）
        auther:yanshunhua
        :return:
        '''
        lcontact = localContactPage()
        GroupPage = GroupListPage()
        GroupPage.open_contacts_page()
        lcontact.click_search_box()
        time.sleep(1)
        lcontact.input_search_text(text='大佬')
        time.sleep(1)
        lcontact.hide_keyboard()
        time.sleep(3)
        els = lcontact.get_element_number()
        self.assertTrue(len(els) > 1)


