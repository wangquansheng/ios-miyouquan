from appium.webdriver.common.mobileby import MobileBy

from library.core.BasePage import BasePage
from library.core.TestLogger import TestLogger
import time
import os


class ContactDetailsPage(BasePage):
    """个人详情"""
    # ACTIVITY = 'com.cmicc.module_contact.activitys.ContactDetailActivity'

    __locators = {

        '返回上一页': (MobileBy.ACCESSIBILITY_ID, 'back'),
        '星标': (MobileBy.ACCESSIBILITY_ID, 'cc contacts profile ic star un'),
        '编辑': (MobileBy.ACCESSIBILITY_ID, '编辑'),
        '好久不见~打个招呼吧': (MobileBy.ACCESSIBILITY_ID, '好久不见~打个招呼吧'),

        '联系人头像': (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="和飞信"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeImage'),
        '大图': (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="和飞信"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeImage'),

        '消息': (MobileBy.ACCESSIBILITY_ID, 'cc profile massage normal'),
        '电话': (MobileBy.ACCESSIBILITY_ID, 'cc profile call normal'),
        '语音通话': (MobileBy.ACCESSIBILITY_ID, 'cc profile voicecall normal'),
        '视频通话': (MobileBy.ACCESSIBILITY_ID, 'cc profile video normal'),
        '和飞信电话': (MobileBy.ACCESSIBILITY_ID, '飞信电话'),

        '详细信息列表容器': (MobileBy.ID, 'com.chinasofti.rcs:id/sv_info'),
        '公司': (MobileBy.XPATH, '(//XCUIElementTypeTextView[@name="vvv"])[1]'),
        '公司名': (MobileBy.ID, 'com.chinasofti.rcs:id/value'),
        '职位': (MobileBy.ID, 'com.chinasofti.rcs:id/property'),
        '职位名': (MobileBy.ID, 'com.chinasofti.rcs:id/value'),
        '邮箱': (MobileBy.ID, 'com.chinasofti.rcs:id/property'),
        '邮箱地址': (MobileBy.ID, 'com.chinasofti.rcs:id/value'),

        '分享名片': (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="分享名片"])[1]'),
        '邀请使用': (MobileBy.XPATH, '(//XCUIElementTypeButton[@name="邀请使用"])[1]'),

        "确定": (MobileBy.ACCESSIBILITY_ID, '确定'),
        "删除联系人": (MobileBy.ACCESSIBILITY_ID, "删除联系人"),
        "确定删除": (MobileBy.ACCESSIBILITY_ID, '删除'),
        "取消删除": (MobileBy.ACCESSIBILITY_ID, '取消'),

        #打电话
        "取消": (MobileBy.ACCESSIBILITY_ID, '取消'),
        "呼叫": (MobileBy.ACCESSIBILITY_ID, '呼叫'),



        "呼叫(1/8)": (MobileBy.ID, "com.chinasofti.rcs:id/tv_sure"),
        "暂不开启": (MobileBy.ID, "android:id/button2"),
        "挂断电话": (MobileBy.ID, "com.chinasofti.rcs:id/ivDecline"),
        "结束通话": (MobileBy.ID, "com.chinasofti.rcs:id/smart_call_out_term"),
        "视频通话呼叫中": (MobileBy.XPATH, "//*[@text='	视频通话呼叫中']"),
        "挂断视频通话": (MobileBy.ID, "com.chinasofti.rcs:id/iv_out_Cancel"),
        "取消拨打": (MobileBy.XPATH, "//*[@text='取消拨打']"),
        "联系人名称": (MobileBy.ID, "com.chinasofti.rcs:id/contact_name"),
        "用户名称": (MobileBy.ID, "com.chinasofti.rcs:id/tv_profile_name"),
        "用户头像": (MobileBy.ID, "com.chinasofti.rcs:id/recyclesafeimageview_profile_photo"),
        "用户号码": (MobileBy.ID, "com.chinasofti.rcs:id/tv_phone"),
        '添加桌面快捷方式': (MobileBy.XPATH, '//*[@text="添加桌面快捷方式"]'),
        '我知道了': (MobileBy.XPATH, '//*[@text="我知道了"]'),
        '快捷方式-确定添加': (MobileBy.ID, "android:id/button1"),
        '快捷方式-取消添加': (MobileBy.ID, "android:id/button2"),
        "和飞信电话-挂断电话": (MobileBy.ID, "com.android.incallui:id/declinebutton"),

    }


    @TestLogger.log('点击返回')
    def click_back(self):
        self.click_element(self.__locators['返回'])


    @TestLogger.log("是否在当前页面")
    def is_on_this_page(self):
        time.sleep(2)
        return self.is_text_present('分享名片')

    @TestLogger.log()
    def page_should_contain_element_first_letter(self):
        """页面应该包含首字母"""
        return self.page_should_contain_element(self.__class__.__locators['联系人头像'])

    @TestLogger.log()
    def page_contain_contacts_avatar(self):
        """页面应该包含联系人头像"""
        return self.page_should_contain_element(self.__class__.__locators['联系人头像'])

    @TestLogger.log()
    def get_people_name(self,name):
        locator = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="%s"]' % name)
        time.sleep(2)
        el = self.get_element(locator)
        return el.text

    @TestLogger.log()
    def get_people_number(self,number):
        locator = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="%s"]' % number)
        time.sleep(2)
        return self.get_element(locator).text

    @TestLogger.log()
    def wait_for_page_load(self, timeout=20, auto_accept_alerts=True):
        """等待个人详情页面加载"""
        try:
            self.wait_until(
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts,
                condition=lambda d: self._is_element_present(self.__class__.__locators["编辑"])
            )
        except:
            raise AssertionError("页面在{}s内，没有加载成功".format(str(timeout)))
        return self

    @TestLogger.log("点击头像查看大图")
    def click_avatar(self):
        """点击头像查看大图"""
        self.click_element(self.__locators['联系人头像'])

    @TestLogger.log("点击大图")
    def click_big_avatar(self):
        """点击大图"""
        self.click_element(self.__locators['大图'])

    @TestLogger.log()
    def is_exists_big_avatar(self):
        """是否存在大图"""
        return self._is_element_present(self.__class__.__locators["大图"])

    @TestLogger.log("删除联系人")
    def change_delete_number(self):
        time.sleep(1)
        self.click_element(self.__locators['删除联系人'])

    @TestLogger.log("确定删除")
    def click_sure_delete(self):
        """确定删除"""
        time.sleep(3)
        self.click_element(self.__class__.__locators['确定删除'])

    @TestLogger.log("点击分享名片")
    def click_share_business_card(self):
        """点击分享名片"""
        self.click_element(self.__locators['分享名片'])

    @TestLogger.log("点击星标")
    def click_star_icon(self):
        self.click_element(self.__class__.__locators['星标'])


    @TestLogger.log("添加桌面快捷方式")
    def click_add_desktop_shortcut(self):
        time.sleep(1)
        self.click_element(self.__locators["添加桌面快捷方式"])

    @TestLogger.log("点击我知道了")
    def click_I_know(self):
        time.sleep(1)
        self.click_element(self.__locators["我知道了"])

    @TestLogger.log("点击确定添加快捷方式")
    def click_sure_add_desktop_shortcut(self):
        time.sleep(1)
        self.click_element(self.__locators["快捷方式-确定添加"])

    @TestLogger.log("更改手机号码")
    def change_mobile_number(self,text='13800138789'):
        self.input_text(self.__locators["电话号码"],text)

    @TestLogger.log("点击呼叫")
    def send_call_number(self):
        time.sleep(1)
        self.click_element(self.__locators["呼叫(1/8)"])
        time.sleep(1)

    @TestLogger.log("设置授权窗口")
    def cancel_permission(self):
        time.sleep(1)
        self.click_element(self.__locators["暂不开启"])

    @TestLogger.log("挂断通话")
    def cancel_call(self):
        time.sleep(7)
        self.click_element(self.__locators["挂断电话"])

    @TestLogger.log("挂断和飞信电话")
    def cancel_hefeixin_call(self):
        time.sleep(7)
        self.click_element(self.__locators["和飞信电话-挂断电话"])

    @TestLogger.log("结束通话")
    def click_end_call(self):
        time.sleep(2)
        self.click_element(self.__locators["结束通话"])



    @TestLogger.log()
    def open_contacts_page(self):
        """切换到标签页：通讯录"""
        self.click_element(self.__locators['通讯录'])

    @TestLogger.log("删除所有的联系人")
    def delete_all_contact(self):
        """使用此方法前，app进入消息界面"""
        self.open_contacts_page()
        flag = True
        while flag:
            time.sleep(2)
            elements = self.get_elements(self.__locators['联系人列表'])
            if elements:
                elements[0].click()
                self.click_edit_contact()
                time.sleep(1)
                self.hide_keyboard()
                time.sleep(1)
                self.page_up()
                self.change_delete_number()
                time.sleep(1)
                self.click_sure_delete()
            else:
                self.take_screen_out()
                print("无可删除联系人")
                flag = False

    @TestLogger.log("通过Name删除指定联系人")
    def delete_contact(self, text):
        """使用此方法前，app进入消息界面"""
        self.open_contacts_page()
        for i in range(10):
            time.sleep(2)
            if self.is_text_present(text):
                self.click_text(text)
                self.click_edit_contact()
                time.sleep(1)
                self.hide_keyboard()
                self.page_up()
                self.change_delete_number()
                self.click_sure_delete()
                break
            else:
                self.page_up()
                if i == 9:
                    print("未找到联系人")

    @TestLogger.log("点击返回按钮")
    def click_back_icon(self):
        """点击返回"""
        self.click_element(self.__locators['返回上一页'])

    @TestLogger.log("点击确定")
    def click_sure_icon(self):
        """点击确定"""
        self.click_element(self.__class__.__locators['确定'])



    @TestLogger.log("点击编辑")
    def click_edit_contact(self):
        """点击编辑按钮"""
        self.click_element(self.__class__.__locators['编辑'])

    @TestLogger.log("获取名片名称")
    def get_contact_name(self, wait_time=0):
        title = self.wait_until(
            condition=lambda d: self.get_element(self.__class__.__locators['名片标题']),
            timeout=wait_time
        )
        return title.text

    @TestLogger.log('获取名片号码')
    def get_contact_number(self, wait_time=0):
        number = self.wait_until(
            condition=lambda d: self.get_element(self.__locators['名片号码']),
            timeout=wait_time
        )
        return number.text

    @TestLogger.log("点击消息图标")
    def click_message_icon(self):
        self.click_element(self.__locators['消息'])

    @TestLogger.log('点击电话图标')
    def click_call_icon(self):
        self.click_element(self.__locators['电话'])

    @TestLogger.log('点击呼叫')
    def click_calling(self):
        self.click_element(self.__locators['呼叫'])


    @TestLogger.log("点击语音通话图标")
    def click_voice_call_icon(self):
        self.click_element(self.__locators['语音通话'])

    @TestLogger.log("点击视频通话图标")
    def click_video_call_icon(self):
        self.click_element(self.__locators['视频通话'])

    @TestLogger.log("点击和飞信电话菜单")
    def click_hefeixin_call_menu(self):
        self.click_element(self.__locators['和飞信电话'])


    @TestLogger.log("邀请使用")
    def click_invitation_use(self):
        """邀请使用"""
        self.click_element(self.__locators['邀请使用'])

    @TestLogger.log()
    def message_btn_is_clickable(self):
        """消息按钮是否可点击"""
        return self._is_enabled(self.__class__.__locators["消息"])

    @TestLogger.log()
    def call_btn_is_clickable(self):
        """电话按钮是否可点击"""
        return self._is_clickable(self.__class__.__locators["电话"])

    @TestLogger.log()
    def voice_btn_is_clickable(self):
        """语音通话按钮状态是否可点击"""
        return self._is_clickable(self.__class__.__locators["语音通话"])

    @TestLogger.log()
    def video_call_btn_is_clickable(self):
        """视频通话按钮状态是否可点击"""
        return self._is_clickable(self.__class__.__locators["视频通话"])

    @TestLogger.log("挂断视频通话")
    def end_video_call(self):
        time.sleep(2)

        if self.get_elements(self.__locators["挂断视频通话"]):
            self.click_element(self.__locators["挂断视频通话"])
        else:
            self.click_element(self.__locators["取消拨打"])

    @TestLogger.log()
    def hefeixin_call_btn_is_clickable(self):
        """和飞信通话按钮状态是否可点击"""
        return self._is_clickable(self.__class__.__locators["和飞信电话"])



    @TestLogger.log()
    def is_exists_contacts_image(self):
        """是否存在联系人头像"""
        return self._is_element_present(self.__class__.__locators["用户头像"])

    @TestLogger.log()
    def click_contacts_image(self):
        """点击联系人头像"""
        self.click_element(self.__class__.__locators["用户头像"])

    @TestLogger.log()
    def is_exists_contacts_name(self):
        """是否存在联系人名"""
        return self._is_element_present(self.__class__.__locators["用户名称"])

    @TestLogger.log()
    def is_exists_contacts_number(self):
        """是否存在联系人号码"""
        return self._is_element_present(self.__class__.__locators["用户号码"])

    @TestLogger.log()
    def is_exists_contacts_image(self):
        """是否存在联系人头像"""
        return self._is_element_present(self.__class__.__locators["用户头像"])


    @TestLogger.log()
    def is_exists_message_icon(self):
        """是否存在消息图标"""
        return self._is_element_present(self.__class__.__locators["消息"])

    @TestLogger.log()
    def message_icon_is_enabled(self):
        """消息图标是否可点击"""
        return self._is_enabled(self.__class__.__locators["消息"])

    @TestLogger.log()
    def is_exists_call_icon(self):
        """是否存在电话图标"""
        return self._is_element_present(self.__class__.__locators["电话"])

    @TestLogger.log()
    def call_icon_is_enabled(self):
        """电话图标是否可点击"""
        return self._is_enabled(self.__class__.__locators["电话"])

    @TestLogger.log()
    def is_exists_voice_call_icon(self):
        """是否存在语音通话图标"""
        return self._is_element_present(self.__class__.__locators["语音通话"])

    @TestLogger.log()
    def voice_call_icon_is_enabled(self):
        """语音通话图标是否可点击"""
        return self._is_enabled(self.__class__.__locators["语音通话"])

    @TestLogger.log()
    def is_exists_video_call_icon(self):
        """是否存在视频通话图标"""
        return self._is_element_present(self.__class__.__locators["视频通话"])

    @TestLogger.log()
    def video_call_icon_is_enabled(self):
        """视频通话图标是否可点击"""
        return self._is_enabled(self.__class__.__locators["视频通话"])

    @TestLogger.log()
    def is_exists_dial_hefeixin_icon(self):
        """是否存在和飞信电话图标"""
        return self._is_element_present(self.__class__.__locators["和飞信电话"])

    @TestLogger.log()
    def dial_hefeixin_icon_is_enabled(self):
        """和飞信电话图标是否可点击"""
        return self._is_enabled(self.__class__.__locators["和飞信电话"])

    @TestLogger.log()
    def is_exists_share_card_icon(self):
        """是否存在分享名片图标"""
        return self._is_element_present(self.__class__.__locators["分享名片"])

    @TestLogger.log()
    def click_share_card_icon(self):
        """点击分享名片图标"""
        self.click_element(self.__class__.__locators["分享名片"])

    @TestLogger.log()
    def is_exists_save_contacts_icon(self):
        """是否存在保存到通讯录图标"""
        return self._is_element_present(self.__class__.__locators["保存到通讯录"])

    @TestLogger.log()
    def click_save_contacts_icon(self):
        """点击保存到通讯录图标"""
        self.click_element(self.__class__.__locators["保存到通讯录"])

    @TestLogger.log()
    def is_exists_value_by_name(self, name):
        """用户信息有值时是否显示"""
        locator = (MobileBy.XPATH,
                   '//*[@resource-id="com.chinasofti.rcs:id/property" and @text="%s"]/../android.widget.TextView[@resource-id="com.chinasofti.rcs:id/value"]' % name)
        if self._is_element_present(locator):
            text = self.get_element(locator).text
            if text:
                # 有此信息有值时返回True
                # print(text)
                return True
            else:
                # 有此信息无值时返回False
                # print("出错")
                return False
        else:
            # 没有此信息时返回True
            # print("无" + name)
            return True

    @TestLogger.log("截图")
    def take_screen_out(self):

        path = os.getcwd() + "/screenshot"
        print(path)
        timestamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        os.popen("adb wait-for-device")
        time.sleep(1)
        os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
        time.sleep(1)
        if not os.path.isdir(os.getcwd() + "/screenshot"):
            os.makedirs(path)
        os.popen("adb pull /data/local/tmp/tmp.png " + path + "/" + timestamp + ".png")
        os.popen("adb shell rm /data/local/tmp/tmp.png")



def add(func):
    def wrapper(*args):
        try:
            func(*args)
        except:  # 等待AssertionError
            path = os.getcwd() + "/screenshot"
            print(path)
            timestamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
            os.popen("adb wait-for-device")
            time.sleep(2)
            os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
            time.sleep(2)
            if not os.path.isdir(os.getcwd() + "/screenshot"):
                os.makedirs(path)
            os.popen("adb pull /data/local/tmp/tmp.png " + path + "/" + timestamp + ".png")
            os.popen("adb shell rm /data/local/tmp/tmp.png")
            # raise ArithmeticError

    return wrapper


