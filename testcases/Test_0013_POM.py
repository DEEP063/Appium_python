import time

from appium.webdriver.common.appiumby import AppiumBy


def test_Alert(setup_function):
    driver = setup_function
    if driver.find_element(by=AppiumBy.ID,value="com.android.permissioncontroller:id/continue_button").is_displayed():
        driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/continue_button").click()

    driver.find_element(by=AppiumBy.ID, value="android:id/button1").click()
    el1 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"android:id/text1\" and @text=\"App\"]")
    el1.click()
    el2 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"android:id/text1\" and @text=\"Alert Dialogs\"]")
    el2.click()
    el3 = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.hmh.api:id/two_buttons"]')
    el3.click()
    time.sleep(4)
    driver.switch_to.alert.accept()

