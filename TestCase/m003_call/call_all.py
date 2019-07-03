import time
import warnings
import datetime
import traceback

from selenium.common.exceptions import TimeoutException

from pages.guide import GuidePage
from pages.login.OneKeyLogin import OneKeyLoginPage
from pages.call.Call import CallPage

from library.core.TestCase import TestCase
from library.core.utils.applicationcache import current_mobile, current_driver, switch_to_mobile
from library.core.utils.testcasefilter import tags
from library.core.common.simcardtype import CardType
from library.core.TestLogger import TestLogger


REQUIRED_MOBILES = {
    'Android-移动-N': 'M960BDQN229CH',
    'Android-移动': 'M960BDQN229CH_NOVA',
    'IOS-移动': 'iphone',
    'IOS-移动-移动': 'iphone_d',
    'Android-电信': 'single_telecom',
    'Android-联通': 'single_union',
    'Android-移动-联通': 'mobile_and_union',
    'Android-移动-电信': '',
    'Android-移动-移动': 'double_mobile',
    'Android-XX-XX': 'others_double',
}


class Preconditions(object):
    """
    分解前置条件
    """

    @staticmethod
    def select_single_cmcc_android_4g_client():
        """
        启动
        1、4G，安卓客户端
        2、移动卡
        :return:
        """
        client = switch_to_mobile(REQUIRED_MOBILES['测试机'])
        client.connect_mobile()

    @staticmethod
    def select_mobile(category):
        """选择手机手机"""
        client = switch_to_mobile(REQUIRED_MOBILES[category])
        client.connect_mobile()
        return client

    @staticmethod
    def select_assisted_mobile2():
        """切换到单卡、异网卡Android手机 并启动应用"""
        switch_to_mobile(REQUIRED_MOBILES['辅助机2'])
        current_mobile().connect_mobile()

    @staticmethod
    def make_already_in_one_key_login_page():
        """
        1、已经进入一键登录页
        :return:
        """
        # 如果当前页面已经是一键登录页，不做任何操作
        one_key = OneKeyLoginPage()
        if one_key.is_on_this_page():
            return
        # 如果当前页不是引导页第一页，重新启动app
        guide_page = GuidePage()
        if not guide_page.is_on_the_first_guide_page():
            current_mobile().launch_app()
            guide_page.wait_for_page_load(20)

        # 跳过引导页
        guide_page.wait_for_page_load(30)
        guide_page.swipe_to_the_second_banner()
        guide_page.swipe_to_the_third_banner()
        guide_page.click_start_the_experience()
        guide_page.click_start_the_one_key()
        time.sleep(2)
        guide_page.click_always_allow()
        one_key.wait_for_page_load(30)

    @staticmethod
    def login_by_one_key_login():
        """
        从一键登录页面登录
        :return:
        """
        # 等待号码加载完成后，点击一键登录
        one_key = OneKeyLoginPage()
        one_key.wait_for_page_load()
        # one_key.wait_for_tell_number_load(60)
        one_key.click_one_key_login()
        time.sleep(2)
        if one_key.is_text_present('用户协议和隐私保护'):
            one_key.click_agree_user_aggrement()
            time.sleep(1)
            one_key.click_agree_login_by_number()

        # 等待通话页面加载
        call_page = CallPage()
        call_page.wait_for_page_call_load()
        call_page.click_always_allow()
        time.sleep(2)
        call_page.remove_mask()

    @staticmethod
    def app_start_for_the_first_time():
        """首次启动APP（使用重置APP代替）"""
        current_mobile().reset_app()

    @staticmethod
    def terminate_app():
        """
        强制关闭app,退出后台
        :return:
        """
        app_id = current_driver().capabilities['appPackage']
        current_mobile().terminate_app(app_id)

    @staticmethod
    def background_app(seconds):
        """后台运行"""
        current_mobile().background_app(seconds)

    @staticmethod
    def reset_and_relaunch_app():
        """首次启动APP（使用重置APP代替）"""
        app_package = 'com.cmic.college'
        current_driver().activate_app(app_package)
        current_mobile().reset_app()

    @staticmethod
    def make_already_in_call_page():
        """
        前置条件：
        1.已登录客户端
        2.当前在消息页面
        """
        # 如果当前页面是在通话录页，不做任何操作
        call_page = CallPage()
        if call_page.is_on_this_page():
            return
        # 如果当前页面已经是一键登录页，进行一键登录页面
        one_key = OneKeyLoginPage()
        if one_key.is_on_this_page():
            Preconditions.login_by_one_key_login()
        # 如果当前页不是引导页第一页，重新启动app
        else:
            try:
                current_mobile().terminate_app('com.cmic.college', timeout=2000)
            except:
                pass
            current_mobile().launch_app()
            try:
                call_page.wait_until(
                    condition=lambda d: call_page.is_on_this_page(),
                    timeout=3
                )
                return
            except TimeoutException:
                pass
            Preconditions.reset_and_relaunch_app()
            Preconditions.make_already_in_one_key_login_page()
            Preconditions.login_by_one_key_login()

    @staticmethod
    def make_sure_in_after_login_callpage():
        Preconditions.make_already_in_call_page()
        current_mobile().wait_until_not(condition=lambda d: current_mobile().is_text_present('正在登录...'), timeout=20)

    @staticmethod
    def get_current_activity_name():
        import os, sys
        global findExec
        findExec = 'findstr' if sys.platform == 'win32' else 'grep'
        device_name = current_driver().capabilities['deviceName']
        cmd = 'adb -s %s shell dumpsys window | %s mCurrentFocus' % (device_name, findExec)
        res = os.popen(cmd)
        time.sleep(2)
        # 截取出activity名称 == ''为第三方软件
        current_activity = res.read().split('u0 ')[-1].split('/')[0]
        res.close()
        return current_activity

    @staticmethod
    def initialize_class(moudel):
        """确保每个用例开始之前在通话界面界面"""
        warnings.simplefilter('ignore', ResourceWarning)
        Preconditions.select_mobile(moudel)
        Preconditions.make_sure_in_after_login_callpage()

    @staticmethod
    def disconnect_mobile(category):
        """断开手机连接"""
        client = switch_to_mobile(REQUIRED_MOBILES[category])
        client.disconnect_mobile()
        return client


