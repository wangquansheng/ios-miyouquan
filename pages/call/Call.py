from appium.webdriver.common.mobileby import MobileBy

from library.core.TestLogger import TestLogger
from library.core.utils.applicationcache import current_mobile

from pages.components.Footer import FooterPage

import traceback
import time


# noinspection PyBroadException
class CallPage(FooterPage):
    """通话页面"""
    ACTIVITY = 'com.cmcc.cmrcs.android.ui.activities.HomeActivity'

    __locators = {
        # 权限框
        '禁止': (MobileBy.IOS_PREDICATE, 'name=="禁止"'),
        '始终允许': (MobileBy.IOS_PREDICATE, 'name=="始终允许"'),
        # '遮罩1': (MobileBy.ID, 'com.cmic.college:id/tvContact'),
        # '遮罩2': (MobileBy.ID, 'com.cmic.college:id/header'),

        # 广告
        '广告_通话_关闭': (MobileBy.ACCESSIBILITY_ID, 'my home cancel@2x'),
        # 攻略
        '攻略_通话_id': (MobileBy.ACCESSIBILITY_ID, 'my_banner_gonglue'),
        '攻略_通话_close': (MobileBy.ACCESSIBILITY_ID, 'my cancel copy'),

        # 通话首页
        '通话_通话_TAB': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="通话"]'),
        '通话_文案_HEAD': (MobileBy.XPATH, '//XCUIElementTypeOther[@name="通话"]'),
        '通话_来电名称': (MobileBy.XPATH, '//XCUIElementTypeCell/XCUIElementTypeStaticText[1]'),
        '通话_详情图标': (MobileBy.ACCESSIBILITY_ID, 'call info outline@2x'),
        '通话_第一个联系人': (MobileBy.XPATH, "//XCUIElementTypeTable/XCUIElementTypeCell[1]"),
        '通话_归属地': (MobileBy.IOS_PREDICATE, 'name=="通话记录"'),
        '空白文案': (MobileBy.IOS_PREDICATE, 'name=="点击下方，打电话不花钱"'),
        '键盘输入框': (MobileBy.XPATH,
                  '//XCUIElementTypeApplication[@name="密友圈"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther'
                  '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                  '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                  '/XCUIElementTypeOther[1]/XCUIElementTypeTextField'),
        '通话_类型': (MobileBy.XPATH, '//XCUIElementTypeCell/XCUIElementTypeStaticText[2]'),
        '[飞信电话]': (MobileBy.IOS_PREDICATE, 'name=="[飞信电话] "'),
        '[视频通话]': (MobileBy.IOS_PREDICATE, 'name=="[视频通话] "'),
        '[多方视频]': (MobileBy.IOS_PREDICATE, 'name=="[多方视频] "'),
        '拨号键盘': (MobileBy.ACCESSIBILITY_ID, 'my dialing nor@2x'),
        '+': (MobileBy.ACCESSIBILITY_ID, 'add normal@2x'),
        '视频通话': (MobileBy.IOS_PREDICATE, 'name=="视频通话"'),
        '多方电话': (MobileBy.IOS_PREDICATE, 'name=="多方电话"'),
        '通话_删除该通话记录': (MobileBy.ACCESSIBILITY_ID, '删除'),
        '通话_搜索_联系人名称': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText[2]'),

        # 通话界面 拨号操作
        '拨号_呼叫': (MobileBy.ACCESSIBILITY_ID, 'my dialing keyboard nor@2x'),
        '拨号_删除': (MobileBy.ACCESSIBILITY_ID, 'my dail cannel ic@2x'),
        '拨号_收起键盘': (MobileBy.ACCESSIBILITY_ID, 'my home dail num ic@2x'),
        '拨号_半_收起键盘': (MobileBy.ACCESSIBILITY_ID, 'my home dail num ic c@2x'),
        '拨号_无联系人': (MobileBy.IOS_PREDICATE, 'name=="无该联系人"'),
        '拨号_文本框': (MobileBy.XPATH,
                   '//*[@name="my dialing keyboard nor@2x"]/../preceding-sibling::*[3]/XCUIElementTypeTextField'),
        '拨号_半_文本框': (MobileBy.XPATH,
                     '//*[@name="my dialing keyboard nor@2x"]/../preceding-sibling::*[2]/XCUIElementTypeTextField'),
        '拨号_请输入正确号码': (MobileBy.IOS_PREDICATE, 'name=="请输入正确号码"'),
        '拨号_搜索_列表联系人': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText[1]'),
        'keyboard_1': (MobileBy.IOS_PREDICATE, 'name ENDSWITH "my_call_1@2x.png"'),
        'keyboard_2': (MobileBy.IOS_PREDICATE, 'name ENDSWITH "my_call_2@2x.png"'),
        'keyboard_3': (MobileBy.IOS_PREDICATE, 'name ENDSWITH "my_call_3@2x.png"'),
        'keyboard_4': (MobileBy.IOS_PREDICATE, 'name ENDSWITH "my_call_4@2x.png"'),
        'keyboard_5': (MobileBy.IOS_PREDICATE, 'name ENDSWITH "my_call_5@2x.png"'),
        'keyboard_6': (MobileBy.IOS_PREDICATE, 'name ENDSWITH "my_call_6@2x.png"'),
        'keyboard_7': (MobileBy.IOS_PREDICATE, 'name ENDSWITH "my_call_7@2x.png"'),
        'keyboard_8': (MobileBy.IOS_PREDICATE, 'name ENDSWITH "my_call_8@2x.png"'),
        'keyboard_9': (MobileBy.IOS_PREDICATE, 'name ENDSWITH "my_call_9@2x.png"'),
        'keyboard_0': (MobileBy.IOS_PREDICATE, 'name ENDSWITH "my_call_0@2x.png"'),
        'keyboard_*': (MobileBy.IOS_PREDICATE, 'name ENDSWITH "my_call_*@2x.png"'),
        'keyboard_#': (MobileBy.IOS_PREDICATE, 'name ENDSWITH "my_call_#@2x.png"'),

        # 详情页面
        '详情_返回': (MobileBy.ACCESSIBILITY_ID, 'contact info back normal@2x'),
        '详情_多方通话_返回': (MobileBy.ACCESSIBILITY_ID, 'me back blue normal@2x'),
        '详情_头像': (MobileBy.XPATH,
                  'XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                  '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                  '/XCUIElementTypeImage[2]'),
        '详情_名称': (MobileBy.XPATH, '//XCUIElementTypeOther/XCUIElementTypeStaticText'),
        '详情_通话时长': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeStaticText[2]'),
        '详情_通话时间': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeStaticText[3]'),
        '详情_通话类型': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[4]/XCUIElementTypeStaticText[1]'),
        '详情_备注内容': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[2]'),
        '详情_>': (MobileBy.ACCESSIBILITY_ID, '更多信息'),
        '详情_邀请使用': (MobileBy.ACCESSIBILITY_ID, '邀请使用'),
        '详情_通话': (MobileBy.ACCESSIBILITY_ID, 'my call white n@2x'),
        '详情_视频按钮': (MobileBy.ID, 'my profile ic vedio n@2x'),
        '详情_发起多方视频': (MobileBy.ACCESSIBILITY_ID, 'chat ic video@2x'),
        '详情_头像_多方视频': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]'),
        '详情_名称_多方视频': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]'),
        '详情_通话时长_多方视频': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeStaticText[2]'),
        '详情_通话时间_多方视频': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeStaticText[3]'),
        '详情_通话类型_多方视频': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeStaticText[1]'),

        # 备注页面
        '备注_保存': (MobileBy.ACCESSIBILITY_ID, '完成'),
        '备注_返回': (MobileBy.ACCESSIBILITY_ID, 'me back blue normal@2x'),
        '备注_修改名称': (MobileBy.XPATH, '//XCUIElementTypeNavigationBar[@name="修改备注名称"]'),
        '备注_清除': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="清除文本"]'),
        '备注_文本': (MobileBy.XPATH, '//XCUIElementTypeOther/XCUIElementTypeTextField'),

        # 视频呼叫
        '视频呼叫_通话选择': (MobileBy.XPATH, '//XCUIElementTypeOther[@name="视频通话"]'),
        '视频呼叫_确定': (MobileBy.XPATH, '//XCUIElementTypeNavigationBar/XCUIElementTypeButton[2]'),
        '视频呼叫_取消': (MobileBy.ACCESSIBILITY_ID, '取消'),
        '视频呼叫_联系人列表': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText[1]'),
        '视频呼叫_字母': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeOther'),
        '视频呼叫_字母第一个': (MobileBy.XPATH, '//XCUIElementTypeOther[@name="C"]'),
        '视频呼叫_字母C': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="C"]'),
        '视频呼叫_搜索_文本框': (MobileBy.XPATH, '//XCUIElementTypeImage[contains(@name, "chat_set_search@2x.png")]'
                                        '/../XCUIElementTypeTextField'),
        '视频呼叫_搜索_号码列表': (MobileBy.XPATH,
                         '//XCUIElementTypeImage[contains(@name, "chat_set_search@2x.png")]'
                         '/../../../XCUIElementTypeOther/XCUIElementTypeTable'
                         '/XCUIElementTypeCell/XCUIElementTypeImage[2]'),
        '视频呼叫_最多只能选择8个人': (MobileBy.IOS_PREDICATE, 'name=="确定"'),

        # 视频接听
        # '视频接听_接听': (MobileBy.IOS_PREDICATE, 'name=="接受"'),
        # '视频接听_挂断': (MobileBy.IOS_PREDICATE, 'name=="拒绝"'),
        # '视频接听_提醒我': (MobileBy.IOS_PREDICATE, 'name=="提醒我"'),
        # '视频接听_通话结束': (MobileBy.IOS_PREDICATE, 'name=="通话结束"'),
        '视频_画笔': (MobileBy.ACCESSIBILITY_ID, 'doodle off@2x'),
        '视频_头像': (MobileBy.ID, 'com.cmic.college:id/ivUser'),
        '视频_时长': (MobileBy.XPATH,
                  '//XCUIElementTypeButton[@name="免提"]/../preceding-sibling::*[1]/XCUIElementTypeStaticText'),
        '视频_备注': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[2]'),
        '视频_挂断': (MobileBy.IOS_PREDICATE, 'name=="挂断"'),
        '视频_免提': (MobileBy.IOS_PREDICATE, 'name=="免提"'),
        '视频_静音': (MobileBy.IOS_PREDICATE, 'name=="静音"'),
        '视频_关闭摄像头': (MobileBy.IOS_PREDICATE, 'name=="关闭摄像头"'),
        '视频_翻转摄像头': (MobileBy.IOS_PREDICATE, 'name=="翻转摄像头"'),
        '视频_切到语音通话': (MobileBy.IOS_PREDICATE, 'name=="切到语音通话"'),
        '视频_切换摄像头': (MobileBy.IOS_PREDICATE, 'name=="切换摄像头"'),
        '呼叫_视频_接听': (MobileBy.IOS_PREDICATE, 'name=="接听"'),
        '呼叫_视频_拒接': (MobileBy.IOS_PREDICATE, 'name=="拒接"'),

        # 弹出框
        '无密友圈_提示文本': (MobileBy.XPATH, '//XCUIElementTypeOther[@name="无密友圈"]'),
        '无密友圈_确定': (MobileBy.IOS_PREDICATE, "name=='确定'"),
        '无密友圈_取消': (MobileBy.IOS_PREDICATE, "name=='取消'"),

        # 飞信电话
        '飞信电话_邀请_短信': (MobileBy.ACCESSIBILITY_ID, '邀请使用'),
        '飞信电话_我知道了': (MobileBy.IOS_PREDICATE, 'name=="我知道了"'),

        # 多方通话
        '多方通话_确定': (MobileBy.XPATH, '//XCUIElementTypeNavigationBar/XCUIElementTypeButton[2]'),
        '多方通话_取消': (MobileBy.IOS_PREDICATE, 'name=="取消"'),
        '多方通话_搜索_文本框': (MobileBy.XPATH, '//XCUIElementTypeImage[contains(@name, "chat_set_search@2x.png")]'
                                        '/../XCUIElementTypeTextField'),
        '多方通话_电话号码': (MobileBy.XPATH, '//XCUIElementTypeImage[contains(@name, "chat_set_search@2x.png")]'
                                      '/../../../XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell'
                                      '/XCUIElementTypeImage[2]'),
        '多方通话_是否确定结束多方电话': (MobileBy.IOS_PREDICATE, "name=='是否确定结束多方电话？'"),
        '多方通话_弹框_确定': (MobileBy.IOS_PREDICATE, "name=='确定'"),
        '多方通话_弹框_取消': (MobileBy.IOS_PREDICATE, "name=='取消'"),

        # 流量优惠提示框
        # '流量_不再提醒': (MobileBy.ID, 'com.cmic.college:id/select_checkbox'),
        # '流量_去开通': (MobileBy.ID, 'com.cmic.college:id/bt_open'),
        # '流量_继续拨打': (MobileBy.ID, 'com.cmic.college:id/tv_continue'),
        # '流量_提示内容': (MobileBy.ID, 'com.cmic.college:id/content'),

        # 多人视频详情页
        # '详情_多人视频': (MobileBy.ID, 'com.cmic.college:id/rlStartMultipartyVideo'),
        # '详情_群聊': (MobileBy.ID, 'com.cmic.college:id/rlCreateGroup'),
        # '群聊_确定': (MobileBy.ID, 'com.cmic.college:id/tv_sure'),
        # '群聊_返回上一层': (MobileBy.ID, 'com.cmic.college:id/back_arrow'),
        # '多人_挂断': (MobileBy.ID, 'com.cmic.college:id/end_video_call_btn'),
        # '信息_聊天框': (MobileBy.ID, 'com.cmic.college:id/et_message'),
        # '信息_发送': (MobileBy.ID, 'com.cmic.college:id/ib_send'),

        # 福利电话
        # '页面规则': (MobileBy.ID, 'com.cmic.college:id/action_rule'),
        # '电话_搜索栏': (MobileBy.ID, 'com.cmic.college:id/action_search'),
        # '搜索_电话': (MobileBy.ID, 'com.cmic.college:id/search_src_text'),
        # '搜索_电话显示': (MobileBy.ID, 'com.cmic.college:id/tvPhoneNum'),
        # '搜索_电话昵称': (MobileBy.ID, 'com.cmic.college:id/tvName'),
        # '免费时长': (MobileBy.ID, 'com.cmic.college:id/tv_leftDuration'),

        # 关闭广告页面
        # '广告_关闭': (MobileBy.ID, 'com.cmic.college:id/ivClose'),
        # '广告_内容': (MobileBy.ID, 'com.cmic.college:id/ivContent'),
        # '广告_立即参与': (MobileBy.ID, 'com.cmic.college:id/ivEnter'),

        # 邀请使用
        # '邀请_微信好友': (MobileBy.ID, 'com.cmic.college:id/tv_wechat'),
        # '邀请_QQ好友': (MobileBy.ID, 'com.cmic.college:id/tv_qq'),

        # 悬浮窗授权提示
        # '悬浮窗_内容': (MobileBy.XPATH, '//*[contains(@text,"您的手机没有授予悬浮窗权限，请开启后再试")]'),
        # '暂不开启': (MobileBy.ID, 'android:id/button2'),
        # '现在去开启': (MobileBy.ID, 'android:id/button1'),

        # 暂停使用，待删除
        # '拨叫号码': (MobileBy.ID, 'com.cmic.college:id/etInputNum'),
        # '拨号界面_挂断': (MobileBy.ID, 'com.android.incallui:id/endButton'),
        # '通话记录_确定': (MobileBy.ID, 'com.cmic.college:id/btnConfirm'),
        # '通话记录_取消': (MobileBy.ID, 'com.cmic.college:id/btnCancel'),
        # '通话记录_删除一条': (
        #     MobileBy.XPATH,
        #     '//android.widget.TextView[@resource-id="com.cmic.college:id/tvContent" and @text="删除该通话记录"]'),
        # '通话记录_删除全部': (
        #     MobileBy.XPATH,
        #     '//android.widget.TextView[@resource-id="com.cmic.college:id/tvContent" and @text="清除全部通话记录"]'),
        # '删除_一条通话记录': (MobileBy.XPATH,
        #               '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout
        #               /android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView
        #               /android.widget.LinearLayout[1]'),
        # '删除_全部通话记录': (MobileBy.XPATH,
        #               '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout
        #               /android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView
        #               /android.widget.LinearLayout[2]'),
        # '通话_发起视频通话': (MobileBy.XPATH, '//android.widget.TextView[@text="发起视频通话"]'),
        # '视频通话_第一个联系人': (MobileBy.XPATH,
        #                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
        #                 'FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.'
        #                 'LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
        #                 'LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.'
        #                 'LinearLayout[1]/android.widget.RelativeLayout'),
        # '视频通话_第二个联系人': (MobileBy.XPATH,
        #                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
        #                 'FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.'
        #                 'LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
        #                 'LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.'
        #                 'LinearLayout[2]/android.widget.RelativeLayout'),
        # '视频通话_第三个联系人': (MobileBy.XPATH,
        #                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
        #                 'FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.'
        #                 'LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
        #                 'LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.'
        #                 'LinearLayout[3]/android.widget.RelativeLayout'),
        # # '详情_信息按钮': (MobileBy.ID, 'com.cmic.college:id/tvSendMessage'),
        # '挂断': (MobileBy.ID, 'com.cmic.college:id/video_iv_term'),
        # '挂断_多方通话': (MobileBy.ID, 'com.cmic.college:id/end_video_call_btn'),
        # 'tip1': (MobileBy.ID, 'com.cmic.college:id/ivFreeCall'),
        # 'tip2': (MobileBy.ID, 'com.cmic.college:id/ivKeyboard'),
        # 'tip3': (MobileBy.ID, 'com.cmic.college:id/tvContact'),
        # '视频': (MobileBy.ID, 'com.cmic.college:id/ivMultipartyCall'),
        # '详情_更多': (MobileBy.ID, 'com.cmic.college:id/iv_more'),
        # '详情_红点': (MobileBy.ID, 'com.cmic.college:id/view_red_dot'),
        # """
    }

    def wait_for_page_load(self, timeout=8, auto_accept_alerts=True):
        """默认使用activity作为判断页面是否加载的条件，继承类应该重写该方法"""
        self.wait_until(
            lambda d: self.is_element_present('通话_通话_TAB'),
            timeout,
            auto_accept_alerts
        )

        try:
            # 判断如果键盘已拉起，则收起键盘
            if self.is_exist_call_key():
                self.click_hide_keyboard()
                time.sleep(1)
        except:
            print("判断如果键盘已拉起，则收起键盘")
        return self

    @TestLogger.log("通话首页弹框关闭广告弹框")
    def close_click_home_advertisement(self):
        """通话首页弹框关闭广告弹框"""
        time.sleep(1)
        if self.is_element_already_exist('广告_通话_关闭'):
            self.click_locator_key('广告_通话_关闭')
            time.sleep(1)

    @TestLogger.log()
    def click_always_allow(self):
        """权限框-点击始终允许"""
        while self.is_text_present('始终允许'):
            self.click_text('始终允许')
            time.sleep(2)

    @TestLogger.log()
    def remove_mask(self):
        """去除遮罩"""
        self.click_element(self.__class__.__locators['遮罩1'])
        self.click_element(self.__class__.__locators['遮罩2'])

    @TestLogger.log("您的手机没有授予悬浮窗权限，请开启后再试")
    def close_suspension_if_exist(self):
        """您的手机没有授予悬浮窗权限，请开启后再试"""
        while self.is_text_present('您的手机没有授予悬浮窗权限，请开启后再试') and self.is_text_present(
                '暂不开启') and self.is_text_present('现在去开启'):
            self.click_text('暂不开启')

    @TestLogger.log('等待页面自动跳转')
    def wait_for_page_call(self, max_wait_time=30):
        self.wait_until(
            condition=lambda d: self.is_text_present("不花钱打电话"),
            timeout=max_wait_time,
        )

    @TestLogger.log('等待页面自动跳转')
    def wait_for_page_call_load(self, max_wait_time=30):
        self.wait_until(
            condition=lambda d: self.is_text_present("通话"),
            timeout=max_wait_time,
        )

    @TestLogger.log('等待页面加载完毕')
    def wait_page_load_common(self, text, max_wait_time=30):
        self.wait_until(
            condition=lambda d: self.is_text_present(text),
            timeout=max_wait_time,
        )

    @TestLogger.log('是否在通话页面')
    def is_on_this_page(self):
        el = self.get_elements(self.__locators['拨号键盘'])
        if len(el) > 0:
            return True
        return False

    @TestLogger.log("点击locators对应的元素")
    def click_locator_key(self, locator):
        self.click_element(self.__locators[locator])

    @TestLogger.log("通话页面点击删除按钮")
    def click_delete_key(self, text):
        locator = (MobileBy.XPATH, "//*[contains(@name,'%s')]/../XCUIElementTypeOther/XCUIElementTypeButton[@name='删除']" % text)
        self.click_element(locator)

    @TestLogger.log("通话页面点击删除按钮，删除所有")
    def click_delete_all_key(self):
        time.sleep(2)
        while self.is_element_already_exist("通话_第一个联系人"):
            time.sleep(2)
            self.swipe_by_direction(self.__locators["通话_第一个联系人"], "left")
            time.sleep(5)
            del_locator = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="删除"]')
            self.click_element(del_locator)
            time.sleep(2)
        # 检查当前页面
        time.sleep(1)
        if self.is_element_already_exist('通话_通话_TAB'):
            return True
        else:
            return False

    @TestLogger.log("当前页面是否包含此文本")
    def check_text_exist(self, text):
        """当前页面是否包含此文本"""
        """当前页面是否包含此文本"""
        return self.is_text_present(text)

    @TestLogger.log("点击包含文本的元素")
    def click_by_text(self, text):
        """点击文本"""
        return self.click_text(text)

    @TestLogger.log("点击包含文本的元素")
    def input_locator_text(self, locator, text):
        """输入文本"""
        return self.input_text(self.__locators[locator], text)

    @TestLogger.log('根据元素模拟三指点击屏幕')
    def tap_screen_three_point(self, locator='视频界面_时长'):
        """根据元素模拟三指点击屏幕"""
        if not self.is_element_already_exist(locator):
            self.tap_coordinate([(100, 100), (100, 110), (100, 120)])
            time.sleep(1)

    @TestLogger.log("通话界面-呼叫-搜索联系人")
    def click_search_phone_first_element(self, text):
        if not self.is_element_already_exist(text):
            return False
        # 获取通话列表所有数据
        time.sleep(2)
        elements_list = self.get_elements(self.__locators[text])
        time.sleep(2)
        elements_list[0].click()
        time.sleep(2)
        return True

    @TestLogger.log("检查列表中元素是否有目标值")
    def get_tag_list_text_exists(self, text, target):
        if not self.is_element_already_exist(text):
            return False
        # 获取通话列表所有数据
        elements_list = self.get_elements(self.__locators[text])
        text_list = [i.text for i in elements_list]
        for index, value in enumerate(text_list):
            for value_c in target:
                if value.strip().find(value_c) > -1:
                    return True
        return False

    @TestLogger.log("点击包含文本的第一个详细信息(i)元素")
    def click_tag_detail_first_element(self, text):
        # 获取通话列表所有数据
        elements_list = self.get_elements(self.__locators['通话_类型'])
        # 获取"详情"按钮列表
        detail_list = self.get_elements(self.__locators['通话_详情图标'])
        text_list = [i.text for i in elements_list]
        # 单击第一个匹配节点
        for index, value in enumerate(text_list):
            if value.strip() == text:
                element_first = detail_list[index]
                element_first.click()
                return
        raise AssertionError("没有找到对应的标签--{}".format(text))

    @TestLogger.log("长按包含文本的第一个通话记录元素")
    def press_tag_detail_first_element(self, text):
        time.sleep(1)
        locator = (MobileBy.IOS_PREDICATE, "name CONTAINS '%s'" % text)
        self.swipe_by_direction(locator, "left")
        time.sleep(5)

    @TestLogger.log('确保页面有点对点视频的记录')
    def make_sure_have_p2p_vedio_record(self):
        if self.is_text_present('[视频通话]'):
            return
        # self.point2point_vedio_call()
        self.wait_until(
            condition=lambda d: self.is_text_present("[视频通话]"),
            timeout=50,
        )

    @TestLogger.log('确保页面有多方视频的记录')
    def make_sure_have_multiplayer_vedio_record(self):
        if self.is_text_present('[多方视频]'):
            return
        # self.multiplayer_vedio_call()
        self.wait_until(
            condition=lambda d: self.is_text_present("[多方视频]"),
            timeout=50,
        )

    @TestLogger.log('确保页面有点对点通话的记录')
    def make_sure_have_p2p_voicecall_record(self):
        if self.is_text_present('飞信电话'):
            return
        # self.point2point_voice_call()
        self.wait_until(
            condition=lambda d: self.is_text_present("飞信电话"),
            timeout=8,
        )

    @TestLogger.log("检查点对点视频通话详细页")
    def check_vedio_call_detail_page(self):
        # 检查视频按钮/电话按钮
        for locator in [self.__locators['详情_视频按钮'], self.__locators['详情_返回']]:
            if not self._is_enabled(locator):
                return "检查点[%s]未通过" % locator

        # 检查文字"通话记录(视频通话)"文字
        time.sleep(1)
        if '通话记录(视频通话)' != self.get_text((MobileBy.ACCESSIBILITY_ID, '通话记录(视频通话)')):
            return "检查点[通话记录 (视频通话)]未通过"
        # 检查头像/名称/通话时间/通话类型
        time.sleep(2)
        if not self.is_element_already_exist('详情_头像'):
            return "检查点[详情_头像]未通过"
        time.sleep(2)
        if not self.is_element_already_exist('详情_名称'):
            return "检查点[详情_名称]未通过"
        time.sleep(2)
        if not self.is_element_already_exist('详情_通话类型'):
            return "检查点[详情_通话类型]未通过"
        time.sleep(2)
        if not self.is_element_already_exist('详情_通话时间'):
            return "检查点[详情_通话时间]未通过"
        time.sleep(2)
        if not self.is_element_already_exist('详情_通话时长'):
            return "检查点[详情_通话时长]未通过"
        return True

    @TestLogger.log("检查多方视频详细页")
    def check_multiplayer_vedio_detail_page(self):
        if not self._is_enabled(self.__locators['详情_多方通话_返回']):
            return False
        if '通话记录(多方视频)' != self.get_text((MobileBy.ACCESSIBILITY_ID, '通话记录(多方视频)')):
            return False
        # 检查头像/名称/通话时间/通话类型
        time.sleep(1)
        if not self.is_element_already_exist('详情_头像_多方视频'):
            return "检查点[详情_头像_多方视频]未通过"
        time.sleep(1)
        if not self.is_element_already_exist('详情_名称_多方视频'):
            return "检查点[详情_名称_多方视频]未通过"
        time.sleep(1)
        if not self.is_element_already_exist('详情_通话类型_多方视频'):
            return "检查点[详情_通话类型_多方视频]未通过"
        time.sleep(1)
        if not self.is_element_already_exist('详情_通话时间_多方视频'):
            return "检查点[详情_通话时间_多方视频]未通过"
        time.sleep(1)
        if not self.is_element_already_exist('详情_通话时长_多方视频'):
            return "检查点[详情_通话时长_多方视频]未通过"
        return True

    @TestLogger.log("截图")
    def take_screen_out(self):
        import os
        import time
        path = os.getcwd() + "/screenshot"
        print(path)
        timestamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        if not os.path.isdir(os.getcwd() + "/screenshot"):
            os.makedirs(path)
        self.driver.get_screenshot_as_file(path + "/" + timestamp + ".png")

    @TestLogger.log("获得元素的文本")
    def get_element_text(self, locator):
        return self.get_text(self.__locators[locator])

    @TestLogger.log("获得元素对应的数量")
    def get_elements_count(self, locator):
        return self.get_elements(self.__locators[locator])

    @TestLogger.log("页面应该包含元素")
    def page_contain_element(self, locator):
        self.page_should_contain_element(self.__locators[locator])

    @TestLogger.log("判断页面元素是否存在")
    def is_element_present(self, locator):
        return self._is_element_present(self.__locators[locator])

    @TestLogger.log("页面应该包含元素")
    def click_keyboard(self):
        self.click_element(self.__locators['拨号键盘'])

    @TestLogger.log("点击键盘输入框")
    def click_keyboard_input_box(self):
        self.click_element(self.__locators['键盘输入框'])

    @TestLogger.log()
    def click_keyboard_call(self, text):
        """点击通话模块文本弹出框"""
        self.click_element(self.__locators[text])

    @TestLogger.log()
    def click_call(self, text):
        """点击事件"""
        self.click_element(self.__locators[text])

    @TestLogger.log("获取输入框文本")
    def get_input_box_text(self, ):
        return self.get_element(self.__class__.__locators['键盘输入框']).text

    @TestLogger.log("点击收起键盘")
    def click_hide_keyboard(self):
        self.click_element(self.__class__.__locators['拨号_收起键盘'])

    @TestLogger.log("点击屏幕中心")
    def click_screen_center(self):
        """
        点击屏幕中心
        :return:
        """
        # iphone 7: xp=(appium x)/375, yp=(appium y)/667
        x_percentage = (375 / 2) / 375 * 100
        y_percentage = (667 / 2) / 667 * 100
        self.click_coordinate(x_percentage, y_percentage)

    @TestLogger.log("多机-视频通话接听")
    def click_close_two_device_popup(self):
        """
        多机-视频通话接听
        :return:
        """
        # iphone 7: xp=(appium x)/375, yp=(appium y)/667
        x_percentage = 276 / 375 * 100
        y_percentage = 578 / 667 * 100
        self.click_coordinate(x_percentage, y_percentage)

    @TestLogger.log("视频通话结束弹出框")
    def click_close_video_popup(self):
        """
        视频通话结束弹出框
        :return:
        """
        # iphone 7: xp=(appium x)/375, yp=(appium y)/667
        x_percentage = 49
        y_percentage = 86.6
        self.click_coordinate(x_percentage, y_percentage)

    @TestLogger.log("多方视频通话结束弹出框")
    def click_close_more_video_popup(self):
        """
        多方视频通话结束弹出框
        :return:
        """
        # iphone 7: xp=(appium x)/375, yp=(appium y)/667
        x_percentage = 51.2
        y_percentage = 89.9
        self.click_coordinate(x_percentage, y_percentage)

    @TestLogger.log("点击打开键盘")
    def click_show_keyboard(self):
        self.click_element(self.__class__.__locators['拨号键盘'])

    @TestLogger.log('是否在拨号界面')
    def is_exist_call_key(self):
        el = self.get_elements(self.__locators['拨号_呼叫'])
        if len(el) > 0:
            return True
        return False

    @TestLogger.log('是否在通话记录详情页面')
    def on_this_page_call_detail(self):
        """是否在通话记录详情页面"""
        el = self.get_elements(self.__locators['详情_通话'])
        if len(el) > 0:
            return True
        return False

    @TestLogger.log('是否在多方视频页面')
    def on_this_page_multi_video_detail(self):
        """是否在多方视频页面"""
        el = self.get_elements(self.__locators['详情_发起多方视频'])
        if len(el) > 0:
            return True
        return False

    @TestLogger.log("点击详情页返回")
    def click_detail_back(self):
        self.click_element(self.__class__.__locators['详情_返回'])

    @TestLogger.log("修改备注")
    def click_modify_nickname(self):
        self.click_element(self.__class__.__locators['详情_>'])

    @TestLogger.log('等待页面自动跳转')
    def wait_for_page_modify_nickname(self, max_wait_time=30):
        self.wait_until(
            condition=lambda d: self.is_element_present('备注_修改名称'),
            timeout=max_wait_time,
        )

    @TestLogger.log("点击备注输入框")
    def click_nickname_input_box(self):
        self.click_element(self.__locators['备注'])

    @TestLogger.log("备注输入框输入文本")
    def input_text_in_nickname(self, text):
        self.input_text(self.__locators['备注_文本'], text)

    @TestLogger.log("获取备注")
    def get_nickname(self):
        return self.get_element(self.__class__.__locators['详情_备注内容']).text

    @TestLogger.log('是否有流量优惠界面')
    def on_this_page_flow(self):
        """是否在流量优惠界面页面"""
        el = self.get_elements(self.__locators['流量_提示内容'])
        if len(el) > 0:
            return True
        return False

    # @TestLogger.log('设置不再提醒为选中')
    # def set_not_reminders(self):
    #     """设置不再提醒为选中"""
    #     el = self.get_elements(self.__locators['流量_不再提醒'])[0].get_attribute('checked')
    #     if 'false' == el:
    #         self.click_element(self.__locators['流量_不再提醒'])
    #         el = self.get_elements(self.__locators['流量_不再提醒'])[0].get_attribute('checked')
    #         if 'true' == el:
    #             return True
    #     return False

    @TestLogger.log('是否有某个标签')
    def on_this_page_common(self, locator):
        """是否有某个标签"""
        try:
            el = self.get_elements(self.__locators[locator])
            if len(el) > 0:
                return True
            return False
        except:
            return False

    @TestLogger.log('选择N个联系人')
    def select_contact_n(self, number):
        """选择N个联系人"""
        try:
            count = 0
            # 联系人列表大于0，和N个联系人
            els = self.get_elements((MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell'))
            time.sleep(2)
            if count >= len(els):
                print('联系人列表为0')
                return False
            if number > len(els):
                print('联系人列表小于选择人员个数')
                return False
            # 选择联系人, 点击之后页面变化，需重新获取元素
            for cell in range(number):
                els = self.get_elements((MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell'))
                els[cell].click()
                time.sleep(2)
                # 向上滑动
                if cell > 0 and (0 == cell % 5):
                    # xp=(appium x)/375, yp=(appium y)/667
                    x_source = 180 / 375 * 100
                    y_source = 380 / 667 * 100
                    x_target = 180 / 375 * 100
                    y_target = 180 / 667 * 100
                    self.swipe_by_percent_on_screen(x_source, y_source, x_target, y_target)
                    time.sleep(2)
            # 最多选择8个联系人
            if 8 < number:
                time.sleep(5)
                if self.is_element_present("视频呼叫_最多只能选择8个人"):
                    self.click_locator_key("视频呼叫_最多只能选择8个人")
                    time.sleep(2)
                    return True
                else:
                    return False
            else:
                # 小于等于选择8个联系人
                selected = self.get_element_text('视频呼叫_确定')
                if selected is not None:
                    spilt_text = selected.split('/')[0].split('(')[-1]
                    if number == int(spilt_text):
                        return True
                else:
                    print('')
                    return False
        except Exception:
            traceback.print_exc()
        return False

    @TestLogger.log('获取指定运营商类型的手机卡（不传类型返回全部配置的手机卡）')
    def get_cards(self, card_type):
        """返回指定类型卡手机号列表"""
        return current_mobile().get_cards(card_type)

    @TestLogger.log('视频通话界面用户名称')
    def get_video_text(self, text):
        try:
            elements = self.get_elements((MobileBy.IOS_PREDICATE, 'name=="%s"' % text))
            if len(elements) > 0:
                return True
            else:
                return False
        except:
            return False

    @TestLogger.log('拨打一个点对点视频通话')
    def pick_up_p2p_video(self, cards):
        self.click_locator_key('+')
        self.click_locator_key('视频通话')
        self.input_text(self.__locators['视频呼叫_搜索_文本框'], cards)
        time.sleep(1)
        self.get_elements(self.__locators['视频呼叫_搜索_号码列表'])[0].click()
        time.sleep(1)
        self.click_locator_key('视频呼叫_确定')
        time.sleep(0.5)
        # if self.on_this_page_common('流量_继续拨打'):
        #     self.click_locator_key('流量_继续拨打')
        if self.on_this_page_common('无密友圈_确定'):
            self.click_locator_key('无密友圈_取消')

    @TestLogger.log("长按操作")
    def long_press_number(self, text):
        """长按"""
        self.swipe_by_direction(self.__class__.__locators[text], 'press', 5)

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

    @TestLogger.log('获取元素')
    def get_one_element(self, locator):
        return self.mobile.get_element(self.__locators[locator])

    @TestLogger.log('获取所有元素')
    def get_some_elements(self, locator):
        return self.mobile.get_elements(self.__locators[locator])

    @TestLogger.log('飞信电话修改备注')
    def check_modify_nickname(self, name):
        """修改并验证备注是否修改成功"""
        time.sleep(2)
        self.click_modify_nickname()
        self.wait_for_page_modify_nickname()
        # 点击清除按钮
        time.sleep(1)
        if self.is_element_already_exist('备注_清除'):
            self.click_locator_key('备注_清除')
            time.sleep(2)
        # 设置文本，并且保存
        self.input_text_in_nickname(name)
        self.click_locator_key('备注_保存')
        time.sleep(3)
        if not self.on_this_page_call_detail():
            return False
        nickname = self.get_nickname()
        if name != nickname:
            return False
        return True

    @TestLogger.log('添加视频通话记录')
    def test_call_video_condition(self):
        """
        添加视频通话记录
        :return:
        """
        # 初始化数据
        time.sleep(2)
        if not self.is_text_present("[视频通话]"):
            self.click_locator_key('+')
            time.sleep(1)
            self.click_call('视频通话')
            self.select_contact_n(1)
            time.sleep(2)
            self.click_locator_key('视频呼叫_确定')
            time.sleep(3)
            self.click_close_video_popup()
            time.sleep(2)
            if self.is_element_present("无密友圈_取消"):
                self.click_locator_key('无密友圈_取消')
                time.sleep(1)

    @TestLogger.log('添加多方视频记录')
    def test_call_more_video_condition(self):
        """
        添加多方视频记录
        :return:
        """
        # 初始化数据
        time.sleep(2)
        if not self.is_text_present("[多方视频]"):
            self.click_locator_key('+')
            time.sleep(2)
            self.click_call('视频通话')
            self.select_contact_n(2)
            time.sleep(2)
            self.click_locator_key('视频呼叫_确定')
            time.sleep(3)
            self.click_close_video_popup()
            time.sleep(2)
            if self.is_element_present("无密友圈_取消"):
                self.click_locator_key('无密友圈_取消')
                time.sleep(1)

    @TestLogger.log('添加飞信电话记录')
    def test_call_phone_condition(self):
        """
        添加飞信电话记录
        :return:
        """
        # 初始化数据
        time.sleep(2)
        self.click_keyboard()
        time.sleep(3)
        self.click_keyboard_call('keyboard_1')
        time.sleep(2)
        self.click_keyboard_call('keyboard_2')
        time.sleep(2)
        self.click_keyboard_call('keyboard_5')
        time.sleep(2)
        self.click_keyboard_call('keyboard_6')
        time.sleep(2)
        self.click_keyboard_call('keyboard_0')
        time.sleep(2)
        self.click_locator_key('拨号_呼叫')
        time.sleep(5)
        self.click_locator_key('飞信电话_我知道了')
        time.sleep(5)
        self.click_close_video_popup()
        time.sleep(2)

    @TestLogger.log('添加飞信电话记录，没有注册')
    def test_call_phone_no_reg_condition(self):
        """
        添加飞信电话记录
        :return:
        """
        # 初始化数据
        self.test_call_phone_no_reg()
        time.sleep(2)
        # 关闭
        self.click_close_video_popup()
        time.sleep(2)

    @TestLogger.log('添加飞信电话记录，没有注册')
    def test_call_phone_no_reg(self):
        """
        添加飞信电话记录
        :return:
        """
        # 初始化数据
        time.sleep(2)
        self.click_keyboard()
        time.sleep(3)
        self.click_keyboard_call('keyboard_1')
        time.sleep(2)
        self.click_keyboard_call('keyboard_8')
        time.sleep(2)
        self.click_keyboard_call('keyboard_6')
        time.sleep(2)
        self.click_keyboard_call('keyboard_0')
        time.sleep(2)
        self.click_keyboard_call('keyboard_0')
        time.sleep(2)
        self.click_keyboard_call('keyboard_0')
        time.sleep(2)
        self.click_keyboard_call('keyboard_0')
        time.sleep(2)
        self.click_keyboard_call('keyboard_1')
        time.sleep(2)
        self.click_keyboard_call('keyboard_0')
        time.sleep(2)
        self.click_locator_key('拨号_呼叫')
        time.sleep(3)
        self.click_locator_key('飞信电话_我知道了')
        time.sleep(2)

    @TestLogger.log('添加多方电话记录')
    def test_call_more_phone_condition(self):
        """
        添加多方视频记录
        :return:
        """
        # 初始化数据
        time.sleep(1)
        if not self.is_text_present("[多方电话]"):
            self.click_locator_key('+')
            time.sleep(2)
            self.click_call('多方电话')
            self.select_contact_n(1)
            time.sleep(3)
            self.click_locator_key('视频呼叫_确定')
            time.sleep(2)
            self.click_locator_key('飞信电话_我知道了')
            time.sleep(3)
            self.click_close_video_popup()
            time.sleep(3)
            if self.is_element_already_exist('多方通话_是否确定结束多方电话'):
                self.click_locator_key('多方通话_弹框_确定')
            time.sleep(2)
            if self.is_element_present("无密友圈_取消"):
                self.click_locator_key('无密友圈_取消')
                time.sleep(1)
