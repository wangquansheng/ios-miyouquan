from appium.webdriver.common.mobileby import MobileBy

from library.core.BasePage import BasePage
from library.core.TestLogger import TestLogger
from pages.components.keyboard import Keyboard


class SelectContactPage(Keyboard, BasePage):
    """发起群聊-选择联系人"""
    ACTIVITY = 'com.cmcc.cmrcs.android.ui.activities.ContactsSelectActivity'

    __locators = {
        '返回': (MobileBy.ID, 'com.chinasofti.rcs:id/back'),
        '选择联系人': (MobileBy.ID, 'com.chinasofti.rcs:id/title'),
        '确定': (MobileBy.ID, 'com.chinasofti.rcs:id/tv_sure'),
        '搜索或输入手机号': (MobileBy.ID, 'com.chinasofti.rcs:id/contact_search_bar'),
        '已添加号码列表': (MobileBy.ID, 'com.chinasofti.rcs:id/image_text'),

        # 没有输入时的几个菜单
        '右箭头图标': (MobileBy.ID, 'com.chinasofti.rcs:id/arrow_right'),
        '一般的菜单文本': (MobileBy.ID, 'com.chinasofti.rcs:id/text_hint'),
        '最近联系人': (MobileBy.ID, 'com.chinasofti.rcs:id/ll_recent_person'),
        '已选择图标': (MobileBy.ID, 'com.chinasofti.rcs:id/asp_selecttion_contact_content'),
        '联系人头像': (MobileBy.XPATH,
                  '//*[@resource-id="com.chinasofti.rcs:id/head_tv" or ' +
                  '@resource-id="com.chinasofti.rcs:id/contact_icon"]'),
        '最近联系人名': (MobileBy.XPATH, '//*[@resource-id="com.chinasofti.rcs:id/tv_name" or ' +
                   '@resource-id="com.chinasofti.rcs:id / contact_name"]'),
        '联系人号码': (MobileBy.ID, 'com.chinasofti.rcs:id/contact_number'),
        '底线': (MobileBy.ID, 'com.chinasofti.rcs:id/view_Line'),

        # 搜索结果
        '搜索结果列表': (MobileBy.XPATH, '//android.support.v7.widget.RecyclerView'),
        '列表项根节点': (MobileBy.XPATH, '//android.support.v7.widget.RecyclerView/*'),
        '搜索和通讯录联系人': (MobileBy.ID, 'com.chinasofti.rcs:id/text_hint'),

    }

    @TestLogger.log("点击返回")
    def click_back(self):
        self.click_element(self.__locators['返回'])

    @TestLogger.log("输入搜索关键字")
    def input_search_key(self, keyword):
        self.input_text(self.__locators['搜索或输入手机号'], keyword)

    @TestLogger.log('选择搜索结果第一项')
    def select_the_first_result(self):
        iterator = self.mobile.list_iterator(self.__locators['搜索结果列表'], self.__locators['列表项根节点'])
        for item in iterator:
            if item.find_elements(*self.__locators['联系人头像']):
                item.click()
                return

    @TestLogger.log('点击确定')
    def click_ok(self):
        self.click_element(self.__locators['确定'])

    @TestLogger.log("查找并选择联系人")
    def search_and_select_contact(self, *contacts):
        for contact in contacts:
            self.input_search_key(contact)
            self.hide_keyboard_if_display()
            self.select_the_first_result()
        self.click_ok()
