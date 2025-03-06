import time
import unittest

from selenium import webdriver
from pages.test_page import TestPage


class MyTests(unittest.TestCase):
    page_url = 'https://practice-automation.com/form-fields/'

    def setUp(self) -> None:
        super().setUp()

        options = webdriver.ChromeOptions()
        ##options.add_argument('headless')

        self.driver = webdriver.Chrome(options=options)

        self.driver.get(self.page_url)

        self.page = TestPage(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

        super().tearDown()

    ## Тестовое задание
    def test_simbir_soft(self):
        userName = 'Andrey'
        userPassword = 'password'
        userEmail = userName.lower()+'@example.com'

        self.page.input_user_name(userName)
        time.sleep(2)

        self.page.input_user_password(userPassword)
        time.sleep(2)

        self.page.click_checkbox_milk()
        time.sleep(2)

        self.page.click_checkbox_coffe()
        time.sleep(2)

        self.page.click_radio_yellow()
        time.sleep(2)

        self.page.select_likeAutomation_yes()
        time.sleep(2)

        self.page.input_user_email(userEmail)
        time.sleep(2)

        maxAutomationTool = self.page.get_max_automationTools()
        lenlistAutomationTools = self.page.get_lenght_automationTools()
        time.sleep(2)

        self.page.input_message(maxAutomationTool, lenlistAutomationTools)
        time.sleep(2)

        self.page.click_button_submit()
        time.sleep(2)

        alert = self.driver.switch_to.alert
        self.assertEqual('Message received!', alert.text)
