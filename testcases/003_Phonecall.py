import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap: Dict[str, Any] = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "automationName": "UIAutomator2",
    "appPackage": "com.android.dialer",
    "appActivity": ".main.impl.MainActivity",
}

url = "http://192.168.1.9:4723"

# adb devices
# adb shell
# dumpsys window windows | grep -E 'mTopActivityComponent'



driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))

el = driver.find_element(by=AppiumBy.ID,value='com.android.dialer:id/call_log_tab')
el.click()

# ef = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='key pad')003_Phonecall.py
# ef.click()


ef = driver.find_element(by=AppiumBy.XPATH,value='//android.widget.ImageView[@content-desc="Call +91 91737 01132"]').click()
# ef = driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@text()="9"]').click()
# ef = driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@text()="1"]').click()
# ef = driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@text()="7"]').click()
# ef = driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@text()="3"]').click()
# ef = driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@text()="7"]').click()
# ef = driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@text()="0"]').click()
# ef = driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@text()="1"]').click()
# ef = driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@text()="1"]').click()
# ef = driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@text()="3"]').click()
# ef = driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@text()="2"]').click()




time.sleep(5)
driver.quit()