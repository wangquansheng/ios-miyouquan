import traceback

from appium.webdriver.common.mobileby import MobileBy

from library.core.TestLogger import TestLogger
from library.core.utils.applicationcache import current_mobile
from pages.components import FooterPage
import time


class ContactsPage(FooterPage):
    """通讯录页面"""
    # ACTIVITY = 'com.cmcc.cmrcs.android.ui.activities.HomeActivity'

    __locators = {
        # 通讯录页面
        '通讯录_标题': (MobileBy.XPATH, '//XCUIElementTypeOther[@name="通讯录"]'),
        '通讯录_搜索': (MobileBy.XPATH, '(//XCUIElementTypeSearchField[@name="搜索"])[1]'),
        '通讯录_群聊': (MobileBy.IOS_PREDICATE, 'name contains "my message ic n"'),
        '通讯录_密友圈_标题': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="密友圈(不限时长)"]'),
        '通讯录_密友圈_管理': (MobileBy.XPATH, '(//XCUIElementTypeButton[@name="管理"])[1]'),
        '通讯录_家庭网_标题': (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="家庭网"])[1]'),
        '通讯录_家庭网_展开': (MobileBy.IOS_PREDICATE, 'name contains "my ic unfold n"'),
        '通讯录_家庭网_管理': (MobileBy.XPATH, '(//XCUIElementTypeButton[@name="管理"])[2]'),
        '通讯录_列表_打电话': (MobileBy.ACCESSIBILITY_ID, 'my contact call icon'),
        '通讯录_不限时长添加': (MobileBy.IOS_PREDICATE, 'name=="添加"'),
        '通讯录_不限时长列表': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText'),
        '通讯录_不限时长列表1': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[1]'),
        '通讯录_不限时长列表2': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[2]'),

        # 不限时长/管理界面
        '密友圈_不限时长管理_标题': (MobileBy.XPATH, '//XCUIElementTypeOther[@name="不限时长成员管理"]'),
        '密友圈_不限时长管理_返回': (MobileBy.IOS_PREDICATE, 'name contains "me back blue normal"'),
        '密友圈_不限时长管理_规则': (MobileBy.IOS_PREDICATE, 'name contains "my tanhao icon n"'),
        '密友圈_不限时长管理_列表': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell'),
        '密友圈_不限时长管理_列表1': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]'),
        '密友圈_不限时长管理_解绑': (MobileBy.IOS_PREDICATE, 'name=="解绑"'),
        '密友圈_不限时长管理_解绑取消': (MobileBy.IOS_PREDICATE, 'name=="取消"'),
        '密友圈_不限时长管理_解绑人数': (MobileBy.IOS_PREDICATE, 'name=="解绑人数已达本月上限"'),
        '密友圈_不限时长管理_解绑成功': (MobileBy.IOS_PREDICATE, 'name=="解绑成功"'),

        # 家庭网 呼叫
        '呼叫': (MobileBy.IOS_PREDICATE, 'name=="呼叫"'),
        '取消': (MobileBy.IOS_PREDICATE, 'name=="取消"'),
        '呼叫_结束通话': (MobileBy.IOS_PREDICATE, 'name=="结束通话"'),
        '呼叫_静音': (MobileBy.IOS_PREDICATE, 'name=="静音"'),
        '呼叫_免提': (MobileBy.IOS_PREDICATE, 'name=="免提"'),
        '呼叫_添加通话': (MobileBy.IOS_PREDICATE, 'name=="添加通话"'),
        '呼叫_通讯录': (MobileBy.IOS_PREDICATE, 'name=="通讯录"'),
        '呼叫_提示文本': (MobileBy.IOS_PREDICATE, 'value contains "正在呼叫"'),
        '呼叫_电话号码': (MobileBy.IOS_PREDICATE, 'name=="PHMarqueeView"'),
        '呼叫_用户正忙': (MobileBy.IOS_PREDICATE, 'name=="PHSingleCallParticipantLabelView_StatusLabel"'),

        # 列表
        '家庭网_列表1': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="联系人"]/preceding::XCUIElementTypeCell[1]'),
        '家庭网_列表2': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="联系人"]/preceding::XCUIElementTypeCell[2]'),
        '家庭网_列表电话1': (MobileBy.XPATH,
                      '//XCUIElementTypeStaticText[@name="联系人"]/preceding::XCUIElementTypeCell[1]/*[@name="my contact call icon"]'),
        '家庭网_列表电话2': (MobileBy.XPATH,
                      '//XCUIElementTypeStaticText[@name="联系人"]/preceding::XCUIElementTypeCell[2]/*[@name="my contact call icon"]'),
        '家庭网_列表文本1': (MobileBy.XPATH,
                      '//XCUIElementTypeStaticText[@name="联系人"]/preceding::XCUIElementTypeCell[1]/XCUIElementTypeStaticText[1]'),
        '家庭网_列表文本2': (MobileBy.XPATH,
                      '//XCUIElementTypeStaticText[@name="联系人"]/preceding::XCUIElementTypeCell[2]/XCUIElementTypeStaticText[1]'),
        '联系人': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="联系人"]'),
        '联系人_列表1': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="联系人"]/following::XCUIElementTypeCell[1]'),
        '联系人_列表2': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="联系人"]/following::XCUIElementTypeCell[2]'),
        '联系人_列表电话1': (MobileBy.XPATH,
                      '//XCUIElementTypeStaticText[@name="联系人"]/following::XCUIElementTypeCell[1]/*[@name="my contact call icon"]'),
        '联系人_列表电话2': (MobileBy.XPATH,
                      '//XCUIElementTypeStaticText[@name="联系人"]/following::XCUIElementTypeCell[2]/*[@name="my contact call icon"]'),
        '联系人_列表文本1': (MobileBy.XPATH,
                      '//XCUIElementTypeStaticText[@name="联系人"]/following::XCUIElementTypeCell[1]/XCUIElementTypeStaticText[1]'),
        '联系人_列表文本2': (MobileBy.XPATH,
                      '//XCUIElementTypeStaticText[@name="联系人"]/following::XCUIElementTypeCell[2]/XCUIElementTypeStaticText[1]'),

        # 联系人
        '联系人_详细_返回': (MobileBy.IOS_PREDICATE, 'name contains "contact info back normal"'),
        '联系人_详细_头像': (MobileBy.XPATH, '//XCUIElementTypeButton[contains(@name, "contact info back normal")]'
                                      '/preceding-sibling::*[1]/XCUIElementTypeImage[2]'),
        '联系人_详细_用户名': (MobileBy.XPATH, '//XCUIElementTypeButton[contains(@name, "contact info back normal")]'
                                       '/preceding-sibling::*[1]/XCUIElementTypeStaticText[1]'),
        '联系人_详细_电话按钮': (MobileBy.IOS_PREDICATE, 'name contains "my call white n"'),
        '联系人_详细_视频按钮': (MobileBy.IOS_PREDICATE, 'name contains "my profile ic vedio n"'),
        '联系人_详细_设置备注名': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="设置备注名"]'),
        '联系人_详细_备注修改': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="设置备注名"]/following-sibling::*[2]'),
        '联系人_详细_手机号码': (MobileBy.IOS_PREDICATE, 'name=="手机号码"'),
        '联系人_详细_短号': (MobileBy.IOS_PREDICATE, 'name=="短号"'),
        '联系人_详细_电话规则': (MobileBy.IOS_PREDICATE, 'name=="电话规则说明"'),

        '联系人_详情_头像': (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="密友圈"]/XCUIElementTypeWindow[1]/XCUIElement'
                                      'TypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElement'
                                      'TypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage[3]'),
        '联系人_详情_用户名': (
            MobileBy.XPATH, '//XCUIElementTypeApplication[@name="密友圈"]/XCUIElementTypeWindow[1]/XCUIElement'
                            'TypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElement'
                            'TypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText[1]'),

        # 密友圈
        '密友圈_管理_标题': (MobileBy.XPATH, '//XCUIElementTypeOther[@name="不限时长成员管理"]'),
        '密友圈_管理_返回': (MobileBy.IOS_PREDICATE, 'name contains "me back blue normal"'),
        '密友圈_管理_感叹号规则': (MobileBy.IOS_PREDICATE, 'name contains "my tanhao icon n"'),
        '密友圈_管理_提示文案': (MobileBy.XPATH, '//XCUIElementTypeTable/preceding-sibling::*[1]'),
        '密友圈_管理_添加成员': (MobileBy.IOS_PREDICATE, 'name contains "my icon addmember n"'),
        '密友圈_管理_成员列表': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell'),
        '密友圈_管理_成员1': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]'),
        '密友圈_管理_成员2': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[2]'),

        # 家庭网
        '家庭网_管理_标题': (MobileBy.XPATH, '//XCUIElementTypeOther[@name="家庭网成员管理"]'),
        '家庭网_管理_返回': (MobileBy.IOS_PREDICATE, 'name contains "me back blue normal"'),
        '家庭网_管理_感叹号规则': (MobileBy.IOS_PREDICATE, 'name contains "ic notice"'),
        '家庭网_管理_感叹号规则返回': (MobileBy.IOS_PREDICATE, 'name contains "me back blue pressed"'),
        '家庭网_管理_添加': (MobileBy.XPATH, '(//XCUIElementTypeButton[@name="添加成员"])[1]'),
        '家庭网_管理_联系人1': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell'),

        '家庭网_添加_返回': (MobileBy.IOS_PREDICATE, 'name contains "me back blue normal"'),
        '家庭网_添加_确定': (MobileBy.IOS_PREDICATE, 'name=="确定"'),
        '家庭网_添加_文本': (MobileBy.XPATH, '//XCUIElementTypeOther/XCUIElementTypeTextField'),
        '家庭网_添加_通讯录': (MobileBy.ACCESSIBILITY_ID, 'ic tx normal'),
        '家庭网_添加_通讯录_取消': (MobileBy.IOS_PREDICATE, 'name=="取消"'),
        '家庭网_添加_通讯录_搜索框': (MobileBy.XPATH, '(//XCUIElementTypeSearchField[@name="搜索或输入手机号码"])[1]'),
        '家庭网_添加_通讯录_搜索列表': (MobileBy.XPATH,
                            '//XCUIElementTypeOther[@name="搜索结果"]/XCUIElementTypeCell/XCUIElementTypeStaticText[2]'),
        '家庭网_添加_通讯录_搜索列表1': (MobileBy.XPATH,
                             '//XCUIElementTypeOther[@name="搜索结果"]/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[1]'),

        '家庭网_详细_返回': (MobileBy.IOS_PREDICATE, 'name contains "contact info back normal"'),
        '家庭网_详细_头像': (MobileBy.XPATH, '//XCUIElementTypeButton[contains(@name, "contact info back normal")]'
                                      '/preceding-sibling::*[1]/XCUIElementTypeImage[2]'),
        '家庭网_详细_用户名': (MobileBy.XPATH, '//XCUIElementTypeButton[contains(@name, "contact info back normal")]'
                                       '/preceding-sibling::*[1]/XCUIElementTypeStaticText[1]'),
        '家庭网_详细_电话按钮': (MobileBy.IOS_PREDICATE, 'name contains "my call white n"'),
        '家庭网_详细_视频按钮': (MobileBy.IOS_PREDICATE, 'name contains "my profile ic vedio n"'),
        '家庭网_详细_设置备注名': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[1]'),
        '家庭网_详细_备注名文本': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[2]'),
        '家庭网_详细_备注修改': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeButton[1]'),
        '家庭网_详细_手机号码': (MobileBy.IOS_PREDICATE, 'name=="手机号码"'),
        '家庭网_详细_短号': (MobileBy.IOS_PREDICATE, 'name=="短号"'),
        '家庭网_详细_短号内容': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="短号"]/following-sibling::*[1]'),
        '家庭网_详细_更多': (MobileBy.IOS_PREDICATE, 'name=="更多"'),
        '家庭网_详细_更多编辑': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="更多"]/following-sibling::*[2]'),
        '家庭网_详细_电话规则': (MobileBy.IOS_PREDICATE, 'name=="电话规则说明"'),

        # 家庭网/详细/更多
        '家庭网_详细_更多性别': (MobileBy.IOS_PREDICATE, 'name=="性别"'),
        '家庭网_详细_更多年龄': (MobileBy.IOS_PREDICATE, 'name=="年龄"'),
        '家庭网_详细_更多职业': (MobileBy.IOS_PREDICATE, 'name=="职业"'),
        '家庭网_详细_更多个性标签': (MobileBy.IOS_PREDICATE, 'name=="个性标签"'),

        # 家庭网 备注修改
        '家庭网_备注修改_标题': (MobileBy.XPATH, '//XCUIElementTypeOther[@name="修改备注名称"]'),
        '家庭网_备注修改_返回': (MobileBy.IOS_PREDICATE, 'name contains "me back blue normal"'),
        '家庭网_备注修改_完成': (MobileBy.IOS_PREDICATE, 'name=="完成"'),
        '家庭网_备注修改_文本框': (MobileBy.XPATH, '//XCUIElementTypeOther/XCUIElementTypeTextField'),
        '家庭网_备注修改_清除': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="清除文本"]'),

        # 搜索
        '搜索_文本': (MobileBy.IOS_PREDICATE, 'type=="XCUIElementTypeSearchField"'),
        '搜索_取消': (MobileBy.IOS_PREDICATE, 'name=="取消"'),
        '搜索_无该联系人': (MobileBy.IOS_PREDICATE, 'name=="无该联系人"'),
        '搜索_联系人_无结果': (MobileBy.IOS_PREDICATE, 'name=="无结果"'),
        '搜索_清除文本': (MobileBy.IOS_PREDICATE, 'name=="清除文本"'),
        # '搜索_列表': (MobileBy.XPATH, '//XCUIElementTypeOther[@name="搜索结果"]/XCUIElementTypeCell'),
        '搜索_列表1': (MobileBy.XPATH, '//XCUIElementTypeOther[@name="搜索结果"]/XCUIElementTypeCell[1]'),
        '搜索_详细_用户名': (MobileBy.XPATH, '//XCUIElementTypeButton[contains(@name, "my call white n")]'
                                      '/preceding-sibling::*[1]/XCUIElementTypeStaticText[1]'),
        # 视频主叫
        '视频主叫_头像': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="网络视频通话呼叫中..."]/preceding-sibling::*[3]'),
        '视频主叫_名称': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="网络视频通话呼叫中..."]/preceding-sibling::*[2]'),
        '视频主叫_电话': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="网络视频通话呼叫中..."]/preceding-sibling::*[1]'),
        '视频主叫_网络视频通话呼叫中': (MobileBy.IOS_PREDICATE, 'name=="网络视频通话呼叫中..."'),
        '视频主叫_挂断': (MobileBy.IOS_PREDICATE, 'name=="挂断"'),

        # 飞信电话
        '飞信电话_我知道了': (MobileBy.IOS_PREDICATE, 'name=="我知道了"'),
        '飞信电话_提示文本': (MobileBy.IOS_PREDICATE, 'name=="请注意接听“飞信电话”来电后将自动呼叫对方"'),
        '飞信电话_挂断': (MobileBy.IOS_PREDICATE, 'name=="call dial key reject"'),
        '飞信电话_缩小': (MobileBy.IOS_PREDICATE, 'name=="my video zoom"'),
        '飞信电话_备注': (MobileBy.XPATH, '//XCUIElementTypeImage/following::XCUIElementTypeStaticText[1]'),
        '飞信电话_号码': (MobileBy.XPATH, '//XCUIElementTypeImage/following::XCUIElementTypeStaticText[2]'),
        '飞信电话_接受': (MobileBy.IOS_PREDICATE, 'name=="接受"'),
        '飞信电话_拒绝': (MobileBy.IOS_PREDICATE, 'name=="拒绝"'),

        # 消息, 右上角
        '通讯_消息': (MobileBy.XPATH, '//XCUIElementTypeOther[@name="消息"]'),
        '通讯_返回': (MobileBy.IOS_PREDICATE, 'name contains "me back blue normal"'),
        '通讯_+': (MobileBy.IOS_PREDICATE, 'name contains "my xiaoxi jiahao"'),
        '通讯_搜索': (MobileBy.XPATH, '(//XCUIElementTypeSearchField[@name="搜索"])[1]'),
        '通讯录_搜索框结果第一条': (MobileBy.XPATH, '//XCUIElementTypeOther[@name="搜索结果"]/XCUIElementTypeCell[1]'),
        '通讯_好友列表': (MobileBy.IOS_PREDICATE, 'name contains "my ic haoyouliebiao n"'),
        '通讯_群聊': (MobileBy.IOS_PREDICATE, 'name=="群聊"'),
        '通讯_公众号': (MobileBy.IOS_PREDICATE, 'name=="公众号"'),

        # 电话
        '结束通话': (MobileBy.IOS_PREDICATE, 'name contains "结束通话"'),
        # 无密友圈 确定
        '无密友圈_确定': (MobileBy.IOS_PREDICATE, "name=='确定'"),
        '无密友圈_取消': (MobileBy.IOS_PREDICATE, "name=='取消'"),

        # 短信关闭
        '短信_关闭': (MobileBy.IOS_PREDICATE, 'name=="关闭"'),

        # 底部标签栏
        '通话': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="通话"]'),
        '通讯录': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="通讯录"]'),
        '我': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="我"]'),

    }

    @TestLogger.log("视频通话结束弹出框")
    def click_viedo_close_phone(self):
        """
        视频通话结束弹出框
        :return:
        """
        if self.is_element_already_exist('结束通话'):
            self.click_locator_key('结束通话')

    @TestLogger.log("关闭飞信电话")
    def click_fetion_close_phone(self):
        try:
            if self.is_element_already_exist('飞信电话_拒绝'):
                self.click_locator_key('飞信电话_拒绝')
                time.sleep(0.5)
        except:
            pass
        try:
            if self.is_element_already_exist('飞信电话_挂断'):
                self.click_locator_key('飞信电话_挂断')
                time.sleep(0.5)
        except:
            pass
        if self.is_element_already_exist('无密友圈_取消'):
            self.click_locator_key('无密友圈_取消')
            time.sleep(0.5)

    @TestLogger.log("通话页面点击删除按钮，删除所有")
    def click_delete_manager_meet(self):
        time.sleep(1)
        if self.is_element_already_exist("密友圈_不限时长管理_列表1"):
            time.sleep(1)
            # 长滑动，自动出现弹框提示
            self.swipe_by_direction(self.__locators["密友圈_不限时长管理_列表1"], "left")
            time.sleep(3)

    @TestLogger.log("获得元素对应的数量")
    def get_elements_list_c(self, locator):
        return self.get_elements(self.__locators[locator])

    @TestLogger.log('获取元素的属性')
    def get_element_attr(self, locator, attr, wait_time=0):
        """获取元素的属性"""
        return self.mobile.get_element_attribute(self.__locators[locator], attr, wait_time)

    @TestLogger.log("获得元素对应的数量")
    def get_elements_count(self, locator):
        return len(self.get_elements(self.__locators[locator]))

    @TestLogger.log('获取元素')
    def get_one_element(self, locator):
        return self.get_elements(self.__locators[locator])

    @TestLogger.log('判断元素是否存在')
    def is_element_already_exist(self, locator):
        """判断元素是否存在"""
        try:
            elements = self.get_elements(self.__locators[locator])
            if len(elements) > 0:
                return True
            else:
                return False
        except Exception:
            traceback.print_exc()
            return False

    @TestLogger.log('获取元素')
    def get_one_element_c(self, locator):
        return self.mobile.get_element(self.__locators[locator])

    @TestLogger.log("点击locators对应的元素")
    def click_locator_key(self, locator):
        self.click_element(self.__locators[locator])

    @TestLogger.log()
    def is_element_exist(self, text):
        """当前页面是否包含此元素"""
        return self._is_element_present(self.__locators[text])

    @TestLogger.log("获得元素的文本")
    def get_element_text(self, locator):
        return self.get_text(self.__locators[locator])

    @TestLogger.log("获得元素对应的数量")
    def get_elements_list_click(self, locator):
        elements = self.get_elements(self.__locators[locator])
        if len(elements) > 0:
            elements[0].click()
            time.sleep(2)
            return True
        else:
            return False

    @TestLogger.log("点击包含文本的元素")
    def input_locator_text(self, locator, text):
        """输入文本"""
        return self.input_text(self.__locators[locator], text)

    @TestLogger.log("清空文本")
    def click_input_clear(self):
        if self.is_element_already_exist('家庭网_备注修改_清除'):
            self.click_locator_key('家庭网_备注修改_清除')
            time.sleep(1)

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
        try:
            locator = self.__class__.__locators["家庭网_列表电话1"]
            return len(self.get_elements(locator)) > 0
        except:
            return False

    @TestLogger.log("点击联系人")
    def click_phone_contact(self):
        """点击联系人"""
        self.click_element(self.__class__.__locators['联系人'])

    @TestLogger.log("点击返回")
    def click_back(self):
        """点击返回"""
        self.click_element(self.__class__.__locators['返回'])

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
    def page_contain_element(self, text='联系人头像'):
        time.sleep(1)
        return self.page_should_contain_element(self.__locators[text])

    @TestLogger.log('点击搜索框')
    def click_search_phone_contact(self):
        """点击搜索联系人"""
        self.click_element(self.__class__.__locators['搜索联系人'])

    @TestLogger.log('输入搜索联系人搜索内容')
    def input_search_keyword(self, keyword):
        self.input_text(self.__locators['搜索联系人'], keyword)

    @TestLogger.log()
    def wait_for_page_load(self, timeout=20):
        """等待通讯录页面加载"""
        try:
            self.wait_until(
                timeout=timeout,
                condition=lambda d: self.is_text_present('家庭网')
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
    def click_element_contact(self, text='联系人头像'):
        self.click_element(self.__class__.__locators[text])

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
    def click_always_allowed(self):
        """获取通讯录权限点击始终允许"""
        if self.get_elements(self.__class__.__locators['弹出框点击允许']):
            self.click_element(self.__class__.__locators['弹出框点击允许'])

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

    @TestLogger.log('获取指定运营商类型的手机卡（不传类型返回全部配置的手机卡）')
    def get_cards(self, card_type):
        """返回指定类型卡手机号列表"""
        return current_mobile().get_cards(card_type)[0]

    @TestLogger.log('根据cards点击元素')
    def click_by_cards(self, cards):
        self.input_text(self.__locators['通讯_搜索'], cards)
        time.sleep(1)
        self.get_element(self.__locators['通讯录_搜索框结果第一条']).click()
