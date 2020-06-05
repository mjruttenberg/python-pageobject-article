from selenium.webdriver.common.by import By
import time

class Login:
    def __init__(self, driver):
        self.driver = driver

        self.email = "tomsmith"
        self.password = "SuperSecretPassword!"

        self.username_locator = "username"
        self.password_locator = "password"
        self.login_button = ".fa.fa-2x.fa-sign-in" # 3 classes chained together, which we will use via a CSS selector

    def login(self):
        self.driver.find_element(By.ID, self.username_locator).send_keys(self.email)
        self.driver.find_element(By.ID, self.password_locator).send_keys(self.password)
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, self.login_button).click()
        time.sleep(3)
