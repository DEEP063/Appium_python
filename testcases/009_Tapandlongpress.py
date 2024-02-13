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
    "appPackage": "com.android.contacts",
    "appActivity": ".activities.PeopleActivity",
}

url = "http://192.168.1.9:4723"

driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
time.sleep(5)
elements = driver.find_elements(AppiumBy.XPATH,"//android.widget.TextView[@resource-id='com.android.contacts:id/cliv_name_textview']")
print(len(elements))

actions = TouchAction(driver)
for i in elements:
    print(i.text)
xyz = elements[1]
# actions.tap(xyz).wait(2000).release().perform()
# actions.long_press(xyz).perform().release()
actions.long_press(driver.find_element(AppiumBy.ACCESSIBILITY_ID)).perform().release()

time.sleep(8)
driver.quit()