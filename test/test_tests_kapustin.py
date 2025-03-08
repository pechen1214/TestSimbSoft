import time
import allure
from selenium import webdriver

from pages.test_page import TestPage


class TestMy:
    page_url = 'https://practice-automation.com/form-fields/'

    def setup_method (self) -> None:

        options = webdriver.ChromeOptions()
        options.add_argument('start-maximized')
        ##options.add_argument('headless')

        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.page_url)
        self.page = TestPage(self.driver)

        ## для красивого скриншота
        self.driver.execute_script('document.body.style.zoom="60%"')

    def teardown_method(self) -> None:
        self.driver.quit()

    ## Тестовое задание
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Filling out the form, clicking the "Submit" button, checking the text in the alert')
    def test_simbir_soft(self):
        userName = 'Andrey'
        userPassword = 'password'
        userEmail = userName.lower()+'@example.com'

        self.page.input_user_name(userName)
        self.driver.save_screenshot('./screenshots/input_user_name.png')
        allure.attach.file(source='./screenshots/input_user_name.png', attachment_type=allure.attachment_type.PNG)

        self.page.input_user_password(userPassword)
        self.driver.save_screenshot('./screenshots/input_user_password.png')
        allure.attach.file(source='./screenshots/input_user_password.png', attachment_type=allure.attachment_type.PNG)

        self.page.click_checkbox_milk()
        self.page.click_checkbox_coffe()
        self.driver.save_screenshot('./screenshots/click_checkbox.png')
        allure.attach.file(source='./screenshots/click_checkbox.png', attachment_type=allure.attachment_type.PNG)

        self.page.click_radio_yellow()
        self.driver.save_screenshot('./screenshots/click_radi.png')
        allure.attach.file(source='./screenshots/click_radi.png', attachment_type=allure.attachment_type.PNG)

        self.page.select_likeAutomation_yes()
        self.driver.save_screenshot('./screenshots/select_likeAutomation.png')
        allure.attach.file(source='./screenshots/select_likeAutomation.png', attachment_type=allure.attachment_type.PNG)

        self.page.input_user_email(userEmail)
        self.driver.save_screenshot('./screenshots/input_user_email.png')
        allure.attach.file(source='./screenshots/input_user_email.png', attachment_type=allure.attachment_type.PNG)

        maxAutomationTool = self.page.get_max_automationTools()
        lenlistAutomationTools = self.page.get_lenght_automationTools()
        self.page.input_message(maxAutomationTool, lenlistAutomationTools)
        self.driver.save_screenshot('./screenshots/input_message.png')
        allure.attach.file(source='./screenshots/input_message.png',attachment_type=allure.attachment_type.PNG)

        self.page.click_button_submit()
        time.sleep(2)
        assert 'Message received!' == self.driver.switch_to.alert.text

        self.driver.switch_to.alert.accept()
