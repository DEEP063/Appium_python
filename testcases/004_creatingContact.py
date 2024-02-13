import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap: Dict[str, Any] = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "automationName": "UIAutomator2",
    "appPackage": "com.android.contacts",
    "appActivity": ".activities.PeopleActivity",
}

url = "http://192.168.1.9:4723"

# adb devices
# adb shell
# dumpsys window windows | grep -E 'mTopActivityComponent'



driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))

el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='Create new contact')
el.click()

time.sleep(5)
driver.find_element(by=AppiumBy.ID,value='com.android.contacts:id/left_button').click()

driver.find_element(by=AppiumBy.XPATH,value='//android.widget.EditText[@text="First name"]').send_keys("Kunal")
driver.find_element(by=AppiumBy.XPATH,value='//android.widget.EditText[@text="Last name"]').send_keys("Patel")
driver.find_element(by=AppiumBy.XPATH,value='//android.widget.EditText[@text="Phone"]').send_keys("987654321")
driver.find_element(by=AppiumBy.XPATH,value='//android.widget.EditText[@text="Email"]').send_keys("kunal@yopmail.com")
driver.find_element(by=AppiumBy.ID,value='com.android.contacts:id/editor_menu_save_button').click()



time.sleep(5)
driver.quit()