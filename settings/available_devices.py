# 可用手机以及启动配置
from library.core.common.simcardtype import CardType
from library.core.common.supportedmodel import SupportedModel

# 测试APP信息
TARGET_APP = dict(
    # DOWNLOAD_URL="https://www.pgyer.com/apiv2/app/install?_api_key=298b363e3288c07f2683b96ca9bc5ab6&appKey=andfetiondev&buildPassword=qwer!234",
    DOWNLOAD_URL="http://dlrcs.fetion-portal.com/mobile/RCS_V6.2.9.0313_20190313.apk",
    APP_PACKAGE="com.chinasofti.rcs",
    APP_ACTIVITY="com.cmcc.cmrcs.android.ui.activities.WelcomeActivity",
    INSTALL_BEFORE_RUN=False
)

# ======================= 移动CI环境手机配置 =======================
AVAILABLE_DEVICES = {
    'M960BDQN229CH': {
        "MODEL": SupportedModel.HUAWEI_P20,
        "SERVER_URL": 'http://221.176.34.113:5000/wd/hub',
        "DEFAULT_CAPABILITY": {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "8DF6R17526001515",
            "udid": "8DF6R17526001515",
            "automationName": "UiAutomator2",
            "newCommandTimeout": 600,
            "appPackage": "com.chinasofti.rcs",
            #  6.2.8
            # "appActivity": "com.cmcc.cmrcs.android.ui.activities.WelcomeActivity",
            #  6.2.9
            "appActivity": "com.cmic.module_main.ui.activity.WelcomeActivity",
        },
        'CARDS': [
            {
                'TYPE': CardType.CHINA_MOBILE,
                'CARD_NUMBER': '18875905984'
            },
        ]
    },
}

