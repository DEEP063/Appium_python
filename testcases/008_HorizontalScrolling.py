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

# adb devices
# adb shell
# dumpsys window windows | grep -E 'mTopActivityComponent'



driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(5)

if driver.find_element(by=AppiumBy.ID,value="com.android.permissioncontroller:id/continue_button").is_displayed():
    driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/continue_button").click()

driver.find_element(by=AppiumBy.ID, value="android:id/button1").click()

el1 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"android:id/text1\" and @text=\"Views\"]")
el1.click()
el2 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"android:id/text1\" and @text=\"Gallery\"]")
el2.click()
el3 = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="android:id/text1" and @text="1. Photos"]')
el3.click()

# # Scroll to View
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollToEnd(3)')
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollToBeginning(3)')

# Scroll to View
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollForward(3)')
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollBackward(3)')


driver.quit()