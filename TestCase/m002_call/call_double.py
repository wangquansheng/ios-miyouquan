import time
import unittest
import warnings
import datetime
import traceback
import multiprocessing

from pages import OneKeyLoginPage
from pages.call.Call import CallPage
from pages.components.Footer import FooterPage

from library.core.TestCase import TestCase
from library.core.utils.applicationcache import current_mobile, switch_to_mobile
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

    # @staticmethod
    # def select_assisted_mobile2():
    #     """切换到单卡、异网卡Android手机 并启动应用"""
    #     switch_to_mobile(REQUIRED_MOBILES['辅助机2'])
    #     current_mobile().connect_mobile()
    #
    # @staticmethod
    # def select_single_cmcc_android_4g_client():
    #     """
    #     启动
    #     1、4G，安卓客户端
    #     2、移动卡
    #     :return:
    #     """
    #     client = switch_to_mobile(REQUIRED_MOBILES['测试机'])
    #     client.connect_mobile()
    #
    # @staticmethod
    # def make_already_in_one_key_login_page():
    #     """
    #     1、已经进入一键登录页
    #     :return:
    #     """
    #     # 如果当前页面已经是一键登录页，不做任何操作
    #     one_key = OneKeyLoginPage()
    #     if one_key.is_on_this_page():
    #         return
    #     # 如果当前页不是引导页第一页，重新启动app
    #     guide_page = GuidePage()
    #     if not guide_page.is_on_the_first_guide_page():
    #         current_mobile().launch_app()
    #         guide_page.wait_for_page_load(20)
    #
    #     # 跳过引导页
    #     guide_page.wait_for_page_load(30)
    #     guide_page.swipe_to_the_second_banner()
    #     guide_page.swipe_to_the_third_banner()
    #     guide_page.click_start_the_experience()
    #     guide_page.click_start_the_one_key()
    #     time.sleep(2)
    #     guide_page.click_always_allow()
    #     one_key.wait_for_page_load(30)
    #
    @staticmethod
    def login_by_one_key_login():
        """
        从一键登录页面登录
        :return:
        """
        # 等待号码加载完成后，点击一键登录
        one_key = OneKeyLoginPage()
        time.sleep(2)
        if one_key.is_text_present('一键登录'):
            one_key.click_text('一键登录')
            time.sleep(3)
        # # one_key.wait_for_page_load()
        # # one_key.wait_for_tell_number_load(60)
        # one_key.click_one_key_login()
        # time.sleep(2)
        # if one_key.is_text_present('用户协议和隐私保护'):
        #     one_key.click_agree_user_aggrement()
        #     time.sleep(1)
        #     one_key.click_agree_login_by_number()

        # 等待通话页面加载
        # call_page = CallPage()
        # call_page.wait_for_page_call_load()
        # call_page.click_always_allow()
        # time.sleep(2)
        # call_page.remove_mask()

    # @staticmethod
    # def app_start_for_the_first_time():
    #     """首次启动APP（使用重置APP代替）"""
    #     current_mobile().reset_app()
    #
    # @staticmethod
    # def terminate_app():
    #     """
    #     强制关闭app,退出后台
    #     :return:
    #     """
    #     app_id = current_driver().capabilities['appPackage']
    #     current_mobile().terminate_app(app_id)
    #
    # @staticmethod
    # def background_app(seconds):
    #     """后台运行"""
    #     current_mobile().background_app(seconds)
    #
    # @staticmethod
    # def reset_and_relaunch_app():
    #     """首次启动APP（使用重置APP代替）"""
    #     app_package = 'com.cmic.college'
    #     current_driver().activate_app(app_package)
    #     current_mobile().reset_app()
    #
    # @staticmethod
    # def get_current_activity_name():
    #     import os, sys
    #     global findExec
    #     findExec = 'findstr' if sys.platform == 'win32' else 'grep'
    #     device_name = current_driver().capabilities['deviceName']
    #     cmd = 'adb -s %s shell dumpsys window | %s mCurrentFocus' % (device_name, findExec)
    #     res = os.popen(cmd)
    #     time.sleep(2)
    #     # 截取出activity名称 == ''为第三方软件
    #     current_activity = res.read().split('u0 ')[-1].split('/')[0]
    #     res.close()
    #     return current_activity

    @staticmethod
    def select_mobile(category):
        """选择手机手机"""
        client = switch_to_mobile(REQUIRED_MOBILES[category])
        client.connect_mobile()
        return client

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
        # # 如果当前页不是引导页第一页，重新启动app
        # else:
        #     try:
        #         current_mobile().terminate_app('com.cmic.college', timeout=2000)
        #     except:
        #         pass
        #     current_mobile().launch_app()
        #     try:
        #         call_page.wait_until(
        #             condition=lambda d: call_page.is_on_this_page(),
        #             timeout=3
        #         )
        #         return
        #     except TimeoutException:
        #         pass
        #     Preconditions.reset_and_relaunch_app()
        #     Preconditions.make_already_in_one_key_login_page()
        #     Preconditions.login_by_one_key_login()

    @staticmethod
    def make_sure_in_after_login_callpage():
        Preconditions.make_already_in_call_page()
        current_mobile().wait_until_not(condition=lambda d: current_mobile().is_text_present('正在登录...'), timeout=20)

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


