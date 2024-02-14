import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

cap: Dict[str, Any] = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "automationName": "UIAutomator2",
    "appPackage": "com.socialnmobile.dictapps.notepad.color.note",
    "appActivity": "com.socialnmobile.colornote.activity.Main",
}

url = "http://192.168.1.9:4723"

driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(5)

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]').click()
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.socialnmobile.dictapps.notepad.color.note:id/btn_start_skip"]').click()
driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.ImageView[@resource-id="com.socialnmobile.dictapps.notepad.color.note:id/icon"])[5]').click()
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.socialnmobile.dictapps.notepad.color.note:id/text" and @text="Like us on Facebook"]').click()

# if(driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.chrome:id/terms_accept"]').is_displayed()):
#     driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.chrome:id/terms_accept"]').click()
# if(driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.chrome:id/negative_button"]').is_displayed()):
#     driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.chrome:id/negative_button"]').click()
# if(driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.chrome:id/negative_button"]').is_displayed()):
#     driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.android.chrome:id/negative_button"]').click()

print(driver.contexts)
print(driver.context)

xx = driver.find_element(by=AppiumBy.XPATH, value='//android.webkit.WebView[@text="ColorNote"]')
print(xx.text)
driver.quit()
