import requests

allureServer = 'http://192.168.99.101:5050' #localhost

def allure_api_get(api):
    return requests.get(allureServer + '/'+ api')
