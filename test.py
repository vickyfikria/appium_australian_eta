import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='',
    appActivity='',
    language='en',
    locale='US',
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
        time.sleep(5)  # Wait for the app to load

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_next(self) -> None:
        self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Next"]').click()
        time.sleep(2)  
        # WhatIsETAActivity page, click Next
        self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Next"]').click()
        time.sleep(2)  
        # AppUseConditionActivity : scrolling and Agree
        self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToEnd(10)')
        time.sleep(2)  # Wait for scroll to end
        self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Agree"]').click()
        time.sleep(3)  
        # Passcode input
        self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="1"]').click()
        self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="1"]').click()
        self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="1"]').click()
        self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="1"]').click()
        self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="1"]').click()
        self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="1"]').click()                                            
        time.sleep(3)    
        # Verify Passcode input               
        self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="1"]').click()
        self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="1"]').click()
        self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="1"]').click()
        self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="1"]').click()
        self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="1"]').click()
        self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="1"]').click()                                           
        
        #biometric : Skip for now with Not now button   
        time.sleep(2)    
        self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Not now"]').click()   
        time.sleep(2)
        #Travel Agent
        self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="No"]').click()   
        self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Next"]').click()   
        time.sleep(2)  
        #Create new request
        self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="New ETA"]').click()   
        time.sleep(2)
        # ConsenAgreement Activity : scrolling and Agree
        self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToEnd(15)')
        time.sleep(2)
        self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Agree"]').click()           
        time.sleep(3)
        # Application process
        # Step 1 : Scan Passport : Click Next
        self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Scan Passport"]').click()
        time.sleep(2)
        self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Scan"]').click()
        #inject here for passport image


if __name__ == '__main__':
    unittest.main()
