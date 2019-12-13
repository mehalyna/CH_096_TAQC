import os
from selenium import webdriver

browser_setup = {
    "browser": "Chrome",
    "url": "https://localhost:44364/home/events?page=1"
    }

path_chrom = os.path.abspath(os.path.dirname(__file__) + '/chromedriver')
path_gecko = os.path.abspath(os.path.dirname(__file__) + '/geckodriver')


def wrapper(browser):
    if browser == "Firefox":
        return webdriver.Firefox(executable_path=path_gecko)
    elif browser == "Chrome":
        return webdriver.Chrome(executable_path=path_chrom)
    else:
        raise Exception("Selected browser not supported")


#
# setup = { 'Chrome': {
#
#                     }
#
# }