class CallPageTest(TestCase):
    """Call 模块--全量"""

    def default_setUp(self):
        """确保每个用例开始之前在通话界面界面"""
        Preconditions.initialize_class('IOS-移动')

    def default_tearDown(self):
        Preconditions.disconnect_mobile('IOS-移动')

    @tags('ALL', 'CMCC', 'call')
    def test_call_0001(self):
        """通话界面显示"""
        time.sleep(2)
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.page_contain_element('通话文案')
        call.page_contain_element('拨号键盘')
        if call.is_element_present('来电名称'):
            call.page_contain_element('来电名称')
        else:
            call.page_should_contain_text('打电话不花钱')

    @tags('ALL', 'CMCC', 'call')
    def test_call_0002(self):
        """通话界面显示"""
        time.sleep(2)
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.page_contain_element('通话文案')
        call.page_contain_element('拨号键盘')
        if call.is_element_present('来电名称'):
            call.page_contain_element('来电名称')
        else:
            call.page_should_contain_text('打电话不花钱')

    @tags('ALL', 'CMCC', 'call')
    def test_call_0003(self):
        """通话界面-拨号键盘显示"""
        time.sleep(2)
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.page_contain_element('拨号键盘')
        if call.is_element_present('来电名称'):
            call.page_contain_element('来电名称')
        else:
            call.page_should_contain_text('打电话不花钱')
        # 点击键盘
        call.click_keyboard()
        time.sleep(5)

        # 文本框输入'123'
        text = '123'
        call.click_keyboard_call('keyboard_1')
        time.sleep(2)
        call.click_keyboard_call('keyboard_2')
        time.sleep(2)
        call.click_keyboard_call('keyboard_3')
        time.sleep(2)
        number = call.get_input_box_text()
        self.assertEqual(text == number, True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_0004(self):
        """通话界面-拨号盘收起"""
        time.sleep(2)
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.page_contain_element('拨号键盘')
        if call.is_element_present('来电名称'):
            call.page_contain_element('来电名称')
        else:
            call.page_should_contain_text('打电话不花钱')
        # 点击键盘
        call.click_keyboard()
        time.sleep(2)
        call.is_keyboard_shown()
        # 再次点击拨号盘
        call.click_hide_keyboard()
        time.sleep(2)
        call.page_contain_element('拨号键盘')

    @tags('ALL', 'CMCC', 'call')
    def test_call_0005(self):
        """通话界面-点击视频通话"""
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.click_locator_key('+')
        time.sleep(2)
        call.is_element_present('视频通话')
        call.is_element_present('多方电话')
        time.sleep(2)
        call.click_call('视频通话')
        time.sleep(2)
        # 视频通话页面
        call.is_element_present('视频通话')

    @tags('ALL', 'CMCC', 'call')
    def test_call_0006(self):
        """展开拨号盘，不可以左右滑动切换tab，上方内容显示通话模块通话记录内容"""
        time.sleep(2)
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        # 向左滑动
        time.sleep(1)
        x_source = 50 / 375 * 100
        y_source = 80 / 667 * 100
        x_target = 50 / 375 * 100
        y_target = 30 / 667 * 100
        call.swipe_by_percent_on_screen(x_source, y_source, x_target, y_target)
        # 判断滑动后是否还在此页面
        time.sleep(3)
        self.assertEqual(call.is_element_already_exist('拨号键盘'), True)
        # 判断如果键盘是拉起的，则不需要再次拉起
        time.sleep(1)
        if call.is_on_this_page():
            time.sleep(1)
            call.click_show_keyboard()
        # 向右滑动
        time.sleep(1)
        x_source = 90 / 375 * 100
        y_source = 50 / 667 * 100
        x_target = 20 / 375 * 100
        y_target = 50 / 667 * 100
        call.swipe_by_percent_on_screen(x_source, y_source, x_target, y_target)
        # 判断滑动后是否还在此页面
        time.sleep(2)
        self.assertEqual(call.is_element_already_exist('拨号键盘'), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_0007(self):
        """跳出下拉框，可选择视频通话与多方电话"""
        time.sleep(2)
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        # 判断如果键盘已拉起，则收起键盘
        if call.is_exist_call_key():
            call.click_hide_keyboard()
            time.sleep(1)
        # 点击加号
        call.click_locator_key('+')
        time.sleep(2)
        # 判断是否有视频通话与多方电话
        self.assertEqual(call.is_element_present('视频通话'), True)
        self.assertEqual(call.is_element_present('多方电话'), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_0008(self):
        """打开视频通话界面-联系人选择器页面（该页面逻辑与现网保持一致）"""
        time.sleep(2)
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        # 点击加号
        call.click_locator_key('+')
        time.sleep(2)
        call.click_locator_key('视频通话')
        time.sleep(2)
        self.assertEqual(call.check_text_exist('视频通话'), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_0009(self):
        """打开多方电话-联系人选择器页面（该页面逻辑与现网保持一致）"""
        time.sleep(2)
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        # 点击加号
        call.click_locator_key('+')
        time.sleep(2)
        call.click_locator_key('多方电话')
        time.sleep(2)
        self.assertEqual(call.check_text_exist('多方电话'), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_00010(self):
        """
            跳转至通话详情页面中，页面布局左上方返回按钮，顶部展示联系人头像与名称，
            中部展示通话、视频通话，设置备注名，下方展示手机号码与号码归属地，通话记录（视频通话），
            显示通话类型、通话时长，通话时间点
        """
        time.sleep(2)
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        # 判断是否有通话记录
        call.test_call_video_condition()
        time.sleep(5)
        # 判断如果键盘已拉起，则收起键盘
        if call.is_exist_call_key():
            call.click_hide_keyboard()
            time.sleep(1)
        # 视频通话
        call.make_sure_have_p2p_vedio_record()
        time.sleep(3)
        # 通话列表筛选"[视频通话]"
        call.click_tag_detail_first_element('[视频通话]')
        # 判断参数校验
        time.sleep(2)
        self.assertEqual(call.on_this_page_call_detail(), True)
        self.assertEqual(call.check_vedio_call_detail_page(), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_00011(self):
        """
            跳转至多方视频详情页面中，页面布局左上方返回按钮，右边为多方视频文字，下方为：
            发起多方视频按钮栏，展示联系人头像与名称，通话记录（多方视频），
            显示通话类型、通话时长，通话时间点
        """
        time.sleep(2)
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        # 判断是否有通话记录
        call.test_call_more_video_condition()
        # 判断如果键盘已拉起，则收起键盘
        if call.is_exist_call_key():
            call.click_hide_keyboard()
            time.sleep(1)
        call.make_sure_have_multiplayer_vedio_record()
        time.sleep(2)
        call.click_tag_detail_first_element('[多方视频]')
        # 判断
        time.sleep(1)
        # 是否在多方视频详情页面
        self.assertEqual(call.on_this_page_multi_video_detail(), True)
        self.assertEqual(call.check_multiplayer_vedio_detail_page(), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_00012(self):
        """
            跳转至通话详情页面中，返回到通话记录列表页面
        """
        time.sleep(2)
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        # 判断是否有通话记录
        call.test_call_more_phone_condition()
        # 判断如果键盘已拉起，则收起键盘
        if call.is_exist_call_key():
            call.click_hide_keyboard()
            time.sleep(1)
        call.click_tag_detail_first_element('[飞信电话]')
        time.sleep(1)
        self.assertEqual(call.on_this_page_call_detail(), True)
        # 单击左上角返回按钮
        call.click_detail_back()
        call.wait_for_page_load()
        self.assertEqual(call.is_on_this_page(), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_00013(self):
        """
            验证通话记录详情页-编辑备注名---正确输入并点击保存（中文、英文、特殊符号）---保存成功
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        # 判断是否有通话记录
        call.test_call_more_phone_condition()
        # 判断如果键盘已拉起，则收起键盘
        if call.is_exist_call_key():
            call.click_hide_keyboard()
            time.sleep(1)
        # 获取当前页面
        call.make_sure_have_p2p_voicecall_record()
        call.click_tag_detail_first_element('[飞信电话]')
        time.sleep(1)
        self.assertEqual(call.on_this_page_call_detail(), True)
        # 1. 修改为中文
        time.sleep(2)
        name = '测试中文备注'
        self.assertEqual(call.check_modify_nickname(name), True)
        # 2. 修改为全英文
        time.sleep(2)
        name = 'testEnglishNickname'
        self.assertEqual(call.check_modify_nickname(name), True)
        # 3. 修改为特殊字符，ios输入限制"&"
        time.sleep(2)
        name = '汉字English%^&*()_!@#'
        self.assertEqual(call.check_modify_nickname(name), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_00014(self):
        """
            超长的字符不显示
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        # 判断是否有通话记录
        call.test_call_more_phone_condition()
        # 判断如果键盘已拉起，则收起键盘
        if call.is_exist_call_key():
            call.click_hide_keyboard()
            time.sleep(1)
        call.make_sure_have_p2p_voicecall_record()
        call.click_tag_detail_first_element('[飞信电话]')
        time.sleep(1)
        self.assertEqual(call.on_this_page_call_detail(), True)
        # 1. 修改为中文
        time.sleep(1)
        name = '测试超长字符TestTooLong@#$%^&%$^&^$&**&^%'
        call.check_modify_nickname(name)
        time.sleep(2)
        word_length = len(name)
        word_utf_8 = len(name.encode('utf-8'))
        size = int((word_utf_8 - word_length) / 2 + word_length)
        self.assertEqual(size > 0, False)
        self.assertEqual(name != call.get_nickname(), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_00015(self):
        """保存后用户名称用回服务器返回的名称"""
        call = CallPage()
        call.wait_for_page_load()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        # 判断是否有通话记录
        call.test_call_more_phone_condition()
        # 判断如果键盘已拉起，则收起键盘
        if call.is_exist_call_key():
            call.click_hide_keyboard()
            time.sleep(1)
        call.make_sure_have_p2p_voicecall_record()
        call.click_tag_detail_first_element('[飞信电话]')
        time.sleep(1)
        self.assertEqual(call.on_this_page_call_detail(), True)
        # 1. 修改为中文，空格" "修改为""
        name = ' '
        self.assertEqual(call.check_modify_nickname(name), False)

    @tags('ALL', 'CMCC', 'call')
    def test_call_00016(self):
        """
            验证通话记录详情页-编辑备注名---输入sql语句并点击保存---保存成功
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        # 判断是否有通话记录
        call.test_call_video_condition()
        # 判断如果键盘已拉起，则收起键盘
        if call.is_exist_call_key():
            call.click_hide_keyboard()
            time.sleep(1)
        call.make_sure_have_p2p_vedio_record()
        call.click_tag_detail_first_element('[视频通话]')
        time.sleep(1)
        self.assertEqual(call.on_this_page_call_detail(), True)
        # 1. 修改为中文
        time.sleep(1)
        name = 'select now()'
        self.assertEqual(call.check_modify_nickname(name), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_00017(self):
        """
            验证通话记录详情页-编辑备注名---输入html标签并点击保存---保存成功
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        # 判断是否有通话记录
        call.test_call_video_condition()
        # 判断如果键盘已拉起，则收起键盘
        if call.is_exist_call_key():
            call.click_hide_keyboard()
            time.sleep(1)
        call.make_sure_have_p2p_vedio_record()
        call.click_tag_detail_first_element('[视频通话]')
        time.sleep(1)
        self.assertEqual(call.on_this_page_call_detail(), True)
        # 1. 修改为中文, ios不支持"<",">"
        time.sleep(1)
        name = '<a href="www.baidu.com"/>a<a/>'
        self.assertEqual(call.check_modify_nickname(name), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_00019(self):
        """
            1、联网正常已登录
            2、对方离线
            3、当前页通话记录详情
            1、点击视频通话---1、进入拨打视频通话界面，并弹出提示窗，“对方未接听，请稍候再尝试”
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        # 判断是否有通话记录
        call.test_call_video_condition()
        # 判断如果键盘已拉起，则收起键盘
        if call.is_exist_call_key():
            call.click_hide_keyboard()
            time.sleep(1)
        call.make_sure_have_p2p_vedio_record()
        call.click_tag_detail_first_element('[视频通话]')
        time.sleep(1)
        self.assertEqual(call.on_this_page_call_detail(), True)
        # 1. 点击视频通话按钮
        call.click_locator_key('详情_视频按钮')
        # time.sleep(1)
        # if call.on_this_page_flow():
        #     call.set_not_reminders()
        #     time.sleep(1)
        #     call.click_locator_key('流量_继续拨打')
        time.sleep(20)
        count = 30
        while count > 0:
            exist = call.is_text_present('对方不在线，暂时无法接听，请稍后重试。')
            if exist:
                break
            time.sleep(0.3)
            count -= 1
        else:
            self.assertEqual("测试等待时间异常。", True)

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00020(self):
        """
            1、联网正常已登录
            2、对方离线
            3、当前页通话记录详情
            点击视频通话---点击取消---进入拨打视频通话界面，并弹出提示窗，“通话结束”---返回通话记录详情页
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        try:
            call.wait_for_page_load()
            # 判断如果键盘已拉起，则收起键盘
            if call.is_exist_call_key():
                call.click_hide_keyboard()
                time.sleep(1)
            # 被叫手机初始化
            Preconditions.initialize_class('IOS-移动-移动')
            # 被叫手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 切换主叫手机
            time.sleep(0.5)
            Preconditions.select_mobile('IOS-移动')
            # 主叫拨打视频电话, 添加通话记录
            call.pick_up_p2p_video(cards)
            time.sleep(3)
            call.click_conversation_popup()
            if call.on_this_page_common('无密友圈_确定'):
                call.click_locator_key('无密友圈_取消')
            # 点击第一条，跳转到详情页面
            time.sleep(2)
            call.click_tag_detail_first_element('[视频通话]')
            time.sleep(1)
            self.assertEqual(call.on_this_page_call_detail(), True)
            # 1. 点击视频通话按钮
            call.click_locator_key('详情_视频按钮')
            time.sleep(1)
            # if call.on_this_page_flow():
            #     call.set_not_reminders()
            #     time.sleep(1)
            #     call.click_locator_key('流量_继续拨打')
            time.sleep(3)
            call.click_conversation_popup()
            if call.on_this_page_common('无密友圈_确定'):
                call.click_locator_key('无密友圈_取消')
            time.sleep(3)
            self.assertEqual(call.on_this_page_call_detail(), True)
        finally:
            # 切换被叫手机
            Preconditions.select_mobile('IOS-移动-移动')
            time.sleep(2)
            Preconditions.disconnect_mobile('IOS-移动-移动')
            # call.set_network_status(0)

    @tags('ALL', 'CMCC', 'call')
    def test_call_00023(self):
        """
            1、联网正常已登录
            2、对方未注册
            3、当前页通话记录详情
            点击视频通话---点击取消---"1、进入拨打视频电话界面，并弹出提示窗--下方是“取消” 和“确定”按钮--返回通话记录详情页"
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        # 判断是否有通话记录
        call.test_call_video_condition()
        # 判断如果键盘已拉起，则收起键盘
        if call.is_exist_call_key():
            call.click_hide_keyboard()
            time.sleep(1)
        call.make_sure_have_p2p_vedio_record()
        call.click_tag_detail_first_element('[视频通话]')
        time.sleep(2)
        self.assertEqual(call.on_this_page_call_detail(), True)
        # 1. 点击视频通话按钮
        call.click_locator_key('详情_视频按钮')
        # time.sleep(1)
        # if call.on_this_page_flow():
        #     call.set_not_reminders()
        #     time.sleep(1)
        #     call.click_locator_key('流量_继续拨打')
        # 点击结束通话
        time.sleep(1)
        call.click_conversation_popup()
        # 无密友圈, 点击取消按钮
        if call.is_element_present("无密友圈_取消"):
            call.click_cancel_popup()
        time.sleep(3)
        self.assertEqual(call.on_this_page_call_detail(), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_00025(self):
        """
            1、联网正常已登录
            2、对方未注册
            3、当前页通话记录详情
            "1、进入拨打视频通话界面，并弹出提示窗，
            下方是“取消” 和“确定”按钮
            2、调起系统短信界面，复制文案到短信编辑器，文案如下：
            我在使用联系人圈，视频通话免流量哦，你也赶紧来使用吧，下载地址：feixin.10086.cn/miyou
            3、发送成功，接收方收到短信"

        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        # 判断是否有通话记录
        call.test_call_video_condition()
        # 判断如果键盘已拉起，则收起键盘
        if call.is_exist_call_key():
            call.click_hide_keyboard()
            time.sleep(1)
        call.make_sure_have_p2p_vedio_record()
        call.click_tag_detail_first_element('[视频通话]')
        time.sleep(2)
        self.assertEqual(call.on_this_page_call_detail(), True)
        # 1. 点击视频通话按钮
        call.click_locator_key('详情_视频按钮')
        # time.sleep(1)
        # if call.on_this_page_flow():
        #     call.set_not_reminders()
        #     time.sleep(1)
        #     call.click_locator_key('流量_继续拨打')
        # 对方没有使用密友圈。
        time.sleep(5)
        if call.is_element_present("无密友圈_确定"):
            call.click_ok_popup()
        else:
            raise RuntimeError("页面元素验证异常")

    @tags('ALL', 'CMCC', 'call')
    def test_call_00026(self):
        """
            1、联网正常已登录
            2、对方未注册
            3、当前页通话记录详情
            点击视频通话---点击取消---"1、进入拨打视频电话界面，并弹出提示窗--下方是“取消” 和“确定”按钮--返回通话记录详情页"
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        # 判断是否有通话记录
        call.test_call_video_condition()
        # 判断如果键盘已拉起，则收起键盘
        if call.is_exist_call_key():
            call.click_hide_keyboard()
            time.sleep(1)
        call.make_sure_have_p2p_vedio_record()
        call.click_tag_detail_first_element('[视频通话]')
        time.sleep(2)
        self.assertEqual(call.on_this_page_call_detail(), True)
        # 1. 点击视频通话按钮
        call.click_locator_key('详情_视频按钮')
        # time.sleep(1)
        # if call.on_this_page_flow():
        #     call.set_not_reminders()
        #     time.sleep(1)
        #     call.click_locator_key('流量_继续拨打')
        # 对方没有使用密友圈。
        time.sleep(5)
        if call.is_element_present("无密友圈_取消"):
            call.click_cancel_popup()
        time.sleep(3)
        self.assertEqual(call.on_this_page_call_detail(), True)

    # ？？？
    @tags('ALL', 'CMCC', 'call')
    def test_call_00027(self):
        """
            1、联网正常已登录
            2、对方未注册
            3、当前页通话记录详情
            点击视频通话---点击取消---"1、进入拨打视频电话界面，并弹出提示窗--下方是“取消” 和“确定”按钮--返回通话记录详情页"
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        call.make_sure_have_p2p_vedio_record()
        # 判断如果键盘已拉起，则收起键盘
        if call.is_exist_call_key():
            call.click_hide_keyboard()
            time.sleep(1)
        call.click_tag_detail_first_element('[视频通话]')
        time.sleep(2)
        self.assertEqual(call.on_this_page_call_detail(), True)
        # 1. 点击视频通话按钮
        call.click_locator_key('详情_视频按钮')
        time.sleep(1)
        if call.on_this_page_flow():
            call.set_not_reminders()
            time.sleep(1)
            call.click_locator_key('回呼_我知道了')
        time.sleep(1)
        # TODO 限时回呼电话

    # @tags('ALL', 'CMCC', 'call')
    # def test_call_00030(self):
    #     """
    #         验证通话记录详情页-编辑备注名---正确输入并点击保存（中文、英文、特殊符号）---保存成功
    #     """
    #     call = CallPage()
    #     call.wait_for_page_load()
    #     # 判断如果键盘已拉起，则收起键盘
    #     if call.is_exist_call_key():
    #         call.click_hide_keyboard()
    #         time.sleep(1)
    #     call.make_sure_have_p2p_voicecall_record()
    #     call.click_tag_detail_first_element('飞信电话')
    #     time.sleep(1)
    #     if not call.on_this_page_call_detail():
    #         raise RuntimeError('通话记录---详情：打开失败')
    #     # 1. 修改为中文
    #     name = '修改后的备注'
    #     if not self.check_modify_nickname(name):
    #         raise RuntimeError('修改备注出错')
    #     call.click_locator_key('详情_返回')
    #     call.wait_for_page_call_load()
    #     self.assertEquals(call.check_text_exist(name), True)

    # ？？？

    @tags('ALL', 'CMCC', 'call')
    def test_call_00031(self):
        """
            1、备注名修改成功后，视频通话入口；
            2、查看用户名
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        # 判断是否有通话记录
        call.test_call_more_phone_condition()
        # 判断如果键盘已拉起，则收起键盘
        if call.is_exist_call_key():
            call.click_hide_keyboard()
            time.sleep(1)
        call.make_sure_have_p2p_voicecall_record()
        call.click_tag_detail_first_element('[飞信电话]')
        time.sleep(1)
        self.assertEqual(call.on_this_page_call_detail(), True)
        # 1. 修改为中文
        name = '修改后的备注'
        self.assertEqual(call.check_modify_nickname(name), True)
        call.click_locator_key('详情_视频按钮')
        time.sleep(2)
        comment = call.is_text_present(name)
        time.sleep(2)
        call.click_cancel_popup()
        if self.is_element_present("无密友圈_取消"):
            self.click_cancel_popup()
            time.sleep(1)
        self.assertEqual(name == comment, True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_00032(self):
        """
            1、联网正常已登录
            2、对方未注册
            3、当前页通话记录详情
            4 点击邀请使用按钮
            5 跳转至系统短信页面，附带发送号码与发送内容
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        # 判断是否有通话记录
        call.test_call_more_phone_no_condition()
        # 判断如果键盘已拉起，则收起键盘
        if call.is_exist_call_key():
            call.click_hide_keyboard()
            time.sleep(1)
        call.make_sure_have_p2p_voicecall_record()
        call.click_tag_detail_first_element('[飞信电话]')
        time.sleep(1)
        self.assertEqual(call.on_this_page_call_detail(), True)
        call.click_locator_key('详情_邀请使用')
        time.sleep(0.5)
        call.click_locator_key('飞信电话_邀请_短信')

    @tags('ALL', 'CMCC', 'call')
    def test_call_00034(self):
        """
            1、4G网络
            2、已登录客户端
            3、当前页面在通话页面
            4、有点对点语音通话和点对点视频通话记录、多方视频通话记录
            5、长按对点语音通话和点对点视频通话记录、多方视频通话记录
            6、弹出删除该通话记录和清除全部通话记录选择框
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        # 判断是否有通话记录
        call.test_call_more_phone_condition()
        # 判断如果键盘已拉起，则收起键盘
        if call.is_exist_call_key():
            call.click_hide_keyboard()
            time.sleep(1)
        call.make_sure_have_p2p_voicecall_record()
        call.press_tag_detail_first_element('[飞信电话]')
        time.sleep(2)
        self.assertEqual(call.is_element_present('通话_删除该通话记录'), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_00035(self):
        """
            1、4G网络
            2、已登录客户端
            3、当前页面在通话页面
            4、有点对点语音通话和点对点视频通话记录、多方视频通话记录
            5、长按对点语音通话和点对点视频通话记录、多方视频通话记录
            6、点击删除该通话记录按钮
            7、弹出删除该通话记录和清除全部通话记录选择框
            8、该条记录删除成功"
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        # 点对点通话
        if not call.make_sure_have_p2p_voicecall_record():
            # 判断是否有通话记录,没有创建
            call.test_call_more_phone_condition()
        call.press_tag_detail_first_element('[飞信电话]')
        self.assertEqual(call.is_element_already_exist('通话_删除该通话记录'), True)
        time.sleep(5)
        call.click_delete_key('[飞信电话]')
        time.sleep(1)
        self.assertEqual(call.is_on_this_page(), True)
        # 点对点视频
        time.sleep(2)
        if not call.make_sure_have_p2p_vedio_record():
            # 判断是否有通话记录,没有创建
            call.test_call_video_condition()
        call.press_tag_detail_first_element('[视频通话]')
        self.assertEqual(call.is_element_already_exist('通话_删除该通话记录'), True)
        time.sleep(5)
        call.click_delete_key('[视频通话]')
        time.sleep(2)
        self.assertEqual(call.is_on_this_page(), True)
        # 多方视频
        time.sleep(5)
        if not call.make_sure_have_multiplayer_vedio_record():
            # 判断是否有通话记录,没有创建
            call.test_call_more_video_condition()
        call.press_tag_detail_first_element('[多方视频]')
        self.assertEqual(call.is_element_already_exist('通话_删除该通话记录'), True)
        time.sleep(5)
        call.click_delete_key('[多方视频]')
        time.sleep(2)
        self.assertEqual(call.is_on_this_page(), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_00036(self):
        """
            1、4G网络
            2、已登录客户端
            3、当前页面在通话页面
            4、有点对点语音通话和点对点视频通话记录、多方视频通话记录
            5、长按对点语音通话和点对点视频通话记录、多方视频通话记录
            6、点击清除全部通话记录按钮
            7、弹出删除该通话记录和清除全部通话记录选择框
            8、所有通话记录删除成功
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        # 通话记录删除
        self.assertEqual(call.click_delete_all_key(), True)
        time.sleep(1)

    @tags('ALL', 'CMCC', 'call')
    def test_call_00037(self):
        """
            1、4G网络
            2、已登录客户端
            3、当前页面在通话页面
            4、有联系人或者家庭网联系人
            5、左上方有通话标题，右上方为"+"图标，下方有指引攻略，页面空白中间区域中有“点击左下角拨号盘icon，打电话不花钱”字样
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        # 通话记录删除
        call.click_delete_all_key()
        # 判断是否有通话标签、‘+’、打电话不花钱
        self.assertEqual(call.on_this_page_common('通话_通话'), True)
        self.assertEqual(call.on_this_page_common('+'), True)
        self.assertEqual(call.is_text_present('打电话不花钱'), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_00038(self):
        """
            1、4G网络
            2、已登录客户端
            3、当前页面在通话页面
            4、有联系人或者家庭网联系人
            5、左上方有通话标题，右上方为"+"图标，下方有指引攻略，
            页面空白中间区域中有“点击左下角拨号盘icon，打电话不花钱”字样
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        # 通话记录删除
        call.click_delete_all_key()
        # 判断是否有通话标签、‘+’、打电话不花钱
        self.assertEqual(call.is_text_present('通话'), True)
        self.assertEqual(call.on_this_page_common('+'), True)
        self.assertEqual(call.is_text_present('打电话不花钱'), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_00039(self):
        """
            1、4G网络
            2、已登录客户端
            3、当前页面在通话页面
            4、有联系人或者家庭网联系人
            5、左上方有通话标题，右上方为"+"图标，下方有指引攻略，
            页面空白中间区域中有“点击左下角拨号盘icon，打电话不花钱”字样
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        # 通话记录删除
        call.click_delete_all_key()
        # 判断是否有通话标签、‘+’、打电话不花钱
        self.assertEqual(call.is_text_present('通话'), True)
        self.assertEqual(call.on_this_page_common('+'), True)
        self.assertEqual(call.is_text_present('打电话不花钱'), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_00040(self):
        """
            点击视频通话图标
            跳转至视频通话选择页面，页面布局左上方返回按钮，多方视频字体，
            右上方呼叫按钮，下面显示不限时长成员，家庭V网与联系人联系人、
            未知号码页面，右边为字母快速定位。
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        call.click_locator_key('+')
        time.sleep(1)
        call.click_locator_key('视频通话')
        time.sleep(2)
        self.assertEqual(call.is_element_already_exist('视频通话'), True)
        time.sleep(1)
        self.assertEqual(call.on_this_page_common('视频呼叫_取消'), True)
        self.assertEqual(call.on_this_page_common('视频呼叫_确定'), True)
        time.sleep(1)
        self.assertEqual(call.on_this_page_common('视频呼叫_联系人列表'), True)
        time.sleep(1)
        self.assertEqual(call.on_this_page_common('视频通话_字母'), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_00041(self):
        """
            点击视频通话图标
            跳转至视频通话选择页面，页面布局左上方返回按钮，多方视频字体，
            右上方呼叫按钮，下面显示不限时长成员，家庭V网与联系人联系人、
            未知号码页面，右边为字母快速定位。
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        call.click_locator_key('+')
        time.sleep(0.5)
        call.click_locator_key('视频通话')
        time.sleep(1)
        call.wait_page_load_common('视频呼叫_通话选择')
        time.sleep(1)
        call.click_locator_key('视频呼叫_字母C')
        time.sleep(0.3)
        text = call.get_element_text('视频呼叫_字母第一个')
        self.assertEqual('C' == text, True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_00042(self):
        """
            点击视频通话图标
            点击选择1个家庭网成员，1个家庭网成员的头像变化为勾选的图标，右上方呼叫字体变为蓝色显示“呼叫（1/8）”。
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        call.click_locator_key('+')
        time.sleep(1)
        call.click_locator_key('视频通话')
        time.sleep(2)
        call.is_element_present('视频呼叫_通话选择')
        time.sleep(2)
        self.assertEqual(call.select_contact_n(1), True)
        time.sleep(1)
        text = call.get_element_text('视频呼叫_确定')
        self.assertEqual('确定(1/8)' == text, True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_00043(self):
        """
            点击视频通话图标
            点击选择2个家庭网成员，2个家庭网成员的头像变化为勾选的图标，右上方呼叫字体变为蓝色显示“呼叫（2/8）”。
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        call.click_locator_key('+')
        time.sleep(0.5)
        call.click_locator_key('视频通话')
        time.sleep(1)
        call.is_element_present('视频呼叫_通话选择')
        # 选择联系人
        time.sleep(1)
        self.assertEqual(call.select_contact_n(2), True)
        # 校验联系人
        text = call.get_element_text('视频呼叫_确定')
        self.assertEqual('确定(2/8)' == text, True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_00044(self):
        """
            点击视频通话图标
            点击选择3个家庭网成员，3个家庭网成员的头像变化为勾选的图标，右上方呼叫字体变为蓝色显示“呼叫（3/8）”。
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        call.click_locator_key('+')
        time.sleep(0.5)
        call.click_locator_key('视频通话')
        time.sleep(1)
        call.is_element_present('视频呼叫_通话选择')
        time.sleep(1)
        self.assertEqual(call.select_contact_n(3), True)
        text = call.get_element_text('视频呼叫_确定')
        self.assertEqual('确定(3/8)' == text, True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_00045(self):
        """
            点击视频通话图标
            点击选择8个家庭网成员，8个家庭网成员的头像变化为勾选的图标，右上方呼叫字体变为蓝色显示“呼叫（8/8）”。
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        call.click_locator_key('+')
        time.sleep(0.5)
        call.click_locator_key('视频通话')
        time.sleep(1)
        call.is_element_present('视频呼叫_通话选择')
        time.sleep(1)
        self.assertEqual(call.select_contact_n(9), True)

    @TestLogger.log('切换手机，接听视频电话')
    def to_pick_phone_video(self):
        call = CallPage()
        # 切换被叫手机
        Preconditions.select_mobile('IOS-移动-移动')
        count = 20
        try:
            while count > 0:
                # 如果在视频通话界面，接听视频
                if call.is_element_already_exist('视频接听_接听'):
                    print('接听视频-->', datetime.datetime.now().date().strftime('%Y-%m-%d'),
                          datetime.datetime.now().time().strftime("%H-%M-%S-%f"))
                    time.sleep(1)
                    call.click_locator_key('视频接听_接听')
                    return True
                else:
                    count -= 1
                    # 1s检测一次，20s没有接听，则失败
                    print(count, '切换手机，接听电话 --->', datetime.datetime.now().date().strftime('%Y-%m-%d'),
                          datetime.datetime.now().time().strftime("%H-%M-%S-%f"))
                    time.sleep(0.5)
                    continue
            else:
                return False
        except Exception as e:
            traceback.print_exc()
            print(e, datetime.datetime.now().date().strftime('%Y-%m-%d'),
                  datetime.datetime.now().time().strftime("%H-%M-%S-%f"))
            return False

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00051(self):
        """
            弹出“通话结束”提示框，页面回到呼叫前的页面中
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        # 初始化被叫手机
        Preconditions.initialize_class('IOS-移动-移动')
        # 获取手机号码
        cards = call.get_cards(CardType.CHINA_MOBILE)
        # 切换主叫手机，打电话
        time.sleep(2)
        Preconditions.select_mobile('IOS-移动')
        # 拨打视频电话
        call.pick_up_p2p_video(cards)
        # 等待返回结果
        result = self.to_pick_phone_video()
        self.assertEqual(result, True)
        time.sleep(2)
        # 切换回主叫手机
        Preconditions.select_mobile('IOS-移动')
        time.sleep(3)
        call.click_conversation_popup()
        if call.on_this_page_common('无密友圈_确定'):
            call.click_locator_key('无密友圈_取消')
        # # 判断是否有‘通话结束’字样
        self.assertEqual(call.is_element_already_exist('视频接听_通话结束'), True)

    @TestLogger.log('切换手机，接听电话')
    def to_pick_phone_00051(self):
        call = CallPage()
        # 切换到被叫手机
        Preconditions.select_mobile('Android-移动-移动')
        count = 40
        try:
            while count > 0:
                if call.is_text_present('进行视频通话'):
                    # 接听视频
                    call.click_locator_key('视频通话_接听')
                    time.sleep(2)
                    return True
                else:
                    count -= 1
                    time.sleep(1)
                    print(count, '切换手机，接听电话')
                    continue
            else:
                return False
        except:
            return False

    # @tags('ALL', 'CMCC_double', 'call')
    # def test_call_00052(self):
    #     """
    #         1、被叫方接到申请后点击“接听”
    #         2、点击“切换语音通话”按钮
    #
    #         3、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），大屏为被叫方界面（默认前摄像头）。
    #         界面右上角为“静音”和“免提”功能，静音默认未选中，免提默认选中。提供“切到语音通话”和“切换摄像头”的功能。
    #         4、跳转至语音通话页面，页面布局上方中间为被叫方头像，头像下方为被叫人名称、号码、时间显示，下方左边为静音按钮、
    #         中间为切到视频通话按钮、右边为免提按钮，再下方为挂断按钮，背景为灰黑色。
    #     """
    #     call = CallPage()
    #     call.wait_for_page_load()
    #     # 初始化被叫手机
    #     Preconditions.initialize_class('Android-移动-N')
    #     # 获取手机号码
    #     cards = call.get_cards(CardType.CHINA_MOBILE)
    #     # 切换主叫手机
    #     Preconditions.select_mobile('Android-移动')
    #     # 拨打视频电话
    #     call.pick_up_p2p_video(cards)
    #     # 等待返回结果
    #     if not self.to_pick_phone_00052():
    #         raise RuntimeError('视频通话出错')
    #
    # @TestLogger.log('切换手机，接听电话')
    # def to_pick_phone_00052(self):
    #     call = CallPage()
    #     # 切换手机
    #     Preconditions.select_mobile('Android-移动-N')
    #     count = 40
    #     try:
    #         while count > 0:
    #             # 如果在视频通话界面，接听视频
    #             if call.is_text_present('进行视频通话'):
    #                 print('接听视频')
    #                 call.pick_up_video_call()
    #                 time.sleep(2)
    #                 # 检测页面元素
    #                 if self.check_video_call_00052():
    #                     return True
    #                 else:
    #                     return False
    #             else:
    #                 count -= 1
    #                 # 1s检测一次，40s没有接听，则失败
    #                 time.sleep(1)
    #                 print(count, '切换手机，接听电话')
    #                 continue
    #         else:
    #             return False
    #     except:
    #         return False
    #
    # @TestLogger.log()
    # def check_video_call_00052(self):
    #     """
    #     1、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），
    #         大屏为被叫方界面（默认前摄像头）。
    #         界面右上角为“静音”和“免提”功能，静音默认未选中，
    #         免提默认选中。提供“切到语音通话”和“切换摄像头”的功能。
    #     2、跳转至语音通话页面，页面布局上方中间为被叫方头像，头像下方为被叫人名称、号码、时间显示，下方左边为静音按钮、
    #         中间为切到视频通话按钮、右边为免提按钮，再下方为挂断按钮，背景为灰黑色。
    #     :return: True
    #     """
    #     call = CallPage()
    #     try:
    #         call.tap_coordinate([(100, 100), (100, 110), (100, 120)])
    #         time.sleep(1)
    #         if not call.is_element_already_exist('视频界面_时长'):
    #             call.tap_coordinate([(100, 100), (100, 110), (100, 120)])
    #         self.assertEqual(call.is_element_already_exist('视频界面_静音'), True)
    #         # time.sleep(12)
    #         if not call.is_element_already_exist('视频界面_时长'):
    #             call.tap_coordinate([(100, 100), (100, 110), (100, 120)])
    #         self.assertEqual('false' == call.get_one_element('视频界面_静音').get_attribute('selected'), True)
    #         # time.sleep(12)
    #         if not call.is_element_already_exist('视频界面_时长'):
    #             call.tap_coordinate([(100, 100), (100, 110), (100, 120)])
    #         self.assertEqual(call.is_element_already_exist('视频界面_免提'), True)
    #         # time.sleep(12)
    #         if not call.is_element_already_exist('视频界面_时长'):
    #             call.tap_coordinate([(100, 100), (100, 110), (100, 120)])
    #         self.assertEqual('true' == call.get_one_element('视频界面_免提').get_attribute('selected'), True)
    #         # time.sleep(12)
    #         if not call.is_element_already_exist('视频界面_时长'):
    #             call.tap_coordinate([(100, 100), (100, 110), (100, 120)])
    #         self.assertEqual(call.is_element_already_exist('视频界面_转为语音'), True)
    #         # time.sleep(12)
    #         if not call.is_element_already_exist('视频界面_时长'):
    #             call.tap_coordinate([(100, 100), (100, 110), (100, 120)])
    #         self.assertEqual(call.is_element_already_exist('视频界面_切换摄像头'), True)
    #         time.sleep(12)
    #         if not call.is_element_already_exist('视频界面_时长'):
    #             call.tap_coordinate([(100, 100), (100, 110), (100, 120)])
    #         call.click_locator_key('视频界面_转为语音')
    #         time.sleep(1)
    #         self.assertEqual(call.is_element_already_exist('视频界面_头像'), True)
    #         self.assertEqual(call.is_element_already_exist('视频界面_备注'), True)
    #         self.assertEqual(call.is_element_already_exist('视频界面_号码'), True)
    #         self.assertEqual(call.is_element_already_exist('语音界面_时长'), True)
    #         self.assertEqual(call.is_element_already_exist('语音界面_静音'), True)
    #         self.assertEqual(call.is_element_already_exist('语音界面_转为视频'), True)
    #         self.assertEqual(call.is_element_already_exist('语音界面_免提'), True)
    #         self.assertEqual(call.is_element_already_exist('语音界面_挂断'), True)
    #         call.click_locator_key('语音界面_挂断')
    #         return True
    #     except:
    #         return False
    #
    # @tags('ALL', 'CMCC_double', 'call')
    # def test_call_00053(self):
    #     """
    #         1、被叫方接到申请后点击“接听”
    #         2、点击“切换语音通话”按钮
    #         3、被叫方接到申请后点击“接听”
    #         4、点击静音按钮
    #     """
    #     call = CallPage()
    #     call.wait_for_page_load()
    #     # 初始化被叫手机
    #     Preconditions.initialize_class('Android-移动-N')
    #     # 获取手机号码
    #     cards = call.get_cards(CardType.CHINA_MOBILE)
    #     # 切换主叫手机
    #     Preconditions.select_mobile('Android-移动')
    #     # 拨打视频电话
    #     call.pick_up_p2p_video(cards)
    #     # 等待返回结果
    #     if not self.to_pick_phone_00053():
    #         raise RuntimeError('视频通话出错')
    #
    # @TestLogger.log('切换手机，接听电话')
    # def to_pick_phone_00053(self):
    #     call = CallPage()
    #     # 切换手机
    #     Preconditions.select_mobile('Android-移动-N')
    #     count = 40
    #     try:
    #         while count > 0:
    #             # 如果在视频通话界面，接听视频
    #             if call.is_text_present('进行视频通话'):
    #                 print('接听视频')
    #                 call.pick_up_video_call()
    #                 time.sleep(2)
    #                 # 检测页面元素
    #                 if self.check_video_call_00053():
    #                     print('静音成功')
    #                     return True
    #                 else:
    #                     print('静音失败')
    #                     return False
    #             else:
    #                 count -= 1
    #                 # 1s检测一次，40s没有接听，则失败
    #                 time.sleep(1)
    #                 print(count, '切换手机，接听电话')
    #                 continue
    #         else:
    #             return False
    #     except:
    #         return False
    #
    # @TestLogger.log()
    # def check_video_call_00053(self):
    #     """
    #     1、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），
    #         大屏为被叫方界面（默认前摄像头）。
    #         界面右上角为“静音”和“免提”功能，静音默认未选中，
    #         免提默认选中。提供“切到语音通话”和“切换摄像头”的功能。
    #     2、跳转至语音通话页面，页面布局上方中间为被叫方头像，头像下方为被叫人名称、号码、时间显示，下方左边为静音按钮、
    #         中间为切到视频通话按钮、右边为免提按钮，再下方为挂断按钮，背景为灰黑色。
    #     :return: True
    #     """
    #     call = CallPage()
    #     try:
    #         call.click_locator_key('视频界面_免提')
    #         call.tap_coordinate([(100, 100), (100, 110), (100, 120)])
    #         time.sleep(1)
    #         if not call.is_element_already_exist('视频界面_时长'):
    #             call.tap_coordinate([(100, 100), (100, 110), (100, 120)])
    #         call.click_locator_key('视频界面_静音')
    #         if 'true' != call.get_one_element('视频界面_静音').get_attribute('selected'):
    #             raise RuntimeError('静音出错')
    #         call.click_locator_key('视频界面_挂断')
    #         return True
    #     except:
    #         return False
    #
    # @tags('ALL', 'CMCC_double', 'call')
    # def test_call_00054(self):
    #     """
    #         1、被叫方接到申请后点击“接听”
    #         2、点击“切换语音通话”按钮
    #         3、被叫方接到申请后点击“接听”
    #         4、点击免提按钮
    #     """
    #     call = CallPage()
    #     call.wait_for_page_load()
    #     # 初始化被叫手机
    #     Preconditions.initialize_class('Android-移动-N')
    #     # 获取手机号码
    #     cards = call.get_cards(CardType.CHINA_MOBILE)
    #     # 切换主叫手机
    #     Preconditions.select_mobile('Android-移动')
    #     # 拨打视频电话
    #     call.pick_up_p2p_video(cards)
    #     # 等待返回结果
    #     if not self.to_pick_phone_00054():
    #         raise RuntimeError('视频通话出错')
    #
    # @TestLogger.log('切换手机，接听电话')
    # def to_pick_phone_00054(self):
    #     call = CallPage()
    #     # 切换手机
    #     Preconditions.select_mobile('Android-移动-N')
    #     count = 40
    #     try:
    #         while count > 0:
    #             # 如果在视频通话界面，接听视频
    #             if call.is_text_present('进行视频通话'):
    #                 print('接听视频')
    #                 call.pick_up_video_call()
    #                 time.sleep(2)
    #                 # 检测页面元素
    #                 if self.check_video_call_00054():
    #                     print('静音成功')
    #                     return True
    #                 else:
    #                     print('静音失败')
    #                     return False
    #             else:
    #                 count -= 1
    #                 # 1s检测一次，40s没有接听，则失败
    #                 time.sleep(1)
    #                 print(count, '切换手机，接听电话')
    #                 continue
    #         else:
    #             return False
    #     except:
    #         return False
    #
    # @TestLogger.log()
    # def check_video_call_00054(self):
    #     """
    #     1、被叫方接到申请后点击“接听”
    #     2、点击免提按钮"
    #     3、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），大屏为被叫方界面（默认前摄像头）。界面右上角为“静音”和“免提”功能，静音默认未选中，免提默认选中。
    #     提供“切到语音通话”和“切换摄像头”的功能。
    #     4、免提按钮亮起（对方说话声音变大）。"
    #     """
    #     call = CallPage()
    #     try:
    #         if not call.is_element_already_exist('视频界面_时长'):
    #             call.tap_coordinate([(100, 100), (100, 110), (100, 120)])
    #         call.click_locator_key('视频界面_免提')
    #         if 'false' != call.get_one_element('视频界面_免提').get_attribute('selected'):
    #             raise RuntimeError('关闭免提出错')
    #         call.click_locator_key('视频界面_挂断')
    #         return True
    #     except:
    #         return False
    #
    # @tags('ALL', 'CMCC_double', 'call')
    # def test_call_00056(self):
    #     """
    #         1、被叫方接到申请后点击“接听”
    #         2、点击“切换语音通话”按钮
    #         3、被叫方接到申请后点击“接听”
    #         4、点击挂断按钮
    #     """
    #     call = CallPage()
    #     call.wait_for_page_load()
    #     try:
    #         # 初始化被叫手机
    #         Preconditions.initialize_class('Android-移动-N')
    #         # 获取手机号码
    #         cards = call.get_cards(CardType.CHINA_MOBILE)
    #         # 切换主叫手机
    #         Preconditions.select_mobile('Android-移动')
    #         # 拨打视频电话
    #         call.pick_up_p2p_video(cards)
    #         # 等待返回结果
    #         if not self.to_pick_phone_00056():
    #             raise RuntimeError('视频通话出错')
    #         # 切换回主叫手机
    #         Preconditions.select_mobile('Android-移动')
    #         time.sleep(12)
    #         if not call.is_element_already_exist('视频界面_时长'):
    #             call.tap_coordinate([(100, 100), (100, 110), (100, 120)])
    #             time.sleep(0.5)
    #         call.click_locator_key('视频界面_挂断')
    #         print('视频界面_挂断')
    #         if not call.is_toast_exist('通话结束'):
    #             raise RuntimeError('没有出现‘通话结束’提示')
    #         else:
    #             print('山检测到‘通话结束’提示')
    #             time.sleep(3)
    #         if not call.is_on_this_page():
    #             raise RuntimeError('没有回到‘通话’页面')
    #         else:
    #             print('回到‘通话’界面')
    #         time.sleep(2)
    #     except:
    #         print('测试出错')
    #         if call.is_element_already_exist('视频界面_挂断'):
    #             call.click_locator_key('视频界面_挂断')
    #
    # @TestLogger.log('切换手机，接听电话')
    # def to_pick_phone_00056(self):
    #     call = CallPage()
    #     # 切换手机
    #     Preconditions.select_mobile('Android-移动-N')
    #     count = 40
    #     try:
    #         while count > 0:
    #             # 如果在视频通话界面，接听视频
    #             if call.is_text_present('进行视频通话'):
    #                 print('接听视频')
    #                 call.pick_up_video_call()
    #                 time.sleep(2)
    #                 # 检测页面元素
    #                 if self.check_video_call_00056():
    #                     print('静音成功')
    #                     return True
    #                 else:
    #                     print('静音失败')
    #                     return False
    #             else:
    #                 count -= 1
    #                 # 1s检测一次，40s没有接听，则失败
    #                 time.sleep(1)
    #                 print(count, '切换手机，接听电话')
    #                 continue
    #         else:
    #             return False
    #     except:
    #         return False
    #
    # @TestLogger.log()
    # def check_video_call_00056(self):
    #     """
    #     1、被叫方接到申请后点击“接听”
    #     2、点击挂断按钮"
    #     3、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），大屏为被叫方界面（默认前摄像头）。界面右上角为“静音”和“免提”功能，静音默认未选中，免提默认选中。
    #     提供“切到语音通话”和“切换摄像头”的功能。
    #     4、弹出“通话结束”提示框，回到呼叫前页面中
    #     """
    #     call = CallPage()
    #     try:
    #         if not call.is_element_already_exist('视频界面_时长'):
    #             call.tap_coordinate([(100, 100), (100, 110), (100, 120)])
    #         call.click_locator_key('视频界面_免提')
    #         if 'false' != call.get_one_element('视频界面_免提').get_attribute('selected'):
    #             raise RuntimeError('关闭免提出错')
    #         return True
    #     except:
    #         return False
    #
    # @tags('ALL', 'CMCC_double', 'call')
    # def test_call_00058(self):
    #     """
    #         1、被叫方接到申请后点击“接听”
    #         2、点击“切换语音通话”按钮
    #         3、被叫方接到申请后点击“接听”
    #         4、点击挂断按钮
    #     """
    #     call = CallPage()
    #     call.wait_for_page_load()
    #     try:
    #         # 初始化被叫手机
    #         Preconditions.initialize_class('Android-移动-N')
    #         # 获取手机号码
    #         cards = call.get_cards(CardType.CHINA_MOBILE)
    #         # 切换主叫手机
    #         Preconditions.select_mobile('Android-移动')
    #         # 拨打视频电话
    #         call.pick_up_p2p_video(cards)
    #         # 等待返回结果
    #         if not self.to_pick_phone_00058():
    #             raise RuntimeError('视频通话出错')
    #     except:
    #         print('测试出错')
    #         raise
    #
    # @TestLogger.log('切换手机，接听电话')
    # def to_pick_phone_00058(self):
    #     call = CallPage()
    #     # 切换手机
    #     try:
    #         Preconditions.select_mobile('Android-移动-N')
    #         self.assertEqual(call.is_element_already_exist('视频界面_头像'), True)
    #         self.assertEqual(call.is_element_already_exist('视频界面_备注'), True)
    #         self.assertEqual(call.is_element_already_exist('视频界面_号码'), True)
    #         self.assertEqual(call.is_text_present('进行视频通话'), True)
    #         self.assertEqual(call.is_element_already_exist('视频通话_挂断'), True)
    #         self.assertEqual(call.is_element_already_exist('视频通话_接听'), True)
    #         return True
    #     except:
    #         return False
    #
    # @tags('ALL', 'CMCC_double', 'call')
    # def test_call_00059(self):
    #     """
    #         视频通话页面（被叫方不在线）
    #         1、被叫方接到申请后长时间未点击“接听”或“挂断”（根据SDK反馈的结果）
    #         2、显示“用户暂时无法接通”，回到呼叫前的页面中
    #     """
    #     call = CallPage()
    #     call.wait_for_page_load()
    #     try:
    #         # 切换主叫手机
    #         Preconditions.initialize_class('Android-移动-N')
    #         # 获取手机号码
    #         cards = call.get_cards(CardType.CHINA_MOBILE)
    #         call.set_network_status(0)
    #         # 切换主叫手机
    #         Preconditions.select_mobile('Android-移动')
    #         # 拨打视频电话
    #         call.pick_up_p2p_video(cards)
    #         time.sleep(20)
    #         if not call.is_toast_exist('对方未接听', timeout=20):
    #             raise
    #     finally:
    #         Preconditions.select_mobile('Android-移动-N')
    #         call.set_network_status(6)
    #         print('已设置被叫手机网络为开启')

    @tags('ALL', 'CMCC', 'call')
    def test_call_000156(self):
        """
            1、正常登录密友圈
            2、使用飞信电话给非联系人/不限时长成员/家庭网成员等关系的陌生号码拨打电话
            3、查看通话记录
            4、生成一条呼出的优惠电话记录，记录中昵称位置显示该陌生电话的全号，
            5、类型显示为：飞信电话，并显示该陌生号码的归属地和运营商
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        call.click_delete_all_key()
        time.sleep(0.5)
        # 呼出一个多方视频通话
        call.test_call_more_video_condition()
        call.wait_for_page_call_load()
        time.sleep(1)
        if call.is_element_already_exist('[多方视频]'):
            call.click_tag_detail_first_element('[多方视频]')
            time.sleep(0.5)
            call.click_locator_key('详情_发起多方视频')
            time.sleep(10)
            # 挂断_多方通话
            call.click_more_phone_popup()
            if call.is_element_already_exist('挂断_多方通话_确定'):
                call.click_locator_key('挂断_多方通话_确定')

    @tags('ALL', 'CMCC', 'call')
    def test_call_000158(self):
        """展开拨号盘，不可以左右滑动切换tab，上方内容显示通话模块通话记录内容"""
        time.sleep(2)
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        # 判断如果键盘是拉起的，则不需要再次拉起
        if call.is_on_this_page():
            time.sleep(2)
            call.click_show_keyboard()
        time.sleep(1)
        # 向左滑动
        x_source = 50 / 375 * 100
        y_source = 80 / 667 * 100
        x_target = 50 / 375 * 100
        y_target = 30 / 667 * 100
        call.swipe_by_percent_on_screen(x_source, y_source, x_target, y_target)
        # 判断滑动后是否还在此页面
        self.assertEqual(call.is_exist_call_key(), True)
        # 向右滑动
        x_source = 90 / 375 * 100
        y_source = 50 / 667 * 100
        x_target = 20 / 375 * 100
        y_target = 50 / 667 * 100
        call.swipe_by_percent_on_screen(x_source, y_source, x_target, y_target)
        # 判断滑动后是否还在此页面
        self.assertEqual(call.is_exist_call_key(), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_000159(self):
        """
        点击拨号盘上面的默认通话记录
        1、正常网络状态下，登录密友圈；
        2、当前页面在通话页面
        3、拨号盘已打开
        4、通话模块存在通话记录
        5、点击该（除详情记录图标）通话记录任意区域
        6、点击右侧详情记录图标
        7、呼叫该记录的通话
        8、跳转该记录的通话详情页面"
        :return:
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        call.click_delete_all_key()
        time.sleep(0.5)
        # 呼出一个点对点视频通话
        call.test_call_video_condition()
        call.click_locator_key("拨号键盘");
        call.click_tag_detail_first_element('[视频通话]')
        self.assertEqual(call.is_text_present('通话记录(视频通话)'), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_000160(self):
        """
        在拨号盘以外的区域，进行上下滑动
        [预期结果]
        拨号盘收起；显示通话页面
        :return:
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        time.sleep(0.5)
        if not call.is_on_this_page():
            call.click_locator_key("拨号键盘")
        # 向上滑动
        time.sleep(1)
        x_source = 28 / 375 * 100
        y_source = 140 / 667 * 100
        x_target = 28 / 375 * 100
        y_target = 100 / 667 * 100
        call.swipe_by_percent_on_screen(x_source, y_source, x_target, y_target)
        # 判断滑动后是否还在此页面
        time.sleep(1)
        self.assertEqual(call.is_element_already_exist('拨号键盘'), True)
        # 向下滑动
        if not call.is_on_this_page():
            call.click_locator_key("拨号键盘")
        time.sleep(1)
        x_source = 28 / 375 * 100
        y_source = 100 / 667 * 100
        x_target = 28 / 375 * 100
        y_target = 140 / 667 * 100
        call.swipe_by_percent_on_screen(x_source, y_source, x_target, y_target)
        # 判断滑动后是否还在此页面
        time.sleep(1)
        self.assertEqual(call.is_element_already_exist('拨号键盘'), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_000161(self):
        """
        在拨号盘以外的区域，进行上下滑动
        [预期结果]
        保持拨号盘半收起状态；
        拨号盘搜索逻辑按号码，
        首字母，全拼模糊匹配，
        搜索的数据源包括：搜索的数据源包括：（本地通讯录+联系人+家庭网+未知电话）
        :return:
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        time.sleep(0.5)
        if call.is_on_this_page():
            call.click_show_keyboard()
        time.sleep(1)
        # 输入文字自动搜索
        call.click_keyboard_call('keyboard_1')
        time.sleep(1)
        # 向上滑动
        x_source = 28 / 375 * 100
        y_source = 140 / 667 * 100
        x_target = 28 / 375 * 100
        y_target = 100 / 667 * 100
        call.swipe_by_percent_on_screen(x_source, y_source, x_target, y_target)
        is_keyboard_0 = call.is_element_already_exist("keyboard_0")
        is_exists = call.is_element_already_exist("呼叫")
        self.assertEqual((not is_keyboard_0) and is_exists, True)
        # 向下滑动
        time.sleep(1)
        call.click_locator_key("拨号_删除")
        time.sleep(1)
        call.click_keyboard_call('keyboard_1')
        time.sleep(1)
        x_source = 28 / 375 * 100
        y_source = 100 / 667 * 100
        x_target = 28 / 375 * 100
        y_target = 140 / 667 * 100
        call.swipe_by_percent_on_screen(x_source, y_source, x_target, y_target)
        is_keyboard_0 = call.is_element_already_exist("keyboard_0")
        is_exists = call.is_element_already_exist("呼叫")
        self.assertEqual((not is_keyboard_0) and is_exists, True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_000162(self):
        """
        1、显示拨号盘半收起; 2、点击拨号盘按钮; 3、清空输入框内容
        [预期结果]
        1、输入框存在输入内容，底部从左往右依次为展开拨号盘按钮、呼叫按钮、清除按钮
        2、拨号盘全部展开
        3、拨号盘全盘展开
        :return:
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        time.sleep(0.5)
        if call.is_on_this_page():
            call.click_show_keyboard()
        time.sleep(1)
        # 输入文字自动搜索
        call.click_keyboard_call('keyboard_1')
        time.sleep(1)
        # 收起键盘
        time.sleep(1)
        call.click_locator_key('拨号_收起键盘')
        # 判断键盘
        time.sleep(2)
        self.assertEqual(call.is_element_already_exist('拨号_半_收起键盘'), True)
        self.assertEqual(call.is_element_already_exist('拨号界面_呼叫'), True)
        self.assertEqual(call.is_element_already_exist('拨号_删除'), True)
        # 拨号盘全盘展开
        time.sleep(2)
        call.click_keyboard_call('拨号_删除')
        self.assertEqual(call.is_element_already_exist('拨号_收起键盘'), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_000163(self):
        """
        在拨号盘以外的区域，进行上下滑动
        [预期结果]
        保持拨号盘半收起状态；显示“无该联系人”的空白页面
        :return:
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        time.sleep(0.5)
        if call.is_on_this_page():
            call.click_show_keyboard()
        time.sleep(1)
        # 输入文字自动搜索
        call.click_keyboard_call('keyboard_5')
        time.sleep(1)
        call.click_keyboard_call('keyboard_3')
        time.sleep(1)
        call.click_keyboard_call('keyboard_6')
        # 判断键盘
        time.sleep(2)
        self.assertEqual(call.is_element_already_exist('拨号_收起键盘'), True)
        self.assertEqual(call.is_element_already_exist('拨号界面_呼叫'), True)
        self.assertEqual(call.is_element_already_exist('拨号_删除'), True)
        # 无联系人
        time.sleep(2)
        self.assertEqual(call.is_element_already_exist('拨号_无联系人'), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_000164(self):
        """
        在拨号盘以外的区域，进行上下滑动
        [预期结果]
        拨号盘任保持半收起状态；
        :return:
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        time.sleep(0.5)
        if call.is_on_this_page():
            call.click_show_keyboard()
        time.sleep(1)
        # 输入文字自动搜索
        call.click_keyboard_call('keyboard_1')
        time.sleep(1)
        # 收起键盘
        time.sleep(1)
        call.click_locator_key('拨号_收起键盘')
        # 判断键盘,半收起状态
        time.sleep(2)
        self.assertEqual(call.is_element_already_exist('拨号_半_收起键盘'), True)
        self.assertEqual(call.is_element_already_exist('拨号界面_呼叫'), True)
        self.assertEqual(call.is_element_already_exist('拨号_删除'), True)
        # 向上滑动
        x_source = 28 / 375 * 100
        y_source = 140 / 667 * 100
        x_target = 28 / 375 * 100
        y_target = 100 / 667 * 100
        call.swipe_by_percent_on_screen(x_source, y_source, x_target, y_target)
        # 判断键盘,半收起状态
        time.sleep(2)
        self.assertEqual(call.is_element_already_exist('拨号_半_收起键盘'), True)
        self.assertEqual(call.is_element_already_exist('拨号界面_呼叫'), True)
        self.assertEqual(call.is_element_already_exist('拨号_删除'), True)
        # 向下滑动
        time.sleep(1)
        x_source = 28 / 375 * 100
        y_source = 100 / 667 * 100
        x_target = 28 / 375 * 100
        y_target = 140 / 667 * 100
        call.swipe_by_percent_on_screen(x_source, y_source, x_target, y_target)
        # 判断键盘,半收起状态
        time.sleep(2)
        self.assertEqual(call.is_element_already_exist('拨号_半_收起键盘'), True)
        self.assertEqual(call.is_element_already_exist('拨号界面_呼叫'), True)
        self.assertEqual(call.is_element_already_exist('拨号_删除'), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_000165(self):
        """
        1、号码输入框输入123; 2、点击左下方“收起”按钮; 3、再点击通话键盘图标
        [预期结果]
        1、输入框显示123
        2、拨号盘半挂起
        3、显示拨号盘半挂起，输入框显示123
        :return:
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        time.sleep(0.5)
        if call.is_on_this_page():
            call.click_show_keyboard()
        # 输入文字"123"自动搜索
        input_text_source = '123'
        time.sleep(1)
        call.click_keyboard_call('keyboard_1')
        time.sleep(1)
        call.click_keyboard_call('keyboard_2')
        time.sleep(1)
        call.click_keyboard_call('keyboard_3')
        # 收起键盘
        time.sleep(1)
        call.click_locator_key('拨号_收起键盘')
        # 拨号盘半挂起
        time.sleep(1)
        self.assertEqual(call.is_element_already_exist('拨号_半_收起键盘'), True)
        # 拨号盘半挂起
        input_text = call.get_element_text('拨号_半_文本框')
        self.assertEqual(input_text_source == input_text, True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_000167(self):
        """
        任意点击“0/9号码和#与*”
        [预期结果]
        输入框显示“0/9号码和#与*”
        :return:
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        time.sleep(0.5)
        if call.is_on_this_page():
            call.click_show_keyboard()
        # 输入文字
        input_text_source = '3*#'
        time.sleep(1)
        call.click_keyboard_call('keyboard_3')
        time.sleep(1)
        call.click_keyboard_call('keyboard_*')
        time.sleep(1)
        call.click_keyboard_call('keyboard_#')
        # 拨号盘半挂起
        input_text = call.get_element_text('拨号_文本框')
        self.assertEqual(input_text_source == input_text, True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_000168(self):
        """
        点击拨打
        [预期结果]
        弹出“请输入正确号码”icon提示
        :return:
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        time.sleep(0.5)
        if call.is_on_this_page():
            call.click_show_keyboard()
        # 拨号界面_呼叫
        time.sleep(1)
        call.click_locator_key('拨号界面_呼叫')
        # 拨号盘半挂起
        call.is_element_already_exist('拨号_请输入正确号码')

    @tags('ALL', 'CMCC', 'call')
    def test_call_000169(self):
        """
        点击2-9任意数字
        [预期结果]
        模糊搜索数字右下角字母匹配
        :return:
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        time.sleep(0.5)
        if call.is_on_this_page():
            call.click_show_keyboard()
        # 输入文字2('a', 'b', 'c')
        text_list = ['a', 'b', 'c']
        time.sleep(1)
        call.click_keyboard_call('keyboard_2')
        # 模糊搜索数字右下角字母匹配
        time.sleep(1)
        self.assertEqual(call.get_tag_list_text_exists('通话_搜索列表_联系人名称', text_list), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_000170(self):
        """
        长按0数字键
        [预期结果]
        输入框显示“+”符号
        :return:
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        time.sleep(0.5)
        if call.is_on_this_page():
            call.click_show_keyboard()
        # 长按0数字键
        input_text_source = '+'
        time.sleep(5)
        call.long_press_number("keyboard_0")
        input_text = call.get_element_text('拨号_文本框')
        self.assertEqual(input_text_source == input_text, True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_000172(self):
        """
            1、点击清除键一下
            2、长按清除键
        [预期结果]
            1、输入框显示12345
            2、清除全部输入内容，输入框显示默认字体“直接拨号或拼音搜索”
        :return:
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        time.sleep(0.5)
        if call.is_on_this_page():
            call.click_show_keyboard()
        # 输入文字
        input_text_source = '12345'
        time.sleep(1)
        call.click_keyboard_call('keyboard_1')
        time.sleep(1)
        call.click_keyboard_call('keyboard_2')
        time.sleep(1)
        call.click_keyboard_call('keyboard_3')
        time.sleep(1)
        call.click_keyboard_call('keyboard_4')
        time.sleep(1)
        call.click_keyboard_call('keyboard_5')
        time.sleep(1)
        call.click_keyboard_call('keyboard_6')
        # 点击清除键一下
        time.sleep(1)
        call.click_locator_key('拨号_删除')
        time.sleep(1)
        input_text = call.get_element_text('拨号_文本框')
        self.assertEqual(input_text_source == input_text, True)
        # 长按清除键
        time.sleep(1)
        input_text_source = '直接拨号或拼音搜索'
        call.long_press_number('拨号_删除')
        time.sleep(1)
        input_text = call.get_element_text('拨号_文本框')
        self.assertEqual(input_text_source == input_text, True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_000178(self):
        """
           输入1234567891234567
        [预期结果]
            输入框只显示123456789123456（15位字符）超过字符不显示
        :return:
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        time.sleep(0.5)
        if call.is_on_this_page():
            call.click_show_keyboard()
        # 输入文字
        input_len = 15
        time.sleep(1)
        call.click_keyboard_call('keyboard_1')
        time.sleep(1)
        call.click_keyboard_call('keyboard_2')
        time.sleep(1)
        call.click_keyboard_call('keyboard_3')
        time.sleep(1)
        call.click_keyboard_call('keyboard_4')
        time.sleep(1)
        call.click_keyboard_call('keyboard_5')
        time.sleep(1)
        call.click_keyboard_call('keyboard_6')
        time.sleep(1)
        call.click_keyboard_call('keyboard_7')
        time.sleep(1)
        call.click_keyboard_call('keyboard_8')
        time.sleep(1)
        call.click_keyboard_call('keyboard_9')
        time.sleep(1)
        call.click_keyboard_call('keyboard_1')
        time.sleep(1)
        call.click_keyboard_call('keyboard_2')
        time.sleep(1)
        call.click_keyboard_call('keyboard_3')
        time.sleep(1)
        call.click_keyboard_call('keyboard_4')
        time.sleep(1)
        call.click_keyboard_call('keyboard_5')
        time.sleep(1)
        call.click_keyboard_call('keyboard_6')
        time.sleep(1)
        call.click_keyboard_call('keyboard_7')
        # 点击清除键一下
        time.sleep(1)
        input_text = call.get_element_text('拨号_文本框')
        self.assertEqual(input_len == len(input_text), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_000180(self):
        """
           1、点击结果栏任意区域
        [预期结果]
            直接呼叫
        :return:
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        time.sleep(0.5)
        if call.is_on_this_page():
            call.click_show_keyboard()
        # 输入文字
        time.sleep(1)
        call.click_keyboard_call('keyboard_1')
        # 选择第一个
        call.click_search_phone_first_element('拨号_搜索_列表联系人')
        # 点击清除键一下
        if call.is_element_already_exist('飞信电话_我知道了'):
            call.click_locator_key('飞信电话_我知道了')
        time.sleep(1)
        call.click_more_phone_popup()

    @tags('ALL', 'CMCC', 'call')
    def test_call_000181(self):
        """
            1、点击（除详情记录图标）该号码栏任意区域
            2、点击右侧详情记录图标
        [预期结果]
            1、直接呼叫
            2、跳转至联系人或家庭网详情页面
        :return:
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        time.sleep(0.5)
        if call.is_on_this_page():
            call.click_show_keyboard()
        # 输入文字
        time.sleep(1)
        call.click_keyboard_call('keyboard_2')
        # 选择第一个
        call.click_search_phone_first_element('拨号_搜索_列表联系人')
        # 点击清除键一下
        if call.is_element_already_exist('飞信电话_我知道了'):
            call.click_locator_key('飞信电话_我知道了')
        time.sleep(1)
        call.click_more_phone_popup()

    @tags('ALL', 'CMCC', 'call')
    def test_call_000184(self):
        """
            1、在【通话&消息】模块主界面，点击右上角“+”——视频通话；
            2、进入任一群聊会话窗口，点击右上角“视频通话”icon
        [预期结果]
            打开多方视频-联系人选择器页面（该页面逻辑与现网保持一致）
        :return:
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        # 点击右上角“+”
        time.sleep(1)
        call.click_locator_key('+')
        # 视频通话
        time.sleep(10)
        call.click_call('视频通话')
        # 页面检查
        time.sleep(1)
        self.assertEqual(call.is_element_already_exist('详情_名称'), True)
        self.assertEqual(call.is_element_already_exist('视频呼叫_确定'), True)
        self.assertEqual(call.is_element_already_exist('视频呼叫_联系人列表'), True)

    @tags('ALL', 'CMCC', 'call')
    def test_call_000185(self):
        """
            选择1名成员，点击“呼叫”按钮
        [预期结果]
            发起单对单视频通话，逻辑与现网保持一致一致
        :return:
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        call.click_locator_key('+')
        time.sleep(1)
        call.click_locator_key('视频通话')
        time.sleep(2)
        call.select_contact_n(1)
        time.sleep(2)
        call.click_locator_key('视频呼叫_确定')
        time.sleep(5)
        call.click_conversation_popup()
        time.sleep(2)
        if call.is_element_present("无密友圈_确定"):
            call.click_cancel_popup()
            time.sleep(1)

    @tags('ALL', 'CMCC', 'call')
    def test_call_000187(self):
        """
            1、选择2名以上联系人，点击“呼叫”按钮；
        [预期结果]
            进入视频通话窗口，所有成员以小格子画面显示，被叫方显示对方设置头像/默认头像，
            头像上浮层显示呼叫中标识“转圈”，
            窗口下方有“免提、静音、关闭摄像头、转换摄像头、挂断”按钮；
        :return:
        """
        call = CallPage()
        # 关闭广告弹框
        call.close_click_home_advertisement()
        call.wait_for_page_load()
        call.click_locator_key('+')
        time.sleep(1)
        call.click_locator_key('视频通话')
        time.sleep(2)
        call.select_contact_n(3)
        time.sleep(2)
        call.click_locator_key('视频呼叫_确定')
        # 免提、静音、关闭摄像头、翻转摄像头
        time.sleep(2)
        call.is_element_already_exist('呼叫_视频_免提')
        time.sleep(2)
        call.is_element_already_exist('呼叫_视频_静音')
        time.sleep(2)
        call.is_element_already_exist('呼叫_视频_关闭摄像头')
        time.sleep(2)
        call.is_element_already_exist('呼叫_视频_翻转摄像头')
        # 关闭
        time.sleep(5)
        call.click_conversation_popup()
        time.sleep(2)
        if call.is_element_present("无密友圈_确定"):
            call.click_cancel_popup()
            time.sleep(1)



