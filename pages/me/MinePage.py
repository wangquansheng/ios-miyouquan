from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from library.core.TestLogger import TestLogger
from pages.components.Footer import FooterPage


class MinePage(FooterPage):
    """ 我 页面"""
    ACTIVITY = 'com.cmcc.cmrcs.android.ui.activities.HomeActivity'

    __locators = {
        '页头-我': (MobileBy.IOS_PREDICATE, 'name="我"'),
        '我_头像': (MobileBy.XPATH,
                 '//XCUIElementTypeStaticText[@name="请完善您的资料"]/preceding-sibling::*[1]/XCUIElementTypeImage'),
        '我_请完善您的资料': (MobileBy.IOS_PREDICATE, 'name="请完善您的资料"'),
        '我_请完善您的资料_图片': (MobileBy.ACCESSIBILITY_ID, 'my bianji icon'),
        '我_已认证': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="my bianji icon"]/following-sibling::*[1]'),
        '我_电话号码': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="my bianji icon"]/following-sibling::*[2]'),
        '我_时长_飞信电话剩余时长': (MobileBy.IOS_PREDICATE, 'name="飞信电话剩余时长"'),
        '我_时长_时间': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="请完善您的资料"]/preceding-sibling::*[2]'),
        '我_时长_分钟': (MobileBy.IOS_PREDICATE, 'name="分钟"'),
        '我_积分': (MobileBy.IOS_PREDICATE, 'name="积分"'),
        '我_积分_详情': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="积分"]/following-sibling::*[2]'),
        '我_每日资讯': (MobileBy.IOS_PREDICATE, 'name="每日资讯"'),
        '我_每日资讯_详情': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="每日资讯"]/following-sibling::*[1]'),
        '我_活动中心': (MobileBy.IOS_PREDICATE, 'name="活动中心"'),
        '我_活动中心_详情': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="活动中心"]/following-sibling::*[1]'),
        '我_卡劵': (MobileBy.IOS_PREDICATE, 'name="卡劵"'),
        '我_卡劵_详情': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="卡劵"]/following-sibling::*[1]'),
        '我_邀请有奖': (MobileBy.IOS_PREDICATE, 'name="邀请有奖"'),
        '我_邀请有奖_详情': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="邀请有奖"]/following-sibling::*[1]'),
        '我_帮助与反馈': (MobileBy.IOS_PREDICATE, 'name="帮助与反馈"'),
        '我_帮助与反馈_详情': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="帮助与反馈"]/following-sibling::*[1]'),
        '我_设置': (MobileBy.IOS_PREDICATE, 'name="设置"'),
        '我_设置_详情': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="设置"]/following-sibling::*[1]'),

        # 资料
        '我_资料_编辑资料': (MobileBy.IOS_PREDICATE, 'name="编辑资料"'),
        '我_资料_取消': (MobileBy.IOS_PREDICATE, 'name="取消"'),
        '我_资料_保存': (MobileBy.IOS_PREDICATE, 'name="保存"'),
        '我_资料_图像': (MobileBy.IOS_PREDICATE, 'name ENDSWITH "my_profile_editor_camera@2x.png"'),
        '我_个人图像_返回': (MobileBy.ACCESSIBILITY_ID, 'me back blue normal@2x'),
        '我_资料_电话号码': (MobileBy.IOS_PREDICATE, 'name="电话号码"'),
        '我_资料_电话号码文本': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="电话号码"]/following-sibling::*[1]'),
        '我_资料_昵称': (MobileBy.IOS_PREDICATE, 'name="昵称"'),
        '我_资料_昵称文本': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="昵称"]/following-sibling::*[2]'),
        '我_资料_性别': (MobileBy.IOS_PREDICATE, 'name="性别"'),
        '我_资料_性别文本': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="性别"]/following-sibling::*[1]'),
        '我_资料_性别详情': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="性别"]/following-sibling::*[2]'),
        '我_资料_年龄': (MobileBy.IOS_PREDICATE, 'name="年龄"'),
        '我_资料_年龄文本': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="年龄"]/following-sibling::*[1]'),
        '我_资料_年龄详情': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="年龄"]/following-sibling::*[2]'),
        '我_资料_我的标签': (MobileBy.IOS_PREDICATE, 'name="我的标签"'),
        '我_资料_我的标签文本': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="我的标签"]/following-sibling::*[1]'),
        '我_资料_我的标签详情': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="我的标签"]/following-sibling::*[2]'),
        '我_资料_职业': (MobileBy.IOS_PREDICATE, 'name="职业"'),
        '我_资料_职业其他': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="职业"]/following-sibling::*[1]'),
        '我_资料_职业文本': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="职业"]/following-sibling::*[2]'),
        '我_资料_职业详情': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="职业"]/following-sibling::*[3]'),

        # 资料标签
        '我_资料标签_返回': (MobileBy.ACCESSIBILITY_ID, 'me back blue normal@2x'),
        '我_资料标签_保存': (MobileBy.IOS_PREDICATE, 'name="保存"'),
        '我_资料标签_添加弹框': (MobileBy.ACCESSIBILITY_ID, 'my biaoqian button n'),
        '我_资料标签_添加文本框': (MobileBy.IOS_PREDICATE, 'name="添加标签"'),
        '我_资料标签_添加保存': (MobileBy.IOS_PREDICATE, 'name="确定"'),
        '我_资料标签_添加取消': (MobileBy.IOS_PREDICATE, 'name="取消"'),
        '我_资料标签_1': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="my biaoqian button n"]/following-sibling::*[1]'),
        '我_资料标签_2': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="my biaoqian button n"]/following-sibling::*[2]'),

        # 资料标签
        '我_资料职业_返回': (MobileBy.ACCESSIBILITY_ID, 'me back blue normal@2x'),
        '我_资料职业_列表': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell'),
        '我_资料职业_1': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]'),
        '我_资料职业_2': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[2]'),

        # '我_请完善您的资料_图片': (MobileBy.ACCESSIBILITY_ID, 'my bianji icon'),
        # '我_请完善您的资料_图片': (MobileBy.ACCESSIBILITY_ID, 'my bianji icon'),
        # '二维码入口': (MobileBy.ACCESSIBILITY_ID, 'cc me qrcode normal'),
        # '我的名称': (MobileBy.ACCESSIBILITY_ID, 'Label'),
        # '查看并编辑个人资料': (MobileBy.ACCESSIBILITY_ID, '查看并编辑个人资料'),
        # '个人头像': (MobileBy.ACCESSIBILITY_ID,
        #          '//XCUIElementTypeApplication[@name="和飞信"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther'
        #          '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
        #          '/XCUIElementTypeOther/XCUIElementTypeOther'
        #          '/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeImage'),
        # '和飞信电话可用时长': (MobileBy.ACCESSIBILITY_ID, 'banner_bg_card.png'),
        # '每天领积分': (MobileBy.ACCESSIBILITY_ID, 'banner_bg_card2.png'),
        # '福利': (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="福利"])[2]'),
        # '热点资讯': (MobileBy.ACCESSIBILITY_ID, '热点资讯'),
        # '移动营业厅': (MobileBy.ACCESSIBILITY_ID, '移动营业厅'),
        # '和包支付': (MobileBy.ACCESSIBILITY_ID, '和包支付'),
        # '收藏': (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="收藏"])[1]'),
        # '设置': (MobileBy.ACCESSIBILITY_ID, '//XCUIElementTypeStaticText[@name="设置"]'),
        # #底部标签栏
        # '消息': (MobileBy.ACCESSIBILITY_ID, 'com.chinasofti.rcs:id/tvMessage'),
        # '通话': (MobileBy.ACCESSIBILITY_ID, '通话'),
        # '工作台': (MobileBy.ACCESSIBILITY_ID, '工作台'),
        # '通讯录': (MobileBy.ACCESSIBILITY_ID, '联系'),
        # '我': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="我"]'),
        # # 编辑资料页面
        # '返回': (MobileBy.ACCESSIBILITY_ID, 'back'),
        # '编辑': (MobileBy.ACCESSIBILITY_ID, '编辑'),
        # '分享名片': (MobileBy.ACCESSIBILITY_ID, '//XCUIElementTypeStaticText[@name="分享名片"]'),
        # '保存': (MobileBy.ACCESSIBILITY_ID, '保存'),
        # '拍照': (MobileBy.ACCESSIBILITY_ID, 'cc me photography normal'),
        # '编辑姓名': (MobileBy.XPATH, '(//XCUIElementTypeTextView[@name="2b610f78-8d44-11e9-95e5-309c23f30f2e"])[1]'),
        # '电话': (MobileBy.ACCESSIBILITY_ID, '19849476421'),
        #
        # '页脚-我': (MobileBy.XPATH, '//*[@resource-id="com.chinasofti.rcs:id/tvMe" and @selected="true"]'),
        # 'com.chinasofti.rcs:id/rl_person': (MobileBy.ID, 'com.chinasofti.rcs:id/rl_person'),
        # 'com.chinasofti.rcs:id/fl_name': (MobileBy.ID, 'com.chinasofti.rcs:id/fl_name'),
        # '请完善名片': (MobileBy.ID, 'com.chinasofti.rcs:id/card_name_hint'),
        # '电话号码': (MobileBy.ID, 'com.chinasofti.rcs:id/card_photo_num'),
        # 'com.chinasofti.rcs:id/profile_photo_out': (MobileBy.ID, 'com.chinasofti.rcs:id/profile_photo_out'),
        # 'com.chinasofti.rcs:id/layout_for_mall': (MobileBy.ID, 'com.chinasofti.rcs:id/layout_for_mall'),
        # 'com.chinasofti.rcs:id/internet_mutil_call_layout_id': (
        #     MobileBy.ID, 'com.chinasofti.rcs:id/internet_mutil_call_layout_id'),
        # '多方电话': (MobileBy.ID, 'com.chinasofti.rcs:id/mutil_call_name_text'),
        # '300': (MobileBy.ID, 'com.chinasofti.rcs:id/mutil_call_number_text'),
        # '分钟': (MobileBy.ID, 'com.chinasofti.rcs:id/mutil_call_unit'),
        # 'com.chinasofti.rcs:id/user_money': (MobileBy.ID, 'com.chinasofti.rcs:id/user_money'),
        # '账户余额': (MobileBy.ID, 'com.chinasofti.rcs:id/money_name_text'),
        # '12.20': (MobileBy.ID, 'com.chinasofti.rcs:id/money_number_text'),
        # '元': (MobileBy.ID, 'com.chinasofti.rcs:id/money_unit'),
        # 'com.chinasofti.rcs:id/layout_flow': (MobileBy.ID, 'com.chinasofti.rcs:id/layout_flow'),
        # '可用流量': (MobileBy.ID, 'com.chinasofti.rcs:id/liuliang_name_text'),
        # '40.98': (MobileBy.ID, 'com.chinasofti.rcs:id/liuliang_number_text'),
        # 'G': (MobileBy.ID, 'com.chinasofti.rcs:id/liuliang_unit'),
        # 'com.chinasofti.rcs:id/redpager': (MobileBy.ID, 'com.chinasofti.rcs:id/redpager'),
        # '钱包': (MobileBy.ID, 'com.chinasofti.rcs:id/repager_text'),
        # 'com.chinasofti.rcs:id/welfare': (MobileBy.ID, 'com.chinasofti.rcs:id/welfare'),
        #
        # '多重好礼等你来领': (MobileBy.ID, 'com.chinasofti.rcs:id/wfCopywriting'),
        # 'com.chinasofti.rcs:id/wfSpace': (MobileBy.ID, 'com.chinasofti.rcs:id/wfSpace'),
        # 'com.chinasofti.rcs:id/welfareArrow': (MobileBy.ID, 'com.chinasofti.rcs:id/welfareArrow'),
        # 'com.chinasofti.rcs:id/collect': (MobileBy.ID, 'com.chinasofti.rcs:id/collect'),
        #
        # 'com.chinasofti.rcs:id/about_app': (MobileBy.ID, 'com.chinasofti.rcs:id/about_app'),
        # '关于和飞信': (MobileBy.ID, 'com.chinasofti.rcs:id/about_app_text'),
        # 'com.chinasofti.rcs:id/about_right_arrow': (MobileBy.ID, 'com.chinasofti.rcs:id/about_right_arrow'),
        # 'com.chinasofti.rcs:id/share_app': (MobileBy.ID, 'com.chinasofti.rcs:id/share_app'),
        # 'com.chinasofti.rcs:id/viewLine': (MobileBy.ID, 'com.chinasofti.rcs:id/viewLine'),
        # 'com.chinasofti.rcs:id/view_bg_home_tab': (MobileBy.ID, 'com.chinasofti.rcs:id/view_bg_home_tab'),
        # 'android:id/statusBarBackground': (MobileBy.ID, 'android:id/statusBarBackground'),
        # 'android:id/navigationBarBackground': (MobileBy.ID, 'android:id/navigationBarBackground'),
        # '推荐好友，赚现金红包': (MobileBy.ID, 'com.chinasofti.rcs:id/wfCopywriting'),
        # '分享客户端': (MobileBy.ID, 'com.chinasofti.rcs:id/share_app_text'),
        # 'com.chinasofti.rcs:id/feedback': (MobileBy.ID, 'com.chinasofti.rcs:id/feedback'),
        # '帮助与反馈': (MobileBy.ID, 'com.chinasofti.rcs:id/feedback_text'),
        # 'com.chinasofti.rcs:id/setting': (MobileBy.ID, 'com.chinasofti.rcs:id/setting'),
        # '姓名': (MobileBy.ID, 'com.chinasofti.rcs:id/card_name'),
        # "联系人管理":("com.chinasofti.rcs:id/manage_contact_text")
    }

    # @TestLogger.log('点击二维码图标')
    # def click_qr_code_icon(self):
    #     self.click_element(self.__locators['二维码入口'])

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

    @TestLogger.log("点击locators对应的元素")
    def click_locator_key(self, locator):
        self.click_element(self.__locators[locator])

    @TestLogger.log()
    def is_on_this_page(self):
        """当前页面是否在我的页面"""
        el = self.get_elements(self.__locators['我_请完善您的资料'])
        if len(el) > 0:
            return True
        return False

    @TestLogger.log()
    def click_view_edit(self):
        """点击查看并编辑资料按钮"""
        self.click_element(self.__locators['查看并编辑个人资料'])

    @TestLogger.log('点击个人名片头像')
    def click_head(self):
        self.click_element(self.__locators['个人头像'])

    @TestLogger.log()
    def wait_for_head_load(self, timeout=60, auto_accept_alerts=True):
        """等待个人名片头像加载"""
        try:
            self.wait_until(
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts,
                condition=lambda d: self._is_element_present(self.__class__.__locators["个人头像"])
            )
        except:
            message = "页面在{}s内，没有加载成功".format(str(timeout))
            raise AssertionError(
                message
            )
        return self

    @TestLogger.log('点击移动营业厅')
    def click_mobile_hall_butten(self):
        self.click_element(self.__locators['移动营业厅'])

    @TestLogger.log("点击菜单项")
    def click_menu(self, menu):
        locator = [MobileBy.XPATH, '//*[@text="{}"]'.format(menu)]
        self._find_menu(locator)
        self.click_element(locator)

    @TestLogger.log("回到列表顶部")
    def scroll_to_top(self):
        self.wait_until(
            condition=lambda d: self.get_element(self.__locators['菜单区域'])
        )
        # 如果找到“短信设置”菜单，则当作已经滑到底部
        if self._is_on_the_start_of_menu_view():
            return True
        max_try = 5
        current = 0
        while current < max_try:
            current += 1
            self.page_up()
            if self._is_on_the_start_of_menu_view():
                break
        return True

    @TestLogger.log("滑到菜单底部")
    def scroll_to_bottom(self):
        """滑到菜单底部"""
        self.wait_until(
            condition=lambda d: self.get_element(self.__locators['页头-我'])
        )

        # 如果找到“设置”菜单，则当作已经滑到底部
        if self._is_on_the_end_of_menu_view():
            return True
        max_try = 5
        current = 0
        while current < max_try:
            current += 1
            self.page_down()
            if self._is_on_the_end_of_menu_view():
                break
        return True

    @TestLogger.log("点击设置菜单")
    def click_setting_menu(self):
        """点击设置菜单"""
        self.scroll_to_bottom()
        self.wait_until(
            condition=lambda d: self.get_element(self.__locators['设置'])
        ).click()

    @TestLogger.log()
    def wait_for_page_load(self, timeout=8, auto_accept_alerts=True):
        """判断页面是否包含选中状态的“我”页脚标签"""
        try:
            self.wait_until(
                condition=lambda d: self.get_element(self.__locators['页脚-我']),
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts
            )
        except:
            message = "页面在{}s内，没有加载成功".format(str(timeout))
            raise AssertionError(
                message
            )
        return self

    @TestLogger.log("下一页")
    def page_down(self):
        self.wait_until(
            condition=lambda d: self.get_element(self.__locators['菜单区域'])
        )
        self.swipe_by_direction(self.__locators['菜单区域'], 'up')

    @TestLogger.log("下一页")
    def page_up(self):
        self.wait_until(
            condition=lambda d: self.get_element(self.__locators['菜单区域'])
        )
        self.swipe_by_direction(self.__locators['菜单区域'], 'down')

    @TestLogger.log()
    def _find_menu(self, locator):
        if not self._is_element_present(locator):
            # 找不到就翻页找到菜单再点击，
            self.scroll_to_top()
            if self._is_element_present(locator):
                return
            max_try = 5
            current = 0
            while current < max_try:
                current += 1
                self.page_down()
                if self._is_element_present(locator):
                    return
                if self._is_on_the_end_of_menu_view():
                    raise NoSuchElementException('页面找不到元素：{}'.format(locator))

    def _is_on_the_start_of_menu_view(self):
        """判断是否在菜单开头"""
        return self._is_element_present(self.__locators['电话号码'])

    def _is_on_the_end_of_menu_view(self):
        """判断是否在菜单开头"""
        return self._is_element_present(self.__locators['设置'])

    @TestLogger.log()
    def click_help_menu(self, timeout=60):
        """点击帮助与反馈菜单"""
        self.scroll_to_bottom()
        self.wait_until(
            timeout=timeout,
            condition=lambda d: self.get_element(self.__locators['帮助与反馈'])
        ).click()

    @TestLogger.log()
    def click_collection(self):
        """点击收藏按钮"""
        self.click_element(self.__locators['收藏'])


    @TestLogger.log()
    def is_element_exist(self, text):
        """当前页面是否包含此元素"""
        return self._is_element_present(self.__locators[text])

    @TestLogger.log()
    def is_text_exist(self, text):
        """当前页面是否包含此元素"""
        return self.is_text_present(text)


    @TestLogger.log()
    def wait_for_me_page_load(self, timeout=20, auto_accept_alerts=True):
        """等待我页面加载"""
        try:
            self.wait_until(
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts,
                condition=lambda d: self._is_element_present(self.__class__.__locators["二维码入口"])
            )
        except:
            raise AssertionError("页面在{}s内，没有加载成功".format(str(timeout)))
        return self

    @TestLogger.log()
    def click_call_multiparty(self, timeout=60):
        """点击多方电话"""
        self.wait_until(
            timeout=timeout,
            condition=lambda d: self.get_element(self.__locators['多方电话'])
        ).click()

    @TestLogger.log()
    def click_welfare(self):
        """点击收藏按钮"""
        self.click_element(self.__locators['福利'])

    @TestLogger.log()
    def _find_text_menu(self, locator):
        import time
        if not self.is_text_present(locator):
            # 找不到就翻页找到菜单再点击，
            self.scroll_to_top()
            time.sleep(1.5)
            if self.is_text_present(locator):
                return True
            max_try = 5
            current = 0
            while current < max_try:
                current += 1
                self.page_down()
                time.sleep(1.5)
                if self.is_text_present(locator):
                    return True
                if self._is_on_the_end_of_menu_view():
                    return False

