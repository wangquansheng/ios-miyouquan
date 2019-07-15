from appium.webdriver.common.mobileby import MobileBy

from library.core.TestLogger import TestLogger
from pages.components import FooterPage
import time


class ContactsPage(FooterPage):
    """通讯录页面"""
    # ACTIVITY = 'com.cmcc.cmrcs.android.ui.activities.HomeActivity'

    __locators = {
        # 通讯录页面
        '通讯录_标题': (MobileBy.XPATH, '//XCUIElementTypeOther[@name="通讯录"]'),
        '通讯录_搜索': (MobileBy.XPATH, '(//XCUIElementTypeSearchField[@name="搜索"])[1]'),
        '通讯录_群聊': (MobileBy.ACCESSIBILITY_ID, 'my message ic n@2x'),
        '通讯录_密友圈_标题': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="密友圈(不限时长)"]'),
        '通讯录_密友圈_管理': (MobileBy.XPATH, '(//XCUIElementTypeButton[@name="管理"])[1]'),
        '通讯录_密友圈_列表': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText'),
        '通讯录_密友圈_列表元素1': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[1]'),
        '通讯录_密友圈_列表元素2': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[2]'),
        '通讯录_密友圈_添加': (MobileBy.IOS_PREDICATE, 'name=="添加"'),
        '通讯录_家庭网_标题': (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="家庭网"])[1]'),
        '通讯录_家庭网_展开': (MobileBy.ACCESSIBILITY_ID, 'my ic unfold n@2x'),
        '通讯录_家庭网_管理': (MobileBy.XPATH, '(//XCUIElementTypeButton[@name="管理"])[2]'),
        '通讯录_列表_打电话': (MobileBy.ACCESSIBILITY_ID, 'my contact call icon'),

        # 列表
        '联系人': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="联系人"]'),
        '联系人_列表': (MobileBy.XPATH, ''),
        '家庭网_列表': (MobileBy.XPATH, ''),
        '搜索_列表': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="联系人"]/following::*'),

        # 联系人
        '联系人_详细_返回': (MobileBy.ACCESSIBILITY_ID, 'contact info back normal@2x'),
        '联系人_详细_头像': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="contact info back normal@2x"]'
                                      '/preceding-sibling::*[1]/XCUIElementTypeImage[2]'),
        '联系人_详细_用户名': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="contact info back normal@2x"]'
                                       '/preceding-sibling::*[1]/XCUIElementTypeStaticText[1]'),
        '联系人_详细_电话按钮': (MobileBy.ACCESSIBILITY_ID, 'my call white n@2x'),
        '联系人_详细_视频按钮': (MobileBy.ACCESSIBILITY_ID, 'my profile ic vedio n@2x'),
        '联系人_详细_设置备注名': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="设置备注名"]'),
        '联系人_详细_备注修改': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="设置备注名"]/following-sibling::*[2]'),
        '联系人_详细_手机号码': (MobileBy.IOS_PREDICATE, 'name=="手机号码"'),
        '联系人_详细_短号': (MobileBy.IOS_PREDICATE, 'name=="短号"'),
        '联系人_详细_电话规则': (MobileBy.IOS_PREDICATE, 'name=="电话规则说明"'),

        # 密友圈
        '密友圈_管理_标题': (MobileBy.XPATH, '//XCUIElementTypeOther[@name="不限时长成员管理"]'),
        '密友圈_管理_返回': (MobileBy.ACCESSIBILITY_ID, 'me back blue normal@2x'),
        '密友圈_管理_感叹号规则': (MobileBy.ACCESSIBILITY_ID, 'my tanhao icon n@2x'),
        '密友圈_管理_提示文案': (MobileBy.XPATH, '//XCUIElementTypeTable/preceding-sibling::*[1]'),
        '密友圈_管理_添加成员': (MobileBy.ACCESSIBILITY_ID, 'my icon addmember n@2x'),
        '密友圈_管理_成员列表': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell'),
        '密友圈_管理_成员1': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]'),
        '密友圈_管理_成员2': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[2]'),

        # 家庭网
        '家庭网_管理_标题': (MobileBy.XPATH, '//XCUIElementTypeOther[@name="家庭网成员管理"]'),
        '家庭网_管理_返回': (MobileBy.ACCESSIBILITY_ID, 'me back blue normal@2x'),
        '家庭网_管理_感叹号规则': (MobileBy.ACCESSIBILITY_ID, 'ic notice@2x'),
        '家庭网_管理_添加': (MobileBy.XPATH, '(//XCUIElementTypeButton[@name="添加成员"])[1]'),
        '家庭网_管理_联系人1': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell'),
        '家庭网_详细_返回': (MobileBy.ACCESSIBILITY_ID, 'contact info back normal@2x'),
        '家庭网_详细_头像': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="contact info back normal@2x"]'
                                      '/preceding-sibling::*[1]/XCUIElementTypeImage[2]'),
        '家庭网_详细_用户名': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="contact info back normal@2x"]'
                                       '/preceding-sibling::*[1]/XCUIElementTypeStaticText[1]'),
        '家庭网_详细_电话按钮': (MobileBy.ACCESSIBILITY_ID, 'my call white n@2x'),
        '家庭网_详细_视频按钮': (MobileBy.ACCESSIBILITY_ID, 'my profile ic vedio n@2x'),
        '家庭网_详细_设置备注名': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="设置备注名"]'),
        '家庭网_详细_备注修改': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="设置备注名"]/following-sibling::*[2]'),
        '家庭网_详细_手机号码': (MobileBy.IOS_PREDICATE, 'name=="手机号码"'),
        '家庭网_详细_短号': (MobileBy.IOS_PREDICATE, 'name=="短号"'),
        '家庭网_详细_短号内容': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="短号"]/following-sibling::*[1]'),
        '家庭网_详细_更多': (MobileBy.IOS_PREDICATE, 'name=="更多"'),
        '家庭网_详细_更多编辑': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="更多"]/following-sibling::*[2]'),
        '家庭网_详细_电话规则': (MobileBy.IOS_PREDICATE, 'name=="电话规则说明"'),

        # 搜索
        '搜索_搜索': (MobileBy.XPATH, '(//XCUIElementTypeSearchField[@name="搜索"])[1]'),
        '搜索_取消': (MobileBy.IOS_PREDICATE, 'name=="取消"'),
        '搜索_清除文本': (MobileBy.IOS_PREDICATE, 'name="清除文本"'),

        # 消息, 右上角
        '通讯_消息': (MobileBy.XPATH, '//XCUIElementTypeOther[@name="消息"]'),
        '通讯_返回': (MobileBy.ACCESSIBILITY_ID, 'me back blue normal@2x'),
        '通讯_+': (MobileBy.ACCESSIBILITY_ID, 'my xiaoxi jiahao@2x'),
        '通讯_搜索': (MobileBy.XPATH, '(//XCUIElementTypeSearchField[@name="搜索"])[1]'),
        '通讯_好友列表': (MobileBy.ACCESSIBILITY_ID, 'my ic haoyouliebiao n@2x'),
        '通讯_群聊': (MobileBy.IOS_PREDICATE, 'name="群聊"'),
        '通讯_公众号': (MobileBy.IOS_PREDICATE, 'name="公众号"'),

        # 底部标签栏
        '通话': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="通话"]'),
        '通讯录': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="通讯录"]'),
        '我': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="我"]'),

        # 通讯录页面
        # '通讯录标题': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="通讯录"]'),
        # '搜索': (MobileBy.XPATH, '(//XCUIElementTypeSearchField[@name="搜索"])[1]'),
        # '群聊': (MobileBy.ACCESSIBILITY_ID, '群聊'),
        # '公众号': (MobileBy.ACCESSIBILITY_ID, '公众号'),
        # '创建团队': (MobileBy.ACCESSIBILITY_ID, '创建团队'),
        # '全部团队': (MobileBy.ACCESSIBILITY_ID, '全部团队'),
        # '默认团队': (MobileBy.ACCESSIBILITY_ID, '默认团队'),
        # '设置': (MobileBy.XPATH, '//XCUIElementTypeOther[@name="默认团队"]/XCUIElementTypeButton'),
        #
        # '团队头像': (MobileBy.ACCESSIBILITY_ID, 'cc_contacts_organization_classA'),
        # '团队名称': (MobileBy.XPATH,''),
        # #搜索结果
        # '输入关键字快速搜索': (MobileBy.XPATH, '(//XCUIElementTypeSearchField[@name="输入关键字快速搜索"])[1]'),
        # '搜索结果列表1': (MobileBy.XPATH,
        #             '//XCUIElementTypeApplication[@name="和飞信"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell'),
        # '搜索结果-团队联系人头像': (MobileBy.XPATH, '(//XCUIElementTypeImage[@name="cc_chat_personal_default"])'),
        # '手机联系人': (MobileBy.ACCESSIBILITY_ID, '手机联系人'),
        # '手机联系人头像':(MobileBy.XPATH,'//XCUIElementTypeApplication[@name="和飞信"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeImage'),
        # '群聊联系人头像': (MobileBy.XPATH,'(//XCUIElementTypeImage[@name="cc_chat_group_default"])[1]'),
        # '和飞信新闻公众号头像': (MobileBy.XPATH,'//XCUIElementTypeImage[@name="/var/mobile/Containers/Data/Application/3FF94A5C-59E9-4E2B-AA59-79FEC854AC76/Library/RCSData/headimage/4cc45369622d4a44066beafd18633c55_(null)"]'),
        # '查看更多1': (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="查看更多"])[1]'),
        # '查看更多2': (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="查看更多"])[2]'),
        #
        # # 手机联系人界面
        # '返回': (MobileBy.ACCESSIBILITY_ID, 'back'),
        # '搜索手机联系人': (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="和飞信"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeTextField'),
        # '+号': (MobileBy.ACCESSIBILITY_ID, 'cc contacts add normal'),
        # '标签分组': (MobileBy.ACCESSIBILITY_ID, '标签分组'),
        # '索引字母容器': (MobileBy.XPATH,
        #            '//XCUIElementTypeApplication[@name="和飞信"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]'),
        # '列表项': (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="和飞信"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeTable/XCUIElementTypeCell'),
        # '联系人头像': (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="和飞信"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeImage'),
        # '本地联系人搜索结果': (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="和飞信"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeTable/XCUIElementTypeCell'),

    }

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

    @TestLogger.log("获得元素对应的数量")
    def get_elements_list(self, locator):
        return self.get_elements(self.__class__.get_locators(self, locator))

    @TestLogger.log()
    def is_on_this_page(self):
        """当前页面是否在通讯录"""
        try:
            self.wait_until(
                timeout=15,
                auto_accept_permission_alert=True,
                condition=lambda d: self._is_element_present(self.__class__.__locators["联系人"])
            )
            return True
        except:
            return False

    @TestLogger.log("家庭网是否展开")
    def if_home_net_expand(self) -> bool:
        """判断家庭网是否展开"""
        locator = (MobileBy.XPATH,
                   '//XCUIElementTypeStaticText[@name="联系人"]/../')
        try:
            # 密友圈占用1行
            return len(self.get_elements(locator)) > 1
        except :
            return False

    @TestLogger.log("点击联系人")
    def click_phone_contact(self):
        """点击联系人"""
        self.click_element(self.__class__.__locators['联系人'])

    @TestLogger.log("点击返回")
    def click_back(self):
        """点击返回"""
        self.click_element(self.__class__.__locators['返回'])

    @TestLogger.log('点击+号')
    def click_add(self):
        """点击+号"""
        self.click_element(self.__class__.__locators['+号'])

    @TestLogger.log('点击消息')
    def click_message_icon(self):
        """点击消息按钮"""
        self.click_element(self.__class__.__locators['消息'])

    @TestLogger.log('点击搜索框')
    def click_search_box(self):
        """点击搜索框"""
        self.click_element(self.__class__.__locators['搜索'])

    @TestLogger.log("输入搜索内容")
    def input_search_text(self, text):
        time.sleep(1)
        self.input_text(self.__locators['输入关键字快速搜索'], text)

    @TestLogger.log("查看控件是否存在")
    def page_contain_element(self,text='联系人头像'):
        time.sleep(1)
        return self.page_should_contain_element(self.__locators[text])

    @TestLogger.log("查看控件是否存在")
    def page_not_contain_element(self,text='联系人头像'):
        time.sleep(1)
        return self.page_should_not_contain_element(self.__locators[text])

    @TestLogger.log('点击搜索框')
    def click_search_phone_contact(self):
        """点击搜索联系人"""
        self.click_element(self.__class__.__locators['搜索联系人'])

    @TestLogger.log('输入搜索联系人搜索内容')
    def input_search_keyword(self, keyword):
        self.input_text(self.__locators['搜索联系人'], keyword)

    @TestLogger.log('打开群聊列表')
    def open_group_chat_list(self):
        self.click_element(self.__class__.__locators['群聊'])

    @TestLogger.log()
    def select_contacts_by_name(self, name):
        """根据名字选择一个联系人"""
        locator = (MobileBy.ACCESSIBILITY_ID, '%s' % name)
        self.click_element(locator, max_try=10)

    @TestLogger.log()
    def wait_for_page_load(self, timeout=20, auto_accept_alerts=True):
        """等待通讯录页面加载"""
        try:
            self.wait_until(
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts,
                condition=lambda d: self._is_element_present(self.__class__.__locators["+号"])
            )
        except:
            raise AssertionError("页面在{}s内，没有加载成功".format(str(timeout)))
        return self

    @TestLogger.log()
    def is_contacts_exist_by_name(self, name):
        """通过联系人名判断联系人是否存在"""
        max_try = 10
        current = 0
        while current < max_try:
            if self.is_text_present(name):
                return True
            current += 1
            self.page_up()
        return False

    @TestLogger.log('获取页面所有联系人')
    def get_page_elements(self, text='搜索结果-联系人头像'):
        return self.get_elements(self.__class__.__locators[text])

    @TestLogger.log('点击搜索出的联系人')
    def click_element_contact(self,text='联系人头像'):
        self.click_element(self.__class__.__locators[text])

    @TestLogger.log('判断列表是否存在XXX联系人')
    def is_contact_in_list(self, name):
        self.scroll_to_top()
        groups = self.mobile.list_iterator(self.__locators['搜索结果列表'], self.__locators['列表项'])
        for group in groups:
            if group.find_elements(MobileBy.XPATH,
                                   '(//XCUIElementTypeStaticText[@name="%s"])[2]'.format(name)):
                return True
        return False

    @TestLogger.log("获取所有联系人名")
    def get_contacts_name(self):
        """获取所有联系人名"""
        max_try = 5
        current = 0
        while current < max_try:
            if self._is_element_present(self.__class__.__locators["联系人名"]):
                break
            current += 1
            self.swipe_by_percent_on_screen(50, 70, 50, 30, 700)
        els = self.get_elements(self.__class__.__locators["联系人名"])
        contacts_name = []
        if els:
            for el in els:
                contacts_name.append(el.text)
        else:
            raise AssertionError("No m004_contacts, please add m004_contacts in address book.")
        if "和通讯录" in contacts_name:
            contacts_name.remove("和通讯录")
        if "和飞信电话" in contacts_name:
            contacts_name.remove("和飞信电话")
        if "本机" in contacts_name:
            contacts_name.remove("本机")
        return contacts_name

    @TestLogger.log()
    def find_element_by_swipe(self, locator, times=15):
        """找不到元素就滑动"""
        if self._is_element_present(self.__class__.__locators[locator]):
            return self.get_element(self.__class__.__locators[locator])
        else:
            c = 0
            while c < times:
                self.swipe_by_percent_on_screen(50, 70, 50, 30, 700)
                if self._is_element_present(self.__class__.__locators[locator]):
                    return self.get_element(self.__class__.__locators[locator])
                c += 1
            return None

    @TestLogger.log("滚动列表到顶部")
    def scroll_to_top(self):
        self.wait_until(
            condition=lambda d: self.get_element(self.__locators['通讯录列表'])
        )
        if self._is_element_present(self.__locators['群聊']):
            return True
        current = 0
        while True:
            current += 1
            if current > 20:
                return
            self.swipe_by_direction(self.__locators['通讯录列表'], 'up')
            if self._is_element_present(self.__locators['群聊']):
                break
        return True

    def page_up(self):
        """向上滑动一页"""
        self.driver.execute_script('mobile: swipe', {'direction': 'up'})

    @TestLogger.log("上一页")
    def page_down(self):
        """向下滑动"""
        self.driver.execute_script('mobile: swipe', {'direction': 'down'})

    @TestLogger.log()
    def get_all_contacts_name(self):
        """获取所有联系人名"""
        els = self.get_elements(self.__class__.__locators["联系人名"])
        contacts_name = []
        if els:
            for el in els:
                contacts_name.append(el.text)
        else:
            raise AssertionError("No m004_contacts, please add m004_contacts in address book.")
        flag = True
        current = 0
        while flag:
            current += 1
            if current > 20:
                return
            self.page_up()
            els = self.get_elements(self.__class__.__locators["联系人名"])
            for el in els:
                if el.text not in contacts_name:
                    contacts_name.append(el.text)
                    flag = True
                else:
                    flag = False
        return contacts_name

    @TestLogger.log()
    def click_label_grouping(self):
        """点击标签分组"""
        self.click_element(self.__class__.__locators['标签分组'])

    @TestLogger.log()
    def click_and_address(self):
        """点击和通讯录"""
        self.click_element(self.__class__.__locators['和通讯录'])

    @TestLogger.log()
    def click_and_address(self):
        """点击和通讯录"""
        self.click_element(self.__class__.__locators['和通讯录'])

    @TestLogger.log()
    def click_always_allowed(self):
        """获取通讯录权限点击始终允许"""
        if self.get_elements(self.__class__.__locators['弹出框点击允许']):
            self.click_element(self.__class__.__locators['弹出框点击允许'])

    @TestLogger.log()
    def click_allow(self):
        """点击始终允许"""
        self.click_element(self.__class__.__locators['始终允许'])

    @TestLogger.log("处理SIM联系人弹框")
    def click_sim_contact(self):
        """点击和通讯录联系人更多"""
        time.sleep(2)
        if self.get_elements(self.__class__.__locators['不显示']):
            self.click_element(self.__class__.__locators['不显示'])

    @TestLogger.log()
    def click_return(self):
        """点击返回"""
        self.click_element(self.__class__.__locators['群聊列表返回'])

    @TestLogger.log()
    def wait_for_contacts_page_load(self, timeout=20, auto_accept_alerts=True):
        """等待通讯录页面加载"""
        try:
            self.wait_until(
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts,
                condition=lambda d: self._is_element_present(self.__class__.__locators["+号"])
            )
        except:
            raise AssertionError("页面在{}s内，没有加载成功".format(str(timeout)))
        return self

