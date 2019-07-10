from selenium.common.exceptions import TimeoutException

from library.core.TestCase import TestCase
from library.core.utils.applicationcache import current_mobile, current_driver, switch_to_mobile
from library.core.utils.testcasefilter import tags

from pages import *

import time
import warnings

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


class Preconditions(object):
    """
    分解前置条件
    """
    @staticmethod
    def select_mobile(category):
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
    def app_start_for_the_first_time():
        """首次启动APP（使用重置APP代替）"""
        current_mobile().reset_app()

    @staticmethod
    def terminate_app():
        """
        强制关闭app,退出后台
        :return:
        """
        app_id = current_driver().capabilities['appPackage']
        current_mobile().terminate_app(app_id)

    @staticmethod
    def background_app(seconds):
        """后台运行"""
        current_mobile().background_app(seconds)

    @staticmethod
    def reset_and_relaunch_app():
        """首次启动APP（使用重置APP代替）"""
        app_package = 'com.chinasofti.rcs'
        current_driver().activate_app(app_package)
        current_mobile().reset_app()

    @staticmethod
    def disconnect_mobile(category):
        """断开手机连接"""
        client = switch_to_mobile(REQUIRED_MOBILES[category])
        client.disconnect_mobile()
        return client

class LoginTest(TestCase):
    """Login 模块"""

    def default_tearDown(self):
        Preconditions.disconnect_mobile('IOS-移动-移动')

    @staticmethod
    def setUp_test_login_0001():
        warnings.simplefilter('ignore', ResourceWarning)
        Preconditions.select_mobile('IOS-移动-移动')

    @tags('ALL', 'CMCC', 'login')
    def test_login_0001(self):
        """
            取消首次登录时登录按钮的置灰显示	"1、正常网络
            2、当前在一键登录页面
            3、用户首次登录"	"1、查看页面显示
            2、点击本机号码一键登录按钮
            3、点击不同意
            4、同2步骤，点击同意
            5、点击确定按钮"	"1、文案“登录即代表阅读并同意《软件许可服务协议》和《隐私和信息保护政策》”显示在底部，无勾选框，登录按钮高亮显示
            2、弹出“用户协议和隐私保护，
            欢迎使用密友圈，我们非常重视保护您的个人协议并严格遵守相关法律法规。
            我们会根据国家相关法律法规不定时更新我们的软件许可协议和隐私协议，您可通过《软件许可服务协议》和《隐私和信息保护政策》查看详细条款，请您在使用密友圈前务必仔细阅读。
            点击下方“同意”按钮，方可开始使用密友圈，与此同时我们将竭力保护您的隐私安全
            ”同意与不同意按钮
            3、弹窗消失，停留当前页面
            4、弹出“使用号码XXXX登录，登录后，在密友圈app内的视频通话、语音通话和聊天将使用该号码发起”确定按钮
            5、成功进入密友圈"
            :return:
        """
        login = OneKeyLoginPage()
        # 检查一键登录
        login.wait_for_page_load()
        time.sleep(2)
        login.click_locator_key('一键登录')
        if login.is_element_already_exist('一键登录_问题_确认'):
            login.click_locator_key('一键登录_问题_取消')
            print("一键登录失败")
        # 判断当前页面
        time.sleep(5)
        if login.is_element_already_exist('广告_通话_关闭'):
            login.click_locator_key('广告_通话_关闭')
        time.sleep(2)
        self.assertEqual(login.is_element_already_exist('拨号键盘'), True)

    @staticmethod
    def setUp_test_login_0003():
        warnings.simplefilter('ignore', ResourceWarning)
        Preconditions.select_mobile('IOS-移动-移动')

    @tags('ALL', 'CMCC', 'me')
    def test_login_0003(self):
        """ 非首次登陆
            "1、正常网络
            2、当前在一键登录页面
            3、用户非首次登录"	"1、点击一键登陆
            2、点击确认使用XX号码登录"	成功登陆密友，进入通话页面
        """
        login = OneKeyLoginPage()
        login.wait_for_page_load()
        if login.is_element_already_exist('一键登录'):
            login.click_locator_key('一键登录')
        # 判断当前页面
        time.sleep(5)
        if login.is_element_already_exist('广告_通话_关闭'):
            login.click_locator_key('广告_通话_关闭')
        time.sleep(2)
        self.assertEqual(login.is_element_already_exist('拨号键盘'), True)

