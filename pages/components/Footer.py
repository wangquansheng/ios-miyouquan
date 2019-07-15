from appium.webdriver.common.mobileby import MobileBy

from library.core.BasePage import BasePage
from library.core.TestLogger import TestLogger


class FooterPage(BasePage):
    """主页页脚标签栏(消息页面)"""

    ACTIVITY = 'com.cmcc.cmrcs.android.ui.activities.HomeActivity'

    __locators = {
        '通话': (MobileBy.IOS_PREDICATE, 'name="通话"'),
        '通讯录': (MobileBy.IOS_PREDICATE, 'name="通讯录"'),
        '我': (MobileBy.IOS_PREDICATE, 'name="我"'),
    }

    @TestLogger.log()
    def open_me_page(self):
        """切换到标签页：我"""
        self.click_element(self.__locators['我'])

    @TestLogger.log()
    def open_call_page(self):
        """切换到标签页：通话"""
        self.click_element(self.__locators['通话'])

    @TestLogger.log()
    def open_contacts_page(self):
        """切换到标签页：通讯录"""
        from pages.contacts.Contacts import ContactsPage
        self.click_element(self.__locators['通讯录'])
        if ContactsPage().is_text_present('需要使用通讯录权限'):
            ContactsPage().click_always_allowed()
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

