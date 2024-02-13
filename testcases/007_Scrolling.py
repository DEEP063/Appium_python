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

el1 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"android:id/text1\" and @text=\"App\"]")
el1.click()
el2 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"android:id/text1\" and @text=\"Activity\"]")
el2.click()

# Scroll to View
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Wallpaper"))')


# device_size = driver.get_window_size()
# print(device_size)
#
# screenwidth = device_size['width']
# screenheight = device_size['height']
# print(device_size['width'])
# print(device_size['height'])

# startX = screenwidth/2
# endX = screenwidth/2
# startY  = screenheight*8/9
# endY = screenheight/9
#
# actions = TouchAction(driver)
# actions.long_press(None,startX,startY).move_to(None,endX,endY).release().perform()

# start_x = screenwidth / 2
# end_x = screenwidth / 2
# start_y = screenheight * 8 / 9
# end_y = screenheight / 9
# actions = TouchAction(driver)
# actions.long_press(None, start_x, start_y).move_to(None, end_x, end_y).release().perform()

# Scroll to View
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToEnd(2)')

time.sleep(5)
driver.quit()