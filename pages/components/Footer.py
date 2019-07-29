import subprocess

from appium.webdriver.common.mobileby import MobileBy

from library.core.BasePage import BasePage
from library.core.TestLogger import TestLogger

import time


class FooterPage(BasePage):
    """主页页脚标签栏(消息页面)"""

    ACTIVITY = 'com.cmcc.cmrcs.android.ui.activities.HomeActivity'

    __locators = {
        '通话': (MobileBy.IOS_PREDICATE, 'name=="通话"'),
        '通讯录': (MobileBy.IOS_PREDICATE, 'name=="通讯录"'),
        '我': (MobileBy.IOS_PREDICATE, 'name=="我"'),

        # 升级
        '立即升级': (MobileBy.IOS_PREDICATE, 'name=="立即升级"'),
        '暂不升级': (MobileBy.IOS_PREDICATE, 'name=="暂不升级"'),

        # 权限框
        '禁止': (MobileBy.IOS_PREDICATE, 'name=="禁止"'),
        '始终允许': (MobileBy.IOS_PREDICATE, 'name=="始终允许"'),

        # 广告
        '广告_通话_关闭': (MobileBy.IOS_PREDICATE, 'name contains "my home cancel"'),

    }

    @TestLogger.log("ios设备日志运行卡死")
    def kill_device_syslog(self):
        """
        ios获取设备运行时log，appium运行时会占用大量的脚本机cpu，所以每次都杀死所有的idevicesyslog进程，可以有效防止ios设备运行卡死
        出现原因：由于每次appium启动ios配置服务时，会有一个获取ios log的cap参数clearSystemFiles，官网文档已删除，但是最新版的appium
        还是在使用这段代码，但是不走那个关闭逻辑了
        :param udid:
        :return:
        """
        command = "pkill idevicesyslog"
        subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE).stdout.readlines()

    @TestLogger.log("通话首页弹框关闭广告弹框")
    def close_click_home_advertisement(self):
        """通话首页弹框关闭广告弹框"""
        time.sleep(0.5)
        if self._is_element_present(self.__class__.__locators['广告_通话_关闭']):
            self.click_element(self.__class__.__locators['广告_通话_关闭'])
            time.sleep(0.5)

    @TestLogger.log("关闭升级弹出框")
    def click_upgrade_close(self):
        if self._is_element_present(self.__class__.__locators['暂不升级']):
            self.click_element(self.__class__.__locators['暂不升级'])
            time.sleep(0.5)

    @TestLogger.log()
    def open_me_page(self):
        """切换到标签页：我"""
        time.sleep(0.5)
        self.click_upgrade_close()
        self.close_click_home_advertisement()
        self.click_element(self.__locators['我'])

    @TestLogger.log()
    def open_call_page(self):
        """切换到标签页：通话"""
        self.click_element(self.__locators['通话'])

    @TestLogger.log()
    def open_contacts_page(self):
        """切换到标签页：通讯录"""
        self.close_click_home_advertisement()
        self.click_element(self.__locators['通讯录'])
        # from pages.contacts.Contacts import ContactsPage
        # if ContactsPage().is_text_present('需要使用通讯录权限'):
        #     ContactsPage().click_always_allowed()
        # ContactsPage().click_sim_contact()

    @TestLogger.log()
    def call_icon_is_enabled(self):
        """通话图标是否可点击"""
        return self._is_enabled(self.__class__.__locators["通话"])

    @TestLogger.log()
    def contacts_icon_is_enabled(self):
        """通讯录图标是否可点击"""
        return self._is_enabled(self.__class__.__locators["通讯录"])

    @TestLogger.log()
    def me_icon_is_enabled(self):
        """我图标是否可点击"""
        return self._is_enabled(self.__class__.__locators["我"])

    @TestLogger.log()
    def is_exist_call_icon(self):
        """是否存在通话图标"""
        return self._is_element_present(self.__class__.__locators["通话"])

    @TestLogger.log()
    def is_exist_contacts_icon(self):
        """是否存在通讯录图标"""
        return self._is_element_present(self.__class__.__locators["通讯录"])

    @TestLogger.log()
    def is_exist_me_icon(self):
        """是否存在我图标"""
        return self._is_element_present(self.__class__.__locators["我"])

