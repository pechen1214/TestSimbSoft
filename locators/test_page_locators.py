from selenium.webdriver.common.by import By


class TestPageLocators:
    input_name = (By.XPATH, '//*[@id="name-input"]')
    input_password = (By.CSS_SELECTOR, 'input[type=password]')
    checkbox_favoriteDrink_milk = (By.CSS_SELECTOR, '#drink2')
    checkbox_favoriteDrink_coffe = (By.CSS_SELECTOR, '#drink3')
    radio_favoriteColor_yellow = (By.XPATH, '//*[@id="color3"]')
    select_automation = (By.ID, 'automation')
    input_email = (By.ID, 'email')
    list_automationTools = (By.CSS_SELECTOR, 'form ul>li')
    input_message = (By.ID, 'message')
    button_submit = (By.CSS_SELECTOR, '#submit-btn')
