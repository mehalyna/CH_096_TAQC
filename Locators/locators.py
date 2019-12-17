from selenium.webdriver.common.by import By
from Data.test_data import ProfilePageEventsMenu, ProfileMenuPageHeaderInfo

class LoginPageLocators:
    # button for opening form of authorization
    SIGNIN = (By.CLASS_NAME, 'MuiButton-label')

    #form of signin/upR

    EMAIL_SIGNIN = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password')
    BUTTON_SIGIN = (By.CSS_SELECTOR,".auth .MuiButtonBase-root.MuiButton-root.MuiButton-text.MuiButton-textPrimary.MuiButton-fullWidth:nth-child(2)")
    CLEAR = (By.CSS_SELECTOR,".auth .MuiButtonBase-root.MuiButton-root.MuiButton-text.MuiButton-textPrimary.MuiButton-fullWidth:nth-child(1)")

class RegisterLocators:
    REGISTER = (By.CSS_SELECTOR, ".MuiTabs-scroller.MuiTabs-fixed button:nth-child(2)")
    EMAIL_SIGNIN = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    RE_PASSWORD = (By.NAME, "RepeatPassword")
    CLEAR = (By.CSS_SELECTOR,"")
    SIGNUP = (By.CSS_SELECTOR,)

class LogoProfileLocators:
    #boris ToDO
    pass

class NavigationMenuLocators:
    Home = (By.CSS_SELECTOR, "nav ul.list-unstyled .sidebar-header:nth-child(1)")
    PROFILE = (By.CSS_SELECTOR, "nav ul.list-unstyled .sidebar-header:nth-child(2)")
    SEARCH_USER = (By.CSS_SELECTOR, "nav ul.list-unstyled .sidebar-header:nth-child(3)")
    COMUNA = (By.CSS_SELECTOR, "nav ul.list-unstyled .sidebar-header:nth-child(4)")
    CONTACT_US = (By.CSS_SELECTOR, "nav ul.list-unstyled .sidebar-header:nth-child(5)")
     # "Navigation menu..."
     #        'Home': ('By.CSS_SELECTOR', ".sidebar-header:nth-child(1) .link"),
     #        'Profile': ('By.CSS_SELECTOR', ".sidebar-header:nth-child(2) .link"),
     #        'Search Users': ('By.CSS_SELECTOR', ".sidebar-header:nth-child(3) .link"),
     #        'Comuna': ('By.CSS_SELECTOR', ".sidebar-header:nth-child(4) .link"),
     #        'Contact us': ('By.CSS_SELECTOR', ".sidebar-header:nth-child(5) .link")

# search available on every page of EventExpress
class SearchMenuLocators:
    pass

class ContactUsPageLocators():

    CONTACT_US = (By.CSS_SELECTOR, '#root > div.left-sidebar-closed.left-sidebar > nav > ul > li:nth-child(5) > a > span > span')
    DESCRIPTION = (By.CSS_SELECTOR, 'textarea')
    SUBMIT = (By.CSS_SELECTOR, 'button:nth-child(3)')
    MESSAGE = (By.CSS_SELECTOR, '#root > div.MuiSnackbar-root.MuiSnackbar-anchorOriginBottomLeft > div')
    CLEAR = (By.CSS_SELECTOR, 'button:nth-child(4) > span.MuiButton-label')
    REQUIRED = (By.CSS_SELECTOR, 'p')


# displayed list of future events on home page
class HomePageLocators:
    pass

class ComunaPageLocators():

    SELECT_CORRESPONDENCE = (By.CSS_SELECTOR, 'button > div')
    SEND_MESSAGE = (By.CSS_SELECTOR, '.card-footer > form > div > div > input')
    SEND = (By.CSS_SELECTOR, '.MuiButton-label')
    OUR_MESSAGE = (By.CSS_SELECTOR, '.msg_card_body > div:nth-child(4) > div')
    MESSAGE = (By.CSS_SELECTOR, '.msg_card_body > div:nth-child(3) > div')

class ProfileMenuLocators:
    ''' Profile page and menu locators '''
    ADD_EVENT = (By.CSS_SELECTOR, ".MuiTabs-scroller.MuiTabs-fixed [type='button']:nth-child(5)")

class ProfilePageEventsMenuLocators:
    ''' Events menu object locators '''
    # User
    locators_dict = {ProfilePageEventsMenu.FUTURE_EVENTS: (By.CSS_SELECTOR, '#full-width-tab-0'),
                     ProfilePageEventsMenu.ARCHIVE_EVENTS: (By.CSS_SELECTOR, '#full-width-tab-1'),
                     ProfilePageEventsMenu.VISITED_EVENTS: (By.CSS_SELECTOR, '#full-width-tab-2'),
                     ProfilePageEventsMenu.EVENTS_TO_GO: (By.CSS_SELECTOR, '#full-width-tab-3'),
                     ProfilePageEventsMenu.ADD_EVENT: (By.CSS_SELECTOR, '#full-width-tab-4'),
                     'EVENT_MENU_PANEL': (By.CSS_SELECTOR, '.mt-2 > header div'), # Whole panel
                     'COUNT_MENU_ITEMS': (By.CSS_SELECTOR,'button[id*="full"]')
    } # panel locator; items align? ToDo
    # # "Events groups menu..."
    #         'FUTURE EVENTS': ('By.CSS_SELECTOR', "#full-width-tab-1 > .MuiTab-wrapper"),
    #         'ARCHIVE EVENTS': ('By.CSS_SELECTOR', "#full-width-tab-2 > .MuiTab-wrapper"),
    #         'VISITED EVENTS': ('By.CSS_SELECTOR', "#full-width-tab-3 > .MuiTab-wrapper"),
    #         'ADD EVENT': ('By.CSS_SELECTOR', "#full-width-tab-4 > .MuiTab-wrapper")
    # Admin ToDo

