from appium.webdriver.common.mobileby import MobileBy

from library.core.BasePage import BasePage
from library.core.TestLogger import TestLogger


class CallTypeSelectPage(BasePage):
    """选择通话方式页面"""
    ACTIVITY = 'com.cmicc.module_call.ui.activity.CallTypeSelectActivity'

    __locators = {
        '普通电话': (MobileBy.XPATH, "//*[contains(@text, '普通电话')]"),
        '语音通话': (MobileBy.XPATH, "//*[contains(@text, '语音通话')]"),
        '和飞信电话': (MobileBy.XPATH, "//*[contains(@text, '和飞信电话')]"),
        '知道了': (MobileBy.XPATH, "//*[contains(@text, '知道了')]"),
        '允许': (MobileBy.XPATH, "//*[contains(@text, '允许')]"),
        '和飞信通话挂断': (MobileBy.ID, "com.chinasofti.rcs:id/ivDecline"),
        '拨号方式': (MobileBy.ID, "com.chinasofti.rcs:id/ll_calltype_fetion"),
        '设置': (MobileBy.XPATH, "//*[contains(@text, '设置')]"),
    }

    @TestLogger.log()
    def get_element_y(self, locator, index=0):
        """获取控件右上角Y值"""
        elements = self.get_elements(locator)
        try:
            if len(elements) > 0:
                return elements[index].location.get('y')
        except:
            raise IndexError("元素超出索引")

    @TestLogger.log()
    def get_call_by_hefeixin_y(self):
        return self.get_element_y(self.__locators["和飞信电话"])

    @TestLogger.log()
    def get_call_by_voice_y(self):
        return self.get_element_y(self.__locators["语音通话"])

    @TestLogger.log()
    def get_call_by_general_y(self):
        return self.get_element_y(self.__locators["普通电话"])

    @TestLogger.log()
    def click_call_by_general(self):
        """点击选择普通电话"""
        self.click_element(self.__locators["普通电话"])

    @TestLogger.log()
    def is_select_call(self):
        """
        当前是否存在选择通话菜单
        """
        return self._is_element_present(self.__locators["普通通话"])

    @TestLogger.log()
    def click_call_by_voice(self):
        """点击选择语音通话"""
        self.click_element(self.__locators["语音通话"])

    @TestLogger.log()
    def click_call_by_app(self):
        """点击选择和飞信电话"""
        self.click_element(self.__locators["和飞信电话"])

    @TestLogger.log()
    def click_sure(self):
        """点击允许"""
        try:
            self.click_element(self.__locators["允许"])
        except:
            pass

    @TestLogger.log()
    def click_i_know(self):
        """点击选择知道了"""
        try:
            self.click_element(self.__locators["知道了"])
        except:
            pass

    @TestLogger.log()
    def click_app_call_end(self):
        """点击和飞信通话挂断"""
        self.click_element(self.__locators["和飞信通话挂断"])

    @TestLogger.log()
    def wait_for_app_call(self, timeout=20, auto_accept_alerts=True):
        """
        等待和飞信通话界面
        """
        try:
            self.wait_until(
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts,
                condition=lambda d: self.is_text_present("我 (主叫)")
            )
        except:
            raise AssertionError("和飞信通话界面未显示")
        return self

    @TestLogger.log()
    def click_setting(self):
        """点击设置"""
        self.click_element(self.__locators["设置"])

