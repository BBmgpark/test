from appium.webdriver.common.appiumby import AppiumBy
import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions


class DdocdocLoginTest(unittest.TestCase):

    dc = {}
    driver = None

    def setUp(self):
        self.dc['udid'] = 'R5CR91CVMDR'
        self.dc['appPackage'] = 'com.bbros.sayup'
        self.dc['appActivity'] = '.ui.view.splash.SplashActivity'
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

    def test_email_login(self):
        #element 노출될때까지 최대 10초 기다린다.
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "com.bbros.sayup:id/confirmBtn")))

        #권한 안내 화면 > [확인] 버튼 클릭
        el_confirmBtn = self.driver.find_element(by=AppiumBy.ID, value='com.bbros.sayup:id/confirmBtn')
        el_confirmBtn.click()

        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "com.android.permissioncontroller:id/permission_allow_button")))
        el_permission_allow_button = self.driver.find_element(by=AppiumBy.ID, value='com.android.permissioncontroller:id/permission_allow_button')
        el_permission_allow_button.click()

        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")))
        el_permission_allow_foreground_only_button = self.driver.find_element(by=AppiumBy.ID, value='com.android.permissioncontroller:id/permission_allow_foreground_only_button')
        el_permission_allow_foreground_only_button.click()

        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "com.android.permissioncontroller:id/permission_allow_button")))
        el_permission_allow_button = self.driver.find_element(by=AppiumBy.ID, value='com.android.permissioncontroller:id/permission_allow_button')
        el_permission_allow_button.click()

        #온보딩 화면 > [이메일 로그인] 버튼 클릭
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ID, "com.bbros.sayup:id/tvEmailLoginBtn")))
        el_tvEmailLoginBtn = self.driver.find_element(by=AppiumBy.ID, value='com.bbros.sayup:id/tvEmailLoginBtn')
        el_tvEmailLoginBtn.click()

        #이메일 아이디 입력
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ID, "com.bbros.sayup:id/etEmail")))
        el_etEmail = self.driver.find_element(by=AppiumBy.ID, value='com.bbros.sayup:id/etEmail')
        el_etEmail.send_keys("qa22@qa.com")

        #이메일 비밀번호 입력
        el_etPassword = self.driver.find_element(by=AppiumBy.ID, value='com.bbros.sayup:id/etPassword')
        el_etPassword.send_keys("qwer1234!")

        #[로그인] 버튼 클릭
        el_tvLoginConfirm = self.driver.find_element(by=AppiumBy.ID, value='com.bbros.sayup:id/tvLoginConfirm')
        el_tvLoginConfirm.click()

        #카카오 전환 유도 팝업 노출 시 닫기
        time.sleep(2)
        el_tvSkipBtn = self.driver.find_element(by=AppiumBy.ID, value='com.bbros.sayup:id/tvSkipBtn')
        if el_tvSkipBtn.is_displayed():
            el_tvSkipBtn.click()

        #홈 화면 메뉴 선택 상태로 노출된다.
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ID, "com.bbros.sayup:id/tabName")))
        el_tabName_home = self.driver.find_element(by=AppiumBy.ID, value='com.bbros.sayup:id/tabName')
        el_tabName_home.is_selected()


    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