class ProfileMenuPageHeaderInfoLocators:
    ''' Locators for user info page header (central header)'''
    # User
    USER_NAME_LABEL = (By.CSS_SELECTOR, '.row:nth-child(1) > .col-4')
    USER_NAME_DATA = (By.CSS_SELECTOR, '.row:nth-child(1) > .col-8')
    USER_AGE_LABEL = (By.CSS_SELECTOR, '.row:nth-child(2) > .col-4')
    USER_AGE_DATA = (By.CSS_SELECTOR, '.row:nth-child(2) > .col-8')
     # ProfileMenuPageHeaderInfo.USER_GENDER_LABEL: (By.CSS_SELECTOR, '.row:nth-child(3) > .col-4'),
     # ProfileMenuPageHeaderInfo.USER_GENDER_DATA: (By.CSS_SELECTOR, '.row:nth-child(3) > .col-8'),
     # ProfileMenuPageHeaderInfo.USER_EMAIL_LABEL: (By.CSS_SELECTOR, '.row:nth-child(4) > .col-4'),
     # ProfileMenuPageHeaderInfo.USER_EMAIL_DATA: (By.CSS_SELECTOR, '.row:nth-child(4) > .col-4'),
     # ProfileMenuPageHeaderInfo.USER_INTERESTS_LABEL: (By.CSS_SELECTOR, '.row:nth-child(5) > .col-4'),
     # ProfileMenuPageHeaderInfo.USER_INTERESTS_DATA: (By.CSS_SELECTOR, '.row:nth-child(5) > .col-4'),
     # }
    # locators_dict = {ProfileMenuPageHeaderInfo.USER_NAME_LABEL: (By.CSS_SELECTOR, '.row:nth-child(1) > .col-4'),
    #                  ProfileMenuPageHeaderInfo.USER_NAME_DATA: (By.CSS_SELECTOR, '.row:nth-child(1) > .col-8'),
    #                  ProfileMenuPageHeaderInfo.USER_AGE_LABEL: (By.CSS_SELECTOR, '.row:nth-child(2) > .col-4'),
    #                  ProfileMenuPageHeaderInfo.USER_AGE_DATA: (By.CSS_SELECTOR, '.row:nth-child(2) > .col-8'),
    #                  ProfileMenuPageHeaderInfo.USER_GENDER_LABEL: (By.CSS_SELECTOR, '.row:nth-child(3) > .col-4'),
    #                  ProfileMenuPageHeaderInfo.USER_GENDER_DATA: (By.CSS_SELECTOR, '.row:nth-child(3) > .col-8'),
    #                  ProfileMenuPageHeaderInfo.USER_EMAIL_LABEL: (By.CSS_SELECTOR, '.row:nth-child(4) > .col-4'),
    #                  ProfileMenuPageHeaderInfo.USER_EMAIL_DATA: (By.CSS_SELECTOR, '.row:nth-child(4) > .col-4'),
    #                  ProfileMenuPageHeaderInfo.USER_INTERESTS_LABEL: (By.CSS_SELECTOR, '.row:nth-child(5) > .col-4'),
    #                  ProfileMenuPageHeaderInfo.USER_INTERESTS_DATA: (By.CSS_SELECTOR, '.row:nth-child(5) > .col-4'),
    #                  }
    # Admin ToDo


class HomePageOptionsPanelLocators:
    '''Left top menu (config, notification, logout) with user logo'''
    # button[type = "button"][title = "Sign out"]
    # user_info_css = 'h4.gs_copied'
    locators_dict = {
            'logout_button': (By.CSS_SELECTOR, 'button[title ="Sign out"]'),
            'user_info': (By.CSS_SELECTOR, 'h4.gs_copied'),
    }

class CartPanelsAtProfilePageLocators:
    '''child(cart_index). cart_index = 0 - EMPTY; >0 carts'''
    BLANK_CART = '.w-100 .h1'  # No Results
    CART_NTH = '.mt-2 .col-12:nth-child(3)'

class CreateEvent:
    EVENT_TITLE = (By.NAME, "title")
    CALENDAR = (By.CSS_SELECTOR, ".react-datepicker-wrapper")
    CALENDAR_VALUE = (By.CSS_SELECTOR, ".react-datepicker-ignore-onclickoutside")
    # calendar begin date of event
    FROM_DATE = (By.CSS_SELECTOR, ".react-datepicker-popper")
    # description about future event
    DESC_TEXT = (By.CSS_SELECTOR, "[name='description']")
    CATEGORY = (By.CSS_SELECTOR, ".rw-input-reset")



