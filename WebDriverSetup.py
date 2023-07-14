from appium.webdriver.common.appiumby import AppiumBy
import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
import HtmlTestRunner
from login import emailLogin

class WebDriverSetup(unittest.TestCase):

    dc = {}
    driver = None

    def setUp(self):
        self.dc['udid'] = 'R5CR91CVMDR'
        self.dc['appPackage'] = 'com.bbros.sayup'
        self.dc['appActivity'] = '.ui.view.splash.SplashActivity'
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)


    #testcase
    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    setup = WebDriverSetup()
    setup.setUp()
    emailLogin().test_email_login(setup.driver)
    reportFoler = "Report"
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=reportFoler, title='Test report', open_in_browser=True))




