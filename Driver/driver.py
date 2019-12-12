import os
from selenium import webdriver
browser_setup = {
    "browser" : "Chrome",
    "url" : "https://localhost:44364/home/events?page=1"
}

#Chrome
path = os.path.abspath(os.path.dirname(__file__) + '/chromedriver')

def wrapper(browser):
    if browser == "Firefox":
        return  webdriver.Firefox(executable_path=path)
    elif browser == "Chrome":
        return  webdriver.Chrome(executable_path=path)
    else:
        raise Exception("Selected browser not supported")

