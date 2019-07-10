import re
import time

from appium.webdriver.common.mobileby import MobileBy

from library.core.TestLogger import TestLogger

from pages.components.Footer import FooterPage


# noinspection PyBroadException
class OneKeyLoginPage(FooterPage):
    """一键登录页"""

    ACTIVITY = 'com.cmcc.cmrcs.android.ui.activities.OneKeyLoginActivity'

    __locators = {
        "一键登录": (MobileBy.XPATH, '(//XCUIElementTypeButton[@name="本机号码一键登录"])[1]'),

        # 通话界面
        '拨号键盘': (MobileBy.ACCESSIBILITY_ID, 'my dialing nor@2x'),

        # 一键登录
        "一键登录_问题_确认": (MobileBy.IOS_PREDICATE, 'name="确定"'),
        "一键登录_问题_取消": (MobileBy.IOS_PREDICATE, 'name="取消"'),

        # 广告
        '广告_通话_关闭': (MobileBy.ACCESSIBILITY_ID, 'my home cancel@2x'),

        # 已登录
        '通话_文案_HEAD': (MobileBy.XPATH, '//XCUIElementTypeOther[@name="通话"]'),
        '我_Tab': (MobileBy.IOS_PREDICATE, 'name="我"'),
        '我_设置_详情': (MobileBy.IOS_PREDICATE, 'name="设置"'),
        '我_退出登录': (MobileBy.IOS_PREDICATE, 'name="退出登录"'),
        '我_退出登录_确认': (MobileBy.XPATH, '(//*[@name="退出登录"])[2]'),
    }

    @TestLogger.log()
    def is_on_this_page(self):
        """当前页面是否在一键登录页"""
        el = self.get_elements(self.__locators['一键登录'])
        if len(el) > 0:
            return True
        return False

    @TestLogger.log()
    def click_one_key_login(self):
        """点击一键登录"""
        self.click_element(self.__locators["一键登录"])
        time.sleep(6)

    @TestLogger.log()
    def click_read_agreement_detail(self):
        """点击查看详情"""
        self.click_element(self.__locators['查看详情'])

    @TestLogger.log()
    def wait_for_page_load(self, timeout=8, auto_accept_alerts=True):
        """等待一键登录页面加载"""
        try:
            el = self.get_elements(self.__locators['通话_文案_HEAD'])
            if len(el) > 0:
                self.click_locator_key('我_Tab')
                time.sleep(1)
                self.click_locator_key('我_设置_详情')
                time.sleep(1)
                self.click_locator_key('我_退出登录')
                time.sleep(1)
                self.click_locator_key('我_退出登录_确认')
                time.sleep(5)
            # 当前页面"一键登录"
            self.wait_until(
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts,
                condition=lambda d: self._is_element_present(self.__class__.__locators["一键登录"])
            )
        except:
            message = "页面在{}s内，没有加载成功".format(timeout)
            raise AssertionError(
                message
            )
        return self

    @TestLogger.log()
    def get_login_number(self, specify_card_slot=0):
        """获取一键登录界面的电话号码"""
        number = self.get_text(self.__locators['电话号码'])
        if number and re.match(r'^\d+$', number.strip()):
            return number
        else:
            print('一键登录页面可能加载手机号失败（{}），改为从配置获取手机号'.format(number))
            card_type, number = self.mobile.get_card(specify_card_slot)
            del card_type
            return number

    @TestLogger.log("点击locators对应的元素")
    def click_locator_key(self, locator):
        self.click_element(self.__locators[locator])

    @TestLogger.log("通话首页弹框关闭广告弹框")
    def close_click_home_advertisement(self):
        """通话首页弹框关闭广告弹框"""
        time.sleep(1)
        if self.is_element_already_exist('广告_通话_关闭'):
            self.click_locator_key('广告_通话_关闭')
            time.sleep(1)

    @TestLogger.log('判断元素是否存在')
    def is_element_already_exist(self, locator):
        """判断元素是否存在"""
        try:
            elements = self.get_elements(self.__locators[locator])
            if len(elements) > 0:
                return True
            else:
                return False
        except:
            return False
