import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class TodosMyTests(unittest.TestCase):
    page_url = 'https://practice-automation.com/form-fields/'

    def setUp(self) -> None:
        super().setUp()

        options = webdriver.ChromeOptions()
        ##options.add_argument('headless')

        self.driver = webdriver.Chrome(options=options)

        self.driver.get(self.page_url)

    def tearDown(self) -> None:
        self.driver.quit()

        super().tearDown()


    ## Тестовое задание
    def test_AddTaskSpaceCharacter_NoElementsInTheList(self):
        userName = 'Andrey'
        arrayAutomationTool = []

        name = self.driver.find_element(By.XPATH, '//*[@id="name-input"]')
        name.send_keys(userName)

        password = self.driver.find_element(By.CSS_SELECTOR,'input[type=password]')
        password.send_keys('password')

        checkboxMilk = self.driver.find_element(By.CSS_SELECTOR, '#drink2')
        checkboxMilk.click()

        checkboxCoffe = self.driver.find_element(By.CSS_SELECTOR, '#drink3')
        checkboxCoffe.click()

        radioYellow = self.driver.find_element(By.XPATH, '//*[@id="color3"]')
        radioYellow.is_selected()

        selectLikeAutomation = Select(self.driver.find_element(By.ID, 'automation'))
        selectLikeAutomation.select_by_value('yes')

        email = self.driver.find_element(By.ID, 'email')
        email.send_keys(userName.lower()+'@example.com')
        time.sleep(2)

        listAutomationTools = self.driver.find_elements(By.CSS_SELECTOR, 'form ul>li')
        message = self.driver.find_element(By.ID, 'message')
        for automationTool in listAutomationTools:
            arrayAutomationTool.append(automationTool.text)
        maxAutomationTool = max(arrayAutomationTool,key=len)
        lenlistAutomationTools = len(listAutomationTools)
        message.send_keys('Kоличество инструментов, описанных в пункте Automation tools - '+str(lenlistAutomationTools)+'\nИнструмент из списка Automation tools, содержащий наибольшее количество символов - '+ maxAutomationTool)
        time.sleep(5)

        buttonSubmit = self.driver.find_element(By.CSS_SELECTOR, '#submit-btn')
        buttonSubmit.click()
        time.sleep(10)

        alert = self.driver.switch_to.alert
        print(alert.text)
        self.assertEqual('Message received!', alert.text)
        time.sleep(10)