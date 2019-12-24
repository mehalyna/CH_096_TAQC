import random
import os

current_path = os.path.abspath(os.path.dirname(__file__))

class Config:
    # HOME_URL = 'https://www.linkedin.com/login'
    # HOME_URL = 'http://google.com'
    # HOME_URL = "http://localhost:3183/home/events?page=1"
    HOME_URL = "https://localhost:44364/home/events?page=1"
    # HOME_URL = "http://localhost:3183/home/events?page=1"
    # HOME_URL = "http://localhost:49862/home/events?page=1"
    # HOME_URL = "http://localhost:49862/home/events?page=1"
    # HOME_URL = "https://localhost:44364/home/events?page=1"
    # BROWSER = 'Chrome'
    BROWSER = 'Firefox'
    # BROWSER = 'IE'
    # CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))

class CreateEventData():


    TITLE = random.choice( ['New Year', 'Christmas', 'Malanka'] )
    IMAGE = os.path.join( current_path,  'imageAddEvent\\party.jpg' )
    LOGIN_USER = 'user@gmail.com'
    PASSWORD_USER = '1qaz1qaz'
    DESCRIPTION = {"New Year": "Happy 2020 Year!!!Weclome to the Party"}
    ATT_DATA = "innerHtml"



class ContactUsData():

    DISCRIPTION = "very nice!!!"


class ProfileMenuPageHeaderInfo:

    USER_NAME_LABEL = 'User Name:'
    USER_NAME_DATA = 'UserTest'

    USER_AGE_LABEL = 'Age:'
    USER_AGE_DATA = '19'

    USER_GENDER_LABEL = 'Gender:'
    USER_GENDER_DATA = 'Other'

    USER_EMAIL_LABEL = 'Email:'
    USER_EMAIL_DATA = 'user@gmail.com'

    USER_INTERESTS_LABEL = 'Interests:'
    USER_INTERESTS_DATA = {'#Mount', '#Golf', '#Team-Building', '#Swimming', '#Gaming',\
                           '#QC testing event', '#Meeting', '#Summer'}

class ProfilePageEventsMenu:
    ''' Testdata: Locators for event's menu.
    class ProfilePageEventsMenuLocators'''
    FUTURE_EVENTS = 'FUTURE EVENTS'
    ARCHIVE_EVENTS = 'ARCHIVE EVENTS'
    VISITED_EVENTS = 'VISITED EVENTS'
    EVENTS_TO_GO = 'EVENTS TO GO'
    ADD_EVENT = 'ADD_EVENT'


class HomePageOptionsPanel:
    '''Left top menu (config, notification, logout) with user logo'''
    USER_NAME_DATA_DICT = {'user@gmail.com': 'UserTest'}
    # ToDo

##
#         # "Navigation menu..."
#         'Home': ('By.CSS_SELECTOR', ".sidebar-header:nth-child(1) .link"),
#         'Profile': ('By.CSS_SELECTOR', ".sidebar-header:nth-child(2) .link"),
#         'Search Users': ('By.CSS_SELECTOR', ".sidebar-header:nth-child(3) .link"),
#         'Comuna': ('By.CSS_SELECTOR', ".sidebar-header:nth-child(4) .link"),
#         'Contact us': ('By.CSS_SELECTOR', ".sidebar-header:nth-child(5) .link"),
#             }


class CartPanelsAtProfilePage:
    ''' Events menu -> panel(s) object locators testdata '''
    CART_NTH = 'CART_NTH'
    BLANK_CART = 'No Results'
    CART_PANEL = 'CART_PANEL'


    BLANK_CART_TEXT = 'No Results'
    CART_NTH_ID = ''  # on mouse hover - tip arising
