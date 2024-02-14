import pytest
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions

@pytest.fixture(scope="function")
def setup_function():
    global driver
    cap: Dict[str, Any] = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "automationName": "UIAutomator2",
        "appPackage": "com.hmh.api",
        "appActivity": ".ApiDemos",
    }
    url = "http://192.168.1.9:4723"
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
    driver.implicitly_wait(5)
    yield driver
    driver.quit()