import random
import os

current_path = os.path.abspath(os.path.dirname(__file__))

class Config:
    HOME_URL = 'http://google.com'
    # HOME_URL = "https://localhost:44364/home/events?page=1"
    BROWSER = 'Chrome'
    # BROWSER = 'Firefox'
    # BROWSER = 'Opera'
    # CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))

class CreateEventData:

    # BASE_URL = "http://localhost:3183/home/events?page=1"
    TITLE = random.choice( ['New Year', 'Christmas', 'Malanka'] )
    IMAGE = os.path.join( current_path, 'party.jpg' )
    LOGIN_USER = 'user@gmail.com'
    PASSWORD_USER = '1qaz1qaz'
    DESCRIPTION = {"New Year": "Happy 2020 Year!!!Weclome to the Party"}
    ATT_DATA = "innerHtml"

class ProfileMenu:
    '''User Name:    UserTest
    Age:    19
    Gender:    Other
    Email:    user@gmail.com
    Interests:      #Mount
                    #Golf
                    #Team-Building
                    #Swimming
                    #Gaming
                    #QC testing event
                    #Meeting
                    #Summer'''
    pass