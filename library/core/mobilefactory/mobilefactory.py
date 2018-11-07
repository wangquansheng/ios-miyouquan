from library.core.common.supportedmodel import SupportedModel
from mobileimplements import *

try:
    from settings.mobile_driver_mapper import MOBILE_DRIVER_CREATORS
except ImportError as e:
    MOBILE_DRIVER_CREATORS = {
        SupportedModel.MI6['Model']: lambda kw: MI6(**kw),
        SupportedModel.MEIZU_PRO_6_PLUS['Model']: lambda kw: MXPro6Plus(**kw)
    }


class MobileFactory:
    @staticmethod
    def from_available_devices_setting(key):

        try:
            from settings.available_devices import AVAILABLE_DEVICES
        except ImportError as e:
            raise ImportError('setting/available_devices.py 中没有设置项：AVAILABLE_DEVICES')
        mobile_config = AVAILABLE_DEVICES.get(key)
        if mobile_config is None:
            raise Exception('AVAILABLE_DEVICES 找不到键位：{} '.format(key) + '的设置')
        params = dict(
            alis_name=key,
            model_info=mobile_config.get('MODEL'),
            command_executor=mobile_config.get('SERVER_URL'),
            desired_capabilities=mobile_config.get('DEFAULT_CAPABILITY'),
            browser_profile=mobile_config.get('BROWSER_PROFILE'),
            proxy=mobile_config.get('PROXY'),
            keep_alive=mobile_config.get('KEEP_ALIVE') if 'KEEP_ALIVE' in mobile_config else False,
            card_slot=mobile_config.get('CARDS')
        )
        mobile_model = mobile_config.get('MODEL')['Model']
        return MOBILE_DRIVER_CREATORS[mobile_model](params)


if __name__ == '__main__':
    main = MobileFactory.from_available_devices_setting
    driver = main('MI6')
    print('test')
