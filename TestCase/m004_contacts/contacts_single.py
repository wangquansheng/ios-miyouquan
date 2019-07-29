import unittest
import uuid
import time
import warnings

from selenium.common.exceptions import NoSuchElementException
from library.core.TestCase import TestCase
from library.core.utils.applicationcache import current_mobile, switch_to_mobile
from library.core.utils.testcasefilter import tags

from pages.components.Footer import FooterPage
from pages import *

from preconditions.BasePreconditions import LoginPreconditions


REQUIRED_MOBILES = {
    'Android-移动': 'M960BDQN229CH',
    'IOS-移动': 'iphone',
    'IOS-移动-移动': 'iphone_d',
    'Android-电信': 'single_telecom',
    'Android-联通': 'single_union',
    'Android-移动-联通': 'mobile_and_union',
    'Android-移动-电信': '',
    'Android-移动-移动': 'double_mobile',
    'Android-XX-XX': 'others_double',
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
    def make_already_in_call_page(reset=False):
        """确保应用在通话页面"""
        # LoginPreconditions.select_mobile('IOS-移动', reset)
        current_mobile().hide_keyboard_if_display()
        time.sleep(1)
        # 如果在消息页，不做任何操作
        call_page = CallPage()
        if call_page.is_on_this_page():
            return

    # @staticmethod
    # def terminate_app():
    #     """
    #     强制关闭app,退出后台
    #     :return:
    #     """
    #     app_id = current_driver().desired_capability['appPackage']
    #     current_mobile().termiate_app(app_id)
    #
    # @staticmethod
    # def background_app():
    #     """后台运行"""
    #     current_mobile().press_home_key()


class ContactlocalPage(TestCase):
    """本地通讯录界面"""

    def default_setUp(self):
        """确保每个用例开始之前在通讯录界面"""
        warnings.simplefilter('ignore', ResourceWarning)
        Preconditions.connect_mobile('IOS-移动')
        Preconditions.make_already_in_call_page()
        FooterPage().open_contacts_page()
        # # 开通权限
        # contact = ContactsPage()
        # contact.permission_box_processing()
        # contact.remove_mask(1)

    def default_tearDown(self):
        Preconditions.disconnect_mobile(REQUIRED_MOBILES['IOS-移动'])
        # 关闭idevice log
        FooterPage().kill_device_syslog()

    @tags('ALL', 'CMCC', 'contact')
    def test_member_001(self):
        """
        1、联网正常
        2、已登陆客户端
        3、在家庭网-联系人详情页面
        查看联系人详情元素	显示：头像，备注名，视频icon、电话icon，手机号码长号和归属地；备注名旁边有编辑icon，
        点击进入备注名修改页面,短号和更多，福利电话规则说明入口（未注册的用户，底部有“邀请使用”按钮）
        :return:
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 展开家庭网
        if not contact_page.if_home_net_expand():
            contact_page.click_locator_key('通讯录_家庭网_展开')
            time.sleep(2)
        # 点击家庭网第一个联系人
        contact_page.get_elements_list_click('家庭网_列表文本1')
        time.sleep(3)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_头像'), True)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_用户名'), True)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_电话按钮'), True)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_视频按钮'), True)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_设置备注名'), True)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_备注修改'), True)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_手机号码'), True)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_短号'), True)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_短号内容'), True)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_更多'), True)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_更多编辑'), True)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_电话规则'), True)
        # self.assertEqual(contact_page.is_element_already_exist('联系人_添加桌面'), True)
        # self.assertEqual(contact_page.is_element_already_exist('联系人_归属地'), True)

    @tags('ALL', 'CMCC', 'contact')
    def test_member_002(self):
        """
        1、联网正常
        2、已登陆客户端
        3、在家庭网-家庭网详情页面
        "	"1、点击编辑按钮
        2、点击取消按钮"	"1、跳转到备注名编辑页
        2、返回到家庭网详情页面"
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 展开家庭网
        if not contact_page.if_home_net_expand():
            contact_page.click_locator_key('通讯录_家庭网_展开')
            time.sleep(1)
        # 点击家庭网第一个联系人
        contact_page.get_elements_list_click('家庭网_列表文本1')
        time.sleep(3)
        contact_page.click_locator_key('家庭网_详细_备注修改')
        time.sleep(0.5)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_备注修改_标题'), True)
        time.sleep(1)
        contact_page.click_locator_key('家庭网_备注修改_返回')
        time.sleep(1)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_用户名'), True)

    @tags('ALL', 'CMCC', 'contact')
    def test_member_003(self):
        """
        1、联网正常
        2、已登陆客户端
        3、在家庭网-家庭网详情页面
        1、点击编辑按钮
        2、编辑任意内容，点击保存"	"1、跳转到备注名编辑页
        2、并回退到家庭网详情页面；用户名展示优先级：
        备注名（存在服务端）>个人中心昵称>本地通讯录>家庭网名>短号
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 展开家庭网
        if not contact_page.if_home_net_expand():
            contact_page.click_locator_key('通讯录_家庭网_展开')
            time.sleep(1)
        # 点击家庭网第一个联系人
        contact_page.get_elements_list_click('家庭网_列表文本1')
        time.sleep(2)
        contact_page.click_locator_key('家庭网_详细_备注修改')
        time.sleep(0.5)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_备注修改_标题'), True)
        contact_page.click_input_clear()
        name = uuid.uuid4().__str__().replace('-', '')
        contact_page.input_locator_text('家庭网_备注修改_文本框', name)
        time.sleep(1)
        contact_page.click_locator_key('家庭网_备注修改_完成')
        time.sleep(1)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_用户名'), True)

    @tags('ALL', 'CMCC', 'contact')
    def test_member_004(self):
        """特殊字符适配"""
        """
        1、联网正常
        2、已登陆客户端
        3、在家庭网详情-编辑资料页面
        正确输入并点击保存（中文、英文、特殊符号）	保存成功
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 展开家庭网
        if not contact_page.if_home_net_expand():
            contact_page.click_locator_key('通讯录_家庭网_展开')
            time.sleep(1)
        # 点击家庭网第一个联系人
        contact_page.get_elements_list_click('家庭网_列表文本1')
        time.sleep(1)
        contact_page.click_locator_key('家庭网_详细_备注修改')
        time.sleep(0.5)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_备注修改_标题'), True)
        contact_page.click_input_clear()
        name = '中文备注'
        contact_page.input_locator_text('家庭网_备注修改_文本框', name)
        contact_page.click_locator_key('家庭网_备注修改_完成')
        time.sleep(0.5)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_备注名文本'), True)
        self.assertEqual(name == contact_page.get_element_text('家庭网_详细_备注名文本'), True)
        time.sleep(0.5)
        contact_page.click_locator_key('家庭网_详细_备注修改')
        time.sleep(1)
        contact_page.click_input_clear()
        name = 'EnglishNickName'
        contact_page.input_locator_text('家庭网_备注修改_文本框', name)
        contact_page.click_locator_key('家庭网_备注修改_完成')
        time.sleep(0.5)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_备注名文本'), True)
        self.assertEqual(name == contact_page.get_element_text('家庭网_详细_备注名文本'), True)
        time.sleep(0.5)
        contact_page.click_locator_key('家庭网_详细_备注修改')
        time.sleep(1)
        contact_page.click_input_clear()
        name = '!@#$%^&*('
        contact_page.input_locator_text('家庭网_备注修改_文本框', name)
        time.sleep(0.5)
        contact_page.click_locator_key('家庭网_备注修改_完成')
        time.sleep(0.5)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_备注名文本'), True)

    @tags('ALL', 'CMCC', 'contact')
    def test_member_006(self):
        """
            1、联网正常
            2、已登陆客户端
            3、在家庭网详情-编辑资料页面
            输入空格并点击保存	使用原来名称
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 展开家庭网
        if not contact_page.if_home_net_expand():
            contact_page.click_locator_key('通讯录_家庭网_展开')
            time.sleep(1)
        # 点击家庭网第一个联系人
        contact_page.get_elements_list_click('家庭网_列表文本1')
        time.sleep(3)
        # 修改备注
        contact_page.click_locator_key('家庭网_详细_备注修改')
        self.assertEqual(contact_page.is_element_already_exist('家庭网_备注修改_标题'), True)
        # 清空输入框内容∂
        contact_page.click_input_clear()
        name = '   '
        contact_page.input_locator_text('家庭网_备注修改_文本框', name)
        contact_page.click_locator_key('家庭网_备注修改_完成')
        try:
            contact_page.get_one_element_c('家庭网_详细_备注名文本')
        except NoSuchElementException:
            print("Pass")
        except Exception:
            raise RuntimeError('测试失败')

    @tags('ALL', 'CMCC', 'contact')
    def test_member_007(self):
        """
            1、联网正常
            2、已登陆客户端
            3、在家庭网详情-编辑资料页面
            输入空格并点击保存	使用原来名称
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 展开家庭网
        if not contact_page.if_home_net_expand():
            contact_page.click_locator_key('通讯录_家庭网_展开')
            time.sleep(1)
        # 点击家庭网第一个联系人
        contact_page.get_elements_list_click('家庭网_列表文本1')
        time.sleep(3)
        # 修改备注
        contact_page.click_locator_key('家庭网_详细_备注修改')
        self.assertEqual(contact_page.is_element_already_exist('家庭网_备注修改_标题'), True)
        # 清空输入框内容
        time.sleep(1)
        contact_page.click_input_clear()
        name = 'select now()'
        contact_page.input_locator_text('家庭网_备注修改_文本框', name)
        contact_page.click_locator_key('家庭网_备注修改_完成')
        time.sleep(1)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_备注名文本'), True)
        self.assertEqual(name == contact_page.get_element_text('家庭网_详细_备注名文本'), True)

    @tags('ALL', 'CMCC', 'contact')
    def test_member_008(self):
        """
            1、联网正常
            2、已登陆客户端
            3、在家庭网详情-编辑资料页面
            输入html标签并点击保存	保存成功
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 展开家庭网
        if not contact_page.if_home_net_expand():
            contact_page.click_locator_key('通讯录_家庭网_展开')
            time.sleep(1)
        # 点击家庭网第一个联系人
        contact_page.get_elements_list_click('家庭网_列表文本1')
        time.sleep(3)
        # 修改备注
        contact_page.click_locator_key('家庭网_详细_备注修改')
        self.assertEqual(contact_page.is_element_already_exist('家庭网_备注修改_标题'), True)
        # 清空输入框内容
        time.sleep(1)
        contact_page.click_input_clear()
        name = "<a href='baidu.com'>aa</a>"
        contact_page.input_locator_text('家庭网_备注修改_文本框', name)
        time.sleep(1)
        contact_page.click_locator_key('家庭网_备注修改_完成')
        contact_page.is_toast_exist('备注失败，请重新输入', timeout=5)

    @tags('ALL', 'CMCC', 'contact')
    def test_member_009(self):
        """
            正确输入并点击保存	保存失败
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 展开家庭网
        if not contact_page.if_home_net_expand():
            contact_page.click_locator_key('通讯录_家庭网_展开')
            time.sleep(1)
        # 点击家庭网第一个联系人
        contact_page.get_elements_list_click('家庭网_列表文本1')
        time.sleep(3)
        # 修改备注
        contact_page.click_locator_key('家庭网_详细_备注修改')
        self.assertEqual(contact_page.is_element_already_exist('家庭网_备注修改_标题'), True)
        # 清空输入框内容
        contact_page.click_input_clear()
        name = '正确的备注'
        contact_page.input_locator_text('家庭网_备注修改_文本框', name)
        contact_page.click_locator_key('家庭网_备注修改_完成')
        time.sleep(1)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_备注名文本'), True)
        self.assertEqual(name == contact_page.get_element_text('家庭网_详细_备注名文本'), True)

    @tags('ALL', 'CMCC', 'contact')
    def test_member_0010(self):
        """
            正确输入并点击保存	保存失败
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 展开家庭网
        if not contact_page.if_home_net_expand():
            contact_page.click_locator_key('通讯录_家庭网_展开')
            time.sleep(1)
        # 点击家庭网第一个联系人
        contact_page.get_elements_list_click('家庭网_列表文本1')
        time.sleep(3)
        # 修改备注
        contact_page.click_locator_key('家庭网_详细_备注修改')
        self.assertEqual(contact_page.is_element_already_exist('家庭网_备注修改_标题'), True)
        # 清空输入框内容
        time.sleep(1)
        contact_page.click_input_clear()
        name = '正确的备注'
        contact_page.input_locator_text('家庭网_备注修改_文本框', name)
        contact_page.click_locator_key('家庭网_备注修改_完成')
        time.sleep(1)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_备注名文本'), True)
        self.assertEqual(name == contact_page.get_element_text('家庭网_详细_备注名文本'), True)

    # @tags('ALL', 'CMCC')
    # def test_member_0011(self):
    #     """
    #         1、联网正常
    #         2、已登陆客户端
    #         3、在家庭网-家庭网详情页面
    #         1、点击福利电话说明规则字体按钮
    #         2、点击返回按钮"	"1、跳转至电话规则H5页面
    #         2、返回家庭网详情页面
    #     """
    #     contact_page = ContactsPage()
    #     # 确保在通讯录界面
    #     self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
    #     # 展开家庭网
    #     if not contact_page.if_home_net_expand():
    #         contact_page.click_locator_key('通讯录_家庭网_展开')
    #         time.sleep(1)
    #     # 点击家庭网第一个联系人
    #     contact_page.get_elements_list_click('家庭网_列表文本1')
    #     time.sleep(3)
    #     # 验证规则
    #     contact_page.click_locator_key('联系人_规则')
    #     time.sleep(1)
    #     self.assertEqual(contact_page.is_element_already_exist('联系人_规则说明'), True)
    #     time.sleep(1)
    #     contact_page.click_locator_key('联系人_规则返回')
    #     time.sleep(0.5)
    #     self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_用户名'), True)

    @tags('ALL', 'CMCC', 'contact')
    def test_member_0011(self):
        """
            1、联网正常
            2、已登陆客户端
            3、在家庭网详情-编辑资料页面
            1、点击通话入口；
            2、在家庭网列表点成员电话icon"	呼叫页面显示成员短号
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 展开家庭网
        if not contact_page.if_home_net_expand():
            contact_page.click_locator_key('通讯录_家庭网_展开')
            time.sleep(1)
        # 点击家庭网第一个联系人
        contact_page.get_elements_list_click('家庭网_列表文本1')
        time.sleep(3)
        # 拨打电话
        contact_page.click_locator_key('家庭网_详细_电话按钮')
        time.sleep(0.5)
        contact_page.click_locator_key('呼叫')
        try:
            self.assertEqual(len(contact_page.get_element_text('呼叫_电话号码')) < 11, True)
        finally:
            try:
                time.sleep(3)
                if contact_page.is_element_already_exist('短信_关闭'):
                    contact_page.click_locator_key('短信_关闭')
            except Exception:
                pass
            try:
                contact_page.click_locator_key('呼叫_结束通话')
            except Exception:
                pass

    @tags('ALL', 'CMCC', 'contact')
    def test_member_0012(self):
        """
            1、联网正常
            2、已登陆客户端
            3、在家庭网详情-编辑资料页面
            1、点击通话入口；
            2、在家庭网列表点成员电话icon"	呼叫页面显示成员短号
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 展开家庭网
        if not contact_page.if_home_net_expand():
            contact_page.click_locator_key('通讯录_家庭网_展开')
            time.sleep(1)
        # 点击家庭网第一个联系人
        contact_page.get_elements_list_click('家庭网_列表文本1')
        time.sleep(3)
        # 修改备注
        contact_page.click_locator_key('家庭网_详细_备注修改')
        time.sleep(1)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_备注修改_标题'), True)
        # 清空输入框内容
        contact_page.click_input_clear()
        name = '修改的备注'
        contact_page.input_locator_text('家庭网_备注修改_文本框', name)
        contact_page.click_locator_key('家庭网_备注修改_完成')
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_备注名文本'), True)
        # 拨打电话
        contact_page.click_locator_key('家庭网_详细_电话按钮')
        time.sleep(0.5)
        contact_page.click_locator_key('呼叫')
        # if contact_page.is_element_already_exist('流量_提示内容'):
        #     contact_page.click_locator_key('流量_继续拨打')
        try:
            self.assertEqual(len(contact_page.get_element_text('呼叫_电话号码')) < 11, True)
        finally:
            try:
                time.sleep(4)
                if contact_page.is_element_already_exist('短信_关闭'):
                    contact_page.click_locator_key('短信_关闭')
            except Exception:
                pass
            try:
                contact_page.click_locator_key('呼叫_结束通话')
            except Exception:
                pass

    @tags('ALL', 'CMCC', 'contact')
    def test_member_0013(self):
        """
            1、联网正常
            2、已登陆客户端
            3、在家庭网详情-编辑资料页面
            1、点击通话入口；
            2、在家庭网列表点成员电话icon"	呼叫页面显示成员短号
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 展开家庭网
        if not contact_page.if_home_net_expand():
            contact_page.click_locator_key('通讯录_家庭网_展开')
            time.sleep(1)
        # 点击家庭网第一个联系人
        contact_page.get_elements_list_click('家庭网_列表文本1')
        time.sleep(3)
        # 修改备注
        contact_page.click_locator_key('家庭网_详细_备注修改')
        time.sleep(0.5)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_备注修改_标题'), True)
        # 清空输入框内容
        contact_page.click_input_clear()
        name = '修改的备注'
        contact_page.input_locator_text('家庭网_备注修改_文本框', name)
        contact_page.click_locator_key('家庭网_备注修改_完成')
        time.sleep(1)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_备注名文本'), True)
        # 拨打电话
        contact_page.click_locator_key('家庭网_详细_电话按钮')
        time.sleep(0.5)
        contact_page.click_locator_key('呼叫')
        # if contact_page.is_element_already_exist('流量_提示内容'):
        #     contact_page.click_locator_key('流量_继续拨打')
        try:
            self.assertEqual(len(contact_page.get_element_text('呼叫_电话号码')) < 11, True)
        finally:
            try:
                time.sleep(4)
                if contact_page.is_element_already_exist('短信_关闭'):
                    contact_page.click_locator_key('短信_关闭')
            except Exception:
                pass
            try:
                contact_page.click_locator_key('呼叫_结束通话')
            except Exception:
                pass

    @tags('ALL', 'CMCC', 'contact')
    def test_member_0016(self):
        """
            1、联网正常
            2、已登陆客户端
            3、在通讯录-不限时长详情页面
            点击不限时长成员头像	弹出拨打电话提示
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        time.sleep(2)
        self.assertEqual(contact_page.is_element_already_exist('通讯录_不限时长列表1') > 0, True)
        contact_page.get_elements_list_click('通讯录_不限时长列表1')
        time.sleep(3)
        contact_page.click_locator_key('飞信电话_我知道了')
        time.sleep(4)
        n = 20
        flag = False
        while n > 0:
            if contact_page.is_element_already_exist('飞信电话_缩小') \
                    or contact_page.is_element_already_exist('飞信电话_拒绝')\
                    or contact_page.is_element_already_exist('飞信电话_备注'):
                flag = True
                break
            time.sleep(0.5)
            n -= 1
        try:
            self.assertEqual(flag, True)
        finally:
            # 飞信电话 拒绝
            time.sleep(5)
            try:
                if contact_page.is_element_already_exist('飞信电话_拒绝'):
                    contact_page.click_locator_key('飞信电话_拒绝')
                    time.sleep(1)
            except:
                pass
            try:
                contact_page.click_locator_key('飞信电话_挂断')
            except:
                pass

    @tags('ALL', 'CMCC', 'contact')
    def test_member_0028(self):
        """
            1、联网正常
            2、已登陆客户端
            3、在家庭网详情-编辑资料页面
            输入html标签并点击保存	保存成功
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 展开家庭网
        if not contact_page.if_home_net_expand():
            contact_page.click_locator_key('通讯录_家庭网_展开')
            time.sleep(1)
        # 点击家庭网第一个联系人
        contact_page.get_elements_list_click('家庭网_列表文本1')
        time.sleep(3)
        # 修改备注
        contact_page.click_locator_key('家庭网_详细_备注修改')
        time.sleep(1)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_备注修改_标题'), True)
        contact_page.click_locator_key('家庭网_备注修改_返回')
        time.sleep(1)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_备注名文本'), True)

    @tags('ALL', 'CMCC', 'contact')
    def test_member_0029(self):
        """
            1、联网正常
            2、已登陆客户端
            3、在家庭网详情-编辑资料页面
            输入空格并点击保存	使用原来名称
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 展开家庭网
        if not contact_page.if_home_net_expand():
            contact_page.click_locator_key('通讯录_家庭网_展开')
            time.sleep(1)
        # 点击家庭网第一个联系人
        contact_page.get_elements_list_click('家庭网_列表文本1')
        time.sleep(3)
        # 修改备注
        contact_page.click_locator_key('家庭网_详细_备注修改')
        time.sleep(1)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_备注修改_标题'), True)
        # 清空输入框内容
        contact_page.click_input_clear()
        name = '   '
        contact_page.input_locator_text('家庭网_备注修改_文本框', name)
        time.sleep(1)
        contact_page.click_locator_key('家庭网_备注修改_完成')
        try:
            time.sleep(2)
            contact_page.get_one_element('家庭网_详细_备注名文本')
        except NoSuchElementException:
            print("Pass")
        except Exception:
            raise RuntimeError('测试失败')

    @tags('ALL', 'CMCC', 'contact')
    def test_member_0036(self):
        """
            家庭网用户非首次登陆APP，密友圈模块显示情况
            1.已登录APP
            2.网络正常"	1.点击通讯录模块	1.家庭网成员正常加载
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 展开家庭网
        if not contact_page.if_home_net_expand():
            contact_page.click_locator_key('通讯录_家庭网_展开')
            time.sleep(1)
        # 点击家庭网第一个联系人
        self.assertEqual(contact_page.get_elements_count('家庭网_列表电话1') > 0, True)

    @tags('ALL', 'CMCC', 'contact')
    def test_member_0037(self):
        """
            1、正常登陆
            2、网络正常
            3、当前页面为家庭网页面
            4、已加入家庭网，等待了24小时"	查看家庭网成员显示	"密友成员改为列表展示，列表项分为左右两个区域：
            （1）左区域为信息展示区域，展示用户头像、用户名、手机号码。点击该区域进入家庭网成员详情页面。
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 展开家庭网
        if not contact_page.if_home_net_expand():
            contact_page.click_locator_key('通讯录_家庭网_展开')
            time.sleep(1)
        # 点击家庭网第一个联系人
        contact_page.get_elements_list_click('家庭网_列表文本1')
        time.sleep(1)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_用户名'), True)

    @tags('ALL', 'CMCC', 'contact')
    def test_member_0042(self):
        """输入框只能输入数字异常"""
        """
            1、正常登陆
            2、网络正常
            3、当前页面为家庭网成员页面
            4、已开通家庭网业务"	点击"添加成员"按钮	"（1）输入手机号码：输入框文字引导用户输入11位中国移动号码。输入框只能输入数字。
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 展开家庭网
        if not contact_page.if_home_net_expand():
            contact_page.click_locator_key('通讯录_家庭网_展开')
            time.sleep(1)
        # 点击家庭网第一个联系人
        contact_page.click_locator_key('通讯录_家庭网_管理')
        time.sleep(1.5)
        contact_page.click_locator_key('家庭网_管理_添加')
        contact_page.input_locator_text('家庭网_添加_文本', '15FSsFS%&dfg12sfdf54sfds11')
        # 判断是否为数字
        text_home = contact_page.get_element_text('家庭网_添加_文本')
        self.assertEqual(text_home is not None and text_home.isdigit(), True)

    # @tags('ALL', 'CMCC', 'contact')
    # def test_member_0042(self):
    #     """
    #         1、正常登陆
    #         2、网络正常
    #         3、当前页面为家庭网成员页面
    #         4、已开通家庭网业务"	点击"添加成员"按钮	"（1）输入手机号码：输入框文字引导用户输入11位中国移动号码。输入框只能输入数字。
    #     """
    #     contact_page = ContactsPage()
    #     # 确保在通讯录界面
    #     self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
    #     # 展开家庭网
    #     if not contact_page.if_home_net_expand():
    #         contact_page.click_locator_key('通讯录_家庭网_展开')
    #         time.sleep(1)
    #     # 点击家庭网第一个联系人
    #     contact_page.click_locator_key('通讯录_家庭网_管理')
    #     time.sleep(1)
    #     contact_page.click_locator_key('家庭网_管理_添加')
    #     time.sleep(1)
    #     contact_page.click_locator_key('家庭网_添加_通讯录')
    #     time.sleep(0.5)
    #     self.assertEqual(contact_page.is_text_present('选择号码'), True)

    @tags('ALL', 'CMCC', 'contact')
    def test_member_0046(self):
        """
            1、正常登陆
            2、网络正常
            3、当前页面为家庭网成员页面
            4、已开通家庭网业务"	点击"添加成员"按钮	"（1）输入手机号码：输入框文字引导用户输入11位中国移动号码。输入框只能输入数字。
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 展开家庭网
        if not contact_page.if_home_net_expand():
            contact_page.click_locator_key('通讯录_家庭网_展开')
            time.sleep(1)
        # 点击家庭网第一个联系人
        contact_page.click_locator_key('通讯录_家庭网_管理')
        time.sleep(1)
        contact_page.click_locator_key('家庭网_管理_添加')
        time.sleep(1)
        contact_page.click_locator_key('家庭网_添加_通讯录')
        time.sleep(1.5)
        self.assertEqual(contact_page.is_text_present('选择联系人'), True)
        contact_page.input_locator_text('家庭网_添加_通讯录_搜索框', '1477597')
        time.sleep(1)
        self.assertEqual(contact_page.get_elements_count('家庭网_添加_通讯录_搜索列表1') > 0, True)

    @tags('ALL', 'CMCC', 'contact')
    def test_member_0047(self):
        """
            1、正常登陆
            2、网络正常
            3、当前页面为家庭网成员页面
            4、已开通家庭网业务"	点击"添加成员"按钮	"（1）输入手机号码：输入框文字引导用户输入11位中国移动号码。输入框只能输入数字。
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 展开家庭网
        if not contact_page.if_home_net_expand():
            contact_page.click_locator_key('通讯录_家庭网_展开')
            time.sleep(1)
        # 点击家庭网第一个联系人
        contact_page.click_locator_key('通讯录_家庭网_管理')
        time.sleep(1)
        contact_page.click_locator_key('家庭网_管理_添加')
        time.sleep(0.5)
        self.assertEqual('false' == contact_page.get_element_attr('家庭网_添加_确定', 'enabled'), True)
        # contact_page.input_locator_text('家庭网_添加_文本', '138')
        # self.assertEqual('true' == contact_page.get_element_attr('家庭网_添加_确定', 'enabled'), True)

    @tags('ALL', 'CMCC', 'contact')
    def test_member_0048(self):
        """
            1、正常登陆
            2、网络正常
            3、当前页面为家庭网成员页面
            4、已开通家庭网业务"	点击"添加成员"按钮	"（1）输入手机号码：输入框文字引导用户输入11位中国移动号码。输入框只能输入数字。
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 展开家庭网
        if not contact_page.if_home_net_expand():
            contact_page.click_locator_key('通讯录_家庭网_展开')
            time.sleep(1)
        # 点击家庭网第一个联系人
        contact_page.click_locator_key('通讯录_家庭网_管理')
        time.sleep(1)
        contact_page.click_locator_key('家庭网_管理_添加')
        time.sleep(1)
        contact_page.input_locator_text('家庭网_添加_文本', '1477597')
        time.sleep(1)
        self.assertEqual('true' == contact_page.get_element_attr('家庭网_添加_确定', 'enabled'), True)

    @tags('ALL', 'CMCC', 'contact')
    def test_member_0050(self):
        """
            1、正常登陆
            2、网络正常
            3、当前页面为家庭网成员页面
            4、已开通家庭网业务"	点击"添加成员"按钮	"（1）输入手机号码：输入框文字引导用户输入11位中国移动号码。输入框只能输入数字。
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 展开家庭网
        if not contact_page.if_home_net_expand():
            contact_page.click_locator_key('通讯录_家庭网_展开')
            time.sleep(1)
        # 点击家庭网第一个联系人
        contact_page.click_locator_key('通讯录_家庭网_管理')
        time.sleep(1)
        contact_page.click_locator_key('家庭网_管理_添加')
        time.sleep(1)
        contact_page.click_locator_key('家庭网_添加_通讯录')
        time.sleep(0.5)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_添加_通讯录_搜索框'), True)
        time.sleep(0.5)
        contact_page.input_locator_text('家庭网_添加_通讯录_搜索框', '1477597')
        time.sleep(1)
        el = contact_page.get_elements_list_c('家庭网_添加_通讯录_搜索列表')[0]
        num = el.text
        el.click()
        time.sleep(1)
        self.assertEqual(num == contact_page.get_element_text('家庭网_添加_文本'), True)

    @tags('ALL', 'CMCC', 'contact')
    def test_member_0056(self):
        """
            "1、正常登陆
            2、网络正常
            3、当前页面为家庭网页面"	点击右上角“！”按钮	跳转至短号家庭网业务的规则说明，顶部有返回按钮
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 展开家庭网
        if not contact_page.if_home_net_expand():
            contact_page.click_locator_key('通讯录_家庭网_展开')
            time.sleep(1)
        # 点击家庭网第一个联系人
        contact_page.click_locator_key('通讯录_家庭网_管理')
        time.sleep(1)
        contact_page.click_locator_key('家庭网_管理_感叹号规则')
        time.sleep(2)
        self.assertEqual(contact_page.is_text_present('业务规则'), True)
        contact_page.click_locator_key('家庭网_管理_感叹号规则返回')
        time.sleep(1)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_管理_添加'), True)

    @tags('ALL', 'CMCC', 'contact')
    def test_member_0061(self):
        """
            "1、正常登陆
            2、网络正常
            3、当前页面为家庭网页面"	点击右上角“！”按钮	跳转至短号家庭网业务的规则说明，顶部有返回按钮
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 展开家庭网
        if not contact_page.if_home_net_expand():
            contact_page.click_locator_key('通讯录_家庭网_展开')
            time.sleep(1)
        # 点击家庭网第一个联系人
        contact_page.get_elements_list_click('家庭网_列表文本1')
        time.sleep(3)
        contact_page.click_locator_key('家庭网_详细_更多编辑')
        time.sleep(1)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_更多性别'), True)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_更多年龄'), True)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_更多职业'), True)
        self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_更多个性标签'), True)

    @tags('ALL', 'CMCC', 'contact')
    def test_member_0065(self):
        """
            "1、非广东、四川移动用户已登录APP；
            2、网络正常；
            3、当前在不限时长成员管理；"	"1、长按要解绑的不限时长成员
            2、点击“解绑”按钮；
            3、点击“取消”键；
            "	弹框消失，取消本次解绑操作；
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 点击管理
        time.sleep(0.5)
        if not contact_page.is_element_already_exist('通讯录_不限时长列表'):
            raise RuntimeError('密友圈没有成员')
        contact_page.click_locator_key('通讯录_密友圈_管理')
        # 长按
        time.sleep(2)
        contact_page.click_delete_manager_meet()
        time.sleep(2)
        contact_page.click_locator_key('密友圈_不限时长管理_解绑取消')
        time.sleep(1)
        self.assertEqual(contact_page.is_element_already_exist('密友圈_不限时长管理_标题'), True)

    @tags('ALL', 'CMCC', 'contact')
    def test_member_0071(self):
        """解绑人数限制弹框显示时间短"""
        """
            当月已解绑过一名成员后再次解绑第二名成员	"1、非四川移动用户已登录APP；
            2、网络正常；
            3、当前在不限时长成员管理；"	长按要解绑的不限时长成员	"解绑达上限，则toast提示“本月解绑人数已达上限”
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 密友圈没有成员
        if not contact_page.is_element_already_exist('通讯录_不限时长列表'):
            raise RuntimeError('密友圈没有成员')
        # 点击管理
        contact_page.click_locator_key('通讯录_密友圈_管理')
        time.sleep(1)
        contact_page.click_delete_manager_meet()
        time.sleep(0.5)
        contact_page.click_locator_key('密友圈_不限时长管理_解绑')
        time.sleep(2)
        if not contact_page.is_element_already_exist('通讯录_不限时长列表'):
            raise RuntimeError('密友圈没有成员')
        # 点击管理
        contact_page.click_delete_manager_meet()
        time.sleep(0.5)
        contact_page.click_locator_key('密友圈_不限时长管理_解绑')
        self.assertEqual(contact_page.is_toast_exist('密友圈_不限时长管理_解绑人数'), True)

    @tags('ALL', 'CMCC', 'contact')
    def test_member_00103(self):
        """
            1、联网正常
            2、已登陆客户端
            3、在家庭网详情-编辑资料页面
            输入空格并点击保存	使用原来名称
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 展开家庭网
        if not contact_page.if_home_net_expand():
            contact_page.click_locator_key('通讯录_家庭网_展开')
            time.sleep(1)
        # 点击家庭网第一个联系人
        contact_page.get_elements_list_click('家庭网_列表文本1')
        time.sleep(3)
        contact_page.is_element_already_exist('家庭网_管理_感叹号规则')

    @tags('ALL', 'CMCC', 'contact')
    def test_member_0107_01(self):
        """
            1、查看密友圈（不限时长）
            2、点击成员电话icon
            3、点击“管理”
            1、列表为横向可滑动显示查看：成员半透明底头像+电话icon，底部为不限时长联系人名称（名称显示优先级：备注名(存在服务端)>个人中心昵称>本地通讯录>家庭网名>短号）；
            2、点击icon发起电话流程（回拨或者CS电话），打电话逻辑不变；
            3、进入不限时长成员管理页面，成员管理页面、添加成员页面以及功能逻辑与现网标准版一致；"
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        time.sleep(2)
        self.assertEqual(contact_page.is_element_already_exist('通讯录_不限时长列表1') > 0, True)
        contact_page.get_elements_list_click('通讯录_不限时长列表1')
        time.sleep(3)
        contact_page.click_locator_key('飞信电话_我知道了')
        time.sleep(4)
        n = 20
        flag = False
        while n > 0:
            if contact_page.is_element_already_exist('飞信电话_缩小') \
                    or contact_page.is_element_already_exist('飞信电话_拒绝') \
                    or contact_page.is_element_already_exist('飞信电话_备注'):
                flag = True
                break
        try:
            self.assertEqual(flag, True)
        finally:
            # 飞信电话 拒绝
            time.sleep(5)
            try:
                if contact_page.is_element_already_exist('飞信电话_拒绝'):
                    contact_page.click_locator_key('飞信电话_拒绝')
                    time.sleep(1)
            except Exception:
                pass
            try:
                contact_page.click_locator_key('飞信电话_挂断')
            except Exception:
                pass

    @tags('ALL', 'CMCC', 'contact')
    def test_member_00107_02(self):
        """
            1、查看密友圈（不限时长）
            2、点击成员电话icon
            3、点击“管理”
            1、列表为横向可滑动显示查看：成员半透明底头像+电话icon，底部为不限时长联系人名称（名称显示优先级：备注名(存在服务端)>个人中心昵称>本地通讯录>家庭网名>短号）；
            2、点击icon发起电话流程（回拨或者CS电话），打电话逻辑不变；
            3、进入不限时长成员管理页面，成员管理页面、添加成员页面以及功能逻辑与现网标准版一致；"
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 密友圈没有成员
        if not contact_page.is_element_already_exist('通讯录_不限时长列表'):
            raise RuntimeError('密友圈没有成员')
        # 点击管理
        contact_page.click_locator_key('通讯录_密友圈_管理')
        time.sleep(1)
        contact_page.click_locator_key('密友圈_管理_添加成员')
        time.sleep(1)
        contact_page.is_text_present('添加不限时长成员')

    @tags('ALL', 'CMCC', 'contact')
    def test_member_00111(self):
        """
            1、联网正常
            2、已登陆客户端（家庭网主号）
            3、当前在通讯录模块页面，已开通家庭网
            "	"1、查看家庭网列表展示
            2、点击“管理”"	"1、家庭网列表默认收起状态；
            2、家庭网主好提供管理入口，点击则进入家庭网成员管理页面；
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 展开家庭网
        self.assertEqual(contact_page.if_home_net_expand(), False)
        # 点击家庭网第一个联系人
        contact_page.click_locator_key('通讯录_家庭网_管理')
        time.sleep(1)
        contact_page.is_text_present('家庭网成员管理')

    @tags('ALL', 'CMCC', 'contact')
    def test_member_00118(self):
        """
            1、联网正常
            2、已登陆客户端
            3、当前通讯录页面"	1、在搜索框中输入“13xx”
            1、分别展示符合内容的家庭网用户、密友用户
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        time.sleep(0.5)
        contact_page.input_locator_text('搜索_文本', '147')
        time.sleep(2)
        self.assertEqual(contact_page.get_elements_count('搜索_列表1') > 0, True)

    @tags('ALL', 'CMCC', 'contact')
    def test_member_00120(self):
        """控件元素值无法获取"""
        """
            1、联网正常
            2、已登陆客户端
            3、当前通讯录页面"	1、在搜索框中输入合法的手机号码
            1、显示：无该联系人
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        time.sleep(0.5)
        contact_page.input_locator_text('搜索_文本', '13800008888')
        time.sleep(3)
        self.assertEqual(contact_page.is_element_already_exist('无该联系人') or
                         contact_page.is_element_already_exist('搜索_联系人_无结果'), True)

    @tags('ALL', 'CMCC', 'contact')
    def test_member_00121(self):
        """
            1.已登录APP
            2.网络断网
            3.当前页面在密友页面"	1.点击搜索按钮
            跳转至搜索页面，搜索框默认字体“搜索手机号/姓名”
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        time.sleep(1)
        contact_page.click_locator_key('搜索_文本')
        time.sleep(1)
        self.assertEqual('搜索' == contact_page.get_element_text('搜索_文本'), True)

    @tags('ALL', 'CMCC', 'contact')
    def test_member_00132(self):
        """
            顶部新增“添加异网成员资格”剩余个数提示	"1、已登录密友圈
            2、网络正常
            3、当前页面不限时长管理
            4、非四川卡
            5、活动期间内"	查看顶部文案显示	文案显示“您还可以设置XX个成员，其中非移动号成员体验名额还有X个”每个主叫号码添加异网成员体验资格为2个，超过2个后，不可再继续添加（体验资格设置为动态更新，默认为2个，方便往后配合活动增加体验资格上限的改造）
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        time.sleep(0.5)
        contact_page.click_locator_key('通讯录_密友圈_管理')
        time.sleep(0.5)
        self.assertEqual(contact_page.is_text_present('其中非移动号成员体验名额还有'), True)

    # @tags('ALL', 'CMCC', 'contact')
    @unittest.skip('元素无法滑动')
    def test_member_00145(self):
        """
            1、已登录密友圈
            2、网络正常
            3、当前页面添加不限时长成员页面"	查看页面数据显示
            1、存在不限时长、家庭网、本地通讯录、好友成员数据，去重显示
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        # 滑动
        time.sleep(1)
        contact_page.click_locator_key('通讯录_不限时长添加')
        time.sleep(1)
        self.assertEqual(contact_page.get_elements_count('密友圈_不限时长管理_列表1') > 0, True)

    @tags('ALL', 'CMCC', 'contact')
    def test_member_00146(self):
        """
            1、已登录密友圈
            2、网络正常
            3、当前页面添加不限时长成员页面"	查看页面数据显示
            1、存在不限时长、家庭网、本地通讯录、好友成员数据，去重显示
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        self.assertEqual(contact_page.get_elements_count('家庭网_列表1') > 0, True)
        self.assertEqual(contact_page.get_elements_count('联系人_列表1') > 0, True)

    @tags('ALL', 'CMCC', 'contact')
    def test_member_00152(self):
        """
            对通讯录列表搜索结果新增按钮	"1、正常网络状态下
            2、已登录密友圈
            3、通讯录列表存在数据"	"1、输入一个与通讯录列表匹配的号码或名称
            2、点击除拨打按钮外的其他区域"	"1、展示的搜索结果右侧新增拨打电话按钮
            2、进入个人详情页面"
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        time.sleep(1)
        contact_page.input_locator_text('搜索_文本', '147')
        time.sleep(1)
        contact_page.click_locator_key('搜索_列表1')
        time.sleep(1)
        self.assertEqual(contact_page.is_element_already_exist('搜索_详细_用户名'), True)

    # @tags('ALL', 'CMCC', 'contact')
    @unittest.skip('添加桌面图标没有')
    def test_member_00155(self):
        """
            1、登录密友圈
            2、跳转通讯录界面"	"1、跳转通讯录tab
            2、点击通讯录成员列表中的去添加快捷方式按钮
            3、点击去开启"	"1、在通讯录界面显示成员列表并显示添加快捷方式按钮
            2、弹窗已尝试添加到桌面弹窗，对于主流手机（华为、OPPO、vivo、小米），弹窗右侧按钮改成“去开启”。点击“去开启”跳转到系统设置页面
            3、若用户未悬浮窗权限，则以长toast的形式，根据机型不同，提示不同的提示文案
            ②若用户已开启悬浮窗权限，则以悬浮窗形式（悬浮窗停留5S），根据机型不同，提示不同文案
        """
        contact_page = ContactsPage()
        # 确保在通讯录界面
        self.assertEqual(contact_page.is_element_already_exist('通讯录_标题'), True)
        contact_page.click_locator_key('添加桌面图标')
        time.sleep(0.5)
        if contact_page.is_text_present('已尝试添加到桌面'):
            contact_page.click_text('去开启')

