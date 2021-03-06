from appium.webdriver.common.mobileby import MobileBy

from library.core.TestLogger import TestLogger
from pages.components.BaseChat import BaseChatPage


class LabelGroupingChatPage(BaseChatPage):
    """标签分组会话页面"""
    ACTIVITY = 'com.cmcc.cmrcs.android.ui.activities.MessageDetailActivity'

    __locators = {'': (MobileBy.ID, ''),
                  'com.chinasofti.rcs:id/action_bar_root': (MobileBy.ID, 'com.chinasofti.rcs:id/action_bar_root'),
                  'android:id/content': (MobileBy.ID, 'android:id/content'),
                  'com.chinasofti.rcs:id/pop_10g_window_drop_view': (
                      MobileBy.ID, 'com.chinasofti.rcs:id/pop_10g_window_drop_view'),
                  'com.chinasofti.rcs:id/id_toolbar': (MobileBy.ID, 'com.chinasofti.rcs:id/id_toolbar'),
                  'com.chinasofti.rcs:id/back': (MobileBy.ID, 'com.chinasofti.rcs:id/back'),
                  '返回': (MobileBy.ID, 'com.chinasofti.rcs:id/back_arrow'),
                  'com.chinasofti.rcs:id/chat_mode_content': (MobileBy.ID, 'com.chinasofti.rcs:id/chat_mode_content'),
                  'lab2': (MobileBy.ID, 'com.chinasofti.rcs:id/title'),
                  '多方通话': (MobileBy.ID, 'com.chinasofti.rcs:id/action_multicall'),
                  'com.chinasofti.rcs:id/action_setting': (MobileBy.ID, 'com.chinasofti.rcs:id/action_setting'),
                  'com.chinasofti.rcs:id/view_line': (MobileBy.ID, 'com.chinasofti.rcs:id/view_line'),
                  'com.chinasofti.rcs:id/contentFrame': (MobileBy.ID, 'com.chinasofti.rcs:id/contentFrame'),
                  'com.chinasofti.rcs:id/message_editor_layout': (
                      MobileBy.ID, 'com.chinasofti.rcs:id/message_editor_layout'),
                  'com.chinasofti.rcs:id/rv_message_chat': (MobileBy.ID, 'com.chinasofti.rcs:id/rv_message_chat'),
                  '刚刚': (MobileBy.ID, 'com.chinasofti.rcs:id/tv_time'),
                  'com.chinasofti.rcs:id/ll': (MobileBy.ID, 'com.chinasofti.rcs:id/ll'),
                  '你好': (MobileBy.ID, 'com.chinasofti.rcs:id/tv_message'),
                  'com.chinasofti.rcs:id/svd_head': (MobileBy.ID, 'com.chinasofti.rcs:id/svd_head'),
                  'com.chinasofti.rcs:id/input_and_menu': (MobileBy.ID, 'com.chinasofti.rcs:id/input_and_menu'),
                  'com.chinasofti.rcs:id/ll_text_input': (MobileBy.ID, 'com.chinasofti.rcs:id/ll_text_input'),
                  'com.chinasofti.rcs:id/layout_for_message': (MobileBy.ID, 'com.chinasofti.rcs:id/layout_for_message'),
                  'com.chinasofti.rcs:id/ll_rich_panel': (MobileBy.ID, 'com.chinasofti.rcs:id/ll_rich_panel'),
                  'com.chinasofti.rcs:id/ib_pic': (MobileBy.ID, 'com.chinasofti.rcs:id/ib_pic'),
                  'com.chinasofti.rcs:id/ib_take_photo': (MobileBy.ID, 'com.chinasofti.rcs:id/ib_take_photo'),
                  'com.chinasofti.rcs:id/ib_profile': (MobileBy.ID, 'com.chinasofti.rcs:id/ib_profile'),
                  'com.chinasofti.rcs:id/ib_gif': (MobileBy.ID, 'com.chinasofti.rcs:id/ib_gif'),
                  'com.chinasofti.rcs:id/ib_more': (MobileBy.ID, 'com.chinasofti.rcs:id/ib_more'),
                  'com.chinasofti.rcs:id/base_input_layout': (MobileBy.ID, 'com.chinasofti.rcs:id/base_input_layout'),
                  'com.chinasofti.rcs:id/input_divider_inside': (
                      MobileBy.ID, 'com.chinasofti.rcs:id/input_divider_inside'),
                  'com.chinasofti.rcs:id/input_layout': (MobileBy.ID, 'com.chinasofti.rcs:id/input_layout'),
                  'com.chinasofti.rcs:id/fl_edit_panel': (MobileBy.ID, 'com.chinasofti.rcs:id/fl_edit_panel'),
                  '说点什么...': (MobileBy.ID, 'com.chinasofti.rcs:id/et_message'),
                  'com.chinasofti.rcs:id/ib_expression': (MobileBy.ID, 'com.chinasofti.rcs:id/ib_expression'),
                  'com.chinasofti.rcs:id/ib_audio': (MobileBy.ID, 'com.chinasofti.rcs:id/ib_audio'),
                  "文件名": (MobileBy.ID, 'com.chinasofti.rcs:id/textview_file_name'),
                  # 消息长按弹窗
                  '收藏': (MobileBy.XPATH, "//*[contains(@text, '收藏')]"),
                  '转发': (MobileBy.XPATH, "//*[contains(@text, '转发')]"),
                  '撤回': (MobileBy.XPATH, "//*[contains(@text, '撤回')]"),
                  '删除': (MobileBy.XPATH, "//*[contains(@text, '删除')]"),
                  '复制': (MobileBy.XPATH, "//*[contains(@text, '复制')]"),
                  '多选': (MobileBy.XPATH, "//*[contains(@text, '多选')]"),
                  }

    @TestLogger.log()
    def is_on_this_page(self):
        """当前页面是否在群聊天页"""
        el = self.get_elements(self.__locators['多方通话'])
        if len(el) > 0:
            return True
        return False

    @TestLogger.log()
    def wait_for_page_load(self, timeout=20, auto_accept_alerts=True):
        """等待标签分组会话页面加载"""
        try:
            self.wait_until(
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts,
                condition=lambda d: self._is_element_present(self.__class__.__locators["多方通话"])
            )
        except:
            message = "页面在{}s内，没有加载成功".format(str(timeout))
            raise AssertionError(
                message
            )
        return self

    @TestLogger.log()
    def click_back(self):
        """点击返回按钮"""
        self.click_element(self.__class__.__locators["返回"])

    @TestLogger.log()
    def get_label_name(self):
        """获取标题名称"""
        el = self.get_element(self.__locators["lab2"])
        return el.text

    @TestLogger.log('文件是否存在')
    def is_element_present_file(self):
        return self._is_element_present(self.__locators['文件名'])

    @TestLogger.log()
    def press_file(self):
        """长按文件"""
        el = self.get_element(self.__class__.__locators['文件名'])
        self.press(el)

    @TestLogger.log()
    def press_last_file(self):
        """长按最后一个文件"""
        el = self.get_elements(self.__class__.__locators['文件名'])[-1]
        self.press(el)



    @TestLogger.log("删除当前分组发送的文件")
    def delete_group_all_file(self):
        msg_file = self.get_elements(('id', 'com.chinasofti.rcs:id/ll_msg'))
        if msg_file:
            for file in msg_file:
                self.press(file)
                self.click_element(self.__class__.__locators['删除'])
        else:
            raise AssertionError('当前窗口没有可以删除的消息')

    @TestLogger.log("撤回当前分组发送的文件")
    def recall_group_all_file(self):
        msg_file = self.get_elements(('id', 'com.chinasofti.rcs:id/ll_msg'))
        if msg_file:
            for file in msg_file:
                self.press(file)
                self.click_element(self.__class__.__locators['撤回'])
        else:
            raise AssertionError('当前窗口没有可以撤回的消息')

    @TestLogger.log()
    def get_file_name(self):
        """获取文件名称"""
        el = self.get_element(self.__locators["文件名"])
        return el.text

    @TestLogger.log()
    def get_one_file_name(self,type):
        """获取文件名称"""
        el = self.get_element(self.__locators["文件名"],type)
        return el.text