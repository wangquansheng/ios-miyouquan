import preconditions
from library.core.TestCase import TestCase
from selenium.common.exceptions import TimeoutException
from library.core.utils.applicationcache import current_mobile, switch_to_mobile, current_driver
from library.core.common.simcardtype import CardType
from library.core.utils.testcasefilter import tags
from pages import *
from pages.components.BaseChat import BaseChatPage
import time
import unittest

REQUIRED_MOBILES = {
    'Android-移动': 'M960BDQN229CH',
    # 'Android-移动': 'single_mobile',
    'IOS-移动': 'iphone',
    'Android-电信': 'single_telecom',
    'Android-联通': 'single_union',
    'Android-移动-联通': 'mobile_and_union',
    'Android-移动-电信': '',
    'Android-移动-移动': 'double_mobile',
    'Android-XX-XX': 'others_double',
    'IOS-移动-移动': 'M960BDQN229CHiphone8',
}


class Preconditions(object):
    """前置条件"""

    @staticmethod
    def make_already_in_call():
        """确保进入通话界面"""
        preconditions.connect_mobile(REQUIRED_MOBILES['IOS-移动'])
        current_mobile().hide_keyboard_if_display()
        cpg = CallPage()
        message_page = MessagePage()
        if message_page.is_on_this_page():
            cpg.click_call()
            return
        if cpg.is_on_the_call_page():
            return
        try:
            current_mobile().terminate_app('com.chinasofti.rcs', timeout=2000)
        except:
            pass
        current_mobile().launch_app()
        try:
            message_page.wait_until(
                condition=lambda d: message_page.is_on_this_page(),
                timeout=15
            )
            cpg.click_call()
            return
        except TimeoutException:
            pass
        preconditions.reset_and_relaunch_app()
        preconditions.make_already_in_one_key_login_page()
        preconditions.login_by_one_key_login()
        cpg.click_call()

    @staticmethod
    def enter_single_chat_page(name):
        """进入单聊聊天会话页面"""
        mp = MessagePage()
        mp.wait_for_page_load()
        # 点击 +
        mp.click_add_icon()
        # 点击“新建消息”
        mp.click_new_message()
        slc = SelectLocalContactsPage()
        slc.wait_for_page_load()
        # 进入单聊会话页面
        slc.selecting_local_contacts_by_name(name)
        bcp = BaseChatPage()
        if bcp.is_exist_dialog():
            # 点击我已阅读
            bcp.click_i_have_read()
        scp = SingleChatPage()
        # 等待单聊会话页面加载
        scp.wait_for_page_load()

    @staticmethod
    def enter_group_chat_page(name):
        """进入群聊聊天会话页面"""

        mp = MessagePage()
        mp.wait_for_page_load()
        # 点击 +
        mp.click_add_icon()
        # 点击发起群聊
        mp.click_group_chat()
        scg = SelectContactsPage()
        times = 15
        n = 0
        # 重置应用时需要再次点击才会出现选择一个群
        while n < times:
            # 等待选择联系人页面加载
            flag = scg.wait_for_page_load()
            if not flag:
                scg.click_back()
                time.sleep(2)
                mp.click_add_icon()
                mp.click_group_chat()
            else:
                break
            n = n + 1
        scg.click_select_one_group()
        sog = SelectOneGroupPage()
        # 等待“选择一个群”页面加载
        sog.wait_for_page_load()
        # 选择一个普通群
        sog.selecting_one_group_by_name(name)
        gcp = GroupChatPage()
        gcp.wait_for_page_load()


