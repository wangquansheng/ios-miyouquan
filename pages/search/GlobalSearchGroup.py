from appium.webdriver.common.mobileby import MobileBy

from library.core.BasePage import BasePage
from library.core.TestLogger import TestLogger
from pages.components.keyboard import Keyboard


class GlobalSearchGroupPage(Keyboard, BasePage):
    """查看更多群组"""
    ACTIVITY = 'com.cmcc.cmrcs.android.ui.activities.search.GlobalSearchGroupActivity'

    __locators = {
        '返回': (MobileBy.ID, 'com.chinasofti.rcs:id/iv_back'),
        '输入关键字搜索': (MobileBy.ID, 'com.chinasofti.rcs:id/edit_query'),
        '清空关键字': (MobileBy.ID, 'com.chinasofti.rcs:id/iv_delect'),
        '数据类型名称': (MobileBy.ID, 'com.chinasofti.rcs:id/text_hint'),
        '列表': (MobileBy.ID, 'com.chinasofti.rcs:id/result_list'),
        '列表项': (MobileBy.XPATH, '//*[@resource-id="com.chinasofti.rcs:id/result_list"]/*'),
        '头像': (MobileBy.ID, 'com.chinasofti.rcs:id/iv_head'),
        '群名': (MobileBy.ID, 'com.chinasofti.rcs:id/tv_conv_name'),
        '成员数量': (MobileBy.ID, 'com.chinasofti.rcs:id / tv_member_count'),
    }

    @TestLogger.log('点击返回')
    def click_back(self):
        self.click_element(self.__locators['返回'])