# ======================= 本地CI环境手机配置 =======================
AVAILABLE_DEVICES_DEV = {
    'M960BDQN229CH': {
        "MODEL": SupportedModel.MEIZU_PRO_6_PLUS,
        "SERVER_URL": 'http://127.0.0.1:4723/wd/hub',
        "DEFAULT_CAPABILITY": {
            "platformName": "Android",
            "platformVersion": "6.0.1",
            "deviceName": "M960BDQN229DK",
            "udid": "M960BDQN229DK",
            "automationName": "UiAutomator2",
            "newCommandTimeout": 600,
            "appPackage": "com.chinasofti.rcs",
            "appActivity": "com.cmic.module_main.ui.activity.WelcomeActivity",
        },
        'CARDS': [
            {
                'TYPE': CardType.CHINA_MOBILE,
                'CARD_NUMBER': '13410559632'
            },
        ]
    },

    'M960BDQN229CK_20': {
        "MODEL": SupportedModel.HUAWEI_P20,
        "SERVER_URL": 'http://127.0.0.1:4723/wd/hub',
        "DEFAULT_CAPABILITY": {
            "platformName": "Android",
            "platformVersion": "9.0",
            "deviceName": "DWT7N18614014715",
            "udid": "DWT7N18614014715",
            "automationName": "UiAutomator2",
            "newCommandTimeout": 600,
            "appPackage": "com.chinasofti.rcs",
            "appActivity": "com.cmcc.cmrcs.android.ui.activities.WelcomeActivity",
        },
        'CARDS': [
            {
                'TYPE': CardType.CHINA_MOBILE,
                'CARD_NUMBER': '18875905984'
            },
            None
        ]
    },
    'M960BDQN229CH-bak': {
        "MODEL": SupportedModel.MEIZU_PRO_6_PLUS,
        "SERVER_URL": 'http://192.168.200.112:4724/wd/hub',
        "DEFAULT_CAPABILITY": {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "M960BDQN229CH",
            "udid": "M960BDQN229CH",
            "automationName": "UiAutomator2",
            "newCommandTimeout": 600,
            "appPackage": "com.chinasofti.rcs",
            "appActivity": "com.cmcc.cmrcs.android.ui.activities.WelcomeActivity",
        },
        'CARDS': [
            {
                'TYPE': CardType.CHINA_MOBILE,
                'CARD_NUMBER': '19876283465'
            },
        ]
    },
    'M960BDQN229CH_me': {
        "MODEL": SupportedModel.RED_MI_NOTE_4X,
        "SERVER_URL": 'http://192.168.1.103:4724/wd/hub',
        "DEFAULT_CAPABILITY": {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "VCO7IFTKKZZ5FI9T",
            "udid": "VCO7IFTKKZZ5FI9T",
            "automationName": "UiAutomator2",
            "newCommandTimeout": 600,
            "appPackage": "com.chinasofti.rcs",
            "appActivity": "com.cmcc.cmrcs.android.ui.activities.WelcomeActivity",
        },
        'CARDS': [
            {
                'TYPE': CardType.CHINA_MOBILE,
                'CARD_NUMBER': '14775290489'
            },
        ]
    },
    'single_mobile': {
        "MODEL": SupportedModel.RED_MI_NOTE_4X,
        "SERVER_URL": 'http://192.168.1.104:4724/wd/hub',
        "DEFAULT_CAPABILITY": {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "VCO7IFTKKZZ5FI9T",
            "udid": "VCO7IFTKKZZ5FI9T",
            "automationName": "UiAutomator2",
            "newCommandTimeout": 600,
            "appPackage": "com.chinasofti.rcs",
            "appActivity": "com.cmcc.cmrcs.android.ui.activities.WelcomeActivity",
        },
        'CARDS': [
            {
                'TYPE': CardType.CHINA_MOBILE,
                'CARD_NUMBER': '14775290489'
            },
        ]
    },
    'single_telecom': {
        "MODEL": SupportedModel.RED_MI_NOTE_4X,
        "SERVER_URL": 'http://127.0.0.1:4723/wd/hub',
        "DEFAULT_CAPABILITY": {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "VCO7IFTKKZZ5FI9T",
            "udid": "VCO7IFTKKZZ5FI9T",
            "automationName": "UiAutomator2",
            "newCommandTimeout": 600,
            "appPackage": "com.chinasofti.rcs",
            "appActivity": "com.cmcc.cmrcs.android.ui.activities.WelcomeActivity",
        },
        'CARDS': [
            {
                'TYPE': CardType.CHINA_TELECOM,
                'CARD_NUMBER': '15338821645'
            },
        ]
    },
    'single_union': {
        "MODEL": SupportedModel.RED_MI_NOTE_4X,
        "SERVER_URL": 'http://127.0.0.1:4723/wd/hub',
        "DEFAULT_CAPABILITY": {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "VCO7IFTKKZZ5FI9T",
            "udid": "VCO7IFTKKZZ5FI9T",
            "automationName": "UiAutomator2",
            "newCommandTimeout": 600,
            "appPackage": "com.chinasofti.rcs",
            "appActivity": "com.cmcc.cmrcs.android.ui.activities.WelcomeActivity",
        },
        'CARDS': [
            {
                'TYPE': CardType.CHINA_UNION,
                'CARD_NUMBER': '18681151872'
            },
        ]
    },
    'double_mobile': {
        "MODEL": SupportedModel.RED_MI_NOTE_4X,
        "SERVER_URL": 'http://127.0.0.1:4723/wd/hub',
        "DEFAULT_CAPABILITY": {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "VCO7IFTKKZZ5FI9T",
            "udid": "VCO7IFTKKZZ5FI9T",
            "automationName": "UiAutomator2",
            "newCommandTimeout": 600,
            "appPackage": "com.chinasofti.rcs",
            "appActivity": "com.cmcc.cmrcs.android.ui.activities.WelcomeActivity",
        },
        'CARDS': [
            {
                'TYPE': CardType.CHINA_MOBILE,
                'CARD_NUMBER': '14775290489'
            },
            {
                'TYPE': CardType.CHINA_MOBILE,
                'CARD_NUMBER': '19876283465'
            }
        ]
    },
    'mobile_and_union': {
        "MODEL": SupportedModel.RED_MI_NOTE_4X,
        "SERVER_URL": 'http://127.0.0.1:4723/wd/hub',
        "DEFAULT_CAPABILITY": {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "VCO7IFTKKZZ5FI9T",
            "udid": "VCO7IFTKKZZ5FI9T",
            "automationName": "UiAutomator2",
            "newCommandTimeout": 600,
            "appPackage": "com.chinasofti.rcs",
            "appActivity": "com.cmcc.cmrcs.android.ui.activities.WelcomeActivity",
        },
        'CARDS': [
            {
                'TYPE': CardType.CHINA_MOBILE,
                'CARD_NUMBER': '14775290489'
            },
            {
                'TYPE': CardType.CHINA_UNION,
                'CARD_NUMBER': '18681151872'
            }
        ]
    },
    'others_double': {
        "MODEL": SupportedModel.RED_MI_NOTE_4X,
        "SERVER_URL": 'http://127.0.0.1:4723/wd/hub',
        "DEFAULT_CAPABILITY": {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "VCO7IFTKKZZ5FI9T",
            "udid": "VCO7IFTKKZZ5FI9T",
            "automationName": "UiAutomator2",
            "newCommandTimeout": 600,
            "appPackage": "com.chinasofti.rcs",
            "appActivity": "com.cmcc.cmrcs.android.ui.activities.WelcomeActivity",
        },
        'CARDS': [
            {
                'TYPE': CardType.CHINA_TELECOM,
                'CARD_NUMBER': '15338821645'
            },
            {
                'TYPE': CardType.CHINA_UNION,
                'CARD_NUMBER': '18681151872'
            }
        ]
    }
}

