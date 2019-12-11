from selenium.webdriver.common.by import By

class Locators_Login():

    username = (By.NAME, "email")
    password = (By.NAME, "password")
    signin = (By.CSS_SELECTOR, ".MuiButton-label")
    enter = (By.CSS_SELECTOR, ".MuiDialogActions-root > button:nth-child(2)")
