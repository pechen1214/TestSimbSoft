from selenium.webdriver.support.ui import Select
from locators.test_page_locators import TestPageLocators


class TestPage:
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def input_user_name(self, userName):
        name = self.driver.find_element(*TestPageLocators.input_name)
        name.send_keys(userName)

    def input_user_password(self, userPassword):
        password = self.driver.find_element(*TestPageLocators.input_password)
        password.send_keys(userPassword)

    def click_checkbox_milk(self):
        checkboxMilk = self.driver.find_element(*TestPageLocators.checkbox_favoriteDrink_milk)
        checkboxMilk.click()

    def click_checkbox_coffe(self):
        checkboxCoffe = self.driver.find_element(*TestPageLocators.checkbox_favoriteDrink_coffe)
        checkboxCoffe.click()

    def click_radio_yellow(self):
        radioYellow = self.driver.find_element(*TestPageLocators.radio_favoriteColor_yellow)
        radioYellow.click()

    def select_likeAutomation_yes(self):
        selectLikeAutomation = Select(self.driver.find_element(*TestPageLocators.select_automation))
        selectLikeAutomation.select_by_value('yes')

    def input_user_email(self, userEmail):
        email = self.driver.find_element(*TestPageLocators.input_email)
        email.send_keys(userEmail)

    def get_max_automationTools(self):
        arrayAutomationTool = []
        listAutomationTools = self.driver.find_elements(*TestPageLocators.list_automationTools)
        for automationTool in listAutomationTools:
            arrayAutomationTool.append(automationTool.text)
        return max(arrayAutomationTool, key=len)

    def get_lenght_automationTools(self):
        listAutomationTools = self.driver.find_elements(*TestPageLocators.list_automationTools)
        return len(listAutomationTools)

    def input_message(self, maxAutomationTool, lenlistAutomationTools):
        message = self.driver.find_element(*TestPageLocators.input_message)
        message.send_keys('Kоличество инструментов, описанных в пункте Automation tools - ' + str(lenlistAutomationTools) + '\nИнструмент из списка Automation tools, содержащий наибольшее количество символов - ' + maxAutomationTool)

    def click_button_submit(self):
        buttonSubmit = self.driver.find_element(*TestPageLocators.button_submit)
        buttonSubmit.click()
