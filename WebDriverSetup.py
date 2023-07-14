import unittest
import time
from appium import webdriver
import HtmlTestRunner
from login import emailLogin
import smtplib
from email.mime.multipart import MIMEMultipart #메일의 Data 영역의 메시지를 만드는 모듈
from email.mime.text import MIMEText # 메일의 본문 내용을 만드는 모듈
from email.mime.application import MIMEApplication # 메일의 첨부 파일을 base64 형식으로 변환
from email.mime.base import MIMEBase
from email import encoders
from email.encoders import encode_base64
import zipfile
import os
import glob

class WebDriverSetup(unittest.TestCase):

    dc = {}
    driver = None

    def setUp(self):
        self.dc['udid'] = 'R5CR91CVMDR'
        self.dc['appPackage'] = 'com.bbros.sayup'
        self.dc['appActivity'] = '.ui.view.splash.SplashActivity'
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)


    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test_1(self):
        emailLogin.test_email_login(self)

if __name__ == '__main__':
    reportFoler = "Report"
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=reportFoler, title='Test report', open_in_browser=True))







