import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException

cap: Dict[str, Any] = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "automationName": "UIAutomator2",
    "appPackage": "com.android.contacts",
    "appActivity": ".activities.PeopleActivity",
}

url = "http://192.168.1.9:4723"


driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value='Create new contact')
el.click()


wait = WebDriverWait(driver,timeout=6,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])
wait.until(EC.presence_of_element_located((AppiumBy.ID,'com.android.contacts:id/left_button'))).click()
driver.find_element(by=AppiumBy.XPATH,value='//android.widget.EditText[@text="First name"]').send_keys("raj")
driver.find_element(by=AppiumBy.XPATH,value='//android.widget.EditText[@text="Last name"]').send_keys("Patel")

# driver.find_element(by=AppiumBy.XPATH,value='//android.widget.EditText[@text="Phone"]').send_keys("987654321")
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Phone")').send_keys("987654321")


driver.find_element(by=AppiumBy.XPATH,value='//android.widget.EditText[@text="Email"]').send_keys("varun@yopmail.com")
driver.find_element(by=AppiumBy.ID,value='com.android.contacts:id/editor_menu_save_button').click()



driver.quit()