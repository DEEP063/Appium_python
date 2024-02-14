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
    "appPackage": "com.hmh.api",
    "appActivity": ".ApiDemos",
}

url = "http://192.168.1.9:4723"

driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
time.sleep(5)

if driver.find_element(by=AppiumBy.ID,value="com.android.permissioncontroller:id/continue_button").is_displayed():
    driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/continue_button").click()

time.sleep(3)

driver.find_element(by=AppiumBy.ID, value="android:id/button1").click()
el1 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"android:id/text1\" and @text=\"App\"]")
el1.click()
el2 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"android:id/text1\" and @text=\"Alert Dialogs\"]")
el2.click()
el3 = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.hmh.api:id/two_buttons"]')
el3.click()
time.sleep(3)

driver.switch_to.alert.accept()
time.sleep(5)

driver.quit()