class CallAll(TestCase):
    """
    模块：通话
    文件位置：全量/ 7.通话（拨号盘、多方视频-非RCS、视频通话、语音通话）全量测试用例-申丽思.xlsx
    表格：通话（拨号盘、多方视频-非RCS、视频通话、语音通话）
    Author:wangquansheng
    """
    #
    # @classmethod
    # def setUpClass(cls):
    #     # 创建联系人
    #     fail_time = 0
    #     import dataproviders
    #     while fail_time < 3:
    #         try:
    #             required_contacts = dataproviders.get_preset_contacts()
    #             conts = ContactsPage()
    #             preconditions.connect_mobile(REQUIRED_MOBILES['Android-移动'])
    #             preconditions.make_already_in_message_page()
    #             current_mobile().hide_keyboard_if_display()
    #             preconditions.make_already_in_message_page()
    #             for name, number in required_contacts:
    #                 conts.open_contacts_page()
    #                 if conts.is_text_present("显示"):
    #                     conts.click_text("不显示")
    #                 conts.create_contacts_if_not_exits(name, number)
    #
    #             # 创建群
    #             required_group_chats = dataproviders.get_preset_group_chats()
    #
    #             conts.open_group_chat_list()
    #             group_list = GroupListPage()
    #             for group_name, members in required_group_chats:
    #                 group_list.wait_for_page_load()
    #                 group_list.create_group_chats_if_not_exits(group_name, members)
    #             group_list.click_back()
    #             conts.open_message_page()
    #             return
    #         except:
    #             fail_time += 1
    #             import traceback
    #             msg = traceback.format_exc()
    #             print(msg)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     current_mobile().hide_keyboard_if_display()
    #     preconditions.make_already_in_message_page()

    def default_setUp(self):
        """进入Call页面,清空通话记录"""
        # preconditions.connect_mobile(REQUIRED_MOBILES['IOS-移动'])
        Preconditions.make_already_in_call()
        # CalllogBannerPage().skip_multiparty_call()
        # CallPage().delete_all_call_entry()

    def default_tearDown(self):
        preconditions.disconnect_mobile(REQUIRED_MOBILES['IOS-移动'])

    @tags('ALL', 'CMCC', 'Call', "ios")
    def test_call_shenlisi_0001(self):
        """检查进入到通话界面，“通话”按钮变为“拨号盘”"""
        # Step:1.点击通话tab
        cpg = CallPage()
        cpg.click_dial()
        # CheckPoint:1.进入到通话记录列表界面，底部“通话”按钮变成“拨号盘”，拨号盘按钮显示9蓝点
        cpg.page_should_contain_text('拨号')
        cpg.page_should_contain_text("直接拨号或开始搜索")
        cpg.click_dial()

    @tags('ALL', 'CMCC', 'Call', "ios")
    def test_call_shenlisi_0004(self):
        """检查拨号盘展开"""
        cpg = CallPage()
        # Step:1.点击“拨号盘"按钮
        cpg.click_dial()
        # CheckPoint:1.拨号盘展示，输入框提示“直接拨号或者开始搜索”，菜单栏被隐藏
        cpg.page_should_contain_text('直接拨号或开始搜索')
        cpg.click_dial()

    @tags('ALL', 'CMCC', 'Call', "ios")
    def test_call_shenlisi_0006(self):
        """检查展开拨号盘，通话记录为空"""
        # Step:1.查看通话记录
        cpg = CallPage()
        # CheckPoint:1.页面中间显示图片以及提示语
        cpg.page_should_contain_text("给你的好友打个电话吧")
        cpg.page_should_contain_text('多方电话')

    @tags('ALL', 'CMCC', 'Call')
    def test_call_shenlisi_0007(self):
        """检查拨号盘按键可点击"""
        cpg = CallPage()
        cpg.click_dial()
        # Step:1.点击按键“1”
        cpg.click_one()
        # Step:2.点击按键“2”
        cpg.click_two()
        # Step:3.点击按键“3”
        cpg.click_three()
        # Step:4.点击按键“4”
        cpg.click_four()
        # Step:5.点击按键“5”
        cpg.click_five()
        # Step:6.点击按键“6”
        cpg.click_six()
        # Step:7.点击按键“7”
        cpg.click_seven()
        # Step:8.点击按键“8”
        cpg.click_eight()
        # Step:9.点击按键“9”
        cpg.click_nine()
        # Step:10.点击按键“0”
        cpg.click_zero()
        # Step:11.点击按键“*”
        cpg.click_star()
        # Step:12.点击按键“#”
        cpg.click_sharp()
        # CheckPoint:1.步骤1-12：拨号盘各键输入正常
        cpg.page_should_contain_text("1234567890*#")
        # 清除拨号盘，返回通话界面
        cpg.press_delete()
        cpg.click_dial()