# noinspection PyShadowingBuiltins,PyBroadException,PyUnresolvedReferences
class CallPageTest(TestCase):
    """Call 模块--全量"""

    def default_setUp(self):
        """前置方法，禁用ResourceWarning提示"""
        warnings.simplefilter('ignore', ResourceWarning)

    def default_tearDown(self):
        """后置方法，断开所有手机"""
        Preconditions.disconnect_mobile('IOS-移动')
        Preconditions.disconnect_mobile('IOS-移动-移动')
        # 关闭idevice log
        FooterPage().kill_device_syslog()

    @TestLogger.log('接听视频电话')
    def to_pick_phone_video(self):
        call = CallPage()
        time.sleep(1)
        count = 30
        try:
            while count > 0:
                # 如果在视频通话界面，接听视频
                if call.is_element_already_exist('视频接听_接听'):
                    call.click_locator_key('视频接听_接听')
                    print('接听视频电话-->', datetime.datetime.now().date().strftime('%Y-%m-%d'),
                          datetime.datetime.now().time().strftime("%H-%M-%S-%f"))
                    return True
                else:
                    count -= 1
                    # 1s检测一次，20s没有接听，则失败
                    print(count, '接听视频电话 --->', datetime.datetime.now().date().strftime('%Y-%m-%d'),
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

    @TestLogger.log('接听视频电话')
    def to_answer_multi_video(self):
        call = CallPage()
        time.sleep(1)
        count = 30
        try:
            while count > 0:
                # 如果在视频通话界面，接听视频
                if call.is_element_already_exist('多方视频_接听'):
                    call.click_locator_key('多方视频_接听')
                    print('接听视频电话-->', datetime.datetime.now().date().strftime('%Y-%m-%d'),
                          datetime.datetime.now().time().strftime("%H-%M-%S-%f"))
                    return True
                else:
                    count -= 1
                    # 1s检测一次，20s没有接听，则失败
                    print(count, '接听视频电话 --->', datetime.datetime.now().date().strftime('%Y-%m-%d'),
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

    @TestLogger.log('接听视频电话')
    def to_pick_phone_voice(self):
        call = CallPage()
        time.sleep(1)
        count = 30
        try:
            while count > 0:
                # 如果在飞信电话界面，接听电话
                if call.is_element_already_exist('飞信电话_接受'):
                    call.click_locator_key('飞信电话_接受')
                    print('接听飞信电话-->', datetime.datetime.now().date().strftime('%Y-%m-%d'),
                          datetime.datetime.now().time().strftime("%H-%M-%S-%f"))
                    return True
                else:
                    count -= 1
                    # 1s检测一次，20s没有接听，则失败
                    print(count, '接听飞信电话 --->', datetime.datetime.now().date().strftime('%Y-%m-%d'),
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

    # ===============test_call_00010==================

    @TestLogger.log('主叫手机')
    def call_00010_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
            c = 1 * 60
            while c > 0:
                if ('hang_up' not in dic.keys()) or (dic['hang_up'] != 'success') or \
                        (not call.is_element_already_exist('通话_文案_HEAD')):
                    # if not call.is_element_already_exist('通话_文案_HEAD'):
                    # continue
                    c -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    call.click_tag_detail_first_element('[视频通话]')
                    # 判断
                    time.sleep(1)
                    self.assertEqual(call.on_this_page_call_detail(), True)
                    # 详情_通话  详情_视频 详情_返回
                    self.assertEqual(call.is_element_already_exist('详情_通话'), True)
                    self.assertEqual(call.is_element_already_exist('详情_视频按钮'), True)
                    self.assertEqual(call.is_element_already_exist('详情_返回'), True)
                    # 头像  名字  通话时间  通话类型
                    self.assertEqual(call.is_element_already_exist('详情_头像'), True)
                    self.assertEqual(call.is_element_already_exist('详情_名称'), True)
                    self.assertEqual(call.is_element_already_exist('详情_通话时间'), True)
                    self.assertEqual(call.is_element_already_exist('详情_通话时长'), True)
                    self.assertEqual(call.is_text_present('通话记录(视频通话)'), True)
                    # 执行成功，写入成功标志
                    dic['res3'] = 'success'
                    break
            else:
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00010_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    time.sleep(6)
                    call.check_element_tap_screen('视频_时长')
                    call.click_locator_key('视频_挂断')
                    dic['hang_up'] = 'success'
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00010(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00010_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00010_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    # ================test_call_00019=================

    @TestLogger.log('主叫手机')
    def call_00019_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    time.sleep(25)
                    c = 2 * 60
                    while c > 0:
                        if not call.is_element_already_exist('视频_未接听'):
                            # 2秒检测一次
                            c -= 1
                            time.sleep(0.2)
                            continue
                        else:
                            # 执行成功，写入成功标志
                            dic['res3'] = 'success'
                            break
                    else:
                        raise

                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00019_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 写入测试成功标志
            dic['res2'] = 'success'
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00019(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00019_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00019_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    # ================test_call_00020=================

    @TestLogger.log('主叫手机')
    def call_00020_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
            c = 1 * 60
            while c > 0:
                if ('hang_up' not in dic.keys()) or (dic['hang_up'] != 'success') or \
                        (not call.is_element_already_exist('通话_文案_HEAD')):
                    c -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    self.assertEqual(call.is_element_already_exist('通话_文案_HEAD'), True)
                    # 执行成功，写入成功标志
                    dic['res3'] = 'success'
                    break
            else:
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00020_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    time.sleep(6)
                    call.check_element_tap_screen('视频_时长')
                    call.click_locator_key('视频_挂断')
                    dic['hang_up'] = 'success'
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00020(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00020_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00020_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    # ================test_call_00029=================

    @TestLogger.log('主叫手机')
    def call_00029_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_voice_keep_time(dic['cards'])
                    time.sleep(2)
                    call.click_locator_key('呼叫_结束通话')
                    call.wait_for_page_load()
                    call.click_tag_detail_first_element('[飞信电话]')
                    time.sleep(1)
                    call.click_locator_key('详情_通话')
                    time.sleep(1)
                    if not call.is_element_already_exist('拨号_呼叫_呼叫'):
                        raise
                    call.click_locator_key('拨号_呼叫_取消')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00029_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 写入测试成功标志
            dic['res2'] = 'success'
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00029(self):
        """
            1、联网正常已登录
            2、对方已登录
            3、当前页通话记录详情
            4、不限时长成员
            点击电话按钮
            进入不限时长回呼电话
            :return:
        """
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00029_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00029_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    # ================test_call_00046=================

    @TestLogger.log('主叫手机')
    def call_00046_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    dic['pick'] = True
                    c = 1 * 60
                    while c > 0:
                        if 'answer' not in dic.keys() or not dic['answer']:
                            c -= 1
                            time.sleep(2)
                            continue
                        else:
                            self.assertEqual(self.check_video_call_00046(), True)
                            break
                    else:
                        raise
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
        except Exception:
            print('主叫手机出错')
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'
            return

    @TestLogger.log('被叫手机')
    def call_00046_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    dic['answer'] = True
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
            # 写入测试成功标志
        except Exception:
            print('被叫手机出错')
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'
            return

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00046(self):
        """
            1、联网正常已登录
            2、对方已登录
            3、当前页通话记录详情
            4、不限时长成员
            点击电话按钮
            进入不限时长回呼电话
            :return:
        """
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00046_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00046_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00046(self):
        """
        1、4G网络
            2、已登录客户端
            3、当前页面在视频电话页面
            4、已加入家庭网
            5、发起方
            6、已选择一人"	点击呼叫按钮
            跳转至视频通话邀请页面，页面布局左上方为时间显示，
            右上方为静音按钮与免提按钮，背景为默认的前置摄像头，
            下方左边为语音通话入口、中间为挂断按钮、右边为摄像头切换按钮。
        """
        call = CallPage()
        try:
            # 主叫
            time.sleep(6)
            call.check_element_tap_screen('视频_静音')
            self.assertEqual(call.is_element_already_exist('视频_静音'), True)
            call.check_element_tap_screen('视频_免提')
            self.assertEqual(call.is_element_already_exist('视频_免提'), True)
            call.check_element_tap_screen('视频_画笔')
            self.assertEqual(call.is_element_already_exist('视频_画笔'), True)
            call.check_element_tap_screen('视频_切到语音通话')
            self.assertEqual(call.is_element_already_exist('视频_切到语音通话'), True)
            call.check_element_tap_screen('视频_挂断')
            self.assertEqual(call.is_element_already_exist('视频_挂断'), True)
            call.check_element_tap_screen('视频_切换摄像头')
            self.assertEqual(call.is_element_already_exist('视频_切换摄像头'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            try:
                call.check_element_tap_screen('视频_挂断')
                call.click_locator_key('视频_挂断')
            except Exception:
                traceback.print_exc()
                time.sleep(30)

    # ================test_call_00048=================

    @TestLogger.log('主叫手机')
    def call_00048_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00048_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00048(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00048(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00048_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00048_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00048(self):
        """
        1、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），
            大屏为被叫方界面（默认前摄像头）。
            界面右上角为“静音”和“免提”功能，静音默认未选中，
            免提默认选中。提供“切到语音通话”和“切换摄像头”的功能。
        2、跳转至语音通话页面，页面布局上方中间为被叫方头像，头像下方为被叫人名称、号码、时间显示，下方左边为静音按钮、
            中间为切到视频通话按钮、右边为免提按钮，再下方为挂断按钮，背景为灰黑色。
        :return: True
        """
        call = CallPage()
        try:
            call.check_element_tap_screen('视频_免提')
            call.click_locator_key('视频_免提')
            time.sleep(1)
            call.check_element_tap_screen('视频_静音')
            call.click_locator_key('视频_静音')
            self.assertEqual(call.check_if_button_selected('视频_静音'), True)
            time.sleep(1)
            call.check_element_tap_screen('视频_静音')
            self.assertEqual(call.is_element_already_exist('视频_静音'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00049=================

    @TestLogger.log('主叫手机')
    def call_00049_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00049_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00049(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00049(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00049_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00049_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00049(self):
        """
        1、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），
            大屏为被叫方界面（默认前摄像头）。
            界面右上角为“静音”和“免提”功能，静音默认未选中，
            免提默认选中。提供“切到语音通话”和“切换摄像头”的功能。
        2、跳转至语音通话页面，页面布局上方中间为被叫方头像，头像下方为被叫人名称、号码、时间显示，下方左边为静音按钮、
            中间为切到视频通话按钮、右边为免提按钮，再下方为挂断按钮，背景为灰黑色。
        :return: True
        """
        call = CallPage()
        try:
            call.check_element_tap_screen('视频_免提')
            call.click_locator_key('视频_免提')
            self.assertEqual(call.check_if_button_selected('视频_免提'), False)
            call.check_element_tap_screen('视频_静音')
            self.assertEqual(call.is_element_already_exist('视频_静音'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00050=================

    @TestLogger.log('主叫手机')
    def call_00050_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00050_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00050(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00050(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00050_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00050_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00050(self):
        """
        1、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），
            大屏为被叫方界面（默认前摄像头）。
            界面右上角为“静音”和“免提”功能，静音默认未选中，
            免提默认选中。提供“切到语音通话”和“切换摄像头”的功能。
        2、跳转至语音通话页面，页面布局上方中间为被叫方头像，头像下方为被叫人名称、号码、时间显示，下方左边为静音按钮、
            中间为切到视频通话按钮、右边为免提按钮，再下方为挂断按钮，背景为灰黑色。
        :return: True
        """
        call = CallPage()
        try:
            call.check_element_tap_screen('视频_切换摄像头')
            call.click_locator_key('视频_切换摄像头')
            call.check_element_tap_screen('视频_切换摄像头')
            self.assertEqual(call.is_element_already_exist('视频_切换摄像头'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00051=================

    @TestLogger.log('主叫手机')
    def call_00051_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00051_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00051(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00051(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00051_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00051_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00051(self):
        """
        1、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），
            大屏为被叫方界面（默认前摄像头）。
            界面右上角为“静音”和“免提”功能，静音默认未选中，
            免提默认选中。提供“切到语音通话”和“切换摄像头”的功能。
        2、跳转至语音通话页面，页面布局上方中间为被叫方头像，头像下方为被叫人名称、号码、时间显示，下方左边为静音按钮、
            中间为切到视频通话按钮、右边为免提按钮，再下方为挂断按钮，背景为灰黑色。
        :return: True
        """
        call = CallPage()
        try:
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')
            self.assertEqual(call.is_element_already_exist('视频_通话结束'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False

    # ================test_call_00052_01=================

    @TestLogger.log('主叫手机')
    def call_00052_01_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00052_02_01(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00052_01(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00052_01(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00052_01_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00052_02_01, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00052_01(self):
        """
        1、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），
            大屏为被叫方界面（默认前摄像头）。
            界面右上角为“静音”和“免提”功能，静音默认未选中，
            免提默认选中。提供“切到语音通话”和“切换摄像头”的功能。
        2、跳转至语音通话页面，页面布局上方中间为被叫方头像，头像下方为被叫人名称、号码、时间显示，下方左边为静音按钮、
            中间为切到视频通话按钮、右边为免提按钮，再下方为挂断按钮，背景为灰黑色。
        :return: True
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_免提')
            self.assertEqual(call.is_element_already_exist('视频_免提'), True)
            self.assertEqual(call.check_if_button_selected('视频_免提'), True)
            call.check_element_tap_screen('视频_静音')
            self.assertEqual(call.is_element_already_exist('视频_静音'), True)
            self.assertEqual(call.check_if_button_selected('视频_静音'), False)
            call.check_element_tap_screen('视频_切到语音通话')
            self.assertEqual(call.is_element_already_exist('视频_切到语音通话'), True)
            call.check_element_tap_screen('视频_切换摄像头')
            self.assertEqual(call.is_element_already_exist('视频_切换摄像头'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00052_02=================

    @TestLogger.log('主叫手机')
    def call_00052_01_02(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00052_02_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00052_02(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00052_02(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00052_01_02, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00052_02_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00052_02(self):
        """
        1、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），
            大屏为被叫方界面（默认前摄像头）。
            界面右上角为“静音”和“免提”功能，静音默认未选中，
            免提默认选中。提供“切到语音通话”和“切换摄像头”的功能。
        2、跳转至语音通话页面，页面布局上方中间为被叫方头像，头像下方为被叫人名称、号码、时间显示，下方左边为静音按钮、
            中间为切到视频通话按钮、右边为免提按钮，再下方为挂断按钮，背景为灰黑色。
        :return: True
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_切到语音通话')
            call.click_locator_key('视频_切到语音通话')
            time.sleep(1)
            self.assertEqual(call.is_element_already_exist('语音_头像'), True)
            self.assertEqual(call.is_element_already_exist('语音_备注'), True)
            self.assertEqual(call.is_element_already_exist('语音_电话'), True)
            self.assertEqual(call.is_element_already_exist('语音_时长'), True)
            self.assertEqual(call.is_element_already_exist('语音_免提'), True)
            self.assertEqual(call.is_element_already_exist('语音_切到视频通话'), True)
            self.assertEqual(call.is_element_already_exist('语音_静音'), True)
            self.assertEqual(call.is_element_already_exist('语音_挂断'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00053=================

    @TestLogger.log('主叫手机')
    def call_00053_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00053_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00053(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00053(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00053_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00053_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00053(self):
        """
        1、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），
            大屏为被叫方界面（默认前摄像头）。
            界面右上角为“静音”和“免提”功能，静音默认未选中，
            免提默认选中。提供“切到语音通话”和“切换摄像头”的功能。
        2、跳转至语音通话页面，页面布局上方中间为被叫方头像，头像下方为被叫人名称、号码、时间显示，下方左边为静音按钮、
            中间为切到视频通话按钮、右边为免提按钮，再下方为挂断按钮，背景为灰黑色。
        :return: True
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('语音_静音')
            self.assertEqual(call.is_element_already_exist('语音_静音'), True)
            self.assertEqual(call.check_if_button_selected('语音_静音'), False)
            call.check_element_tap_screen('语音_静音')
            call.click_locator_key('语音_静音')
            self.assertEqual(call.check_if_button_selected('语音_静音'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00054=================

    @TestLogger.log('主叫手机')
    def call_00054_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00054_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00054(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00054(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00054_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00054_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00054(self):
        """
        1、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），
            大屏为被叫方界面（默认前摄像头）。
            界面右上角为“静音”和“免提”功能，静音默认未选中，
            免提默认选中。提供“切到语音通话”和“切换摄像头”的功能。
        2、跳转至语音通话页面，页面布局上方中间为被叫方头像，头像下方为被叫人名称、号码、时间显示，下方左边为静音按钮、
            中间为切到视频通话按钮、右边为免提按钮，再下方为挂断按钮，背景为灰黑色。
        :return: True
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_免提')
            self.assertEqual(call.is_element_already_exist('视频_免提'), True)
            self.assertEqual(call.check_if_button_selected('视频_免提'), True)
            call.check_element_tap_screen('视频_免提')
            call.click_locator_key('视频_免提')
            self.assertEqual(call.check_if_button_selected('视频_免提'), False)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00055=================

    @TestLogger.log('主叫手机')
    def call_00055_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00055_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00055(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00055(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00055_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00055_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00055(self):
        """
        1、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），
            大屏为被叫方界面（默认前摄像头）。
            界面右上角为“静音”和“免提”功能，静音默认未选中，
            免提默认选中。提供“切到语音通话”和“切换摄像头”的功能。
        2、跳转至语音通话页面，页面布局上方中间为被叫方头像，头像下方为被叫人名称、号码、时间显示，下方左边为静音按钮、
            中间为切到视频通话按钮、右边为免提按钮，再下方为挂断按钮，背景为灰黑色。
        :return: True
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_切换摄像头')
            call.click_locator_key('视频_切换摄像头')
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00056=================

    @TestLogger.log('主叫手机')
    def call_00056_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00056_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00056(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00056(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00056_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00056_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00056(self):
        """
        1、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），
            大屏为被叫方界面（默认前摄像头）。
            界面右上角为“静音”和“免提”功能，静音默认未选中，
            免提默认选中。提供“切到语音通话”和“切换摄像头”的功能。
        2、跳转至语音通话页面，页面布局上方中间为被叫方头像，头像下方为被叫人名称、号码、时间显示，下方左边为静音按钮、
            中间为切到视频通话按钮、右边为免提按钮，再下方为挂断按钮，背景为灰黑色。
        :return: True
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')
            self.assertEqual(call.is_element_already_exist('视频_通话结束'), True)
            time.sleep(5)
            self.assertEqual(call.is_element_already_exist('通话_文案_HEAD'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False

    # ================test_call_00057=================

    @TestLogger.log('主叫手机')
    def call_00057_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00057_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00057(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00057(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00057_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00057_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00057(self):
        """
        1、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），
            大屏为被叫方界面（默认前摄像头）。
            界面右上角为“静音”和“免提”功能，静音默认未选中，
            免提默认选中。提供“切到语音通话”和“切换摄像头”的功能。
        2、跳转至语音通话页面，页面布局上方中间为被叫方头像，头像下方为被叫人名称、号码、时间显示，下方左边为静音按钮、
            中间为切到视频通话按钮、右边为免提按钮，再下方为挂断按钮，背景为灰黑色。
        :return: True
        """
        call = CallPage()
        try:
            time.sleep(2)
            call.click_locator_key('视频_小屏')
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00058=================

    @TestLogger.log('主叫手机')
    def call_00058_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00058_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00058(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00058(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00058_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00058_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00058(self):
        """
        1、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），
            大屏为被叫方界面（默认前摄像头）。
            界面右上角为“静音”和“免提”功能，静音默认未选中，
            免提默认选中。提供“切到语音通话”和“切换摄像头”的功能。
        2、跳转至语音通话页面，页面布局上方中间为被叫方头像，头像下方为被叫人名称、号码、时间显示，下方左边为静音按钮、
            中间为切到视频通话按钮、右边为免提按钮，再下方为挂断按钮，背景为灰黑色。
        :return: True
        """
        call = CallPage()
        try:
            time.sleep(2)
            self.assertEqual(call.is_element_already_exist('视频接听_头像'), True)
            self.assertEqual(call.is_element_already_exist('视频接听_备注'), True)
            self.assertEqual(call.is_element_already_exist('视频接听_电话号码'), True)
            self.assertEqual(call.is_element_already_exist('视频接听_提示文本'), True)
            self.assertEqual(call.is_element_already_exist('视频接听_接听'), True)
            self.assertEqual(call.is_element_already_exist('视频接听_拒接'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.click_locator_key('视频接听_拒接')

    # ================test_call_00059=================

    @TestLogger.log('主叫手机')
    def call_00059_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    time.sleep(25)
                    c = 2 * 60
                    while c > 0:
                        if not call.is_element_already_exist('视频_未接听'):
                            # 2秒检测一次
                            c -= 1
                            time.sleep(0.2)
                            continue
                        else:
                            # 执行成功，写入成功标志
                            dic['res3'] = 'success'
                            break
                    else:
                        raise

                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00059_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 写入成功标志
            dic['res2'] = 'success'
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00059(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00059_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00059_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    # ================test_call_00060=================

    @TestLogger.log('主叫手机')
    def call_00060_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00060_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00060(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00060(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00060_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00060_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00060(self):
        """
        1、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），
            大屏为被叫方界面（默认前摄像头）。
            界面右上角为“静音”和“免提”功能，静音默认未选中，
            免提默认选中。提供“切到语音通话”和“切换摄像头”的功能。
        2、跳转至语音通话页面，页面布局上方中间为被叫方头像，头像下方为被叫人名称、号码、时间显示，下方左边为静音按钮、
            中间为切到视频通话按钮、右边为免提按钮，再下方为挂断按钮，背景为灰黑色。
        :return: True
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('语音_静音')
            call.click_locator_key('语音_静音')
            self.assertEqual(call.check_if_button_selected('语音_静音'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00061=================

    @TestLogger.log('主叫手机')
    def call_00061_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00061_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00061(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00061(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00061_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00061_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00061(self):
        """
        1、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），
            大屏为被叫方界面（默认前摄像头）。
            界面右上角为“静音”和“免提”功能，静音默认未选中，
            免提默认选中。提供“切到语音通话”和“切换摄像头”的功能。
        2、跳转至语音通话页面，页面布局上方中间为被叫方头像，头像下方为被叫人名称、号码、时间显示，下方左边为静音按钮、
            中间为切到视频通话按钮、右边为免提按钮，再下方为挂断按钮，背景为灰黑色。
        :return: True
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_免提')
            call.click_locator_key('视频_免提')
            self.assertEqual(call.check_if_button_selected('视频_免提'), False)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00063=================

    @TestLogger.log('主叫手机')
    def call_00063_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00063_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00063(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00063(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00063_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00063_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00063(self):
        """
        1、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），
            大屏为被叫方界面（默认前摄像头）。
            界面右上角为“静音”和“免提”功能，静音默认未选中，
            免提默认选中。提供“切到语音通话”和“切换摄像头”的功能。
        2、跳转至语音通话页面，页面布局上方中间为被叫方头像，头像下方为被叫人名称、号码、时间显示，下方左边为静音按钮、
            中间为切到视频通话按钮、右边为免提按钮，再下方为挂断按钮，背景为灰黑色。
        :return: True
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_切到语音通话')
            call.click_locator_key('视频_切到语音通话')
            time.sleep(2)
            call.click_locator_key('语音_切到视频通话')
            self.assertEqual(call.is_element_already_exist('切视频_头像'), True)
            self.assertEqual(call.is_element_already_exist('切视频_备注'), True)
            self.assertEqual(call.is_element_already_exist('切视频_电话号码'), True)
            self.assertEqual(call.is_element_already_exist('切视频_提示文本'), True)
            self.assertEqual(call.is_element_already_exist('语音_挂断'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.click_locator_key('语音_挂断')

    # ================test_call_00064=================

    @TestLogger.log('主叫手机')
    def call_00064_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00064_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00064(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00064(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00064_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00064_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00064(self):
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_切到语音通话')
            call.click_locator_key('视频_切到语音通话')
            time.sleep(2)
            call.click_locator_key('语音_切到视频通话')
            time.sleep(1)
            call.click_locator_key('语音_挂断')
            self.assertEqual(call.is_element_already_exist('视频_通话结束'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False

    # ================test_call_00065=================

    @TestLogger.log('主叫手机')
    def call_00065_01(self, dic):
        call = CallPage()
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
            count = 1 * 60
            while count > 0:
                if ('to_video' not in dic.keys()) or (not dic['to_video']):
                    count -= 1
                    # 2秒检查一次
                    time.sleep(2)
                    continue
                else:
                    time.sleep(1)
                    self.assertEqual(call.is_text_present('发起视频请求'), True)
                    call.click_text('接受')
                    time.sleep(6)
                    self.assertEqual(call.is_element_already_exist('视频_小屏'), True)
                    break
            else:
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'
        finally:
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    @TestLogger.log('被叫手机')
    def call_00065_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    time.sleep(6)
                    call.check_element_tap_screen('视频_切到语音通话')
                    call.click_locator_key('视频_切到语音通话')
                    time.sleep(2)
                    call.click_locator_key('语音_切到视频通话')
                    dic['to_video'] = True
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00065(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00065_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00065_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    # ================test_call_00066=================

    @TestLogger.log('主叫手机')
    def call_00066_01(self, dic):
        call = CallPage()
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
            count = 1 * 60
            while count > 0:
                if ('to_video' not in dic.keys()) or (not dic['to_video']):
                    count -= 1
                    # 2秒检查一次
                    time.sleep(2)
                    continue
                else:
                    time.sleep(1)
                    self.assertEqual(call.is_text_present('发起视频请求'), True)
                    call.click_text('取消')
                    time.sleep(6)
                    self.assertEqual(call.is_element_already_exist('语音_切到视频通话'), True)
                    break
            else:
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'
        finally:
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    @TestLogger.log('被叫手机')
    def call_00066_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    time.sleep(6)
                    call.check_element_tap_screen('视频_切到语音通话')
                    call.click_locator_key('视频_切到语音通话')
                    time.sleep(2)
                    call.click_locator_key('语音_切到视频通话')
                    dic['to_video'] = True
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00066(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00066_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00066_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    # ================test_call_00067=================

    @TestLogger.log('主叫手机')
    def call_00067_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    self.check_video_call_00067()
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00067_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00067(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00067_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00067_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00067(self):
        call = CallPage()
        try:
            self.assertEqual(call.is_element_already_exist('视频主叫_头像'), True)
            self.assertEqual(call.is_element_already_exist('视频主叫_名称'), True)
            self.assertEqual(call.is_element_already_exist('视频主叫_电话'), True)
            self.assertEqual(call.is_text_present('网络视频通话呼叫中'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.click_locator_key('视频主叫_挂断')

    # ================test_call_00068=================

    @TestLogger.log('主叫手机')
    def call_00068_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00068_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00068(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00068(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00068_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00068_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00068(self):
        """
        1、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），
            大屏为被叫方界面（默认前摄像头）。
            界面右上角为“静音”和“免提”功能，静音默认未选中，
            免提默认选中。提供“切到语音通话”和“切换摄像头”的功能。
        2、跳转至语音通话页面，页面布局上方中间为被叫方头像，头像下方为被叫人名称、号码、时间显示，下方左边为静音按钮、
            中间为切到视频通话按钮、右边为免提按钮，再下方为挂断按钮，背景为灰黑色。
        :return: True
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_切到语音通话')
            call.click_locator_key('视频_切换摄像头')
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.click_locator_key('语音_挂断')

    # ================test_call_00069=================

    @TestLogger.log('主叫手机')
    def call_00069_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00069_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00069(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00069(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00069_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00069_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00069(self):
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_切到语音通话')
            call.click_locator_key('视频_切到语音通话')
            time.sleep(2)
            call.click_locator_key('语音_切到视频通话')
            time.sleep(1)
            call.click_locator_key('语音_挂断')
            self.assertEqual(call.is_element_already_exist('视频_通话结束'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False

    # ================test_call_00070=================

    @TestLogger.log('主叫手机')
    def call_00070_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00070_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00070(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00070(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00070_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00070_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00070(self):
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_切到语音通话')
            call.click_locator_key('视频_切到语音通话')
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.click_locator_key('语音_挂断')

    # ================test_call_00071=================

    @TestLogger.log('主叫手机')
    def call_00071_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00071_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00071(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00071(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00071_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00071_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00071(self):
        """
        1、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），
            大屏为被叫方界面（默认前摄像头）。
            界面右上角为“静音”和“免提”功能，静音默认未选中，
            免提默认选中。提供“切到语音通话”和“切换摄像头”的功能。
        2、跳转至语音通话页面，页面布局上方中间为被叫方头像，头像下方为被叫人名称、号码、时间显示，下方左边为静音按钮、
            中间为切到视频通话按钮、右边为免提按钮，再下方为挂断按钮，背景为灰黑色。
        :return: True
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('语音_静音')
            self.assertEqual(call.is_element_already_exist('语音_静音'), True)
            self.assertEqual(call.check_if_button_selected('语音_静音'), False)
            call.check_element_tap_screen('语音_静音')
            call.click_locator_key('语音_静音')
            self.assertEqual(call.check_if_button_selected('语音_静音'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00072=================

    @TestLogger.log('主叫手机')
    def call_00072_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00072_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00072(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00072(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00072_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00072_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00072(self):
        """
        1、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），
            大屏为被叫方界面（默认前摄像头）。
            界面右上角为“静音”和“免提”功能，静音默认未选中，
            免提默认选中。提供“切到语音通话”和“切换摄像头”的功能。
        2、跳转至语音通话页面，页面布局上方中间为被叫方头像，头像下方为被叫人名称、号码、时间显示，下方左边为静音按钮、
            中间为切到视频通话按钮、右边为免提按钮，再下方为挂断按钮，背景为灰黑色。
        :return: True
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_免提')
            self.assertEqual(call.is_element_already_exist('视频_免提'), True)
            self.assertEqual(call.check_if_button_selected('视频_免提'), True)
            call.check_element_tap_screen('视频_免提')
            call.click_locator_key('视频_免提')
            self.assertEqual(call.check_if_button_selected('视频_免提'), False)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00073=================

    @TestLogger.log('主叫手机')
    def call_00073_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00073_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00073(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00073(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00073_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00073_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00073(self):
        """
        1、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），
            大屏为被叫方界面（默认前摄像头）。
            界面右上角为“静音”和“免提”功能，静音默认未选中，
            免提默认选中。提供“切到语音通话”和“切换摄像头”的功能。
        2、跳转至语音通话页面，页面布局上方中间为被叫方头像，头像下方为被叫人名称、号码、时间显示，下方左边为静音按钮、
            中间为切到视频通话按钮、右边为免提按钮，再下方为挂断按钮，背景为灰黑色。
        :return: True
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_切换摄像头')
            call.click_locator_key('视频_切换摄像头')
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00074=================

    @TestLogger.log('主叫手机')
    def call_00074_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00074_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00074(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00074(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00074_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00074_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00074(self):
        """
        1、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），
            大屏为被叫方界面（默认前摄像头）。
            界面右上角为“静音”和“免提”功能，静音默认未选中，
            免提默认选中。提供“切到语音通话”和“切换摄像头”的功能。
        2、跳转至语音通话页面，页面布局上方中间为被叫方头像，头像下方为被叫人名称、号码、时间显示，下方左边为静音按钮、
            中间为切到视频通话按钮、右边为免提按钮，再下方为挂断按钮，背景为灰黑色。
        :return: True
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')
            self.assertEqual(call.is_element_already_exist('视频_通话结束'), True)
            time.sleep(5)
            self.assertEqual(call.is_element_already_exist('通话_文案_HEAD'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False

    # ================test_call_00075=================

    @TestLogger.log('主叫手机')
    def call_00075_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00075_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00075(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00075(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00075_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00075_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00075(self):
        """
        1、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），
            大屏为被叫方界面（默认前摄像头）。
            界面右上角为“静音”和“免提”功能，静音默认未选中，
            免提默认选中。提供“切到语音通话”和“切换摄像头”的功能。
        2、跳转至语音通话页面，页面布局上方中间为被叫方头像，头像下方为被叫人名称、号码、时间显示，下方左边为静音按钮、
            中间为切到视频通话按钮、右边为免提按钮，再下方为挂断按钮，背景为灰黑色。
        :return: True
        """
        call = CallPage()
        try:
            time.sleep(2)
            call.click_locator_key('视频_小屏')
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00077=================

    @TestLogger.log('主叫手机')
    def call_00077_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00077_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00077(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00077(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00077_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00077_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00077(self):
        """
        查看页面显示	弹出“通话结束”提示框，回到呼叫前的页面中，
        在底部“挂断”按钮上面展示
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')
            self.assertEqual(call.is_element_already_exist('视频_通话结束'), True)
            time.sleep(4)
            self.assertEqual(call.is_element_already_exist('通话_文案_HEAD'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False

    # ================test_call_00078=================

    @TestLogger.log('主叫手机')
    def call_00078_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    time.sleep(25)
                    c = 2 * 60
                    while c > 0:
                        if not call.is_element_already_exist('视频_未接听'):
                            # 2秒检测一次
                            c -= 1
                            time.sleep(0.2)
                            continue
                        else:
                            # 执行成功，写入成功标志
                            dic['res3'] = 'success'
                            break
                    else:
                        raise

                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00078_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 写入测试成功标志
            dic['res2'] = 'success'
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00078(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00078_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00078_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    # ================test_call_00079=================

    @TestLogger.log('主叫手机')
    def call_00079_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00079_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00079(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00079(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00079_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00079_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00079(self):
        call = CallPage()
        try:
            time.sleep(6)
            call.click_locator_key('视频接听_拒接')
            self.assertEqual(call.is_element_already_exist('视频_通话结束'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False

    # ================test_call_00080=================

    @TestLogger.log('主叫手机')
    def call_00080_01(self, dic):
        # 主叫手机初始化
        call = CallPage()
        try:
            Preconditions.initialize_class('IOS-移动')
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
            # 循环检测60次 * 2s
            c = 1 * 60
            while c > 0:
                if ('to_video' not in dic.keys()) or (not dic['to_video']):
                    c -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    # 拨打电话
                    time.sleep(1)
                    call.click_text('接受')
                    time.sleep(3)
                    call.check_element_tap_screen('视频_切到语音通话')
                    self.assertEqual(call.is_element_already_exist('视频_切到语音通话'), True)
                    time.sleep(12)
                    call.check_element_tap_screen('视频_切到语音通话')
                    call.click_locator_key('视频_切到语音通话')
                    time.sleep(2)
                    self.assertEqual(call.is_element_already_exist('语音_切到视频通话'), True)
                    # 执行成功，写入成功标志
                    dic['res4'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'
        finally:
            if call.is_element_already_exist('视频_小屏'):
                call.check_element_tap_screen('视频_挂断')
                call.click_locator_key('视频_挂断')
            if call.is_element_already_exist('语音_挂断'):
                call.click_locator_key('语音_挂断')

    @TestLogger.log('被叫手机')
    def call_00080_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00080(dic), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00080(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00080_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00080_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00080(self, dic):
        """
        查看页面显示	弹出“通话结束”提示框，回到呼叫前的页面中，
        在底部“挂断”按钮上面展示
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_切到语音通话')
            call.click_locator_key('视频_切到语音通话')
            time.sleep(1)
            self.assertEqual(call.is_element_already_exist('语音_切到视频通话'), True)
            call.click_locator_key('语音_切到视频通话')
            dic['to_video'] = True
            return True
        except Exception:
            traceback.print_exc()
            if call.is_element_already_exist('视频_小屏'):
                call.check_element_tap_screen('视频_挂断')
                call.click_locator_key('视频_挂断')
            if call.is_element_already_exist('语音_挂断'):
                call.click_locator_key('语音_挂断')
            return False

    # ================test_call_00081=================

    @TestLogger.log('主叫手机')
    def call_00081_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00081_02(self, dic):
        call = CallPage()
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00081(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00081(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00081_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00081_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00081(self):
        """
            点击“编辑笔”按钮
            则在下方依次弹出“线条调色”、“线条粗细”、“橡皮檫粗细”、“清除涂鸦”、“表情贴纸”和“分享”；
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_免提')
            call.click_locator_key('视频_免提')
            call.check_element_tap_screen('视频_切到语音通话')
            call.click_locator_key('视频_画笔')
            time.sleep(1)
            self.assertEqual(call.is_element_already_exist('涂鸦_圆点'), True)
            self.assertEqual(call.is_element_already_exist('涂鸦_线条'), True)
            self.assertEqual(call.is_element_already_exist('涂鸦_表情'), True)
            self.assertEqual(call.is_element_already_exist('涂鸦_橡皮'), True)
            self.assertEqual(call.is_element_already_exist('涂鸦_删除'), True)
            self.assertEqual(call.is_element_already_exist('涂鸦_分享'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            if call.is_element_already_exist('涂鸦_返回'):
                call.click_locator_key('涂鸦_返回')
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00082=================

    @TestLogger.log('主叫手机')
    def call_00082_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00082_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00082(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00082(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00082_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00082_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00082(self):
        """
            点击“编辑笔”按钮
            则在下方依次弹出“线条调色”、“线条粗细”、“橡皮檫粗细”、“清除涂鸦”、“表情贴纸”和“分享”；
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_免提')
            call.click_locator_key('视频_免提')
            call.check_element_tap_screen('视频_切到语音通话')
            call.click_locator_key('视频_画笔')
            time.sleep(1)
            call.click_locator_key('涂鸦_圆点')
            time.sleep(1)
            call.click_locator_key('涂鸦_橙色')
            time.sleep(1)
            call.swipe_by_direction_element('涂鸦_画布', 'down')
            time.sleep(2)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            if call.is_element_already_exist('涂鸦_返回'):
                call.click_locator_key('涂鸦_返回')
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00083=================

    @TestLogger.log('主叫手机')
    def call_00083_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00083_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00083(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00083(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00083_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00083_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00083(self):
        """
            点击“编辑笔”按钮
            则在下方依次弹出“线条调色”、“线条粗细”、“橡皮檫粗细”、“清除涂鸦”、“表情贴纸”和“分享”；
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_免提')
            call.click_locator_key('视频_免提')
            call.check_element_tap_screen('视频_切到语音通话')
            call.click_locator_key('视频_画笔')
            time.sleep(1)
            call.click_locator_key('涂鸦_表情')
            time.sleep(1)
            call.click_locator_key('涂鸦_表情1')
            time.sleep(1)
            call.click_locator_key('涂鸦_画布')
            time.sleep(2)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            if call.is_element_already_exist('涂鸦_返回'):
                call.click_locator_key('涂鸦_返回')
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00084_01=================

    @TestLogger.log('主叫手机')
    def call_00084_01_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00084_01_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00084_01(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00084_01(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00084_01_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00084_01_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00084_01(self):
        """
            点击“编辑笔”按钮
            则在下方依次弹出“线条调色”、“线条粗细”、“橡皮檫粗细”、“清除涂鸦”、“表情贴纸”和“分享”；
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_免提')
            call.click_locator_key('视频_免提')
            call.check_element_tap_screen('视频_切到语音通话')
            call.click_locator_key('视频_画笔')
            time.sleep(1)
            call.click_locator_key('涂鸦_线条')
            time.sleep(2)
            call.swipe_to_direction('涂鸦_滑块', 'right')
            call.click_locator_key('涂鸦_线条')
            time.sleep(1)
            call.swipe_by_direction_element('涂鸦_画布', 'down')
            time.sleep(2)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            if call.is_element_already_exist('涂鸦_返回'):
                call.click_locator_key('涂鸦_返回')
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00084_02=================

    @TestLogger.log('主叫手机')
    def call_00084_02_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00084_02_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00084_02(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00084_02(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00084_02_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00084_02_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00084_02(self):
        """
            点击“编辑笔”按钮
            则在下方依次弹出“线条调色”、“线条粗细”、“橡皮檫粗细”、“清除涂鸦”、“表情贴纸”和“分享”；
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_免提')
            call.click_locator_key('视频_免提')
            call.check_element_tap_screen('视频_切到语音通话')
            call.click_locator_key('视频_画笔')
            time.sleep(1)
            call.click_locator_key('涂鸦_线条')
            time.sleep(2)
            call.swipe_to_direction('涂鸦_滑块', 'left')
            call.click_locator_key('涂鸦_线条')
            time.sleep(1)
            call.swipe_by_direction_element('涂鸦_画布', 'down')
            time.sleep(2)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            if call.is_element_already_exist('涂鸦_返回'):
                call.click_locator_key('涂鸦_返回')
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00085_01=================

    @TestLogger.log('主叫手机')
    def call_00085_01_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00085_01_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00085_01(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00085_01(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00085_01_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00085_01_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00085_01(self):
        """
            点击“编辑笔”按钮
            则在下方依次弹出“线条调色”、“线条粗细”、“橡皮檫粗细”、“清除涂鸦”、“表情贴纸”和“分享”；
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_免提')
            call.click_locator_key('视频_免提')
            call.check_element_tap_screen('视频_切到语音通话')
            call.click_locator_key('视频_画笔')
            time.sleep(1)
            call.swipe_by_direction_element('涂鸦_画布', 'right')
            time.sleep(1)
            call.click_locator_key('涂鸦_橡皮')
            time.sleep(2)
            call.swipe_to_direction('涂鸦_滑块', 'right')
            call.click_locator_key('涂鸦_橡皮')
            time.sleep(1)
            call.swipe_by_direction_element('涂鸦_画布', 'down')
            time.sleep(2)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            if call.is_element_already_exist('涂鸦_返回'):
                call.click_locator_key('涂鸦_返回')
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00085_02=================

    @TestLogger.log('主叫手机')
    def call_00085_02_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00085_02_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00085_02(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00085_02(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00085_02_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00085_02_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00085_02(self):
        """
            点击“编辑笔”按钮
            则在下方依次弹出“线条调色”、“线条粗细”、“橡皮檫粗细”、“清除涂鸦”、“表情贴纸”和“分享”；
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_免提')
            call.click_locator_key('视频_免提')
            call.check_element_tap_screen('视频_切到语音通话')
            call.click_locator_key('视频_画笔')
            time.sleep(1)
            call.swipe_by_direction_element('涂鸦_画布', 'right')
            time.sleep(1)
            call.click_locator_key('涂鸦_橡皮')
            time.sleep(2)
            call.swipe_to_direction('涂鸦_滑块', 'left')
            call.click_locator_key('涂鸦_橡皮')
            time.sleep(1)
            call.swipe_by_direction_element('涂鸦_画布', 'down')
            time.sleep(2)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            if call.is_element_already_exist('涂鸦_返回'):
                call.click_locator_key('涂鸦_返回')
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00086=================

    @TestLogger.log('主叫手机')
    def call_00086_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00086_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00086(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00086(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00086_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00086_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00086(self):
        """
            点击“编辑笔”按钮
            则在下方依次弹出“线条调色”、“线条粗细”、“橡皮檫粗细”、“清除涂鸦”、“表情贴纸”和“分享”；
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_免提')
            call.click_locator_key('视频_免提')
            call.check_element_tap_screen('视频_切到语音通话')
            call.click_locator_key('视频_画笔')
            time.sleep(1)
            call.swipe_by_direction_element('涂鸦_画布', 'right')
            call.click_locator_key('涂鸦_删除')
            time.sleep(1)
            if call.is_element_already_exist('涂鸦_您要清除所有涂鸦'):
                call.click_locator_key('涂鸦_删除_取消')
                time.sleep(1)
            call.click_locator_key('涂鸦_删除')
            time.sleep(1)
            if call.is_element_already_exist('涂鸦_您要清除所有涂鸦'):
                call.click_locator_key('涂鸦_删除_确定')
                time.sleep(1)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            if call.is_element_already_exist('视频_画笔'):
                call.click_locator_key('视频_画笔')
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00087=================

    @TestLogger.log('主叫手机')
    def call_00087_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00087_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00087(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00087(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00087_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00087_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00087(self):
        """
            点击“编辑笔”按钮
            则在下方依次弹出“线条调色”、“线条粗细”、“橡皮檫粗细”、“清除涂鸦”、“表情贴纸”和“分享”；
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_免提')
            call.click_locator_key('视频_免提')
            call.check_element_tap_screen('视频_切到语音通话')
            call.click_locator_key('视频_画笔')
            time.sleep(1)
            call.click_locator_key('涂鸦_分享')
            time.sleep(1)
            self.assertEqual(call.is_element_already_exist('涂鸦_分享到'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.click_locator_key('涂鸦_画布')
            call.click_locator_key('涂鸦_返回')
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00096=================

    @TestLogger.log('主叫手机')
    def call_00096_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
            c = 1 * 60
            while c > 0:
                if ('answer' not in dic.keys()) or (not dic['answer']):
                    c -= 1
                    time.sleep(2)
                    continue
                else:
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00096(), True)
                    dic['res4'] = 'success'
                    break
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00096_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    time.sleep(2)
                    dic['answer'] = True
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00096(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00096_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00096_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00096(self):
        """
            点击“编辑笔”按钮
            则在下方依次弹出“线条调色”、“线条粗细”、“橡皮檫粗细”、“清除涂鸦”、“表情贴纸”和“分享”；
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_免提')
            call.click_locator_key('视频_免提')
            call.check_element_tap_screen('视频_切到语音通话')
            call.click_locator_key('视频_画笔')
            self.assertEqual(call.is_element_already_exist('涂鸦_圆点'), True)
            self.assertEqual(call.is_element_already_exist('视频_静音'), False)
            self.assertEqual(call.is_element_already_exist('视频_免提'), False)
            self.assertEqual(call.is_element_already_exist('视频_挂断'), False)
            self.assertEqual(call.is_element_already_exist('视频_切换摄像头'), False)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.click_locator_key('涂鸦_画布')
            call.click_locator_key('涂鸦_返回')
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00097=================

    @TestLogger.log('主叫手机')
    def call_00097_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
            c = 1 * 60
            while c > 0:
                if ('answer' not in dic.keys()) or (not dic['answer']):
                    c -= 1
                    time.sleep(2)
                    continue
                else:
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00097(), True)
                    dic['doodle'] = True
                    break
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00097_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    time.sleep(2)
                    dic['answer'] = True
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
            c = 1 * 60
            while c > 0:
                # 循环判断元素是否存在
                if ('doodle' not in dic.keys()) or (not dic['doodle']):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 检查项目
                    self.assertEqual(self.check_video_call_00097_b(), True)
                    time.sleep(2)
                    # 写入测试成功标志
                    dic['res3'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00097(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00097_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00097_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00097(self):
        """
            点击“编辑笔”按钮
            则在下方依次弹出“线条调色”、“线条粗细”、“橡皮檫粗细”、“清除涂鸦”、“表情贴纸”和“分享”；
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_免提')
            call.click_locator_key('视频_免提')
            call.check_element_tap_screen('视频_切到语音通话')
            call.click_locator_key('视频_画笔')
            return True
        except Exception:
            traceback.print_exc()
            if call.is_element_already_exist('涂鸦_返回'):
                call.click_locator_key('涂鸦_返回')
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')
            return False

    @TestLogger.log()
    def check_video_call_00097_b(self):
        """
            点击“编辑笔”按钮
            则在下方依次弹出“线条调色”、“线条粗细”、“橡皮檫粗细”、“清除涂鸦”、“表情贴纸”和“分享”；
        """
        call = CallPage()
        try:
            time.sleep(2)
            self.assertEqual(call.is_element_already_exist('涂鸦_圆点'), True)
            self.assertEqual(call.is_element_already_exist('视频_静音'), False)
            self.assertEqual(call.is_element_already_exist('视频_免提'), False)
            self.assertEqual(call.is_element_already_exist('视频_挂断'), False)
            self.assertEqual(call.is_element_already_exist('视频_切换摄像头'), False)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            if call.is_element_already_exist('涂鸦_返回'):
                call.click_locator_key('涂鸦_返回')
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00098=================

    @TestLogger.log('主叫手机')
    def call_00098_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
            c = 1 * 60
            while c > 0:
                if ('answer' not in dic.keys()) or (not dic['answer']):
                    c -= 1
                    time.sleep(2)
                    continue
                else:
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00098(), True)
                    dic['res4'] = 'success'
                    break
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00098_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    time.sleep(2)
                    dic['answer'] = True
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00098(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00098_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00098_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00098(self):
        """
            点击“编辑笔”按钮
            则在下方依次弹出“线条调色”、“线条粗细”、“橡皮檫粗细”、“清除涂鸦”、“表情贴纸”和“分享”；
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_免提')
            call.click_locator_key('视频_免提')
            call.check_element_tap_screen('视频_切到语音通话')
            call.click_locator_key('视频_画笔')
            time.sleep(2)
            call.click_locator_key('涂鸦_返回')
            time.sleep(2)
            call.check_element_tap_screen('视频_静音')
            self.assertEqual(call.is_element_already_exist('视频_静音'), True)
            call.check_element_tap_screen('视频_免提')
            self.assertEqual(call.is_element_already_exist('视频_免提'), True)
            call.check_element_tap_screen('视频_挂断')
            self.assertEqual(call.is_element_already_exist('视频_挂断'), True)
            call.check_element_tap_screen('视频_切换摄像头')
            self.assertEqual(call.is_element_already_exist('视频_切换摄像头'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            if call.is_element_already_exist('涂鸦_返回'):
                call.click_locator_key('涂鸦_返回')
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_00099=================

    @TestLogger.log('主叫手机')
    def call_00099_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
            c = 1 * 60
            while c > 0:
                if ('answer' not in dic.keys()) or (not dic['answer']):
                    c -= 1
                    time.sleep(2)
                    continue
                else:
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_00099(), True)
                    dic['doodle'] = True
                    break
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_00099_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    time.sleep(2)
                    dic['answer'] = True
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
            c = 1 * 60
            while c > 0:
                # 循环判断元素是否存在
                if ('doodle' not in dic.keys()) or (not dic['doodle']):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 检查项目
                    self.assertEqual(self.check_video_call_00099_b(), True)
                    time.sleep(2)
                    # 写入测试成功标志
                    dic['res3'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_00099(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_00099_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_00099_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_00099(self):
        """
            点击“编辑笔”按钮
            则在下方依次弹出“线条调色”、“线条粗细”、“橡皮檫粗细”、“清除涂鸦”、“表情贴纸”和“分享”；
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_免提')
            call.click_locator_key('视频_免提')
            call.check_element_tap_screen('视频_切到语音通话')
            call.click_locator_key('视频_画笔')
            time.sleep(2)
            call.click_locator_key('涂鸦_返回')
            time.sleep(2)
            return True
        except Exception:
            traceback.print_exc()
            if call.is_element_already_exist('涂鸦_返回'):
                call.click_locator_key('涂鸦_返回')
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')
            return False

    @TestLogger.log()
    def check_video_call_00099_b(self):
        """
            点击“编辑笔”按钮
            则在下方依次弹出“线条调色”、“线条粗细”、“橡皮檫粗细”、“清除涂鸦”、“表情贴纸”和“分享”；
        """
        call = CallPage()
        try:
            time.sleep(2)
            call.check_element_tap_screen('视频_静音')
            self.assertEqual(call.is_element_already_exist('视频_静音'), True)
            call.check_element_tap_screen('视频_免提')
            self.assertEqual(call.is_element_already_exist('视频_免提'), True)
            call.check_element_tap_screen('视频_挂断')
            self.assertEqual(call.is_element_already_exist('视频_挂断'), True)
            call.check_element_tap_screen('视频_切换摄像头')
            self.assertEqual(call.is_element_already_exist('视频_切换摄像头'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            if call.is_element_already_exist('涂鸦_返回'):
                call.click_locator_key('涂鸦_返回')
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_000103=================

    @TestLogger.log('主叫手机')
    def call_000103_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_000103_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_000103(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_000103(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_000103_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_000103_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_000103(self):
        """
            点击“编辑笔”按钮
            则在下方依次弹出“线条调色”、“线条粗细”、“橡皮檫粗细”、“清除涂鸦”、“表情贴纸”和“分享”；
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_免提')
            self.assertEqual(call.check_if_button_selected('视频_免提'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_000104=================

    @TestLogger.log('主叫手机')
    def call_000104_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_000104_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_000104(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_000104(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_000104_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_000104_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_000104(self):
        """
            点击“编辑笔”按钮
            则在下方依次弹出“线条调色”、“线条粗细”、“橡皮檫粗细”、“清除涂鸦”、“表情贴纸”和“分享”；
        """
        call = CallPage()
        try:
            time.sleep(1)
            call.click_screen_center()
            self.assertEqual(call.is_element_already_exist('视频_时长'), False)
            self.assertEqual(call.is_element_already_exist('视频_免提'), False)
            self.assertEqual(call.is_element_already_exist('视频_静音'), False)
            self.assertEqual(call.is_element_already_exist('视频_画笔'), False)
            self.assertEqual(call.is_element_already_exist('视频_挂断'), False)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_000106=================

    @TestLogger.log('主叫手机')
    def call_000106_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_000106_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_000106(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_000106(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_000106_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_000106_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_000106(self):
        """
            点击“编辑笔”按钮
            则在下方依次弹出“线条调色”、“线条粗细”、“橡皮檫粗细”、“清除涂鸦”、“表情贴纸”和“分享”；
        """
        call = CallPage()
        try:
            time.sleep(6)
            self.assertEqual(call.is_element_already_exist('视频_时长'), False)
            self.assertEqual(call.is_element_already_exist('视频_免提'), False)
            self.assertEqual(call.is_element_already_exist('视频_静音'), False)
            self.assertEqual(call.is_element_already_exist('视频_画笔'), False)
            self.assertEqual(call.is_element_already_exist('视频_挂断'), False)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_000107=================

    @TestLogger.log('主叫手机')
    def call_000107_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_000107_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_000107(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_000107(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_000107_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_000107_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_000107(self):
        """
            点击“编辑笔”按钮
            则在下方依次弹出“线条调色”、“线条粗细”、“橡皮檫粗细”、“清除涂鸦”、“表情贴纸”和“分享”；
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.click_screen_center()
            time.sleep(10)
            self.assertEqual(call.is_element_already_exist('视频_时长'), False)
            self.assertEqual(call.is_element_already_exist('视频_免提'), False)
            self.assertEqual(call.is_element_already_exist('视频_静音'), False)
            self.assertEqual(call.is_element_already_exist('视频_画笔'), False)
            self.assertEqual(call.is_element_already_exist('视频_挂断'), False)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_000114_01=================

    @TestLogger.log('主叫手机')
    def call_000114_01_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    time.sleep(2)
                    call.click_locator_key('视频主叫_挂断')
                    time.sleep(5)
                    self.assertEqual(call.is_text_present('视频通话'), True)
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_000114_01_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 写入测试成功标志
            dic['res2'] = 'success'
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_000114_01(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_000114_01_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_000114_01_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    # ================test_call_000114_02=================

    @TestLogger.log('主叫手机')
    def call_000114_02_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    call.pick_up_p2p_video(dic['cards'])
                    time.sleep(2)
                    call.click_locator_key('视频主叫_挂断')
                    time.sleep(5)
                    self.assertEqual(call.is_text_present('视频通话'), True)
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_000114_02_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 写入测试成功标志
            dic['res2'] = 'success'
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_000114_02(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_000114_02_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_000114_02_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    # ================test_call_000114_03=================

    @TestLogger.log('主叫手机')
    def call_000114_03_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    call.pick_up_p2p_video(dic['cards'])
                    time.sleep(2)
                    call.click_locator_key('视频主叫_挂断')
                    dic['hang_up'] = True
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_000114_03_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'hang_up' not in dic.keys() or not dic['hang_up']:
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    time.sleep(3)
                    self.assertEqual(call.is_text_present('视频通话'), True)
                    dic['res2'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            time.sleep(30)
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_000114_03(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_000114_03_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_000114_03_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    # ================test_call_000114_04=================

    @TestLogger.log('主叫手机')
    def call_000114_04_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_voice_keep_time(dic['cards'])
                    time.sleep(3)
                    dic['pick_up'] = True
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_000114_04_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if ('pick_up' not in dic.keys()) or (not dic['pick_up']):
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    time.sleep(3)
                    call.click_locator_key('飞信电话_接受')
                    time.sleep(2)
                    call.click_locator_key('飞信电话_结束通话')
                    time.sleep(3)
                    print('检测。。。。。')
                    self.assertEqual(call.is_text_present('飞信电话'), True)
                    dic['res2'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            time.sleep(30)
            # 写入成功标志
            dic['res2'] = 'fail'

    @unittest.skip('飞信电话接听或拒接都没有通话记录')
    @tags('ALL', 'CMCC_double', 'call')
    def test_call_000114_04(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_000114_04_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_000114_04_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    # ================test_call_000114_05=================

    @TestLogger.log('主叫手机')
    def call_000114_05_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_voice_keep_time(dic['cards'])
                    time.sleep(5)
                    call.click_locator_key('飞信电话_结束通话')
                    time.sleep(5)
                    self.assertEqual(call.is_text_present('飞信电话'), True)
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_000114_05_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 写入测试成功标志
            dic['res2'] = 'success'
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_000114_05(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_000114_05_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_000114_05_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    # ================test_call_000134=================

    @TestLogger.log('主叫手机')
    def call_000134_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_multi_voice_call(dic['cards'])
                    print('打电话了')
                    time.sleep(5)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_000134(), True)
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_000134_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 写入测试成功标志
            dic['res2'] = 'success'
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_000134(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_000134_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_000134_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_000134(self):
        """
            点击“编辑笔”按钮
            则在下方依次弹出“线条调色”、“线条粗细”、“橡皮檫粗细”、“清除涂鸦”、“表情贴纸”和“分享”；
        """
        call = CallPage()
        try:
            time.sleep(5)
            self.assertEqual(call.is_element_already_exist('飞信电话_接受'), True)
            self.assertEqual(call.is_element_already_exist('飞信电话_拒绝'), True)
            call.click_locator_key('飞信电话_拒绝')
            time.sleep(5)
            call.click_locator_key('飞信电话_挂断')
            time.sleep(1)
            call.click_locator_key('多方通话_弹框_确定')
            return True
        except Exception:
            traceback.print_exc()
            time.sleep(65)
            return False

    # ================test_call_000139=================

    @TestLogger.log('主叫手机')
    def call_000139_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            times = call.get_times()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_multi_voice_call(dic['cards'])
                    time.sleep(5)
                    self.assertEqual(call.is_element_already_exist('飞信电话_接受'), True)
                    self.assertEqual(call.is_element_already_exist('飞信电话_拒绝'), True)
                    call.click_locator_key('飞信电话_接受')
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
            time.sleep(dic['t'] * 60)
            for i in range(3):
                if ('hang_up' in dic.keys()) and dic['hang_up']:
                    time.sleep(5)
                    times2 = call.get_times()
                    self.assertEqual(times - times2 >= dic['t'], True)
                    dic['res3'] = 'success'
                    break
                time.sleep(5)
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_000139_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                print('飞信电话-----准备接听')
                if not call.is_element_exist('飞信电话_接受'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_voice(), True)
                    print('电话已接听。。。。')
                    time.sleep(dic['t'] * 60)
                    call.click_locator_key('呼叫_结束通话')
                    print('飞信电话-----挂断')
                    dic['hang_up'] = True
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_000139(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            dic['t'] = 1
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_000139_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_000139_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    # ================test_call_000183=================

    @TestLogger.log('主叫手机')
    def call_000183_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.click_locator_key('拨号键盘')
                    time.sleep(1)
                    for i in dic['cards']:
                        call.click_locator_key('keyboard_{}'.format(i))
                    time.sleep(1)
                    self.assertEqual(call.is_element_already_exist('通话_详情图标'), True)
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_000183_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 写入测试成功标志
            dic['res2'] = 'success'
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_000183(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_000183_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_000183_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    # ================test_call_000185=================

    @TestLogger.log('主叫手机')
    def call_000185_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    self.check_video_call_000185()
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_000185_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_000185(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_000185_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_000185_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_000185(self):
        call = CallPage()
        try:
            self.assertEqual(call.is_element_already_exist('视频主叫_头像'), True)
            self.assertEqual(call.is_element_already_exist('视频主叫_名称'), True)
            self.assertEqual(call.is_element_already_exist('视频主叫_电话'), True)
            self.assertEqual(call.is_text_present('网络视频通话呼叫中'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.click_locator_key('视频主叫_挂断')

    # ================test_call_000187=================

    @TestLogger.log('主叫手机')
    def call_000187_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_multi_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_000187_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('多方视频_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_answer_multi_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_000187(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_000187(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_000187_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_000187_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_000187(self):
        call = CallPage()
        try:
            time.sleep(2)
            self.assertEqual(call.is_element_already_exist('多方视频_免提'), True)
            self.assertEqual(call.is_element_already_exist('多方视频_静音'), True)
            self.assertEqual(call.is_element_already_exist('多方视频_关闭摄像头'), True)
            self.assertEqual(call.is_element_already_exist('多方视频_翻转摄像头'), True)
            self.assertEqual(call.is_element_already_exist('多方视频_缩放'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.click_locator_key('多方视频_挂断')

    # ================test_call_000205=================

    @TestLogger.log('主叫手机')
    def call_000205_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_000205_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_000205(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_000205(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_000205_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_000205_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_000205(self):
        """
        1、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），
            大屏为被叫方界面（默认前摄像头）。
            界面右上角为“静音”和“免提”功能，静音默认未选中，
            免提默认选中。提供“切到语音通话”和“切换摄像头”的功能。
        2、跳转至语音通话页面，页面布局上方中间为被叫方头像，头像下方为被叫人名称、号码、时间显示，下方左边为静音按钮、
            中间为切到视频通话按钮、右边为免提按钮，再下方为挂断按钮，背景为灰黑色。
        :return: True
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_免提')
            self.assertEqual(call.is_element_already_exist('视频_免提'), True)
            self.assertEqual(call.check_if_button_selected('视频_免提'), True)
            call.check_element_tap_screen('视频_免提')
            call.click_locator_key('视频_免提')
            self.assertEqual(call.check_if_button_selected('视频_免提'), False)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_000206=================

    @TestLogger.log('主叫手机')
    def call_000206_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_000206_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_000206(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_000206(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_000206_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_000206_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_000206(self):
        """
        1、显示视频通话接通界面，小屏为主叫方界面（默认为前摄像头），
            大屏为被叫方界面（默认前摄像头）。
            界面右上角为“静音”和“免提”功能，静音默认未选中，
            免提默认选中。提供“切到语音通话”和“切换摄像头”的功能。
        2、跳转至语音通话页面，页面布局上方中间为被叫方头像，头像下方为被叫人名称、号码、时间显示，下方左边为静音按钮、
            中间为切到视频通话按钮、右边为免提按钮，再下方为挂断按钮，背景为灰黑色。
        :return: True
        """
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('语音_静音')
            self.assertEqual(call.is_element_already_exist('语音_静音'), True)
            self.assertEqual(call.check_if_button_selected('语音_静音'), False)
            call.check_element_tap_screen('语音_静音')
            call.click_locator_key('语音_静音')
            self.assertEqual(call.check_if_button_selected('语音_静音'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_000207=================

    @TestLogger.log('主叫手机')
    def call_000207_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_multi_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_000207_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('多方视频_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_answer_multi_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_000207(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_000207(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_000207_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_000207_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_000207(self):
        call = CallPage()
        try:
            time.sleep(2)
            self.assertEqual(call.is_element_already_exist('多方视频_关闭摄像头'), True)
            self.assertEqual(call.check_if_button_selected('多方视频_关闭摄像头'), False)
            call.click_locator_key('多方视频_关闭摄像头')
            self.assertEqual(call.is_element_already_exist('多方视频_打开摄像头'), True)
            self.assertEqual(call.is_element_already_exist('多方视频_打开摄像头'), True)
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.click_locator_key('多方视频_挂断')

    # ================test_call_000208=================

    @TestLogger.log('主叫手机')
    def call_000208_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    print('打电话了')
                    # 执行成功，写入成功标志
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_000208_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                # 循环判断元素是否存在
                if not call.is_element_exist('视频接听_接听'):
                    n -= 1
                    time.sleep(2)
                    continue
                else:
                    # 接听视频电话
                    self.assertEqual(self.to_pick_phone_video(), True)
                    # 验证检验项目
                    self.assertEqual(self.check_video_call_000208(), True)
                    # 写入测试成功标志
                    dic['res2'] = 'success'
                    break
            else:
                # 失败后抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_000208(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_000208_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_000208_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    @TestLogger.log()
    def check_video_call_000208(self):
        call = CallPage()
        try:
            time.sleep(6)
            call.check_element_tap_screen('视频_切换摄像头')
            call.click_locator_key('视频_切换摄像头')
            time.sleep(2)
            call.check_element_tap_screen('视频_切换摄像头')
            call.click_locator_key('视频_切换摄像头')
            return True
        except Exception:
            traceback.print_exc()
            return False
        finally:
            call.check_element_tap_screen('视频_挂断')
            call.click_locator_key('视频_挂断')

    # ================test_call_000244=================

    @TestLogger.log('主叫手机')
    def call_000244_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.click_locator_key('拨号键盘')
                    time.sleep(1)
                    for i in dic['cards']:
                        call.click_locator_key('keyboard_{}'.format(i))
                    time.sleep(1)
                    call.click_locator_key('拨号_呼叫')
                    time.sleep(1)
                    call.click_locator_key('拨号_呼叫_呼叫')
                    time.sleep(5)
                    call.click_locator_key('飞信电话_结束通话')
                    time.sleep(5)
                    call.click_first_record()
                    time.sleep(1)
                    call.click_locator_key('拨号_呼叫_呼叫')
                    time.sleep(2)
                    self.assertEqual(call.is_element_already_exist('飞信电话_结束通话'), True)
                    call.click_locator_key('飞信电话_结束通话')
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_000244_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 写入测试成功标志
            dic['res2'] = 'success'
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_000244(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_000244_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_000244_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    # ================test_call_000253_01=================

    @TestLogger.log('主叫手机')
    def call_000253_01_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_video(dic['cards'])
                    time.sleep(2)
                    call.click_locator_key('视频主叫_挂断')
                    time.sleep(5)
                    self.assertEqual(call.is_text_present('视频通话'), True)
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_000253_01_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 写入测试成功标志
            dic['res2'] = 'success'
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_000253_01(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_000253_01_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_000253_01_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    # ================test_call_000253_02=================

    @TestLogger.log('主叫手机')
    def call_000253_02_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    call.pick_up_p2p_video(dic['cards'])
                    time.sleep(2)
                    call.click_locator_key('视频主叫_挂断')
                    time.sleep(5)
                    self.assertEqual(call.is_text_present('视频通话'), True)
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_000253_02_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 写入测试成功标志
            dic['res2'] = 'success'
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_000253_02(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_000253_02_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_000253_02_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    # ================test_call_000253_03=================

    @TestLogger.log('主叫手机')
    def call_000253_03_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    call.pick_up_p2p_video(dic['cards'])
                    time.sleep(2)
                    call.click_locator_key('视频主叫_挂断')
                    dic['hang_up'] = True
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_000253_03_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'hang_up' not in dic.keys() or not dic['hang_up']:
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    time.sleep(3)
                    self.assertEqual(call.is_text_present('视频通话'), True)
                    dic['res2'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            time.sleep(30)
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_000253_03(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_000253_03_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_000253_03_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    # ================test_call_000253_04=================

    @TestLogger.log('主叫手机')
    def call_000253_04_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_voice_keep_time(dic['cards'])
                    time.sleep(3)
                    dic['pick_up'] = True
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_000253_04_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if ('pick_up' not in dic.keys()) or (not dic['pick_up']):
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    time.sleep(3)
                    call.click_locator_key('飞信电话_接受')
                    time.sleep(2)
                    call.click_locator_key('飞信电话_结束通话')
                    time.sleep(3)
                    print('检测。。。。。')
                    self.assertEqual(call.is_text_present('飞信电话'), True)
                    dic['res2'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 捕获异常
            traceback.print_exc()
            time.sleep(30)
            # 写入成功标志
            dic['res2'] = 'fail'

    @unittest.skip('飞信电话接听或拒接都没有通话记录')
    @tags('ALL', 'CMCC_double', 'call')
    def test_call_000253_04(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_000253_04_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_000253_04_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    # ================test_call_000253_05=================

    @TestLogger.log('主叫手机')
    def call_000253_05_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.pick_up_p2p_voice_keep_time(dic['cards'])
                    time.sleep(5)
                    call.click_locator_key('飞信电话_结束通话')
                    time.sleep(5)
                    self.assertEqual(call.is_text_present('飞信电话'), True)
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_000253_05_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 写入测试成功标志
            dic['res2'] = 'success'
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_000253_05(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_000253_05_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_000253_05_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')

    # ================test_call_000292=================

    @TestLogger.log('主叫手机')
    def call_000292_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    print('已经获取电话号码')
                    # 拨打电话
                    call.click_locator_key('拨号键盘')
                    time.sleep(1)
                    for i in dic['cards']:
                        call.click_locator_key('keyboard_{}'.format(i))
                    time.sleep(1)
                    call.click_locator_key('拨号_呼叫')
                    time.sleep(1)
                    call.click_locator_key('拨号_呼叫_呼叫')
                    time.sleep(5)
                    call.click_locator_key('飞信电话_结束通话')
                    time.sleep(5)
                    call.click_first_record()
                    time.sleep(1)
                    call.click_locator_key('拨号_呼叫_呼叫')
                    time.sleep(2)
                    self.assertEqual(call.is_element_already_exist('飞信电话_结束通话'), True)
                    call.click_locator_key('飞信电话_结束通话')
                    dic['res1'] = 'success'
                    break
            else:
                # 超时抛出异常
                raise
        except Exception:
            # 出错捕获异常
            traceback.print_exc()
            # 写入失败标志
            dic['res1'] = 'fail'

    @TestLogger.log('被叫手机')
    def call_000292_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            call = CallPage()
            call.wait_for_page_load()
            call.click_delete_all_key()
            # 获取手机号码
            cards = call.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
            # 写入测试成功标志
            dic['res2'] = 'success'
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_call_000292(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.call_000292_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.call_000292_02, args=(dic,))
            # 启动进程
            p2.start()
            # 进程阻塞
            p1.join()
            p2.join()
            # 等待子进程都执行完毕后，判断是否有执行失败的标志
            if 'fail' in dic.values():
                raise RuntimeError('Test Fail')
            else:
                # 若没有失败标志，测试执行成功
                print('Test Success')