# ======================= 个人本机执行环境手机配置 =======================

DEVICES_CONFIG_CYH = {
    'iphone': {
        "MODEL": SupportedModel.iPhone_XR,
        "SERVER_URL": 'http://127.0.0.1:4723/wd/hub',
        "DEFAULT_CAPABILITY": {
            "platformName": "ios",
            "platformVersion": "11.0.1",
            "deviceName": "iPhone 8",
            "udid": "4eca812fe46b9296e7e8c626ed38b806a883a2a0",
            "automationName": "XCUITest",
            "app": "com.cmic.college",
            "xcodeOrgId": "92GST8LVB9",
            "newCommandTimeout": 120,
            "xcodeSigningId": "iPhone Developer"
        },
        'CARDS': [
            {
                'TYPE': CardType.CHINA_MOBILE,
                'CARD_NUMBER': '13641490071'
            },
        ]
    },
    'iphone_d': {
        "MODEL": SupportedModel.iPhone_XR,
        "SERVER_URL": 'http://127.0.0.1:4725/wd/hub',
        "DEFAULT_CAPABILITY": {
            "platformName": "ios",
            "platformVersion": "12.0.1",
            "deviceName": "iPhone7st",
            "udid": "d20ea7886c5fcea7f6494de6b878f94bb1cf3727",
            "automationName": "XCUITest",
            "app": "com.cmic.college",
            "xcodeOrgId": "92GST8LVB9",
            "newCommandTimeout": 120,
            "xcodeSigningId": "iPhone Developer"
        },
        'CARDS': [
            {
                'TYPE': CardType.CHINA_MOBILE,
                'CARD_NUMBER': '14775970982'
            },
        ]
    },
}

DEVICES_CONFIG_WJH = {
    'iphone': {
        "MODEL": SupportedModel.iPhone_XR,
        "SERVER_URL": 'http://127.0.0.1:4723/wd/hub',
        "DEFAULT_CAPABILITY": {
            "platformName": "ios",
            "platformVersion": "11.0.1",
            "deviceName": "iPhone 8",
            "udid": "d20ea7886c5fcea7f6494de6b878f94bb1cf3727",
            "automationName": "XCUITest",
            "app": "com.cmic.college",
            "xcodeOrgId": "TCBU5AR586",
            "newCommandTimeout": 120,
            "xcodeSigningId": "iPhone Developer"
        },
        'CARDS': [
            {
                'TYPE': CardType.CHINA_MOBILE,
                'CARD_NUMBER': '14775970982'
            },
        ]
    },
    'iphone_d': {
        "MODEL": SupportedModel.iPhone_XR,
        "SERVER_URL": 'http://127.0.0.1:4725/wd/hub',
        "DEFAULT_CAPABILITY": {
            "platformName": "ios",
            "platformVersion": "12.0.1",
            "deviceName": "iPhone7st",
            "udid": "13ca1b2deeeac7446f3a0cec3fec65dc6875714a",
            "automationName": "XCUITest",
            "app": "com.cmic.college",
            "xcodeOrgId": "92GST8LVB9",
            "newCommandTimeout": 120,
            "xcodeSigningId": "iPhone Developer"
        },
        'CARDS': [
            {
                'TYPE': CardType.CHINA_MOBILE,
                'CARD_NUMBER': '14775451723'
            },
        ]
    },
}
