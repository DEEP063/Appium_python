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
    "appPackage": "com.google.android.contacts",
    "appActivity": "com.google.android.apps.contacts.activities.PeopleActivity",
}

url = "http://192.168.1.9:4723"

driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
time.sleep(5)


ele= driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="android:id/button2"]').click()
time.sleep(4)
elem= driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]').click()
time.sleep(3)


elem= driver.find_element(AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="com.google.android.contacts:id/og_apd_ring_view"]').click()
time.sleep(4)
elefm= driver.find_element(AppiumBy.XPATH,'//android.widget.ImageView[@content-desc="Close"]').click()

time.sleep(5)

elements = driver.find_elements(AppiumBy.XPATH,"//android.widget.TextView[@resource-id='com.google.android.contacts:id/cliv_name_textview']")
print(len(elements))

# actions = TouchAction(driver)
for i in elements:
    print(i.text)

# actions.tap(xyz).wait(2000).release().perform()
# actions.long_press(xyz).perform().release()
time.sleep(4)  # Add a delay to ensure previous actions are completed before performing the long press
element = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@content-desc="aryan khan"]')

TouchAction(driver).long_press(element).perform()

time.sleep(2)  # Add a delay to observe the result before quitting the driver
driver.quit()