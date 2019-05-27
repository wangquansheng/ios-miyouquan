from library.core.TestLogger import TestLogger
from library.core.common.simcardtype import CardType
from library.core.mobile.mobiledriver import MobileDriver


class iPhoneXR(MobileDriver):
    """iPhoneXR"""

    def supported_card_types(self):
        return [
            CardType.CHINA_MOBILE,
            CardType.CHINA_UNION,
            CardType.CHINA_TELECOM,
        ]

    def total_card_slot(self):
        return 2

    @TestLogger.log('获取手机型号')
    def get_mobile_model_info(self):
        try:
            result = "iPhoneXR"
        except:
            result = "暂无信息"
        return result.strip()
