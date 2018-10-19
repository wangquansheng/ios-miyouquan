import re
import unittest

from appium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as  EC
from selenium.webdriver.support.wait import WebDriverWait

from library import config, keywords, locators
from library.elementfinder import ElementFinder


class C0004(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = config.GlobalConfig.get_desired_caps()
        url = config.GlobalConfig.get_server_url()
        if not keywords.current_driver():
            keywords.Android.open_app(url, desired_caps)
        else:
            keywords.current_driver().launch_app()

    @classmethod
    def tearDownClass(cls):
        # keywords.Android.closed_current_driver()
        pass

    def setUp(self):
        self.assertTrue(keywords.current_driver().is_app_installed('com.chinasofti.rcs'))
        keywords.GuidePage.jump_over_the_guide_page()
        keywords.PermissionListPage.accept_all_permission_in_list()
        keywords.Login.wait_for_one_key_login_page_load()

    def tearDown(self):
        keywords.Android.back()
        keywords.current_driver().close()

    def test_switch_to_verification_code_login(self):
        """切换验证码登录"""
        keywords.Login.click_use_another_number_to_login()
        keywords.Login.wait_for_sms_login_page_load()

        # 先获取当前通知栏的短信数量再点击获取验证码
        keywords.Android.open_notifications()
        before = keywords.Android.get_last_verification_code()
        keywords.Android.back()

        keywords.Login.input_phone_number('13510772034')
        keywords.Login.wait_for_phone_number_text_match('13510772034')

        # 获取新的验证码
        keywords.Login.wait_for_get_verification_code_clickable()
        keywords.Login.click_get_verification_code()
        keywords.Android.open_notifications()
        keywords.Android.wait_new_verification_code(before)
        code = keywords.Android.get_last_verification_code()
        keywords.Android.back()

        keywords.Login.input_verification_code(code)
        keywords.Login.click_login()
        keywords.Login.click_i_know()
        keywords.current_driver().wait_activity('com.cmcc.cmrcs.android.ui.activities.HomeActivity', 20)
