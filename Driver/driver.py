import os
from selenium import webdriver
browser_setup = {
    "browser" : "Firefox",
    "url" : "http://localhost:57690/home/events?page=1"
}

#Chrome
path = os.path.abspath(os.path.dirname(__file__) + '\\geckodriver')

def wrapper(browser):
    if browser == "Firefox":
        return  webdriver.Firefox(executable_path=path)
    elif browser == "Chrome":
        return  webdriver.Chrome()
    else:
        raise Exception("Selected browser not supported")

