import random
import re
import time
import unittest

from library.core.TestCase import TestCase
from library.core.common.simcardtype import CardType
from library.core.utils.applicationcache import current_mobile, switch_to_mobile, current_driver
from library.core.utils.testcasefilter import tags
from pages import *
from pages.components import BaseChatPage
from pages.groupset.GroupChatSetPicVideo import GroupChatSetPicVideoPage

from preconditions.BasePreconditions import WorkbenchPreconditions


class Preconditions(WorkbenchPreconditions):
    """前置条件"""

    @staticmethod
    def make_already_in_message_page(reset=False):
        """确保应用在消息页面"""
        # 如果在消息页，不做任何操作
        mp = MessagePage()
        if mp.is_on_this_page():
            return
        else:
            try:
                current_mobile().launch_app()
                mp.wait_for_page_load()
            except:
                # 进入一键登录页
                Preconditions.make_already_in_one_key_login_page()
                #  从一键登录页面登录
                Preconditions.login_by_one_key_login()

    @staticmethod
    def make_already_have_my_picture():
        """确保当前群聊页面已有图片"""
        # 1.点击输入框左上方的相册图标
        gcp = GroupChatPage()
        cpg = ChatPicPage()
        gcp.is_on_this_page()
        if gcp.is_exist_msg_image():
            return
        else:
            # 2.进入相片页面,选择一张片相发送
            time.sleep(2)
            gcp.click_picture()
            cpg.wait_for_page_load()
            cpg.select_pic_fk(1)
            cpg.click_send()
            time.sleep(5)

    @staticmethod
    def make_already_have_my_videos():
        """确保当前群聊页面已有视频"""
        # 1.点击输入框左上方的相册图标
        gcp = GroupChatPage()
        cpg = ChatPicPage()
        gcp.wait_for_page_load()
        if gcp.is_exist_msg_videos():
            return
        else:
            # 2.进入相片页面,选择一张片相发送
            gcp.click_picture()
            cpg.wait_for_page_load()
            cpg.select_video_fk(1)
            cpg.click_send()
            time.sleep(5)

    @staticmethod
    def get_into_group_chat_page(name):
        """进入群聊聊天会话页面"""

        mp = MessagePage()
        mp.wait_for_page_load()
        # 点击 +
        mp.click_add_icon()
        # 点击发起群聊
        mp.click_group_chat()
        scg = SelectContactsPage()
        scg.wait_for_page_load()
        scg.click_select_one_group()
        sog = SelectOneGroupPage()
        # 等待“选择一个群”页面加载
        sog.wait_for_page_load()
        sog.click_search_box()
        time.sleep(1)
        sog.input_search_box(name)
        time.sleep(2)
        # 选择一个普通群
        sog.selecting_one_group_by_name(name)
        gcp = GroupChatPage()
        gcp.wait_for_page_load()

    @staticmethod
    def make_no_message_send_failed_status():
        """确保当前消息列表没有消息发送失败的标识影响验证结果"""

        mp = MessagePage()
        mp.wait_for_page_load()
        # 确保当前消息列表没有消息发送失败的标识影响验证结果
        if mp.is_iv_fail_status_present():
            mp.clear_fail_in_send_message()

    @staticmethod
    def if_exists_multiple_enterprises_enter_group_chat(types):
        """选择团队联系人时存在多个团队时返回获取当前团队名，再进入群聊转发图片/视频"""

        shc = SelectHeContactsDetailPage()
        # 测试号码是否存在多个团队
        if not shc.is_exist_corporate_grade():
            mp = MessagePage()
            scg = SelectContactsPage()
            gcp = GroupChatPage()
            shc.click_back()
            scg.wait_for_page_load()
            scg.click_back()
            gcp.wait_for_page_load()
            gcp.click_back()
            mp.wait_for_page_load()
            mp.open_workbench_page()
            wbp = WorkbenchPage()
            wbp.wait_for_workbench_page_load()
            time.sleep(2)
            # 获取当前团队名
            workbench_name = wbp.get_workbench_name()
            mp.open_message_page()
            mp.wait_for_page_load()
            group_name = "群聊1"
            Preconditions.get_into_group_chat_page(group_name)
            # 转发图片/视频
            if types == "pic":
                gcp.forward_pic()
            elif types == "video":
                gcp.forward_video()
            scg.wait_for_page_load()
            scg.click_he_contacts()
            shc.wait_for_he_contacts_page_load()
            # 选择当前团队
            shc.click_department_name(workbench_name)


