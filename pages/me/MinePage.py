from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from library.core.TestLogger import TestLogger
from pages.components.Footer import FooterPage

import time
import traceback
import uuid


class MinePage(FooterPage):
    """ 我 页面"""
    ACTIVITY = 'com.cmicc.module_aboutme.ui.activity.UserProfileShowActivity'

    __locators = {
        '页头-我': (MobileBy.IOS_PREDICATE, 'name="我"'),
        '我_头像': (MobileBy.XPATH,
                 '//XCUIElementTypeStaticText[@name="请完善您的资料"]/preceding-sibling::*[1]/XCUIElementTypeImage'),
        '我_名称': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="my bianji icon"]/preceding-sibling::*[1]'),
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
        '我_卡劵_详情': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeButton'),
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
        # 资料 - 个人图像
        '我_个人图像_返回': (MobileBy.ACCESSIBILITY_ID, 'me back blue normal@2x'),
        '我_个人图像_详情': (MobileBy.ACCESSIBILITY_ID, 'icon more@2x'),
        '我_个人图像_从手机相册选择': (MobileBy.IOS_PREDICATE, 'name="从手机相册选择"'),
        '我_个人图像_保存到手机': (MobileBy.IOS_PREDICATE, 'name="保存到手机"'),
        # 资料 - 电话号码
        '我_资料_电话号码': (MobileBy.IOS_PREDICATE, 'name="电话号码"'),
        '我_资料_电话号码文本': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="电话号码"]/following-sibling::*[1]'),
        # 资料 - 昵称
        '我_资料_昵称': (MobileBy.XPATH, '//*[@name="昵称"]'),
        '我_资料_昵称文本': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="昵称"]/following-sibling::*[2]'),
        '我_备注_清除': (MobileBy.IOS_PREDICATE, 'name="清除文本"'),
        # 资料 - 性别
        '我_资料_性别': (MobileBy.IOS_PREDICATE, 'name="性别"'),
        '我_资料_性别文本': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="性别"]/following-sibling::*[1]'),
        '我_资料_性别详情': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="性别"]/following-sibling::*[2]'),
        # 资料 - 年龄
        '我_资料_年龄': (MobileBy.IOS_PREDICATE, 'name="年龄"'),
        '我_资料_年龄文本': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="年龄"]/following-sibling::*[1]'),
        '我_资料_年龄详情': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="年龄"]/following-sibling::*[2]'),
        # 资料 - 我的标签
        '我_资料_我的标签': (MobileBy.IOS_PREDICATE, 'name="我的标签"'),
        '我_资料_我的标签文本': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="我的标签"]/following-sibling::*[1]'),
        '我_资料_我的标签详情': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="我的标签"]/following-sibling::*[2]'),
        # 资料 - 职业
        '我_资料_职业': (MobileBy.IOS_PREDICATE, 'name="职业"'),
        '我_资料_职业其他': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="职业"]/following-sibling::*[1]'),
        '我_资料_职业文本': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="职业"]/following-sibling::*[2]'),
        '我_资料_职业详情': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="职业"]/following-sibling::*[3]'),

        # 下拉框
        '我_下拉框_完成': (MobileBy.IOS_PREDICATE, 'name="完成"'),

        # 资料 - 标签
        '我_资料标签_返回': (MobileBy.ACCESSIBILITY_ID, 'me back blue normal@2x'),
        '我_资料标签_保存': (MobileBy.IOS_PREDICATE, 'name="保存"'),
        '我_资料标签_添加弹框': (MobileBy.ACCESSIBILITY_ID, 'my biaoqian button n'),
        '我_资料标签_添加文本框': (MobileBy.XPATH, '//*[@name="新增标签"]/following-sibling::*[1]'),
        '我_资料标签_添加确定': (MobileBy.IOS_PREDICATE, 'name="确定"'),
        '我_资料标签_添加取消': (MobileBy.IOS_PREDICATE, 'name="取消"'),
        '我_资料标签_1': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="my biaoqian button n"]/following-sibling::*[1]'),
        '我_资料标签_2': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="my biaoqian button n"]/following-sibling::*[2]'),
        '我_资料标签_3': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="my biaoqian button n"]/following-sibling::*[3]'),
        '我_资料标签_4': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="my biaoqian button n"]/following-sibling::*[4]'),
        '我_资料标签_5': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="my biaoqian button n"]/following-sibling::*[5]'),
        '我_资料标签_6': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="my biaoqian button n"]/following-sibling::*[6]'),
        '我_资料标签_最多选择5个标签': (MobileBy.IOS_PREDICATE, 'name="最多选择5个标签"'),
        '我_资料标签_我知道了': (MobileBy.IOS_PREDICATE, 'name="我知道了"'),

        # 资料 - 职业
        '我_资料职业_返回': (MobileBy.ACCESSIBILITY_ID, 'me back blue normal@2x'),
        '我_资料职业_列表': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell'),
        '我_资料职业_1': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]'),
        '我_资料职业_2': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[2]'),

        # 二级页面
        '我_二级页面_相同返回':  (MobileBy.ACCESSIBILITY_ID, 'me back blue pressed@2x'),

        # tab 积分
        '我_积分_积分': (MobileBy.IOS_PREDICATE, 'name="积分"'),
        '我_积分_返回': (MobileBy.ACCESSIBILITY_ID, 'me back blue pressed@2x'),

        # tab 每日资讯
        '我_每日资讯_每日资讯': (MobileBy.IOS_PREDICATE, 'name="每日资讯"'),
        '我_每日资讯_返回': (MobileBy.ACCESSIBILITY_ID, 'me back blue pressed@2x'),
        '我_每日资讯_皇冠': (MobileBy.XPATH,
                      '//XCUIElementTypeButton[@name="me back blue pressed@2x"]/following-sibling::*[2]'),

        # tab 活动中心
        '我_活动中心_活动中心': (MobileBy.IOS_PREDICATE, 'name="活动中心"'),
        '我_活动中心_返回': (MobileBy.ACCESSIBILITY_ID, 'me back blue pressed@2x'),

        # tab 卡劵
        '我_卡劵_卡劵': (MobileBy.IOS_PREDICATE, 'name="我的卡券"'),
        '我_卡劵_返回': (MobileBy.ACCESSIBILITY_ID, 'me back blue pressed@2x'),

        # tab 邀请有奖
        '我_邀请有奖_邀请有奖': (MobileBy.IOS_PREDICATE, 'name="邀请有奖"'),
        '我_邀请有奖_返回': (MobileBy.ACCESSIBILITY_ID, 'me back blue pressed@2x'),

        # tab 帮助与反馈
        '我_帮助与反馈_帮助与反馈': (MobileBy.IOS_PREDICATE, 'name="帮助与反馈"'),
        '我_帮助与反馈_返回': (MobileBy.ACCESSIBILITY_ID, 'me back blue pressed@2x'),

        # 设置
        '我_设置_设置': (MobileBy.IOS_PREDICATE, 'name="帮助与反馈"'),
        '我_设置_返回': (MobileBy.ACCESSIBILITY_ID, 'me back blue pressed@2x'),
        '我_设置_退出登录': (MobileBy.IOS_PREDICATE, 'name="退出登录"'),
        '我_退出登录_确认': (MobileBy.XPATH, '(//*[@name="退出登录"])[2]'),
        '一键登录': (MobileBy.XPATH, '(//XCUIElementTypeButton[@name="本机号码一键登录"])[1]'),

    }

    @TestLogger.log('获取元素文本内容')
    def get_text(self, locator):
        return self.mobile.get_text(self.__locators[locator])

    @TestLogger.log("校验text提示内容")
    def check_text_exist(self, text):
        return self.is_toast_exist(text)

    @TestLogger.log('输入文本内容')
    def input_profile_name(self, locator, text):
        self.input_text(self.__locators[locator], text)

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
    def is_element_exist(self, text):
        """当前页面是否包含此元素"""
        return self._is_element_present(self.__locators[text])

    @TestLogger.log()
    def is_text_exist(self, text):
        """当前页面是否包含此元素"""
        return self.is_text_present(text)

    @TestLogger.log('元素是否为text文本')
    def check_wait_text_exits(self, text, timeout=20):
        bol = self.wait_until(
            condition=lambda d: self.is_text_present(text), timeout=timeout
            , auto_accept_permission_alert=False)
        return bol

    @TestLogger.log("输入随机昵称")
    def input_random_nickname(self):
        """输入随机昵称"""
        uid = str(uuid.uuid4())
        nickname_uid = ''.join(uid.split('-'))
        name = nickname_uid[:15]
        self.clear_nickname_text('我_资料_昵称文本')
        time.sleep(0.5)
        self.input_profile_name('我_资料_昵称文本', name)
        time.sleep(1)
        # 滑动隐藏
        if self.is_element_already_exist('我_资料_电话号码'):
            x_source = 30 / 375 * 100
            y_source = 180 / 667 * 100
            x_target = 30 / 375 * 100
            y_target = 90 / 667 * 100
            self.swipe_by_percent_on_screen(x_source, y_source, x_target, y_target)
            time.sleep(1)

    @TestLogger.log("清空昵称内容")
    def clear_nickname_text(self, locator):
        """清空昵称内容"""
        try:
            self.click_locator_key(locator)
            time.sleep(2)
            self.click_locator_key('我_备注_清除')
            time.sleep(1)
            return True
        except:
            traceback.print_exc()
            return False

    @TestLogger.log()
    def is_on_this_page(self):
        """当前页面是否在我的页面"""
        el = self.get_elements(self.__locators['我_请完善您的资料_图片'])
        if len(el) > 0:
            return True
        return False

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
            condition=lambda d: self.get_element(self.__locators['我_设置'])
        ).click()

    @TestLogger.log()
    def wait_for_page_load(self, timeout=8, auto_accept_alerts=True):
        """判断页面是否包含选中状态的“我”页脚标签"""
        try:
            self.wait_until(
                condition=lambda d: self.get_element(self.__locators['页头-我']),
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts
            )
        except:
            message = "页面在{}s内，没有加载成功".format(str(timeout))
            raise AssertionError(
                message
            )
        return self

    @TestLogger.log()
    def wait_for_element_load(self, locator, timeout=15):
        """判断页面是否包含控件"""
        try:
            self.wait_until(
                condition=lambda d: self.get_element(self.__locators[locator]),
                timeout=timeout,
            )
        except:
            message = "页面在{}s内，没有加载成功".format(str(timeout))
            raise AssertionError(
                message
            )
        return self

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
        return self._is_element_present(self.__locators['我_设置'])

    @TestLogger.log()
    def click_collection(self):
        """点击收藏按钮"""
        self.click_element(self.__locators['收藏'])

    # @TestLogger.log()
    # def click_help_menu(self, timeout=60):
    #     """点击帮助与反馈菜单"""
    #     self.scroll_to_bottom()
    #     self.wait_until(
    #         timeout=timeout,
    #         condition=lambda d: self.get_element(self.__locators['帮助与反馈'])
    #     ).click()
    # @TestLogger.log()
    # def wait_for_me_page_load(self, timeout=20, auto_accept_alerts=True):
    #     """等待我页面加载"""
    #     try:
    #         self.wait_until(
    #             timeout=timeout,
    #             auto_accept_permission_alert=auto_accept_alerts,
    #             condition=lambda d: self._is_element_present(self.__class__.__locators["二维码入口"])
    #         )
    #     except:
    #         raise AssertionError("页面在{}s内，没有加载成功".format(str(timeout)))
    #     return self
    #
    # @TestLogger.log()
    # def click_call_multiparty(self, timeout=60):
    #     """点击多方电话"""
    #     self.wait_until(
    #         timeout=timeout,
    #         condition=lambda d: self.get_element(self.__locators['多方电话'])
    #     ).click()
    #
    # @TestLogger.log()
    # def click_welfare(self):
    #     """点击收藏按钮"""
    #     self.click_element(self.__locators['福利'])
    #
    # @TestLogger.log()
    # def _find_text_menu(self, locator):
    #     import time
    #     if not self.is_text_present(locator):
    #         # 找不到就翻页找到菜单再点击，
    #         self.scroll_to_top()
    #         time.sleep(1.5)
    #         if self.is_text_present(locator):
    #             return True
    #         max_try = 5
    #         current = 0
    #         while current < max_try:
    #             current += 1
    #             self.page_down()
    #             time.sleep(1.5)
    #             if self.is_text_present(locator):
    #                 return True
    #             if self._is_on_the_end_of_menu_view():
    #                 return False
    #
    # @TestLogger.log()
    # def click_view_edit(self):
    #     """点击查看并编辑资料按钮"""
    #     self.click_element(self.__locators['查看并编辑个人资料'])
    #
    # @TestLogger.log('点击个人名片头像')
    # def click_head(self):
    #     self.click_element(self.__locators['个人头像'])
    #
    # @TestLogger.log()
    # def wait_for_head_load(self, timeout=60, auto_accept_alerts=True):
    #     """等待个人名片头像加载"""
    #     try:
    #         self.wait_until(
    #             timeout=timeout,
    #             auto_accept_permission_alert=auto_accept_alerts,
    #             condition=lambda d: self._is_element_present(self.__class__.__locators["个人头像"])
    #         )
    #     except:
    #         message = "页面在{}s内，没有加载成功".format(str(timeout))
    #         raise AssertionError(
    #             message
    #         )
    #     return self
    #
    # @TestLogger.log('点击移动营业厅')
    # def click_mobile_hall_butten(self):
    #     self.click_element(self.__locators['移动营业厅'])
    #
    # @TestLogger.log("点击菜单项")
    # def click_menu(self, menu):
    #     locator = [MobileBy.XPATH, '//*[@text="{}"]'.format(menu)]
    #     self._find_menu(locator)
    #     self.click_element(locator)
    #
    # @TestLogger.log('点击二维码图标')
    # def click_qr_code_icon(self):
    #     self.click_element(self.__locators['二维码入口'])
