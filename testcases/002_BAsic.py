import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap: Dict[str, Any] = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "automationName": "UIAutomator2",
}

url = "http://192.168.1.9:4723"

driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))

el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='Chrome')
el.click()

ef = driver.find_element(by=AppiumBy.ID,value='com.android.chrome:id/search_box_text')
ef.send_keys("Dragon")

time.sleep(5)
driver.quit()