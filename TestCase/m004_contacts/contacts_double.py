import multiprocessing
import time
import traceback
import warnings

from library.core.TestLogger import TestLogger
from library.core.common.simcardtype import CardType
from library.core.TestCase import TestCase
from library.core.utils.applicationcache import current_mobile, current_driver, switch_to_mobile
from library.core.utils.testcasefilter import tags

from pages import *
from pages.components.Footer import FooterPage


REQUIRED_MOBILES = {
    'Android-移动': 'M960BDQN229CH',
    'Android-移动-N': 'M960BDQN229CH_N',
    'IOS-移动': 'iphone',
    'IOS-移动-移动': 'iphone_d',
    'Android-电信': 'single_telecom',
    'Android-联通': 'single_union',
    'Android-移动-联通': 'mobile_and_union',
    'Android-移动-电信': '',
    'Android-移动-移动': 'double_mobile',
    'Android-XX-XX': 'others_double',
}


# noinspection PyBroadException
class Preconditions(object):
    """
    分解前置条件
    """

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

    @staticmethod
    def make_sure_in_after_login_callpage():
        Preconditions.make_already_in_call_page()
        # current_mobile().wait_until_not(condition=lambda d: current_mobile().is_text_present('正在登录'), timeout=20)
        fp = FooterPage()
        fp.open_contacts_page()
        # current_mobile().wait_until(condition=lambda d: current_mobile().is_text_present('家庭网'), timeout=20)


    @staticmethod
    def initialize_class(moudel):
        """确保每个用例开始之前在通讯录界面"""
        warnings.simplefilter('ignore', ResourceWarning)
        Preconditions.select_mobile(moudel)
        Preconditions.make_sure_in_after_login_callpage()

    @staticmethod
    def disconnect_mobile(category):
        """断开手机连接"""
        client = switch_to_mobile(REQUIRED_MOBILES[category])
        client.disconnect_mobile()
        return client


# noinspection PyUnresolvedReferences
class ContactlocalPage(TestCase):
    """本地通讯录界面"""

    def default_setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)

    def default_tearDown(self):
        """断开所有手机"""
        Preconditions.disconnect_mobile('IOS-移动')
        Preconditions.disconnect_mobile('IOS-移动-移动')

    # ===============test_contact_00014==================

    @TestLogger.log('主叫手机')
    def contact_00014_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            contact_page = ContactsPage()
            contact_page.wait_for_page_load()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    contact_page.click_by_cards(dic['cards'])
                    time.sleep(5)
                    self.assertEqual(contact_page.is_element_already_exist('联系人_详情_头像'), True)
                    self.assertEqual(contact_page.is_element_already_exist('联系人_详情_用户名'), True)
                    self.assertEqual(contact_page.is_element_already_exist('联系人_详细_电话按钮'), True)
                    self.assertEqual(contact_page.is_element_already_exist('联系人_详细_视频按钮'), True)
                    self.assertEqual(contact_page.is_element_already_exist('联系人_详细_设置备注名'), True)
                    self.assertEqual(contact_page.is_element_already_exist('联系人_详细_备注修改'), True)
                    self.assertEqual(contact_page.is_element_already_exist('联系人_详细_手机号码'), True)
                    self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_更多'), True)
                    self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_更多编辑'), True)
                    self.assertEqual(contact_page.is_element_already_exist('家庭网_详细_电话规则'), True)
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
    def contact_00014_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            contact_page = ContactsPage()
            contact_page.wait_for_page_load()
            # 获取手机号码
            cards = contact_page.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'contact')
    def test_contact_00014(self):
            # 实例化ManagerServer进程，这个进程是阻塞的
            with multiprocessing.Manager() as manager:
                # 创建一个用于进程间通信的字典
                dic = manager.dict()
                # 实例化进程
                p1 = multiprocessing.Process(target=self.contact_00014_01, args=(dic,))
                # 启动进程
                p1.start()
                # 实例化进程
                p2 = multiprocessing.Process(target=self.contact_00014_02, args=(dic,))
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

    # ===============test_contact_00030==================

    @TestLogger.log('主叫手机')
    def contact_00030_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            contact_page = ContactsPage()
            contact_page.wait_for_page_load()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    contact_page.click_by_cards(dic['cards'])
                    time.sleep(2)
                    contact_page.click_locator_key('联系人_详细_视频按钮')
                    time.sleep(3)
                    self.assertEqual(contact_page.is_text_present('网络视频通话呼叫中'), True)
                    time.sleep(5)
                    contact_page.click_locator_key('视频主叫_挂断')
                    dic['call_up'] = True
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
    def contact_00030_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            contact_page = ContactsPage()
            contact_page.wait_for_page_load()
            # 获取手机号码
            cards = contact_page.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_contact_00030(self):
            # 实例化ManagerServer进程，这个进程是阻塞的
            with multiprocessing.Manager() as manager:
                # 创建一个用于进程间通信的字典
                dic = manager.dict()
                # 实例化进程
                p1 = multiprocessing.Process(target=self.contact_00030_01, args=(dic,))
                # 启动进程
                p1.start()
                # 实例化进程
                p2 = multiprocessing.Process(target=self.contact_00030_02, args=(dic,))
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

    # ===============test_contact_000112==================

    @tags('ALL', 'CMCC_double', 'contact')
    def test_contact_00112(self):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            contact_page = ContactsPage()
            contact_page.wait_for_page_load()
            self.assertEqual(contact_page.is_element_already_exist('通讯录_家庭网_管理'), False)
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    # ===============test_contact_00119==================

    @TestLogger.log('主叫手机')
    def contact_00119_01(self, dic):
        try:
            # 主叫手机初始化
            Preconditions.initialize_class('IOS-移动')
            contact_page = ContactsPage()
            contact_page.wait_for_page_load()
            # 循环检测60次 * 2s
            n = 1 * 60
            while n > 0:
                if 'cards' not in dic.keys() or dic['cards'] == '':
                    n -= 1
                    # 2秒检测一次
                    time.sleep(2)
                    continue
                else:
                    contact_page.input_locator_text('通讯_搜索', dic['cards'])
                    time.sleep(1)
                    self.assertEqual(contact_page.is_element_already_exist('通讯录_搜索框结果第一条'), True)
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
    def contact_00119_02(self, dic):
        try:
            # 初始化被叫手机
            Preconditions.initialize_class('IOS-移动-移动')
            contact_page = ContactsPage()
            contact_page.wait_for_page_load()
            # 获取手机号码
            cards = contact_page.get_cards(CardType.CHINA_MOBILE)
            # 给共享变量中写入变量参数
            dic['cards'] = cards
        except Exception:
            # 捕获异常
            traceback.print_exc()
            # 写入成功标志
            dic['res2'] = 'fail'

    @tags('ALL', 'CMCC_double', 'call')
    def test_contact_00119(self):
        # 实例化ManagerServer进程，这个进程是阻塞的
        with multiprocessing.Manager() as manager:
            # 创建一个用于进程间通信的字典
            dic = manager.dict()
            # 实例化进程
            p1 = multiprocessing.Process(target=self.contact_00119_01, args=(dic,))
            # 启动进程
            p1.start()
            # 实例化进程
            p2 = multiprocessing.Process(target=self.contact_00119_02, args=(dic,))
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
