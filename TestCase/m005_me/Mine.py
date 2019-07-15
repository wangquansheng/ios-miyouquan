from pages.components import FooterPage
from preconditions.BasePreconditions import LoginPreconditions

from library.core.TestCase import TestCase
from library.core.utils.applicationcache import switch_to_mobile
from library.core.utils.testcasefilter import tags

from pages import *

import warnings
import time

REQUIRED_MOBILES = {
    'Android-移动': 'M960BDQN229CH',
    'IOS-移动': 'iphone',
    'IOS-移动-移动': 'iphone_d',
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

    # @staticmethod
    # def create_contacts(name, number):
    #     """
    #     导入联系人数据
    #     :param name:
    #     :param number:
    #     :return:
    #     """
    #     contacts_page = ContactsPage()
    #     detail_page = ContactDetailsPage()
    #     try:
    #         contacts_page.wait_for_page_load()
    #         contacts_page.open_contacts_page()
    #     except:
    #         Preconditions.make_already_in_message_page(reset=False)
    #         contacts_page.open_contacts_page()
    #     # 创建联系人
    #     contacts_page.click_search_box()
    #     contact_search = ContactListSearchPage()
    #     contact_search.wait_for_page_load()
    #     contact_search.input_search_keyword(name)
    #     contact_search.click_back()
    #     contacts_page.click_add()
    #     create_page = CreateContactPage()
    #     create_page.hide_keyboard_if_display()
    #     create_page.create_contact(name, number)
    #     detail_page.wait_for_page_load()
    #     detail_page.click_back_icon()
    #
    # @staticmethod
    # def take_logout_operation_if_already_login():
    #     """已登录状态，执行登出操作"""
    #     message_page = MessagePage()
    #     message_page.wait_for_page_load()
    #     message_page.open_me_page()
    #
    #     me = MinePage()
    #     me.scroll_to_bottom()
    #     me.scroll_to_bottom()
    #     me.scroll_to_bottom()
    #     me.click_setting_menu()
    #
    #     setting = SettingPage()
    #     setting.scroll_to_bottom()
    #     setting.click_logout()
    #     setting.click_ok_of_alert()
    #
    # @staticmethod
    # def reset_and_relaunch_app():
    #     """首次启动APP（使用重置APP代替）"""
    #     app_package = 'com.chinasofti.rcs'
    #     current_driver().activate_app(app_package)
    #     current_mobile().reset_app()
    #
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
    #
    # @staticmethod
    # def activate_app(app_id=None):
    #     """激活APP"""
    #     if not app_id:
    #         app_id = current_mobile().driver.desired_capabilities['appPackage']
    #     current_mobile().driver.activate_app(app_id)


class Meprofile(TestCase):
    """我页面-个人资料"""

    def default_setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        Preconditions.select_mobile('IOS-移动')
        FooterPage().open_me_page()
        time.sleep(2)

    def default_tearDown(self):
        Preconditions.disconnect_mobile(REQUIRED_MOBILES['IOS-移动'])

    @tags('ALL', 'CMCC', 'me')
    def test_me_0001(self):
        """资料页面的字段可显示并且可以编辑"""
        me_page = MinePage()
        time.sleep(1)
        self.assertEqual(me_page.is_on_this_page(), True)
        me_page.click_locator_key('我_请完善您的资料_图片')
        time.sleep(2)
        self.assertEqual(me_page.is_element_already_exist("我_资料_昵称"), True)
        self.assertEqual(me_page.is_element_already_exist("我_资料_性别"), True)
        self.assertEqual(me_page.is_element_already_exist("我_资料_年龄"), True)
        self.assertEqual(me_page.is_element_already_exist("我_资料_我的标签"), True)
        self.assertEqual(me_page.is_element_already_exist("我_资料_职业"), True)
        me_page.click_locator_key('我_资料_图像')
        time.sleep(0.5)
        me_page.click_locator_key('我_个人图像_返回')
        # 显示并且可以编辑
        time.sleep(2)
        self.assertEqual(me_page.is_element_already_exist('我_资料_电话号码文本'), True)
        self.assertEqual(me_page.is_element_already_exist("我_资料_昵称文本"), True)
        self.assertEqual(me_page.is_element_already_exist("我_资料_性别文本"), True)
        self.assertEqual(me_page.is_element_already_exist("我_资料_性别文本"), True)
        self.assertEqual(me_page.is_element_already_exist("我_资料_我的标签文本"), True)
        self.assertEqual(me_page.is_element_already_exist("我_资料_职业文本"), True)

    @tags('ALL', 'CMCC', 'me')
    def test_me_0002(self):
        """编辑资料页面里面点击头像"""
        me_page = MinePage()
        self.assertEqual(me_page.is_on_this_page(), True)
        me_page.click_locator_key('我_请完善您的资料_图片')
        time.sleep(1)
        me_page.click_locator_key('我_资料_图像')
        time.sleep(1)
        me_page.click_locator_key('我_个人图像_详情')
        time.sleep(1)
        me_page.is_element_already_exist('从手机相册选择')
        me_page.is_element_already_exist('保存到手机')

    @tags('ALL', 'CMCC', 'me')
    def test_me_0003(self):
        """编辑资料页面昵称里面输入sql语句"""
        me_page = MinePage()
        self.assertEqual(me_page.is_on_this_page(), True)
        time.sleep(1)
        me_page.click_locator_key('我_请完善您的资料_图片')
        time.sleep(1)
        nickname = me_page.get_text('我_资料_昵称文本')
        if nickname is not None and '' != nickname:
            me_page.clear_nickname_text('我_资料_昵称文本')
            me_page.input_profile_name('我_资料_昵称文本', 'select from')
        else:
            me_page.input_profile_name('我_资料_昵称文本', 'select from')
        time.sleep(1)
        me_page.click_locator_key('我_资料_保存')
        for i in range(3):
            if me_page.is_toast_exist('上传成功', timeout=0.3) \
                    or me_page.is_toast_exist('正在上传...', timeout=0.3):
                break

    @tags('ALL', 'CMCC', 'me')
    def test_me_0004(self):
        """编辑资料页面昵称里面输入字符串"""
        me_page = MinePage()
        self.assertEqual(me_page.is_on_this_page(), True)
        me_page.click_locator_key('我_请完善您的资料_图片')
        time.sleep(1)
        nickname = me_page.get_text('我_资料_昵称文本')
        if nickname is not None and '' != nickname:
            me_page.clear_nickname_text('我_资料_昵称文本')
            me_page.input_profile_name('我_资料_昵称文本', r"<>'\"&\n\r")
        else:
            me_page.input_profile_name('我_资料_昵称文本', r"<>'\"&\n\r")
        self.assertEqual(me_page.is_toast_exist('不能包含特殊字符和表情'), True)

    @tags('ALL', 'CMCC', 'me')
    def test_me_0005(self):
        """编辑资料页面昵称里面输入数字"""
        me_page = MinePage()
        self.assertEqual(me_page.is_on_this_page(), True)
        me_page.click_locator_key('我_请完善您的资料_图片')
        time.sleep(1)
        nickname = me_page.get_text('我_资料_昵称文本')
        if nickname is not None and '' != nickname:
            me_page.clear_nickname_text('我_资料_昵称文本')
            me_page.input_profile_name('我_资料_昵称文本', '4135435')
        else:
            me_page.input_profile_name('我_资料_昵称文本', '4135435')
        me_page.click_locator_key('我_资料_保存')
        for i in range(3):
            if me_page.is_toast_exist('上传成功', timeout=0.3) \
                    or me_page.is_toast_exist('正在上传...', timeout=0.3):
                break

    @tags('ALL', 'CMCC', 'me')
    def test_me_0006(self):
        """点击性别选项选择性别"""
        me_page = MinePage()
        self.assertEqual(me_page.is_on_this_page(), True)
        me_page.click_locator_key('我_请完善您的资料_图片')
        time.sleep(0.5)
        me_page.input_random_nickname()
        me_page.click_locator_key('我_资料_性别详情')
        # 向上滑动
        time.sleep(0.5)
        x_source = 300 / 375 * 100
        y_source = 500 / 667 * 100
        x_target = 300 / 375 * 100
        y_target = 560 / 667 * 100
        me_page.swipe_by_percent_on_screen(x_source, y_source, x_target, y_target)
        time.sleep(0.5)
        me_page.click_locator_key('我_下拉框_完成')
        # 提交
        me_page.click_locator_key('我_资料_保存')
        for i in range(3):
            if me_page.is_toast_exist('上传成功', timeout=0.3) \
                    or me_page.is_toast_exist('正在上传...', timeout=0.3):
                break

    @tags('ALL', 'CMCC', 'me')
    def test_me_0007(self):
        """编辑年龄选项选择年龄"""
        me_page = MinePage()
        self.assertEqual(me_page.is_on_this_page(), True)
        me_page.click_locator_key('我_请完善您的资料_图片')
        # 修改昵称
        time.sleep(0.5)
        me_page.input_random_nickname()
        me_page.click_locator_key('我_资料_年龄详情')
        # 向上滑动
        time.sleep(0.5)
        x_source = 300 / 375 * 100
        y_source = 560 / 667 * 100
        x_target = 300 / 375 * 100
        y_target = 500 / 667 * 100
        me_page.swipe_by_percent_on_screen(x_source, y_source, x_target, y_target)
        time.sleep(0.5)
        me_page.click_locator_key('我_下拉框_完成')
        # 提交
        me_page.click_locator_key('我_资料_保存')
        for i in range(3):
            if me_page.is_toast_exist('上传成功', timeout=0.3) \
                    or me_page.is_toast_exist('正在上传...', timeout=0.3):
                break

    @tags('ALL', 'CMCC', 'me')
    def test_me_0008(self):
        """编辑标签选项选择标签"""
        me_page = MinePage()
        self.assertEqual(me_page.is_on_this_page(), True)
        me_page.click_locator_key('我_请完善您的资料_图片')
        time.sleep(0.5)
        me_page.click_locator_key('我_资料_我的标签详情')
        time.sleep(2)
        for i in range(6):
            me_page.click_locator_key('我_资料标签_%s' % (i+1))
            time.sleep(2)
            if i >= 5:
                break
        # 检查选择标签
        time.sleep(2)
        self.assertTrue(me_page.is_element_already_exist('我_资料标签_最多选择5个标签'))

    @tags('ALL', 'CMCC', 'me')
    def test_me_0009(self):
        """编辑职业选项选择职业"""
        me_page = MinePage()
        self.assertEqual(me_page.is_on_this_page(), True)
        me_page.click_locator_key('我_请完善您的资料_图片')
        time.sleep(0.5)
        me_page.input_random_nickname()
        me_page.click_locator_key('我_资料_职业详情')
        time.sleep(1)
        me_page.click_locator_key('我_资料职业_2')
        time.sleep(2)
        # 提交
        me_page.click_locator_key('我_资料_保存')
        for i in range(3):
            if me_page.is_toast_exist('上传成功', timeout=0.3) \
                    or me_page.is_toast_exist('正在上传...', timeout=0.3):
                break

    # @unittest.skip('app改版没有二维码')
    # def test_me_0010(self):
    #     """查看我的二维码页面显示"""
    #     me_page = MinePage()
    #     me_page.click_locator_key('我的二维码')
    #     self.assertTrue(me_page.element_is_clickable('二维码_转到上一层级'))
    #     self.assertTrue(me_page.element_is_clickable('二维  码_更多'))
    #     self.assertTrue(me_page.is_text_exist('我的二维码'))
    #     self.assertTrue(me_page.is_text_exist('密友圈扫描二维码，添加我为密友'))
    #     self.assertTrue(me_page.check_qr_code_exist())
    #     self.assertTrue(me_page.check_element_name_photo_exist())
    #
    # @unittest.skip('app改版没有二维码')
    # def test_me_0011(self):
    #     """个人二维码点击更多"""
    #     me_page = MinePage()
    #     me_page.click_locator_key('我的二维码')
    #     me_page.click_locator_key('二维码_更多')
    #     time.sleep(2)
    #     self.assertEqual(me_page.get_element_text('分享二维码'), '分享我的二维码')
    #     self.assertTrue(me_page.element_is_enable('分享二维码'))
    #     self.assertEqual(me_page.get_element_text('保存二维码'), '保存二维码图片')
    #     self.assertTrue(me_page.element_is_enable('保存二维码'))
    #
    # @unittest.skip('app改版没有二维码')
    # def test_me_0012(self):
    #     """个人二维码点击更多"""
    #     me_page = MinePage()
    #     me_page.click_locator_key('我的二维码')
    #     me_page.click_locator_key('二维码_更多')
    #     me_page.click_locator_key('分享二维码')
    #     self.assertEqual(me_page.get_element_text('分享_密友圈'), '密友圈')
    #     self.assertEqual(me_page.get_element_text('分享_朋友圈'), '朋友圈')
    #     self.assertEqual(me_page.get_element_text('分享_微信'), '微信')
    #     self.assertEqual(me_page.get_element_text('分享_QQ'), 'QQ')
    #     self.assertEqual(me_page.get_element_text('分享_QQ空间'), 'QQ空间')

    @tags('ALL', 'CMCC', 'me')
    def test_me_0013(self):
        """验证活动中心页面正常打开"""
        me_page = MinePage()
        time.sleep(1)
        me_page.click_locator_key('我_活动中心_详情')
        # 加载页面
        me_page.wait_for_element_load('我_活动中心_活动中心')
        self.assertTrue(me_page.is_element_already_exist('我_活动中心_活动中心'))
        time.sleep(1)
        me_page.click_locator_key('我_二级页面_相同返回')

    @tags('ALL', 'CMCC', 'me')
    def test_me_0014(self):
        """验证卡券页面正常打开"""
        me_page = MinePage()
        time.sleep(1)
        self.assertEqual(me_page.is_on_this_page(), True)
        # 加载页面, 使用name查找不到
        time.sleep(1)
        me_page.click_locator_key('我_卡劵_详情')
        time.sleep(3)
        me_page.wait_for_element_load('我_卡劵_卡劵')
        self.assertTrue(me_page.is_element_already_exist('我_卡劵_卡劵'))
        time.sleep(1)
        me_page.click_locator_key('我_二级页面_相同返回')

    @tags('ALL', 'CMCC', 'me')
    def test_me_0015(self):
        """验证积分页面正常打开"""
        me_page = MinePage()
        time.sleep(1)
        self.assertEqual(me_page.is_on_this_page(), True)
        time.sleep(1)
        me_page.click_locator_key('我_积分_详情')
        time.sleep(3)
        me_page.wait_for_element_load('我_积分_积分')
        if me_page.is_text_present('已连续签到'):
            me_page.click_text('我知道了')
        # 积分
        self.assertTrue(me_page.is_element_already_exist('我_积分_积分'))
        me_page.click_locator_key('我_二级页面_相同返回')

    # @tags('ALL', 'CMCC', 'me')
    # def test_me_0016(self):
    #     """验证网上营业厅正常打开"""
    #     me_page = MinePage()
    #     me_page.click_locator_key('网上营业厅')
    #     self.assertTrue(me_page.check_wait_text_exits('网上营业厅'))
    #     me_page.click_locator_key('我_二级页面_相同返回')

    @tags('ALL', 'CMCC', 'me')
    def test_me_0017(self):
        """验证邀请有礼正常打开"""
        me_page = MinePage()
        time.sleep(1)
        self.assertEqual(me_page.is_on_this_page(), True)
        time.sleep(1)
        me_page.click_locator_key('我_邀请有奖_详情')
        time.sleep(5)
        me_page.wait_for_element_load('我_邀请有奖_邀请有奖')
        self.assertTrue(me_page.is_element_already_exist('我_邀请有奖_邀请有奖'))
        me_page.click_locator_key('我_二级页面_相同返回')

    @tags('ALL', 'CMCC', 'me')
    def test_me_0018(self):
        """验证帮助与反馈正常打开"""
        me_page = MinePage()
        time.sleep(1)
        self.assertEqual(me_page.is_on_this_page(), True)
        time.sleep(1)
        me_page.click_locator_key('我_帮助与反馈_详情')
        time.sleep(5)
        me_page.wait_for_element_load('我_帮助与反馈_帮助与反馈')
        self.assertTrue(me_page.is_element_already_exist('我_帮助与反馈_帮助与反馈'))
        me_page.click_locator_key('我_二级页面_相同返回')

    @tags('ALL', 'CMCC', 'me')
    def test_me_0019(self):
        """验证我-设置-退出当前账号	中	"1、联网正常
        2、已登陆客户端
        3、在我模块-设置页面"	点击退出当前账号	成功退出登录显示，并跳转至登录页
        """
        me_page = MinePage()
        time.sleep(1)
        self.assertEqual(me_page.is_on_this_page(), True)
        if me_page.is_element_already_exist('我_设置_详情'):
            me_page.click_locator_key('我_设置_详情')
        time.sleep(2)
        me_page.click_locator_key('我_设置_退出登录')
        time.sleep(2)
        me_page.click_locator_key('我_退出登录_确认')
        time.sleep(5)
        self.assertTrue(me_page.check_wait_text_exits('本机号码一键登录'))
        time.sleep(2)
        me_page.click_locator_key('一键登录')
        print('重新登录')

