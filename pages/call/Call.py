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
        # 攻略
        '攻略_通话_id': (MobileBy.ACCESSIBILITY_ID, 'my_banner_gonglue'),
        '攻略_通话_close': (MobileBy.ACCESSIBILITY_ID, 'my cancel copy'),

        # 通话首页
        '通话_通话_TAB': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="通话"]'),
        '通话_文案_HEAD': (MobileBy.XPATH, '//XCUIElementTypeOther[@name="通话"]'),
        '通话_来电名称': (MobileBy.XPATH, '//XCUIElementTypeCell/XCUIElementTypeStaticText[1]'),
        '通话_详情图标': (MobileBy.IOS_PREDICATE, 'name contains "call info outline"'),
        '通话_第一个联系人': (MobileBy.XPATH, "//XCUIElementTypeTable/XCUIElementTypeCell[1]"),
        '通话_通话记录列表': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell'),

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
        '拨号键盘': (MobileBy.IOS_PREDICATE, 'name contains "my dialing nor"'),
        '+': (MobileBy.IOS_PREDICATE, 'name contains "add normal"'),
        '视频通话': (MobileBy.IOS_PREDICATE, 'name=="视频通话"'),
        '多方电话': (MobileBy.IOS_PREDICATE, 'name=="多方电话"'),
        '通话_删除该通话记录': (MobileBy.ACCESSIBILITY_ID, '删除'),
        '通话_搜索_用户备注': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText[1]'),
        '通话_搜索_联系人名称': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText[2]'),

        # 通话界面 拨号操作
        '拨号_呼叫': (MobileBy.IOS_PREDICATE, 'name contains "my dialing keyboard nor"'),
        '拨号_呼叫_呼叫': (MobileBy.IOS_PREDICATE, 'name=="呼叫"'),
        '拨号_呼叫_取消': (MobileBy.IOS_PREDICATE, 'name=="取消"'),
        '拨号_删除': (MobileBy.IOS_PREDICATE, 'name contains "my dail cannel ic"'),
        '拨号_收起键盘': (MobileBy.IOS_PREDICATE, 'name contains "my home dail num ic"'),
        '拨号_半_收起键盘': (MobileBy.IOS_PREDICATE, 'name contains "my home dail num ic c"'),
        '拨号_无联系人': (MobileBy.IOS_PREDICATE, 'name=="无该联系人"'),
        '拨号_文本框': (MobileBy.XPATH, '//XCUIElementTypeOther/XCUIElementTypeTextField'),
        '拨号_半_文本框': (MobileBy.XPATH, '//XCUIElementTypeOther/XCUIElementTypeTextField'),
        '拨号_请输入正确号码': (MobileBy.IOS_PREDICATE, 'name=="请输入正确号码"'),
        '拨号_搜索_列表联系人': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText[1]'),
        '拨号_搜索_列表联系人详细': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeButton[1]'),
        'keyboard_1': (MobileBy.IOS_PREDICATE, 'name contains "my_call_1"'),
        'keyboard_2': (MobileBy.IOS_PREDICATE, 'name contains "my_call_2"'),
        'keyboard_3': (MobileBy.IOS_PREDICATE, 'name contains "my_call_3"'),
        'keyboard_4': (MobileBy.IOS_PREDICATE, 'name contains "my_call_4"'),
        'keyboard_5': (MobileBy.IOS_PREDICATE, 'name contains "my_call_5"'),
        'keyboard_6': (MobileBy.IOS_PREDICATE, 'name contains "my_call_6"'),
        'keyboard_7': (MobileBy.IOS_PREDICATE, 'name contains "my_call_7"'),
        'keyboard_8': (MobileBy.IOS_PREDICATE, 'name contains "my_call_8"'),
        'keyboard_9': (MobileBy.IOS_PREDICATE, 'name contains "my_call_9"'),
        'keyboard_0': (MobileBy.IOS_PREDICATE, 'name contains "my_call_0"'),
        'keyboard_*': (MobileBy.IOS_PREDICATE, 'name contains "my_call_*"'),
        'keyboard_#': (MobileBy.IOS_PREDICATE, 'name contains "my_call_#"'),

        # 呼叫页面
        '呼叫_结束通话': (MobileBy.IOS_PREDICATE, 'name=="结束通话"'),
        '呼叫_静音': (MobileBy.IOS_PREDICATE, 'name=="静音"'),
        '呼叫_免提': (MobileBy.IOS_PREDICATE, 'name=="免提"'),
        '呼叫_添加通话': (MobileBy.IOS_PREDICATE, 'name=="添加通话"'),
        '呼叫_通讯录': (MobileBy.IOS_PREDICATE, 'name=="通讯录"'),
        '呼叫_提示文本': (MobileBy.IOS_PREDICATE, 'value contains "正在呼叫手机"'),
        '呼叫_电话号码': (MobileBy.IOS_PREDICATE, 'name=="PHMarqueeView"'),
        '呼叫_用户正忙': (MobileBy.IOS_PREDICATE, 'name=="PHSingleCallParticipantLabelView_StatusLabel"'),
        '呼叫_取消': (MobileBy.IOS_PREDICATE, 'name=="取消"'),
        '呼叫_回拨': (MobileBy.IOS_PREDICATE, 'name=="回拨"'),

        # 详情页面
        '详情_返回': (MobileBy.IOS_PREDICATE, 'name contains "contact info back normal"'),
        '详情_多方通话_返回': (MobileBy.IOS_PREDICATE, 'name contains "me back blue normal"'),
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
        '详情_通话': (MobileBy.IOS_PREDICATE, 'name contains "my call white n"'),
        '详情_视频按钮': (MobileBy.IOS_PREDICATE, 'name contains "my profile ic vedio n"'),
        '详情_发起多方视频': (MobileBy.IOS_PREDICATE, 'name contains "chat ic video"'),
        '详情_头像_多方视频': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]'),
        '详情_名称_多方视频': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]'),
        '详情_通话时长_多方视频': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeStaticText[2]'),
        '详情_通话时间_多方视频': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeStaticText[3]'),
        '详情_通话类型_多方视频': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeStaticText[1]'),

        # 备注页面
        '备注_保存': (MobileBy.ACCESSIBILITY_ID, '完成'),
        '备注_返回': (MobileBy.IOS_PREDICATE, 'name contains "me back blue normal"'),
        '备注_修改名称': (MobileBy.XPATH, '//XCUIElementTypeNavigationBar[@name="修改备注名称"]'),
        '备注_清除': (MobileBy.XPATH, '//XCUIElementTypeButton[@name="清除文本"]'),
        '备注_文本': (MobileBy.XPATH, '//XCUIElementTypeOther/XCUIElementTypeTextField'),

        # 视频联系人选择
        '视频呼叫_通话选择': (MobileBy.XPATH, '//XCUIElementTypeOther[@name="视频通话"]'),
        '视频呼叫_确定': (MobileBy.XPATH, '//XCUIElementTypeNavigationBar/XCUIElementTypeButton[2]'),
        '视频呼叫_取消': (MobileBy.ACCESSIBILITY_ID, '取消'),
        '视频呼叫_联系人列表': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText[1]'),
        '视频呼叫_字母': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeOther'),
        '视频呼叫_字母第一个': (MobileBy.XPATH, '//XCUIElementTypeOther[@name="C"]'),
        '视频呼叫_字母C': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="C"]'),
        '视频呼叫_搜索_文本框': (MobileBy.IOS_PREDICATE, 'type=="XCUIElementTypeTextField"'),
        '视频呼叫_搜索_号码列表': (MobileBy.XPATH, '(//XCUIElementTypeTable)[2]/XCUIElementTypeCell'),
        '视频呼叫_最多只能选择8个人': (MobileBy.IOS_PREDICATE, 'name=="确定"'),

        # 视频主叫
        '视频主叫_头像': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="网络视频通话呼叫中..."]/preceding-sibling::*[3]'),
        '视频主叫_名称': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="网络视频通话呼叫中..."]/preceding-sibling::*[2]'),
        '视频主叫_电话': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="网络视频通话呼叫中..."]/preceding-sibling::*[1]'),
        '视频主叫_网络视频通话呼叫中': (MobileBy.IOS_PREDICATE, 'name=="网络视频通话呼叫中..."'),
        '视频主叫_挂断': (MobileBy.IOS_PREDICATE, 'name=="挂断"'),

        # 视频被叫
        '视频接听_头像': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="邀请你进行网络视频通话"]/preceding-sibling::*[3]'),
        '视频接听_备注': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="邀请你进行网络视频通话"]/preceding-sibling::*[2]'),
        '视频接听_电话号码': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="邀请你进行网络视频通话"]/preceding-sibling::*[1]'),
        '视频接听_提示文本': (MobileBy.IOS_PREDICATE, 'name=="邀请你进行网络视频通话"'),
        '视频接听_通话结束': (MobileBy.IOS_PREDICATE, 'name=="通话结束"'),
        '视频接听_接听': (MobileBy.IOS_PREDICATE, 'name=="接听"'),
        '视频接听_拒接': (MobileBy.IOS_PREDICATE, 'name=="拒接"'),
        '视频接听_切换弹框_接受': (MobileBy.IOS_PREDICATE, 'name=="接受"'),
        '视频接听_切换弹框_取消': (MobileBy.IOS_PREDICATE, 'name=="取消"'),

        # 视频通话界面
        '视频_时长': (MobileBy.XPATH,
                  '//XCUIElementTypeButton[@name="免提"]/../preceding-sibling::*[1]/XCUIElementTypeStaticText'),
        '视频_备注': (MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[2]'),
        '视频_免提': (MobileBy.IOS_PREDICATE, 'name=="免提"'),
        '视频_静音': (MobileBy.IOS_PREDICATE, 'name=="静音"'),
        '视频_画笔': (MobileBy.IOS_PREDICATE, 'name contains "doodle"'),
        '视频_切到语音通话': (MobileBy.IOS_PREDICATE, 'name=="切到语音通话"'),
        '视频_挂断': (MobileBy.IOS_PREDICATE, 'name=="挂断"'),
        '视频_切换摄像头': (MobileBy.IOS_PREDICATE, 'name=="切换摄像头"'),
        '视频_未接听': (MobileBy.IOS_PREDICATE, 'name=="对方不在线，暂时无法接听，请稍后重试。"'),
        '视频_正在通话中': (MobileBy.IOS_PREDICATE, 'name=="对方正在通话中，请稍后再拨。"'),
        '视频_确定': (MobileBy.IOS_PREDICATE, 'name=="确定"'),
        '视频_通话结束': (MobileBy.IOS_PREDICATE, 'name=="通话结束"'),
        '视频_小屏': (MobileBy.XPATH,
                  '//XCUIElementTypeApplication[@name="密友圈"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[5]'),

        # 视频-语音界面
        '语音_名称': (MobileBy.XPATH,
                  '//XCUIElementTypeButton[@name="免提"]/../preceding-sibling::*[1]/XCUIElementTypeStaticText[1]'),
        '语音_头像': (MobileBy.XPATH,
                  '//XCUIElementTypeApplication[@name="密友圈"]/XCUIElementTypeWindow[1]/XCUIElement'
                  'TypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeImage'),
        '语音_备注': (MobileBy.XPATH,
                  '//XCUIElementTypeApplication[@name="密友圈"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/'
                  'XCUIElementTypeOther[1]/XCUIElementTypeStaticText[1]'),

        '语音_电话': (MobileBy.XPATH,
                  '//XCUIElementTypeApplication[@name="密友圈"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/'
                  'XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]'),
        '语音_时长': (MobileBy.XPATH,
                  '//XCUIElementTypeApplication[@name="密友圈"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/'
                  'XCUIElementTypeOther[1]/XCUIElementTypeStaticText[3]'),
        '语音_免提': (MobileBy.IOS_PREDICATE, 'name=="免提"'),
        '语音_切到视频通话': (MobileBy.IOS_PREDICATE, 'name=="切到视频通话"'),
        '语音_静音': (MobileBy.IOS_PREDICATE, 'name=="静音"'),
        '语音_挂断': (MobileBy.IOS_PREDICATE, 'name=="挂断"'),

        # 语音切视频页面
        '切视频_头像': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="正在等待对方接受邀请..."]/preceding-sibling::*[3]'),
        '切视频_提示文本': (MobileBy.IOS_PREDICATE, 'name contains "正在等待对方接受邀请"'),
        '切视频_电话号码': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="正在等待对方接受邀请..."]/preceding-sibling::*[1]'),
        '切视频_备注': (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="正在等待对方接受邀请..."]/preceding-sibling::*[2]'),

        # 视频涂鸦
        '涂鸦_返回': (MobileBy.IOS_PREDICATE, 'name contains "doodle on"'),
        '涂鸦_圆点': (MobileBy.XPATH, '//XCUIElementTypeButton[contains(@name,"doodle line")]/preceding-sibling::*[1]'),
        '涂鸦_线条': (MobileBy.IOS_PREDICATE, 'name contains "doodle line"'),
        '涂鸦_表情': (MobileBy.IOS_PREDICATE, 'name contains "doodle sticker"'),
        '涂鸦_橡皮': (MobileBy.IOS_PREDICATE, 'name contains "doodle eraser"'),
        '涂鸦_删除': (MobileBy.IOS_PREDICATE, 'name contains "doodle clear"'),
        '涂鸦_分享': (MobileBy.IOS_PREDICATE, 'name contains "doodle share"'),
        '涂鸦_分享到': (MobileBy.IOS_PREDICATE, 'name contains "分享到"'),
        '涂鸦_您要清除所有涂鸦': (MobileBy.IOS_PREDICATE, 'name=="您要清除所有涂鸦吗？"'),
        '涂鸦_删除_确定': (MobileBy.IOS_PREDICATE, 'name=="确定"'),
        '涂鸦_删除_取消': (MobileBy.IOS_PREDICATE, 'name=="取消"'),
        '涂鸦_橙色': (MobileBy.XPATH,
                  '//XCUIElementTypeApplication[@name="密友圈"]/XCUIElementTypeWindow[1]/XCUIElementType'
                  'Other[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]'),
        '涂鸦_线条_滑动': (MobileBy.XPATH,
                     '//XCUIElementTypeApplication[@name="密友圈"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElement'
                     'TypeOther[4]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeSlider'),
        '涂鸦_橡皮_滑动': (MobileBy.XPATH,
                     '//XCUIElementTypeButton[contains(@name,"doodle share")]/../following-sibling::*[1]/XCUIElementTypeSlider'),
        '涂鸦_画布': (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="密友圈"]/XCUIElementType'
                                  'Window[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[4]'),
        '涂鸦_表情1': (
            MobileBy.XPATH,
            '//XCUIElementTypeApplication[@name="密友圈"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/'
            'XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther[4]/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]'),
        '涂鸦_滑块': (MobileBy.XPATH,
                  '//XCUIElementTypeApplication[@name="密友圈"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElement'
                  'TypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeSlider'),

        # 多方通话联系人选择
        '多方通话_确定': (MobileBy.IOS_PREDICATE, 'name contains "确定"'),
        '多方通话_取消': (MobileBy.IOS_PREDICATE, 'name=="取消"'),
        '多方通话_搜索_文本框': (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="密友圈"]/XCUIElement'
                                        'TypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElement'
                                        'TypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElement'
                                        'TypeOther[1]/XCUIElementTypeOther/XCUIElementTypeTextField'),
        '多方通话_电话号码': (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="密友圈"]/XCUIElement'
                                      'TypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElement'
                                      'TypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElement'
                                      'TypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell'),
        '多方通话_搜索_电话号码列表1': (MobileBy.XPATH,
                            '//XCUIElementTypeNavigationBar[@name="多方电话"]/following-sibling::*[1]'
                            '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]'
                            '/XCUIElementTypeTable/XCUIElementTypeCell[1]'),

        # 多方通话被叫
        '多方通话_是否确定结束多方电话': (MobileBy.IOS_PREDICATE, "name=='是否确定结束多方电话？'"),
        '多方通话_弹框_确定': (MobileBy.IOS_PREDICATE, "name=='确定'"),
        '多方通话_弹框_取消': (MobileBy.IOS_PREDICATE, "name=='取消'"),

        # 多方视频主叫
        '多方视频_免提': (MobileBy.IOS_PREDICATE, 'name=="免提"'),
        '多方视频_静音': (MobileBy.IOS_PREDICATE, 'name=="静音"'),
        '多方视频_关闭摄像头': (MobileBy.IOS_PREDICATE, 'name=="关闭摄像头"'),
        '多方视频_打开摄像头': (MobileBy.IOS_PREDICATE, 'name=="打开摄像头"'),
        '多方视频_翻转摄像头': (MobileBy.IOS_PREDICATE, 'name=="翻转摄像头"'),
        '多方视频_返回通话': (MobileBy.IOS_PREDICATE, 'name=="点击返回通话"'),
        '多方视频_被_邀请你进行多方视频': (MobileBy.IOS_PREDICATE, 'name=="邀请你进行多方视频"'),
        '多方视频_通话结束': (MobileBy.IOS_PREDICATE, 'name=="通话结束"'),
        '多方视频_可用时长': (MobileBy.IOS_PREDICATE, 'name contains "多方电话可用时长"'),
        '多方视频_缩放': (MobileBy.IOS_PREDICATE, 'name contains "my video zoom"'),
        '多方视频_增加成员': (MobileBy.IOS_PREDICATE, 'name contains "my video addmy"'),
        '多方视频_挂断': (MobileBy.IOS_PREDICATE, 'name contains "call dial key reject"'),
        '多方视频_接听': (MobileBy.IOS_PREDICATE, 'name contains "call dial key answer"'),

        # 弹出框
        '无密友圈_提示文本': (MobileBy.XPATH, '//XCUIElementTypeOther[@name="无密友圈"]'),
        '无密友圈_确定': (MobileBy.IOS_PREDICATE, "name=='确定'"),
        '无密友圈_取消': (MobileBy.IOS_PREDICATE, "name=='取消'"),

        # 飞信电话
        '飞信电话_我知道了': (MobileBy.IOS_PREDICATE, 'name=="我知道了"'),
        '飞信电话_接受': (MobileBy.IOS_PREDICATE, 'name=="接受"'),
        '飞信电话_拒绝': (MobileBy.IOS_PREDICATE, 'name=="拒绝"'),
        '飞信电话_挂断': (MobileBy.IOS_PREDICATE, 'name=="call dial key reject"'),
        '飞信电话_结束通话': (MobileBy.IOS_PREDICATE, 'name contains "结束通话"'),

        # 邀请 短信发送
        "邀请_短信发送": (MobileBy.IOS_PREDICATE, 'name=="sendButton"'),

    }

    def wait_for_page_load(self, timeout=8, auto_accept_alerts=True):
        """默认使用activity作为判断页面是否加载的条件，继承类应该重写该方法"""
        self.click_upgrade_close()
        # 通话
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
        self.click_upgrade_close()
        el = self.get_elements(self.__locators['拨号键盘'])
        if len(el) > 0:
            return True
        return False

    @TestLogger.log("点击locators对应的元素")
    def click_locator_key(self, locator):
        self.click_element(self.__locators[locator])

    @TestLogger.log("通话页面点击删除按钮")
    def click_delete_key(self, text):
        locator = (
            MobileBy.XPATH,
            "//*[contains(@name,'%s')]/../XCUIElementTypeOther/XCUIElementTypeButton[@name='删除']" % text)
        self.click_element(locator)

    @TestLogger.log("通话页面点击删除按钮，删除所有")
    def click_delete_all_key(self):
        time.sleep(1)
        try:
            while self.is_element_already_exist("通话_第一个联系人"):
                # time.sleep(1)
                self.swipe_by_direction(self.__locators["通话_第一个联系人"], "left")
                time.sleep(2)
                del_locator = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="删除"]')
                self.click_element(del_locator)
                time.sleep(2)
            # 检查当前页面
            time.sleep(1)
        except Exception:
            traceback.print_exc()
        if self.is_element_already_exist('通话_通话_TAB'):
            return True
        else:
            return False

    @TestLogger.log("通话页面点击删除按钮，删除所有")
    def clear_all_records(self):
        del_locator = (MobileBy.NAME, '删除')
        time.sleep(2)
        els = self.get_elements(self.__locators['通话_通话记录列表'])
        for el in els:
            self.swipe_by_direction_element(el, "left")
            time.sleep(0.5)
            self.click_element(del_locator)
            time.sleep(0.5)
        # 检查当前页面
        time.sleep(1)
        if self.is_element_already_exist(self.__locators['通话_通话_TAB']):
            return True
        else:
            return False

    def swipe_by_direction_element(self, locator, direction, duration=0.5, locator2=None):
        """
        在元素内滑动
        :param locator: 定位器
        :param direction: 方向（left,right,up,down）
        :param duration: 持续时间ms
        :return:
        """
        element = self.mobile.get_element(self.__locators[locator])
        rect = element.rect
        left, right = int(rect['x']) + 1, int(rect['x'] + rect['width']) - 1
        top, bottom = int(rect['y']) + 50, int(rect['y'] + rect['height']) - 1
        width = int(rect['width']) - 2
        height = int(rect['height']) - 2

        if self._get_platform() == 'android':
            if direction.lower() == 'left':
                x_start = right
                x_end = left
                y_start = (top + bottom) // 2
                y_end = (top + bottom) // 2
                self.driver.swipe(x_start, y_start, x_end, y_end, duration)
            elif direction.lower() == 'right':
                x_start = left
                x_end = right
                y_start = (top + bottom) // 2
                y_end = (top + bottom) // 2
                self.driver.swipe(x_start, y_start, x_end, y_end, duration)
            elif direction.lower() == 'up':
                x_start = (left + right) // 2
                x_end = (left + right) // 2
                y_start = bottom
                y_end = top
                self.driver.swipe(x_start, y_start, x_end, y_end, duration)
            elif direction.lower() == 'down':
                x_start = (left + right) // 2
                x_end = (left + right) // 2
                y_start = top
                y_end = bottom
                self.driver.swipe(x_start, y_start, x_end, y_end, duration)

        elif self._get_platform() == 'ios':
            if direction.lower() == 'left':
                x_start = right
                x_end = left
                y_start = (top + bottom) // 2
                y_end = (top + bottom) // 2
                self.driver.execute_script("mobile:dragFromToForDuration",
                                           {"duration": duration, "element": locator2, "fromX": x_start,
                                            "fromY": y_start,
                                            "toX": x_end, "toY": y_end})
            elif direction.lower() == 'right':
                x_start = left
                x_end = right
                y_start = (top + bottom) // 2
                y_end = (top + bottom) // 2
                self.driver.execute_script("mobile:dragFromToForDuration",
                                           {"duration": duration, "element": locator2, "fromX": x_start,
                                            "fromY": y_start,
                                            "toX": x_end, "toY": y_end})
            elif direction.lower() == 'up':
                x_start = (left + right) // 2
                x_end = (left + right) // 2
                y_start = bottom
                y_end = top
                self.driver.execute_script("mobile:dragFromToForDuration",
                                           {"duration": duration, "element": locator2, "fromX": x_start,
                                            "fromY": y_start,
                                            "toX": x_end, "toY": y_end})
            elif direction.lower() == 'down':
                x_start = (left + right) // 2
                x_end = (left + right) // 2
                y_start = top
                y_end = bottom
                self.driver.execute_script("mobile:dragFromToForDuration",
                                           {"duration": duration, "element": locator2, "fromX": x_start,
                                            "fromY": y_start,
                                            "toX": x_end, "toY": y_end})
            elif direction.lower() == 'press':
                x_start = (left + right) // 2
                x_end = (left + right) // 2
                y_start = (top + bottom) // 2
                y_end = (top + bottom) // 2
                self.driver.execute_script("mobile:dragFromToForDuration",
                                           {"duration": duration, "element": locator2, "fromX": x_start,
                                            "fromY": y_start,
                                            "toX": x_end, "toY": y_end})

        else:
            if direction.lower() == 'left':
                x_start = right
                x_offset = width
                y_start = (top + bottom) // 2
                y_offset = 0
                self.driver.swipe(x_start, y_start, x_offset, y_offset, duration)
            elif direction.lower() == 'right':
                x_start = left
                x_offset = width
                y_start = -(top + bottom) // 2
                y_offset = 0
                self.driver.swipe(x_start, y_start, x_offset, y_offset, duration)
            elif direction.lower() == 'up':
                x_start = (left + right) // 2
                x_offset = 0
                y_start = bottom
                y_offset = -height
                self.driver.swipe(x_start, y_start, x_offset, y_offset, duration)
            elif direction.lower() == 'down':
                x_start = (left + right) // 2
                x_offset = 0
                y_start = top
                y_offset = height
                self.driver.swipe(x_start, y_start, x_offset, y_offset, duration)

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
        time.sleep(0.5)
        elements_list = self.get_elements(self.__locators[text])
        time.sleep(1)
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

    @TestLogger.log('确保页面有点对点视频记录')
    def make_sure_have_p2p_vedio_record(self):
        if self.is_text_present('[视频通话]'):
            return True
        # self.point2point_vedio_call()
        # self.wait_until(
        #     condition=lambda d: self.is_text_present("[视频通话]"),
        #     timeout=10,
        # )
        return self.is_element_already_exist('[视频通话]')

    @TestLogger.log('确保页面有多方视频记录')
    def make_sure_have_multiplayer_vedio_record(self):
        if self.is_text_present('[多方视频]'):
            return True
        # self.multiplayer_vedio_call()
        # self.wait_until(
        #     condition=lambda d: self.is_text_present("[多方视频]"),
        #     timeout=10,
        # )
        return self.is_element_already_exist('[多方视频]')

    @TestLogger.log('确保页面有飞信电话记录')
    def make_sure_have_p2p_voicecall_record(self):
        if self.is_text_present('[飞信电话]'):
            return True
        # self.point2point_voice_call()
        # self.wait_until(
        #     condition=lambda d: self.is_text_present("飞信电话"),
        #     timeout=10,
        # )
        return self.is_element_already_exist('[飞信电话]')

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

    @TestLogger.log("判断页面元素是否存在")
    def is_element_exist(self, locator):
        try:
            el = self.get_elements(self.__locators[locator])
            if len(el) > 0:
                return True
            return False
        except:
            return False

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

    @TestLogger.log("没有元素时点击屏幕")
    def check_element_tap_screen(self, locator):
        if not self.is_element_already_exist(locator):
            self.click_screen_center()

    @TestLogger.log("视频通话结束弹出框")
    def click_video_hangup(self):
        """
        视频通话结束弹出框
        :return:
        """
        if self.is_element_already_exist('视频主叫_挂断'):
            self.click_locator_key('视频主叫_挂断')

    @TestLogger.log("视频通话接听")
    def click_video_answer(self):
        """
        视频通话接听
        :return:
        """
        # # iphone 7: xp=(appium x)/375, yp=(appium y)/667
        # x_percentage = 276 / 375 * 100
        # y_percentage = 578 / 667 * 100
        # self.click_coordinate(x_percentage, y_percentage)
        self.click_locator_key('视频接听_接听')

    @TestLogger.log("多方视频，多方电话通话主叫挂断")
    def click_close_more_video_popup(self):
        """
        多方视频，多方电话通话主叫挂断
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
            time.sleep(0.5)
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
                time.sleep(0.5)
                els = self.get_elements((MobileBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[%s]' % (cell+1)))
                time.sleep(2)
                # 休眠等待节点生产
                els[0].click()
                time.sleep(4)
                # 向上滑动，百分比
                if cell > 0 and (0 == cell % 5):
                    x_source = 180 / 375 * 100
                    y_source = 380 / 667 * 100
                    x_target = 180 / 375 * 100
                    y_target = 180 / 667 * 100
                    self.swipe_by_percent_on_screen(x_source, y_source, x_target, y_target)
                    time.sleep(2)
            # 最多选择8个联系人
            if 8 < number:
                time.sleep(0.5)
                if self.is_element_present("视频呼叫_最多只能选择8个人"):
                    self.click_locator_key("视频呼叫_最多只能选择8个人")
                    time.sleep(0.5)
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
        return current_mobile().get_cards(card_type)[0]

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

    @TestLogger.log('拨打一个点对点视频通话')  # pass
    def pick_up_p2p_video(self, cards):
        self.click_locator_key('+')
        self.click_locator_key('视频通话')
        self.input_text(self.__locators['视频呼叫_搜索_文本框'], cards)
        time.sleep(1)
        self.get_elements(self.__locators['视频呼叫_搜索_号码列表'])[0].click()
        time.sleep(1)
        self.click_locator_key('视频呼叫_确定')
        time.sleep(0.5)
        if self.on_this_page_common('无密友圈_确定'):
            self.click_locator_key('无密友圈_取消')

    @TestLogger.log('拨打一个点对点视频通话')
    def pick_up_multi_video(self, cards):
        self.click_locator_key('+')
        self.click_locator_key('视频通话')
        self.input_text(self.__locators['视频呼叫_搜索_文本框'], cards)
        time.sleep(1)
        self.get_elements(self.__locators['视频呼叫_搜索_号码列表'])[0].click()
        time.sleep(1)
        self.input_text(self.__locators['视频呼叫_搜索_文本框'], '13800138000')
        time.sleep(1)
        self.get_elements(self.__locators['视频呼叫_搜索_号码列表'])[0].click()
        time.sleep(1)
        self.click_locator_key('视频呼叫_确定')
        time.sleep(0.5)

    @TestLogger.log("长按操作")
    def long_press_number(self, text, default_time=3):
        """长按"""
        try:
            self.swipe_by_direction(self.__class__.__locators[text], 'press', default_time)
        except:
            print('长按异常，正常执行')
            pass

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
    def test_call_video(self, cards='14775451723'):
        """
        添加视频通话记录
        :return:
        """
        # 初始化数据
        time.sleep(0.5)
        try:
            if not self.is_text_present("[视频通话]"):
                self.click_locator_key('+')
                time.sleep(0.5)
                self.click_call('视频通话')
                self.input_locator_text('视频呼叫_搜索_文本框', cards)
                self.get_elements(self.__locators['视频呼叫_搜索_号码列表'])[0].click()
                time.sleep(0.5)
                self.click_locator_key('视频呼叫_确定')
                time.sleep(1)
                self.click_video_hangup()
                time.sleep(2)
        finally:
            if self.is_element_present("无密友圈_取消"):
                self.click_locator_key('无密友圈_取消')
                time.sleep(0.5)

    @TestLogger.log('添加未注册视频通话记录')
    def test_call_video_no(self, cards='13800'):
        """添加未注册视频通话记录"""
        # 初始化数据
        time.sleep(0.5)
        try:
            self.click_locator_key('+')
            time.sleep(0.5)
            self.click_call('视频通话')
            self.input_locator_text('视频呼叫_搜索_文本框', cards)
            self.get_elements(self.__locators['视频呼叫_搜索_号码列表'])[0].click()
            time.sleep(0.5)
            self.click_locator_key('视频呼叫_确定')
            time.sleep(1)
            self.click_video_hangup()
            time.sleep(2)
        finally:
            if self.is_element_present("无密友圈_取消"):
                self.click_locator_key('无密友圈_取消')
                time.sleep(0.5)

    @TestLogger.log('添加多方视频记录')
    def test_call_more_video(self):
        """
        添加多方视频记录
        :return:
        """
        # 初始化数据
        time.sleep(0.5)
        if not self.is_text_present("[多方视频]"):
            self.click_locator_key('+')
            time.sleep(1)
            self.click_call('视频通话')
            self.select_contact_n(2)
            time.sleep(1)
            self.click_locator_key('视频呼叫_确定')
            time.sleep(3)
            self.click_close_more_video_popup()
            time.sleep(2)
            if self.is_element_present("无密友圈_取消"):
                self.click_locator_key('无密友圈_取消')
                time.sleep(0.5)

    @TestLogger.log('添加飞信电话记录')
    def test_call_phone_condition(self):
        """
        添加飞信电话记录
        :return:
        """
        # 初始化数据
        if not self.is_text_present("[飞信电话]"):
            self.click_keyboard()
            time.sleep(0.5)
            cards = "12560"
            for i in cards:
                self.click_locator_key('keyboard_{}'.format(i))
            try:
                self.click_locator_key('拨号_呼叫')
                time.sleep(1)
                self.click_locator_key('飞信电话_我知道了')
            finally:
                # 睡眠等待弹框切换
                time.sleep(6)
                self.test_close_my_phone_calling()

    @TestLogger.log('关闭飞信电话')
    def test_close_my_phone_calling(self):
        """关闭飞信电话 """
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
        self.click_close_more_video_popup()
        time.sleep(2)

    @TestLogger.log('添加飞信电话记录，没有注册')
    def test_call_phone_no_reg(self):
        """
        添加飞信电话记录
        :return:
        """
        # 初始化数据
        time.sleep(1)
        self.click_keyboard()
        time.sleep(1)
        cards = "186000010"
        for i in cards:
            self.click_locator_key('keyboard_{}'.format(i))
        time.sleep(0.5)
        self.click_locator_key('拨号_呼叫')
        time.sleep(3)
        self.click_locator_key('飞信电话_我知道了')
        time.sleep(0.5)

    @TestLogger.log('添加多方电话记录')
    def test_call_more_phone_condition(self):
        """
        添加多方视频记录
        :return:
        """
        # 初始化数据
        time.sleep(0.5)
        if not self.is_text_present("[多方电话]"):
            self.click_locator_key('+')
            time.sleep(0.5)
            self.click_call('多方电话')
            self.select_contact_n(1)
            time.sleep(1)
            self.click_locator_key('视频呼叫_确定')
            time.sleep(2)
            self.click_locator_key('飞信电话_我知道了')
            # 包括飞信电话
            time.sleep(5)
            try:
                if self.is_element_already_exist('飞信电话_拒绝'):
                    self.click_locator_key('飞信电话_拒绝')
                    time.sleep(0.5)
            except:
                pass
            # 结束通话
            try:
                self.click_close_more_video_popup()
                time.sleep(1.5)
                if self.is_element_already_exist('多方通话_是否确定结束多方电话'):
                    self.click_locator_key('多方通话_弹框_确定')
                    time.sleep(0.5)
            except:
                pass
            if self.is_element_present("无密友圈_取消"):
                self.click_locator_key('无密友圈_取消')
                time.sleep(0.5)

    @TestLogger.log('查找所有元素')
    def get_elements_list(self, locator):
        return self.get_elements(self.__locators[locator])

    @TestLogger.log('查找所有元素')
    def pick_up_p2p_voice_keep_time(self, cards):
        if self.is_element_already_exist('拨号键盘'):
            self.click_locator_key('拨号键盘')
            time.sleep(2)
        for i in cards:
            self.click_locator_key('keyboard_{}'.format(i))
        time.sleep(1)
        self.click_locator_key('拨号_呼叫')
        time.sleep(1)
        self.click_locator_key('拨号_呼叫_呼叫')

    @TestLogger.log('判断按钮是否被选中')
    def check_if_button_selected(self, locator):
        """判断按钮是否被选中"""
        try:
            el = self.get_element(self.__locators[locator])
            if el.text == '1':
                return True
            else:
                return False
        except Exception:
            return False

    def swipe_to_direction(self, locator, direction, duration=0.5, locator2=None):
        """
        在元素内滑动
        :param locator: 定位器
        :param direction: 方向（left,right）
        :param duration: 持续时间ms
        :return:
        """
        element = self.get_element(self.__locators[locator])
        rect = element.rect
        left, right = int(rect['x']) + 1, int(rect['x'] + rect['width']) - 1
        top, bottom = int(rect['y']) + 1, int(rect['y'] + rect['height']) - 1
        width = int(rect['width']) - 2
        # height = int(rect['height']) - 2
        value = int(element.text.replace('%', '')) / 100

        if direction.lower() == 'left':
            x_start = width * value + left
            x_end = left
            y_start = (top + bottom) // 2
            y_end = (top + bottom) // 2
            self.driver.execute_script("mobile:dragFromToForDuration",
                                       {"duration": duration, "element": locator2, "fromX": x_start,
                                        "fromY": y_start,
                                        "toX": x_end, "toY": y_end})
        elif direction.lower() == 'right':
            x_start = width * value + left
            x_end = width + left
            y_start = (top + bottom) // 2
            y_end = (top + bottom) // 2
            self.driver.execute_script("mobile:dragFromToForDuration",
                                       {"duration": duration, "element": locator2, "fromX": x_start,
                                        "fromY": y_start,
                                        "toX": x_end, "toY": y_end})

    @TestLogger.log('拨打点对点多方电话')
    def pick_up_multi_voice_call(self, cards):
        time.sleep(1)
        self.click_locator_key('+')
        self.click_locator_key('多方电话')
        self.input_text(self.__locators['多方通话_搜索_文本框'], cards)
        time.sleep(1)
        self.get_elements(self.__locators['多方通话_电话号码'])[0].click()
        time.sleep(1)
        self.click_locator_key('多方通话_确定')
        time.sleep(0.5)
        if self.is_text_present('我知道了'):
            self.click_text('我知道了')

    @TestLogger.log('获取多方电话可用时长')
    def get_times(self):
        self.click_locator_key('+')
        self.click_locator_key('多方电话')
        time.sleep(2)
        text = self.get_element(self.__locators['多方视频_可用时长']).text
        self.click_locator_key('多方通话_取消')
        import re
        return int(re.sub(r'\D', "", text))

    @TestLogger.log('获取多方电话可用时长')
    def click_first_record(self):
        locator = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="密友圈"]/XCUIElement'
                                   'TypeWindow[1]/XCUIElementTypeOther/XCUIElement'
                                   'TypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElement'
                                   'TypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementType'
                                   'Table/XCUIElementTypeCell[1]')
        self.get_elements(locator)[0].click()