class MsgGroupChatVideoPicAllTest(TestCase):

    # @classmethod
    # def setUpClass(cls):
    #
    #     Preconditions.select_mobile('IOS-移动')
    #     # 导入测试联系人、群聊
    #     fail_time1 = 0
    #     flag1 = False
    #     import dataproviders
    #     while fail_time1 < 3:
    #         try:
    #             required_contacts = dataproviders.get_preset_contacts()
    #             conts = ContactsPage()
    #             current_mobile().hide_keyboard_if_display()
    #             Preconditions.make_already_in_message_page()
    #             conts.open_contacts_page()
    #             try:
    #                 if conts.is_text_present("发现SIM卡联系人"):
    #                     conts.click_text("显示")
    #             except:
    #                 pass
    #             for name, number in required_contacts:
    #                 # 创建联系人
    #                 conts.create_contacts_if_not_exits(name, number)
    #             required_group_chats = dataproviders.get_preset_group_chats()
    #             conts.open_group_chat_list()
    #             group_list = GroupListPage()
    #             for group_name, members in required_group_chats:
    #                 group_list.wait_for_page_load()
    #                 # 创建群
    #                 group_list.create_group_chats_if_not_exits(group_name, members)
    #             group_list.click_back()
    #             conts.open_message_page()
    #             flag1 = True
    #         except:
    #             fail_time1 += 1
    #         if flag1:
    #             break
    #
    #     # 导入团队联系人
    #     fail_time2 = 0
    #     flag2 = False
    #     while fail_time2 < 5:
    #         try:
    #             Preconditions.make_already_in_message_page()
    #             contact_names = ["大佬1", "大佬2", "大佬3", "大佬4"]
    #             Preconditions.create_he_contacts(contact_names)
    #             flag2 = True
    #         except:
    #             fail_time2 += 1
    #         if flag2:
    #             break
    #
    #     # 确保有企业群
    #     fail_time3 = 0
    #     flag3 = False
    #     while fail_time3 < 5:
    #         try:
    #             Preconditions.make_already_in_message_page()
    #             Preconditions.ensure_have_enterprise_group()
    #             flag3 = True
    #         except:
    #             fail_time3 += 1
    #         if flag3:
    #             break

    def default_setUp(self):
        """
        1、成功登录和飞信
        2、确保当前页面在群聊聊天会话页面
        """

        Preconditions.select_mobile('IOS-移动')
        mp = MessagePage()
        name = "群聊1"
        if mp.is_on_this_page():
            Preconditions.get_into_group_chat_page(name)
            return
        gcp = GroupChatPage()
        if not gcp.is_on_this_page():
            current_mobile().launch_app()
            Preconditions.make_already_in_message_page()
            Preconditions.get_into_group_chat_page(name)

    def default_tearDown(self):

        Preconditions.disconnect_mobile('IOS-移动')

    @tags('ALL', 'CMCC', 'LXD', 'high')
    def test_msg_xiaoliping_D_0021(self):
        """群聊会话页面，打开拍照，立刻返回会话窗口"""

        gcp = GroupChatPage()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        # 点击富媒体行拍照图标
        gcp.click_take_photo()
        cpp = ChatPhotoPage()
        # 等待聊天拍照页面加载
        cpp.wait_for_page_load()
        # 点击"∨"
        cpp.take_photo_back()
        # 1.等待群聊页面加载
        gcp.wait_for_page_load()

    @tags('ALL', 'CMCC', 'LXD')
    def test_msg_xiaoliping_D_0041(self):
        """群聊会话页面,转发自己发送的图片到当前会话窗口"""

        gcp = GroupChatPage()
        gcp.wait_for_page_load()
        # 给当前会话页面发送一张图片,确保最近聊天中有记录
        time.sleep(2)
        gcp.click_picture()
        if gcp.is_text_present("想访问您的照片"):
            gcp.click_text("好")
        cpg = ChatPicPage()
        cpg.wait_for_page_load()
        cpg.select_picture()
        cpg.click_send()
        time.sleep(5)
        # 1.长按自己发送的图片并转发
        gcp.forward_pic()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载
        scg.wait_for_page_load()
        time.sleep(2)
        # 3.选择最近聊天中的当前会话窗口
        group_name = "群聊1"
        scg.select_recent_chat_by_name(group_name)
        # 确定转发
        scg.click_sure_forward()
        # 4.是否提示已转发,等待群聊页面加载
        # self.assertEquals(gcp.is_exist_forward(), True)
        gcp.wait_for_page_load()
        # 5.验证是否发送成功
        cwp = ChatWindowPage()
        cwp.wait_for_msg_send_status_become_to('发送成功', 30)

    @tags('ALL', 'CMCC', 'LXD', 'high')
    def test_msg_xiaoliping_D_0042(self):
        """群聊会话页面，转发自己发送的图片到当前会话窗口时失败"""

        gcp = GroupChatPage()
        gcp.wait_for_page_load()
        # 给当前会话页面发送一张图片,确保最近聊天中有记录
        time.sleep(2)
        gcp.click_picture()
        cpg = ChatPicPage()
        cpg.wait_for_page_load()
        cpg.select_pic_fk(1)
        cpg.click_send()
        time.sleep(5)
        gcp.click_back()
        # 确保当前消息列表没有消息发送失败的标识影响验证结果
        Preconditions.make_no_message_send_failed_status()
        group_name = "群聊1"
        Preconditions.get_into_group_chat_page(group_name)
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        # 设置手机网络断开
        # gcp.set_network_status(0)
        # 1.长按自己发送的图片并转发
        gcp.forward_pic()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载
        scg.wait_for_page_load()
        # 3.选择最近聊天中的当前会话窗口
        scg.select_recent_chat_by_name(group_name)
        # 确定转发
        scg.click_sure_forward()
        # 4.是否提示已转发,等待群聊页面加载
        self.assertEquals(gcp.is_exist_forward(), True)
        gcp.wait_for_page_load()
        gcp.click_back()
        mp = MessagePage()
        mp.wait_for_page_load()
        # 5.是否存在消息发送失败的标识
        self.assertEquals(mp.is_iv_fail_status_present(), True)

    @tags('ALL', 'CMCC', 'LXD')
    def test_msg_xiaoliping_D_0043(self):
        """群聊会话页面，转发自己发送的图片到当前会话窗口时点击取消转发"""

        gcp = GroupChatPage()
        gcp.wait_for_page_load()
        # 给当前会话页面发送一张图片,确保最近聊天中有记录
        time.sleep(2)
        gcp.click_picture()
        cpg = ChatPicPage()
        cpg.wait_for_page_load()
        cpg.select_pic_fk(1)
        cpg.click_send()
        time.sleep(5)
        # 解决发送图片后，最近聊天窗口没有记录，需要退出刷新的问题
        gcp.click_back()
        group_name = "群聊1"
        Preconditions.get_into_group_chat_page(group_name)
        # 1.长按自己发送的图片并转发
        gcp.forward_pic()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载
        scg.wait_for_page_load()
        # 3.选择最近聊天中的当前会话窗口
        scg.select_recent_chat_by_name(group_name)
        # 取消转发
        scg.click_cancel_forward()
        # 4.等待选择联系人页面加载
        scg.wait_for_page_load()
        # 返回群聊天页面
        scg.click_back()

    @tags('ALL', 'CMCC', 'LXD')
    def test_msg_xiaoliping_D_0044(self):
        """群聊会话页面，转发自己发送的图片给手机联系人"""

        # 确保当前群聊页面已有图片
        Preconditions.make_already_have_my_picture()
        gcp = GroupChatPage()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        # 1.长按自己发送的图片并转发
        gcp.forward_pic()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载
        scg.wait_for_page_load()
        # 点击“选择本地联系人”菜单
        scg.select_local_contacts()
        slc = SelectLocalContactsPage()
        # 等待选择联系人->本地联系人 页面加载
        slc.wait_for_page_load()
        name = "大佬1"
        # 3.选择一个手机联系人
        slc.selecting_local_contacts_by_name(name)
        # 确定转发
        scg.click_sure_forward()
        # 4.是否提示已转发,等待群聊页面加载
        self.assertEquals(gcp.is_exist_forward(), True)
        gcp.wait_for_page_load()
        # 返回到消息页
        gcp.click_back()
        mp = MessagePage()
        # 等待消息页面加载
        mp.wait_for_page_load()
        # 选择刚发送消息的聊天页
        mp.choose_chat_by_name(name)
        time.sleep(2)
        chat = BaseChatPage()
        if chat.is_exist_dialog():
            # 点击我已阅读
            chat.click_i_have_read()
        # 5.验证是否发送成功
        cwp = ChatWindowPage()
        cwp.wait_for_msg_send_status_become_to('发送成功', 30)
        # 返回消息页
        gcp.click_back()

    @tags('ALL', 'CMCC', 'LXD', 'high')
    def test_msg_xiaoliping_D_0045(self):
        """群聊会话页面，转发自己发送的图片到手机联系人时失败"""

        gcp = GroupChatPage()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        gcp.click_back()
        # 确保当前消息列表没有消息发送失败的标识影响验证结果
        Preconditions.make_no_message_send_failed_status()
        group_name = "群聊1"
        Preconditions.get_into_group_chat_page(group_name)
        # 确保当前群聊页面已有图片
        Preconditions.make_already_have_my_picture()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        # 设置手机网络断开
        # gcp.set_network_status(0)
        # 1.长按自己发送的图片并转发
        gcp.forward_pic()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载
        scg.wait_for_page_load()
        # 点击“选择本地联系人”菜单
        scg.select_local_contacts()
        slc = SelectLocalContactsPage()
        # 等待选择联系人->本地联系人 页面加载
        slc.wait_for_page_load()
        contact_name = "大佬1"
        # 3.选择一个手机联系人
        slc.selecting_local_contacts_by_name(contact_name)
        # 确定转发
        scg.click_sure_forward()
        # 4.是否提示已转发,等待群聊页面加载
        self.assertEquals(gcp.is_exist_forward(), True)
        gcp.wait_for_page_load()
        # 返回到消息页
        gcp.click_back()
        mp = MessagePage()
        mp.wait_for_page_load()
        # 5.是否存在消息发送失败的标识
        self.assertEquals(mp.is_iv_fail_status_present(), True)

    @tags('ALL', 'CMCC', 'LXD')
    def test_msg_xiaoliping_D_0046(self):
        """群聊会话页面，转发自己发送的图片到手机联系人时点击取消转发"""

        # 确保当前群聊页面已有图片
        Preconditions.make_already_have_my_picture()
        gcp = GroupChatPage()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        # 1.长按自己发送的图片并转发
        gcp.forward_pic()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载
        scg.wait_for_page_load()
        # 点击“选择本地联系人”菜单
        scg.select_local_contacts()
        slc = SelectLocalContactsPage()
        # 等待选择联系人->本地联系人 页面加载
        slc.wait_for_page_load()
        name = "大佬1"
        # 3.选择一个手机联系人
        slc.selecting_local_contacts_by_name(name)
        # 取消转发
        scg.click_cancel_forward()
        # 4.等待选择联系人->本地联系人 页面加载
        slc.wait_for_page_load()
        # 返回群聊天页面
        slc.click_back()
        scg.wait_for_page_load()
        scg.click_back()

    @tags('ALL', 'CMCC', 'LXD', 'high')
    def test_msg_xiaoliping_D_0047(self):
        """群聊会话页面，转发自己发送的图片给团队联系人"""

        gcp = GroupChatPage()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        # 确保当前群聊页面已有图片
        Preconditions.make_already_have_my_picture()
        # 1.长按自己发送的图片并转发
        gcp.forward_pic()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载
        scg.wait_for_page_load()
        # 点击“选择和通讯录联系人”菜单
        scg.click_he_contacts()
        shc = SelectHeContactsDetailPage()
        # 等待选择联系人->和通讯录联系人 页面加载
        shc.wait_for_he_contacts_page_load()
        # 3.选择一个团队联系人
        # 需要考虑测试号码存在多个团队的情况
        Preconditions.if_exists_multiple_enterprises_enter_group_chat("pic")
        name = "大佬3"
        shc.selecting_he_contacts_by_name(name)
        # 确定转发
        scg.click_sure_forward()
        # 4.是否提示已转发,等待群聊页面加载
        self.assertEquals(gcp.is_exist_forward(), True)
        gcp.wait_for_page_load()
        # 返回到消息页
        gcp.click_back()
        mp = MessagePage()
        # 等待消息页面加载
        mp.wait_for_page_load()
        # 选择刚发送消息的聊天页
        mp.choose_chat_by_name(name)
        time.sleep(2)
        chat = BaseChatPage()
        if chat.is_exist_dialog():
            # 点击我已阅读
            chat.click_i_have_read()
        # 5.验证是否发送成功
        cwp = ChatWindowPage()
        cwp.wait_for_msg_send_status_become_to('发送成功', 30)
        # 返回消息页
        gcp.click_back()

    @tags('ALL', 'CMCC', 'LXD')
    def test_msg_xiaoliping_D_0048(self):
        """群聊会话页面，转发自己发送的图片到团队联系人时失败"""

        gcp = GroupChatPage()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        gcp.click_back()
        # 确保当前消息列表没有消息发送失败的标识影响验证结果
        Preconditions.make_no_message_send_failed_status()
        group_name = "群聊1"
        Preconditions.get_into_group_chat_page(group_name)
        # 确保当前群聊页面已有图片
        Preconditions.make_already_have_my_picture()
        # 设置手机网络断开
        # gcp.set_network_status(0)
        # 1.长按自己发送的图片并转发
        gcp.forward_pic()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载
        scg.wait_for_page_load()
        # 点击“选择和通讯录联系人”菜单
        scg.click_he_contacts()
        shc = SelectHeContactsDetailPage()
        # 等待选择联系人->和通讯录联系人 页面加载
        shc.wait_for_he_contacts_page_load()
        # 3.选择一个团队联系人
        # 需要考虑测试号码存在多个团队的情况
        Preconditions.if_exists_multiple_enterprises_enter_group_chat("pic")
        contact_name = "大佬3"
        shc.selecting_he_contacts_by_name(contact_name)
        # 确定转发
        scg.click_sure_forward()
        # 4.是否提示已转发,等待群聊页面加载
        self.assertEquals(gcp.is_exist_forward(), True)
        gcp.wait_for_page_load()
        # 返回到消息页
        gcp.click_back()
        mp = MessagePage()
        mp.wait_for_page_load()
        # 5.是否存在消息发送失败的标识
        self.assertEquals(mp.is_iv_fail_status_present(), True)

    @tags('ALL', 'CMCC', 'LXD')
    def test_msg_xiaoliping_D_0049(self):
        """群聊会话页面，转发自己发送的图片到团队联系人时点击取消转发"""

        gcp = GroupChatPage()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        # 确保当前群聊页面已有图片
        Preconditions.make_already_have_my_picture()
        # 1.长按自己发送的图片并转发
        gcp.forward_pic()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载
        scg.wait_for_page_load()
        # 点击“选择和通讯录联系人”菜单
        scg.click_he_contacts()
        shc = SelectHeContactsDetailPage()
        # 等待选择联系人->和通讯录联系人 页面加载
        shc.wait_for_he_contacts_page_load()
        # 3.选择一个团队联系人
        # 需要考虑测试号码存在多个团队的情况
        Preconditions.if_exists_multiple_enterprises_enter_group_chat("pic")
        name = "大佬3"
        shc.selecting_he_contacts_by_name(name)
        # 取消转发
        scg.click_cancel_forward()
        # 4.等待选择联系人->和通讯录联系人 页面加载
        shc.wait_for_he_contacts_page_load()
        # 返回群聊天页面
        shc.click_back()
        shc.click_back()
        scg.wait_for_page_load()
        scg.click_back()
        gcp.wait_for_page_load()

    @tags('ALL', 'CMCC', 'LXD', 'high')
    def test_msg_xiaoliping_D_0050(self):
        """群聊会话页面，转发自己发送的图片给陌生人"""

        # 确保当前群聊页面已有图片
        Preconditions.make_already_have_my_picture()
        gcp = GroupChatPage()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        # 1.长按自己发送的图片并转发
        gcp.forward_pic()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载
        scg.wait_for_page_load()
        number = "13855558888"
        # 输入陌生手机号码
        scg.input_search_keyword(number)
        time.sleep(2)
        current_mobile().hide_keyboard_if_display()
        # 3.选择陌生号码转发
        scg.click_unknown_member()
        # 确定转发
        scg.click_sure_forward()
        # 4.是否提示已转发,等待群聊页面加载
        self.assertEquals(gcp.is_exist_forward(), True)
        gcp.wait_for_page_load()
        # 返回到消息页
        gcp.click_back()
        mp = MessagePage()
        # 等待消息页面加载
        mp.wait_for_page_load()
        # 选择刚发送消息的陌生联系人
        mp.choose_chat_by_name(number)
        time.sleep(2)
        chat = BaseChatPage()
        if chat.is_exist_dialog():
            # 点击我已阅读
            chat.click_i_have_read()
        # 5.验证是否发送成功
        cwp = ChatWindowPage()
        cwp.wait_for_msg_send_status_become_to('发送成功', 30)
        # 返回消息页
        gcp.click_back()

    @tags('ALL', 'CMCC', 'LXD')
    def test_msg_xiaoliping_D_0051(self):
        """群聊会话页面，转发自己发送的图片到陌生人时失败"""

        gcp = GroupChatPage()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        gcp.click_back()
        # 确保当前消息列表没有消息发送失败的标识影响验证结果
        Preconditions.make_no_message_send_failed_status()
        group_name = "群聊1"
        Preconditions.get_into_group_chat_page(group_name)
        # 确保当前群聊页面已有图片
        Preconditions.make_already_have_my_picture()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        # 设置手机网络断开
        # gcp.set_network_status(0)
        # 1.长按自己发送的图片并转发
        gcp.forward_pic()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载
        scg.wait_for_page_load()
        number = "13855558888"
        # 输入陌生手机号码
        scg.input_search_keyword(number)
        time.sleep(2)
        current_mobile().hide_keyboard_if_display()
        # 3.选择陌生号码转发
        scg.click_unknown_member()
        # 确定转发
        scg.click_sure_forward()
        # 4.是否提示已转发,等待群聊页面加载
        self.assertEquals(gcp.is_exist_forward(), True)
        gcp.wait_for_page_load()
        # 返回到消息页
        gcp.click_back()
        mp = MessagePage()
        mp.wait_for_page_load()
        # 5.是否存在消息发送失败的标识
        self.assertEquals(mp.is_iv_fail_status_present(), True)

    @tags('ALL', 'CMCC', 'LXD')
    def test_msg_xiaoliping_D_0052(self):
        """群聊会话页面，转发自己发送的图片到陌生人时点击取消转发"""

        # 确保当前群聊页面已有图片
        Preconditions.make_already_have_my_picture()
        gcp = GroupChatPage()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        # 1.长按自己发送的图片并转发
        gcp.forward_pic()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载
        scg.wait_for_page_load()
        number = "13855558888"
        # 输入陌生手机号码
        scg.input_search_keyword(number)
        time.sleep(2)
        current_mobile().hide_keyboard_if_display()
        # 3.选择陌生号码转发
        scg.click_unknown_member()
        # 取消转发
        scg.click_cancel_forward()
        # 4.等待选择联系人页面加载
        scg.wait_for_page_load()
        # 返回群聊天页面
        scg.click_back()

    @tags('ALL', 'CMCC', 'LXD')
    def test_msg_xiaoliping_D_0053(self):
        """群聊会话页面，转发自己发送的图片到普通群"""

        # 确保当前群聊页面已有图片
        Preconditions.make_already_have_my_picture()
        gcp = GroupChatPage()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        # 1.长按自己发送的图片并转发
        gcp.forward_pic()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载
        scg.wait_for_page_load()
        # 点击“选择一个群”菜单
        scg.click_select_one_group()
        sog = SelectOneGroupPage()
        # 等待“选择一个群”页面加载
        sog.wait_for_page_load()
        name = "群聊2"
        # 3.选择一个普通群
        sog.selecting_one_group_by_name(name)
        # 确定转发
        sog.click_sure_forward()
        # 4.是否提示已转发,等待群聊页面加载
        self.assertEquals(gcp.is_exist_forward(), True)
        gcp.wait_for_page_load()
        # 返回到消息页
        gcp.click_back()
        mp = MessagePage()
        # 等待消息页面加载
        mp.wait_for_page_load()
        # 选择刚发送消息的聊天页
        mp.choose_chat_by_name(name)
        time.sleep(2)
        # 5.验证是否发送成功
        cwp = ChatWindowPage()
        cwp.wait_for_msg_send_status_become_to('发送成功', 30)
        # 返回消息页
        gcp.click_back()

    @tags('ALL', 'CMCC', 'LXD')
    def test_msg_xiaoliping_D_0054(self):
        """群聊会话页面，转发自己发送的图片到普通群时失败"""

        gcp = GroupChatPage()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        gcp.click_back()
        # 确保当前消息列表没有消息发送失败的标识影响验证结果
        Preconditions.make_no_message_send_failed_status()
        group_name = "群聊1"
        Preconditions.get_into_group_chat_page(group_name)
        # 确保当前群聊页面已有图片
        Preconditions.make_already_have_my_picture()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        # 设置手机网络断开
        # gcp.set_network_status(0)
        # 1.长按自己发送的图片并转发
        gcp.forward_pic()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载
        scg.wait_for_page_load()
        # 点击“选择一个群”菜单
        scg.click_select_one_group()
        sog = SelectOneGroupPage()
        # 等待“选择一个群”页面加载
        sog.wait_for_page_load()
        name = "群聊2"
        # 3.选择一个普通群
        sog.selecting_one_group_by_name(name)
        # 确定转发
        sog.click_sure_forward()
        # 4.是否提示已转发,等待群聊页面加载
        self.assertEquals(gcp.is_exist_forward(), True)
        gcp.wait_for_page_load()
        # 返回到消息页
        gcp.click_back()
        mp = MessagePage()
        mp.wait_for_page_load()
        # 5.是否存在消息发送失败的标识
        self.assertEquals(mp.is_iv_fail_status_present(), True)

    @tags('ALL', 'CMCC', 'LXD')
    def test_msg_xiaoliping_D_0055(self):
        """群聊会话页面，转发自己发送的图片到普通群时点击取消转发"""

        # 确保当前群聊页面已有图片
        Preconditions.make_already_have_my_picture()
        gcp = GroupChatPage()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        # 1.长按自己发送的图片并转发
        gcp.forward_pic()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载
        scg.wait_for_page_load()
        # 点击“选择一个群”菜单
        scg.click_select_one_group()
        sog = SelectOneGroupPage()
        # 3.等待“选择一个群”页面加载
        sog.wait_for_page_load()
        name = "群聊2"
        # 4.选择一个普通群
        sog.selecting_one_group_by_name(name)
        # 取消转发
        sog.click_cancel_forward()
        # 5.等待“选择一个群”页面加载
        sog.wait_for_page_load()
        sog.click_back()
        # 等待选择联系人页面加载
        scg.wait_for_page_load()
        # 返回群聊天页面
        scg.click_back()

    @tags('ALL', 'CMCC', 'LXD')
    def test_msg_xiaoliping_D_0056(self):
        """群聊会话页面，转发自己发送的图片到企业群"""

        gcp = GroupChatPage()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        # 确保当前群聊页面已有图片
        Preconditions.make_already_have_my_picture()
        # 1.长按自己发送的图片并转发
        gcp.forward_pic()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载
        scg.wait_for_page_load()
        # 点击“选择一个群”菜单
        scg.click_select_one_group()
        sog = SelectOneGroupPage()
        # 等待“选择一个群”页面加载
        sog.wait_for_page_load()
        # 3.选择一个企业群
        name = sog.select_one_enterprise_group()
        # 确定转发
        sog.click_sure_forward()
        # 4.是否提示已转发,等待群聊页面加载
        self.assertEquals(gcp.is_exist_forward(), True)
        gcp.wait_for_page_load()
        # 返回到消息页
        gcp.click_back()
        mp = MessagePage()
        # 等待消息页面加载
        mp.wait_for_page_load()
        # 选择刚发送消息的聊天页
        mp.choose_chat_by_name(name)
        time.sleep(2)
        # 5.验证是否发送成功
        cwp = ChatWindowPage()
        cwp.wait_for_msg_send_status_become_to('发送成功', 30)
        # 返回消息页
        gcp.click_back()

    @tags('ALL', 'CMCC', 'LXD')
    def test_msg_xiaoliping_D_0057(self):
        """群聊会话页面，转发自己发送的图片到企业群时失败"""

        gcp = GroupChatPage()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        gcp.click_back()
        # 确保当前消息列表没有消息发送失败的标识影响验证结果
        Preconditions.make_no_message_send_failed_status()
        group_name = "群聊1"
        Preconditions.get_into_group_chat_page(group_name)
        # 确保当前群聊页面已有图片
        Preconditions.make_already_have_my_picture()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        # 设置手机网络断开
        # gcp.set_network_status(0)
        # 1.长按自己发送的图片并转发
        gcp.forward_pic()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载
        scg.wait_for_page_load()
        # 点击“选择一个群”菜单
        scg.click_select_one_group()
        sog = SelectOneGroupPage()
        # 等待“选择一个群”页面加载
        sog.wait_for_page_load()
        # 3.选择一个企业群
        sog.select_one_enterprise_group()
        # 确定转发
        sog.click_sure_forward()
        # 4.是否提示已转发,等待群聊页面加载
        self.assertEquals(gcp.is_exist_forward(), True)
        gcp.wait_for_page_load()
        # 返回到消息页
        gcp.click_back()
        mp = MessagePage()
        mp.wait_for_page_load()
        # 5.是否存在消息发送失败的标识
        self.assertEquals(mp.is_iv_fail_status_present(), True)

    @tags('ALL', 'CMCC', 'LXD')
    def test_msg_xiaoliping_D_0058(self):
        """群聊会话页面，转发自己发送的图片到企业群时点击取消转发"""

        gcp = GroupChatPage()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        # 确保当前群聊页面已有图片
        Preconditions.make_already_have_my_picture()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        # 1.长按自己发送的图片并转发
        gcp.forward_pic()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载
        scg.wait_for_page_load()
        # 点击“选择一个群”菜单
        scg.click_select_one_group()
        sog = SelectOneGroupPage()
        # 3.等待“选择一个群”页面加载
        sog.wait_for_page_load()
        # 4.选择一个企业群
        sog.select_one_enterprise_group()
        # 取消转发
        sog.click_cancel_forward()
        # 5.等待“选择一个群”页面加载
        sog.wait_for_page_load()
        sog.click_back()
        # 等待选择联系人页面加载
        scg.wait_for_page_load()
        # 返回群聊天页面
        scg.click_back()

    @tags('ALL', 'CMCC', 'LXD', 'high')
    def test_msg_xiaoliping_D_0069(self):
        """群聊会话页面，转发自己发送的视频给手机联系人"""

        # 确保当前群聊页面已有视频
        Preconditions.make_already_have_my_videos()
        time.sleep(5)
        gcp = GroupChatPage()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        # 1.长按自己发送的视频并转发
        gcp.forward_video()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载,点击“选择本地联系人”菜单
        scg.wait_for_page_load()
        scg.select_local_contacts()
        slc = SelectLocalContactsPage()
        # 等待选择联系人->本地联系人 页面加载
        slc.wait_for_page_load()
        name = "大佬1"
        # 3.选择一个手机联系人
        slc.selecting_local_contacts_by_name(name)
        # 确定转发
        scg.click_sure_forward()
        # 4.是否提示已转发,等待群聊页面加载
        self.assertEquals(gcp.is_exist_forward(), True)
        gcp.wait_for_page_load()
        # 返回到消息页
        gcp.click_back()
        mp = MessagePage()
        # 等待消息页面加载
        mp.wait_for_page_load()
        # 选择刚发送消息的聊天页
        mp.choose_chat_by_name(name)
        time.sleep(2)
        chat = BaseChatPage()
        if chat.is_exist_dialog():
            # 点击我已阅读
            chat.click_i_have_read()
        # 5.验证是否发送成功
        cwp = ChatWindowPage()
        cwp.wait_for_msg_send_status_become_to('发送成功', 30)
        # 返回消息页
        gcp.click_back()

    @tags('ALL', 'CMCC', 'LXD')
    def test_msg_xiaoliping_D_0070(self):
        """群聊会话页面，转发自己发送的视频给手机联系人时失败"""

        gcp = GroupChatPage()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        gcp.click_back()
        # 确保当前消息列表没有消息发送失败的标识影响验证结果
        Preconditions.make_no_message_send_failed_status()
        group_name = "群聊1"
        Preconditions.get_into_group_chat_page(group_name)
        # 确保当前群聊页面已有视频
        Preconditions.make_already_have_my_videos()
        time.sleep(5)
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        # 设置手机网络断开
        # gcp.set_network_status(0)
        # 1.长按自己发送的视频并转发
        gcp.forward_video()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载,点击“选择本地联系人”菜单
        scg.wait_for_page_load()
        scg.select_local_contacts()
        slc = SelectLocalContactsPage()
        # 等待选择联系人->本地联系人 页面加载
        slc.wait_for_page_load()
        contact_name = "大佬1"
        # 3.选择一个手机联系人
        slc.selecting_local_contacts_by_name(contact_name)
        # 确定转发
        scg.click_sure_forward()
        # 4.是否提示已转发,等待群聊页面加载
        self.assertEquals(gcp.is_exist_forward(), True)
        gcp.wait_for_page_load()
        # 返回到消息页
        gcp.click_back()
        mp = MessagePage()
        mp.wait_for_page_load()
        # 5.是否存在消息发送失败的标识
        self.assertEquals(mp.is_iv_fail_status_present(), True)

    @tags('ALL', 'CMCC', 'LXD')
    def test_msg_xiaoliping_D_0071(self):
        """群聊会话页面，转发自己发送的视频给手机联系人时点击取消转发"""

        # 确保当前群聊页面已有视频
        Preconditions.make_already_have_my_videos()
        time.sleep(5)
        gcp = GroupChatPage()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        # 1.长按自己发送的视频并转发
        gcp.forward_video()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载
        scg.wait_for_page_load()
        # 点击“选择本地联系人”菜单
        scg.select_local_contacts()
        slc = SelectLocalContactsPage()
        # 等待选择联系人->本地联系人 页面加载
        slc.wait_for_page_load()
        name = "大佬1"
        # 3、4.选择一个手机联系人
        slc.selecting_local_contacts_by_name(name)
        # 取消转发
        scg.click_cancel_forward()
        # 5.等待选择联系人->本地联系人 页面加载
        slc.wait_for_page_load()
        # 返回群聊天页面
        slc.click_back()
        scg.wait_for_page_load()
        scg.click_back()

    @tags('ALL', 'CMCC', 'LXD', 'high')
    def test_msg_xiaoliping_D_0072(self):
        """群聊会话页面，转发自己发送的视频给团队联系人"""

        gcp = GroupChatPage()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        # 确保当前群聊页面已有视频
        Preconditions.make_already_have_my_videos()
        # 1.长按自己发送的视频并转发
        gcp.forward_video()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载
        scg.wait_for_page_load()
        # 点击“选择和通讯录联系人”菜单
        scg.click_he_contacts()
        shc = SelectHeContactsDetailPage()
        # 等待选择联系人->和通讯录联系人 页面加载
        shc.wait_for_he_contacts_page_load()
        # 3.选择一个团队联系人
        # 需要考虑测试号码存在多个团队的情况
        Preconditions.if_exists_multiple_enterprises_enter_group_chat("video")
        name = "大佬3"
        shc.selecting_he_contacts_by_name(name)
        # 确定转发
        scg.click_sure_forward()
        # 4.是否提示已转发,等待群聊页面加载
        self.assertEquals(gcp.is_exist_forward(), True)
        gcp.wait_for_page_load()
        # 返回到消息页
        gcp.click_back()
        mp = MessagePage()
        # 等待消息页面加载
        mp.wait_for_page_load()
        # 选择刚发送消息的聊天页
        mp.choose_chat_by_name(name)
        time.sleep(2)
        chat = BaseChatPage()
        if chat.is_exist_dialog():
            # 点击我已阅读
            chat.click_i_have_read()
        # 5.验证是否发送成功
        cwp = ChatWindowPage()
        cwp.wait_for_msg_send_status_become_to('发送成功', 30)
        # 返回消息页
        gcp.click_back()

    @tags('ALL', 'CMCC', 'LXD')
    def test_msg_xiaoliping_D_0073(self):
        """群聊会话页面，转发自己发送的视频给团队联系人时失败"""

        gcp = GroupChatPage()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        gcp.click_back()
        # 确保当前消息列表没有消息发送失败的标识影响验证结果
        Preconditions.make_no_message_send_failed_status()
        group_name = "群聊1"
        Preconditions.get_into_group_chat_page(group_name)
        # 确保当前群聊页面已有视频
        Preconditions.make_already_have_my_videos()
        # 设置手机网络断开
        # gcp.set_network_status(0)
        # 1.长按自己发送的视频并转发
        gcp.forward_video()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载
        scg.wait_for_page_load()
        # 点击“选择和通讯录联系人”菜单
        scg.click_he_contacts()
        shc = SelectHeContactsDetailPage()
        # 等待选择联系人->和通讯录联系人 页面加载
        shc.wait_for_he_contacts_page_load()
        # 3.选择一个团队联系人
        # 需要考虑测试号码存在多个团队的情况
        Preconditions.if_exists_multiple_enterprises_enter_group_chat("video")
        name = "大佬3"
        shc.selecting_he_contacts_by_name(name)
        # 确定转发
        scg.click_sure_forward()
        # 4.是否提示已转发,等待群聊页面加载
        self.assertEquals(gcp.is_exist_forward(), True)
        gcp.wait_for_page_load()
        # 返回到消息页
        gcp.click_back()
        mp = MessagePage()
        mp.wait_for_page_load()
        # 5.是否存在消息发送失败的标识
        self.assertEquals(mp.is_iv_fail_status_present(), True)

    @tags('ALL', 'CMCC', 'LXD')
    def test_msg_xiaoliping_D_0074(self):
        """群聊会话页面，转发自己发送的视频给团队联系人时点击取消转发"""

        gcp = GroupChatPage()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        # 确保当前群聊页面已有视频
        Preconditions.make_already_have_my_videos()
        # 1.长按自己发送的视频并转发
        gcp.forward_video()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载
        scg.wait_for_page_load()
        # 点击“选择和通讯录联系人”菜单
        scg.click_he_contacts()
        shc = SelectHeContactsDetailPage()
        # 等待选择联系人->和通讯录联系人 页面加载
        shc.wait_for_he_contacts_page_load()
        # 3、4.选择一个团队联系人
        # 需要考虑测试号码存在多个团队的情况
        Preconditions.if_exists_multiple_enterprises_enter_group_chat("video")
        name = "大佬3"
        shc.selecting_he_contacts_by_name(name)
        # 取消转发
        scg.click_cancel_forward()
        # 5.等待选择联系人->和通讯录联系人 页面加载
        shc.wait_for_he_contacts_page_load()
        # 返回群聊天页面
        shc.click_back()
        shc.click_back()
        scg.wait_for_page_load()
        scg.click_back()
        gcp.wait_for_page_load()

    @tags('ALL', 'CMCC', 'LXD', 'high')
    def test_msg_xiaoliping_D_0075(self):
        """群聊会话页面，转发自己发送的视频给陌生人"""

        # 确保当前群聊页面已有视频
        Preconditions.make_already_have_my_videos()
        time.sleep(5)
        gcp = GroupChatPage()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        # 1.长按自己发送的视频并转发
        gcp.forward_video()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载
        scg.wait_for_page_load()
        number = "13855558888"
        # 输入陌生手机号码
        scg.input_search_keyword(number)
        time.sleep(2)
        current_mobile().hide_keyboard_if_display()
        # 3.选择陌生号码转发
        scg.click_unknown_member()
        # 确定转发
        scg.click_sure_forward()
        # 4.是否提示已转发,等待群聊页面加载
        self.assertEquals(gcp.is_exist_forward(), True)
        gcp.wait_for_page_load()
        # 返回到消息页
        gcp.click_back()
        message = MessagePage()
        # 等待消息页面加载
        message.wait_for_page_load()
        # 选择刚发送消息的陌生联系人
        message.choose_chat_by_name(number)
        time.sleep(2)
        chat = BaseChatPage()
        if chat.is_exist_dialog():
            # 点击我已阅读
            chat.click_i_have_read()
        # 5.验证是否发送成功
        cwp = ChatWindowPage()
        cwp.wait_for_msg_send_status_become_to('发送成功', 30)
        # 返回消息页
        gcp.click_back()

    @tags('ALL', 'CMCC', 'LXD')
    def test_msg_xiaoliping_D_0076(self):
        """群聊会话页面，转发自己发送的视频给陌生人时失败"""

        gcp = GroupChatPage()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        gcp.click_back()
        # 确保当前消息列表没有消息发送失败的标识影响验证结果
        Preconditions.make_no_message_send_failed_status()
        group_name = "群聊1"
        Preconditions.get_into_group_chat_page(group_name)
        # 确保当前群聊页面已有视频
        Preconditions.make_already_have_my_videos()
        time.sleep(5)
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        # 设置手机网络断开
        # gcp.set_network_status(0)
        # 1.长按自己发送的视频并转发
        gcp.forward_video()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载
        scg.wait_for_page_load()
        number = "13855558888"
        # 输入陌生手机号码
        scg.input_search_keyword(number)
        time.sleep(2)
        current_mobile().hide_keyboard_if_display()
        # 3.选择陌生号码转发
        scg.click_unknown_member()
        # 确定转发
        scg.click_sure_forward()
        # 4.是否提示已转发,等待群聊页面加载
        self.assertEquals(gcp.is_exist_forward(), True)
        gcp.wait_for_page_load()
        # 返回到消息页
        gcp.click_back()
        mp = MessagePage()
        mp.wait_for_page_load()
        # 5.是否存在消息发送失败的标识
        self.assertEquals(mp.is_iv_fail_status_present(), True)

    @tags('ALL', 'CMCC', 'LXD')
    def test_msg_xiaoliping_D_0077(self):
        """群聊会话页面，转发自己发送的视频给陌生人时点击取消转发"""

        # 确保当前群聊页面已有视频
        Preconditions.make_already_have_my_videos()
        time.sleep(5)
        gcp = GroupChatPage()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        # 1.长按自己发送的视频并转发
        gcp.forward_video()
        scg = SelectContactsPage()
        # 2.等待选择联系人页面加载
        scg.wait_for_page_load()
        number = "13855558888"
        # 输入陌生手机号码
        scg.input_search_keyword(number)
        time.sleep(2)
        current_mobile().hide_keyboard_if_display()
        # 3、4.选择陌生号码转发
        scg.click_unknown_member()
        # 取消转发
        scg.click_cancel_forward()
        # 5.等待选择联系人页面加载
        scg.wait_for_page_load()
        # 返回群聊天页面
        scg.click_back()

    @unittest.skip("断网后返回会话页面，趣图列表关闭，无法打开")
    def test_msg_xiaoliping_D_0118(self):
        """在群聊会话窗，趣图发送失败后出现重新发送按钮"""

        gcp = GroupChatPage()
        # 如果当前群聊页面已有消息发送失败标识，需要先清除聊天记录
        if not gcp.is_send_sucess():
            # 点击聊天设置
            gcp.click_setting()
            gcs = GroupChatSetPage()
            gcs.wait_for_page_load()
            # 点击清空聊天记录
            gcs.click_clear_chat_record()
            # 点击确定按钮
            gcs.click_sure()
            time.sleep(1)
            # 返回上一级
            gcp.click_back()
        # 等待群聊页面加载
        gcp.wait_for_page_load()
        # 1.点击gif图标
        gcp.click_gif()
        gcp.wait_for_gif_ele_load()
        # 输入关键字搜索gif图片
        gcp.input_gif("2")
        # 等待gif图片页面加载
        gcp.wait_for_gif_ele_load()
        # 设置手机网络断开
        # gcp.set_network_status(0)
        # 点击发送
        gcp.send_gif()
        cwp = ChatWindowPage()
        # 2.检验发送失败的标识
        cwp.wait_for_msg_send_status_become_to('发送失败', 30)
        # 重新连接网络
        # gcp.set_network_status(6)
        # 点击重发
        gcp.click_send_again()
        # 3.验证是否发送成功
        cwp.wait_for_msg_send_status_become_to('发送成功', 30)
