import time

from appium.webdriver.common.mobileby import MobileBy

from library.core.BasePage import BasePage
from library.core.TestLogger import TestLogger
from library.core.utils.applicationcache import current_mobile


class SelectHeContactsDetailPage(BasePage):
    """选择和通讯录联系人页面"""
    ACTIVITY = 'com.cmicc.module_enterprise.ui.activity.EnterPriseContactSelectInnerActivity'

    __locators = {'返回': (MobileBy.ACCESSIBILITY_ID, 'back'),
                  '选择联系人': (MobileBy.ACCESSIBILITY_ID, '选择联系人'),
                  '搜索当前组织': (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="和飞信"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField'),
                '团队联系人列表第一个': (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="和飞信"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]'),
                '团队联系人列表第二个': (MobileBy.XPATH,
                       '//XCUIElementTypeApplication[@name="和飞信"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]'),

                  '发送名片': (MobileBy.ACCESSIBILITY_ID, '发送名片'),
                  #搜索结果
                  '搜索结果-联系人头像': (MobileBy.ACCESSIBILITY_ID, 'cc_chat_personal_default'),
                  '搜索结果列表': (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="和飞信"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeTable/XCUIElementTypeCell'),


                  'com.chinasofti.rcs:id/action_bar_root': (MobileBy.ID, 'com.chinasofti.rcs:id/action_bar_root'),
                  'android:id/content': (MobileBy.ID, 'android:id/content'),
                  'com.chinasofti.rcs:id/actionbar_enterprise_contactselect_activity': (
                      MobileBy.ID, 'com.chinasofti.rcs:id/actionbar_enterprise_contactselect_activity'),
                  'com.chinasofti.rcs:id/btn_close_actionbar': (
                      MobileBy.ID, 'com.chinasofti.rcs:id/btn_close_actionbar'),
                  'com.chinasofti.rcs:id/layout_search_enterprise_contactSelect_activity': (
                      MobileBy.ID, 'com.chinasofti.rcs:id/layout_search_enterprise_contactSelect_activity'),
                  '搜索': (MobileBy.ID, 'com.chinasofti.rcs:id/contact_search_bar'),
                  'com.chinasofti.rcs:id/layout_nomal_enterprise_contactSelect_activity': (
                      MobileBy.ID, 'com.chinasofti.rcs:id/layout_nomal_enterprise_contactSelect_activity'),
                  'com.chinasofti.rcs:id/breadCrumbs_enterprise_contactSelect_activity': (
                      MobileBy.ID, 'com.chinasofti.rcs:id/breadCrumbs_enterprise_contactSelect_activity'),
                  'com.chinasofti.rcs:id/breadcrumbs_layout': (MobileBy.ID, 'com.chinasofti.rcs:id/breadcrumbs_layout'),
                  '和通讯录': (MobileBy.ID, 'android:id/title'),
                  'android:id/icon': (MobileBy.ID, 'android:id/icon'),
                  'myteam': (MobileBy.ID, 'android:id/title'),
                  'com.chinasofti.rcs:id/enterprise_fragment_contactSelect_activity': (
                      MobileBy.ID, 'com.chinasofti.rcs:id/enterprise_fragment_contactSelect_activity'),
                  'android:id/list': (MobileBy.ID, 'android:id/list'),
                  'com.chinasofti.rcs:id/layout_personal_contactlist': (
                      MobileBy.ID, 'com.chinasofti.rcs:id/layout_personal_contactlist'),
                  'com.chinasofti.rcs:id/img_icon_contactlist': (
                      MobileBy.ID, 'com.chinasofti.rcs:id/img_icon_contactlist'),
                  'com.chinasofti.rcs:id/line_search_contactlist': (
                      MobileBy.ID, 'com.chinasofti.rcs:id/line_search_contactlist'),
                  'axzq': (MobileBy.ID, 'com.chinasofti.rcs:id/tv_name_personal_contactlist'),
                  '13510772034': (MobileBy.ID, 'com.chinasofti.rcs:id/tv_position_personal_contactlist'),
                  '测试号': (MobileBy.ID, 'com.chinasofti.rcs:id/tv_name_personal_contactlist'),
                  '14775290489': (MobileBy.ID, 'com.chinasofti.rcs:id/tv_position_personal_contactlist'),
                  '张三': (MobileBy.ID, 'com.chinasofti.rcs:id/tv_name_personal_contactlist'),
                  '联系人名': (MobileBy.ID, 'com.chinasofti.rcs:id/tv_name_personal_contactlist'),
                  'com.chinasofti.rcs:id/line_big_contactlist': (
                      MobileBy.ID, 'com.chinasofti.rcs:id/line_big_contactlist'),
                  'com.chinasofti.rcs:id/layout_department_contactlist': (
                      MobileBy.ID, 'com.chinasofti.rcs:id/layout_department_contactlist'),
                  'com.chinasofti.rcs:id/img_icon_department': (
                      MobileBy.ID, 'com.chinasofti.rcs:id/img_icon_department'),
                  '测试一部': (MobileBy.ID, 'com.chinasofti.rcs:id/tv_title_department'),
                  '部门名称': (MobileBy.ID, 'com.chinasofti.rcs:id/tv_title_department'),
                  'com.chinasofti.rcs:id/img_right_department': (
                      MobileBy.ID, 'com.chinasofti.rcs:id/img_right_department'),
                  'com.chinasofti.rcs:id/line_contactlist1': (MobileBy.ID, 'com.chinasofti.rcs:id/line_contactlist1'),
                  # 选择一个和通讯录联系人转发消息时的弹框
                  '发送给': (MobileBy.XPATH, "//*[contains(@text, '发送给')]"),
                  '取消': (MobileBy.XPATH, "//*[contains(@text, '取消')]"),
                  '确定': (MobileBy.XPATH, "//*[contains(@text, '确定')]"),
                  '企业层级': (MobileBy.ID, "android:id/title"),
                  }

    @TestLogger.log()
    def click_first_he_contact(self):
        """点击第一个和通讯录联系人"""
        self.click_element(self.__class__.__locators['团队联系人列表第一个'])

    @TestLogger.log()
    def click_share_card(self):
        """点击发送名片"""
        self.click_element(self.__class__.__locators['发送名片'])

    @TestLogger.log()
    def wait_for_he_contacts_page_load(self, timeout=8, auto_accept_alerts=True):
        """等待选择联系人->和通讯录联系人 页面加载"""
        try:
            self.wait_until(
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts,
                condition=lambda d: self._is_element_present(self.__locators['团队联系人列表第一个'])
            )
        except:
            message = "页面在{}s内，没有加载成功".format(str(timeout))
            raise AssertionError(
                message
            )
        return self

    @TestLogger.log()
    def select_one_he_contact_by_number(self, number):
        """通过名称选择一个联系人"""
        self.click_element((MobileBy.ACCESSIBILITY_ID, '%s' % number))

    @TestLogger.log()
    def select_one_he_contact_by_name(self, name):
        """通过名称选择一个联系人"""
        self.click_element((MobileBy.ACCESSIBILITY_ID, '%s' % name))


    @TestLogger.log()
    def click_search_box(self):
        """点击搜索框"""
        self.click_element(self.__class__.__locators['搜索当前组织'])

    @TestLogger.log()
    def input_search_text(self,text):
        """输入搜索文本"""
        self.input_text(self.__class__.__locators['搜索当前组织'],text)

    @TestLogger.log()
    def click_search_result(self):
        """点击搜索结果"""
        self.click_element(self.__class__.__locators['搜索结果列表'])


    @TestLogger.log()
    def click_sure_forward(self):
        """点击确定转发"""
        self.click_element(self.__class__.__locators['确定'])

    @TestLogger.log()
    def click_cancel_forward(self):
        """点击取消转发"""
        self.click_element(self.__class__.__locators['取消'])

    @TestLogger.log()
    def select_one_linkman(self, name):
        """选择一个联系人"""
        self.click_element((MobileBy.ACCESSIBILITY_ID, "%s" % name))

    @TestLogger.log()
    def select_one_department(self, name):
        """选择一个部门"""
        self.click_element((MobileBy.XPATH, "//*[@text='%s']" % name))

    @TestLogger.log()
    def get_contacts_names(self):
        """获取联系人名"""
        els = self.get_elements(self.__class__.__locators['联系人名'])
        contacts_names = []
        if els:
            for el in els:
                contacts_names.append(el.text)
        return contacts_names

    @TestLogger.log()
    def get_department_names(self):
        """获取部门名称"""
        els = self.get_elements(self.__class__.__locators['部门名称'])
        department_names = []
        if els:
            for el in els:
                department_names.append(el.text)
        return department_names

    @TestLogger.log()
    def click_back(self):
        """点击 返回"""
        self.click_element(self.__class__.__locators["返回"])

    @TestLogger.log()
    def input_search(self, text):
        """输入名字"""
        self.input_text(self.__locators["搜索"], text)
        time.sleep(2.5)
        current_mobile().hide_keyboard_if_display()

    @TestLogger.log()
    def is_exists_search_box(self):
        """是否存在搜索输入框"""
        return self._is_element_present(self.__class__.__locators['搜索'])

    @TestLogger.log()
    def selecting_he_contacts_by_name(self, name):
        """根据名字选择一个团队联系人"""
        locator = (
            MobileBy.XPATH,
            '//*[@resource-id="com.chinasofti.rcs:id/tv_name_personal_contactlist" and contains(@text,"%s")]' % name)
        max_try = 20
        current = 0
        while current < max_try:
            if self._is_element_present(locator):
                break
            current += 1
            self.swipe_by_percent_on_screen(50, 70, 50, 30, 700)
        self.click_element(locator)


    @TestLogger.log()
    def click_department_name(self, name):
        """点击指定企业/部门名称"""
        locator = (MobileBy.XPATH, '//*[@resource-id="com.chinasofti.rcs:id/tv_title_department" and @text="%s"]' % name)
        max_try = 20
        current = 0
        while current < max_try:
            if self._is_element_present(locator):
                break
            current += 1
            self.swipe_by_percent_on_screen(50, 70, 50, 30, 700)
        self.click_element(locator)

    @TestLogger.log()
    def is_exist_corporate_grade(self):
        """是否存在企业层级"""
        return self._is_element_present(self.__class__.__locators['企业层级'])