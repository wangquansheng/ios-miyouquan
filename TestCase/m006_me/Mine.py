from preconditions.BasePreconditions import LoginPreconditions

from library.core.TestCase import TestCase
from library.core.utils.applicationcache import current_mobile, current_driver, switch_to_mobile
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
        # Preconditions.make_already_in_message_page()
        MessagePage().open_me_page()
        time.sleep(2)

    def default_tearDown(self):
        Preconditions.disconnect_mobile(REQUIRED_MOBILES['IOS-移动'])

    @tags('ALL', 'CMCC', 'me')
    def test_me_0001(self):
        """资料页面的字段可显示并且可以编辑"""
        me_page = MinePage()
        time.sleep(1)
        self.assertEqual(me_page.is_on_this_page(), True)
        me_page.click_locator_key('我_请完善您的资料')
        time.sleep(2)
        self.assertEqual(me_page.is_text_exist("我_资料_昵称"), True)
        self.assertEqual(me_page.is_text_exist("我_资料_性别"), True)
        self.assertEqual(me_page.is_text_exist("我_资料_年龄"), True)
        self.assertEqual(me_page.is_text_exist("我_资料_我的标签"), True)
        self.assertEqual(me_page.is_text_exist("我_资料_职业"), True)
        me_page.click_locator_key('我_资料_图像')
        me_page.click_locator_key('我_个人图像_返回')
        time.sleep(2)
        self.assertEqual(me_page.is_element_already_exist('我_资料_电话号码文本'), False)
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
        me_page.click_locator_key('我_请完善您的资料')
        me_page.click_locator_key('我_资料_图像')
        me_page.click_locator_key('我_个人图像_返回')
        time.sleep(2)
        me_page.element_is_clickable('从手机相册选择')
        me_page.element_is_clickable('保存到手机')

    @tags('ALL', 'CMCC', 'me')
    def test_me_0003(self):
        """编辑资料页面昵称里面输入sql语句"""
        me_page = MinePage()
        time.sleep(2)
        self.assertEqual(me_page.is_on_this_page(), True)
        me_page.click_personal_photo()
        meEdit_page = MeEditProfilePage()
        meEdit_page.input_profile_name('昵称', 'selectfrom')
        time.sleep(1)
        meEdit_page.click_save()
        for i in range(3):
            if meEdit_page.is_toast_exist('保存成功', timeout=0.3) \
                    or meEdit_page.is_toast_exist('您的资料未变化', timeout=0.3):
                break

    @tags('ALL', 'CMCC', 'me')
    def test_me_0004(self):
        """编辑资料页面昵称里面输入字符串"""
        me_page = MinePage()
        self.assertEqual(me_page.is_on_this_page(), True)
        me_page.click_personal_photo()
        meEdit_page = MeEditProfilePage()
        meEdit_page.input_profile_name('昵称', r"<>'\"&\n\r")
        self.assertEqual(meEdit_page.is_toast_exist('不能包含特殊字符和表情'), True)

    @tags('ALL', 'CMCC', 'me')
    def test_me_0005(self):
        """编辑资料页面昵称里面输入数字"""
        me_page = MinePage()
        self.assertEqual(me_page.is_on_this_page(), True)
        me_page.click_personal_photo()
        meEdit_page = MeEditProfilePage()
        meEdit_page.input_profile_name('昵称', '4135435')
        meEdit_page.click_save()
        self.assertTrue(meEdit_page.check_text_exist('保存成功'))

    @tags('ALL', 'CMCC', 'me')
    def test_me_0006(self):
        """点击性别选项选择性别"""
        me_edit_page = MeEditProfilePage()
        MinePage().click_personal_photo()
        time.sleep(0.5)
        me_edit_page.input_random_name()
        me_edit_page.click_locator_key('性别')
        me_edit_page.click_locator_key('性别_男')
        me_edit_page.click_locator_key('保存')
        self.assertTrue(me_edit_page.is_toast_exist('保存成功'), True)

    @tags('ALL', 'CMCC', 'me')
    def test_me_0007(self):
        """编辑年龄选项选择年龄"""
        me_edit_page = MeEditProfilePage()
        MinePage().click_personal_photo()
        time.sleep(0.5)
        me_edit_page.input_random_name()
        me_edit_page.click_locator_key('年龄')
        me_edit_page.click_locator_key('年龄_90后')
        me_edit_page.click_locator_key('保存')
        self.assertTrue(me_edit_page.check_text_exist('保存成功'))

    @tags('ALL', 'CMCC', 'me')
    def test_me_0008(self):
        """编辑标签选项选择标签"""
        me_edit_page = MeEditProfilePage()
        MinePage().click_personal_photo()
        time.sleep(0.5)
        me_edit_page.click_locator_key('我的标签')
        time.sleep(2)
        me_edit_page.click_locator_key('添加个性标签')
        me_edit_page.click_locator_key('标签取消')
        for i in range(6):
            me_edit_page.click_tag_index('标签', i)
        self.assertTrue(me_edit_page.check_text_exist('最多选择5个标签来形容自己'))

    @tags('ALL', 'CMCC', 'me')
    def test_me_0009(self):
        """编辑职业选项选择职业"""
        me_edit_page = MeEditProfilePage()
        MinePage().click_personal_photo()
        time.sleep(0.5)
        me_edit_page.input_random_name()
        me_edit_page.click_locator_key('职业')
        me_edit_page.click_locator_key('职业_计算机')
        me_edit_page.click_locator_key('保存')
        for i in range(3):
            if me_edit_page.is_toast_exist('保存成功', timeout=0.3) \
                    or me_edit_page.is_toast_exist('您的资料未变化', timeout=0.3):
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
        me_page.click_locator_key_c('活动中心')
        self.assertTrue(me_page.check_wait_text_exits('活动中心', timeout=3 * 60))
        me_page.click_locator_key_c('我_二级页面_相同返回')

    @tags('ALL', 'CMCC', 'me')
    def test_me_0014(self):
        """验证卡券页面正常打开"""
        me_page = MinePage()
        me_page.click_locator_key_c('卡券')
        self.assertTrue(me_page.check_wait_text_exits('我的卡券'))
        me_page.click_locator_key_c('我_二级页面_相同返回')

    @tags('ALL', 'CMCC', 'me')
    def test_me_0015(self):
        """验证积分页面正常打开"""
        me_page = MinePage()
        count = 3
        flag = False
        while count > 0:
            times = 1 * 60
            me_page.click_locator_key_c('积分')
            while times > 0:
                if me_page.is_text_present_c('已连续签到', default_timeout=0.5):
                    me_page.click_text('我知道了')
                if me_page.is_text_present_c('我的积分', default_timeout=0.5):
                    flag = True
                    break
                times -= 1
            else:
                me_page.click_locator_key_c('我_二级页面_相同返回')
            if flag:
                break
            count -= 1
        self.assertTrue(me_page.check_wait_text_exits('我的积分'))
        me_page.click_locator_key_c('我_二级页面_相同返回')

    @tags('ALL', 'CMCC', 'me')
    def test_me_0016(self):
        """验证网上营业厅正常打开"""
        me_page = MinePage()
        me_page.click_locator_key_c('网上营业厅')
        self.assertTrue(me_page.check_wait_text_exits('网上营业厅'))
        me_page.click_locator_key_c('我_二级页面_相同返回')

    @tags('ALL', 'CMCC', 'me')
    def test_me_0017(self):
        """验证邀请有礼正常打开"""
        me_page = MinePage()
        me_page.click_locator_key_c('邀请有礼')
        self.assertTrue(me_page.check_wait_text_exits('邀请有奖'))
        me_page.click_locator_key_c('我_二级页面_相同返回')

    @tags('ALL', 'CMCC', 'me')
    def test_me_0018(self):
        """验证帮助与反馈正常打开"""
        me_page = MinePage()
        me_page.click_locator_key_c('帮助与反馈')
        self.assertTrue(me_page.check_wait_text_exits('帮助与反馈'))
        me_page.click_locator_key_c('我_二级页面_相同返回')

    @tags('ALL', 'CMCC', 'me')
    def test_me_0019(self):
        """验证我-设置-退出当前账号	中	"1、联网正常
        2、已登陆客户端
        3、在我模块-设置页面"	点击退出当前账号	成功退出登录显示，并跳转至登录页
        """
        me_page = MinePage()
        time.sleep(1)
        for i in range(3):
            if me_page.is_element_already_exist_c('设置'):
                me_page.click_locator_key_c('设置')
                break
            else:
                me_page.page_up()
        time.sleep(1)
        me_page.click_locator_key_c('退出当前账号')
        time.sleep(3)
        self.assertTrue(me_page.check_wait_text_exits('一键登录'))
