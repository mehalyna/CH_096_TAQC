from selenium.webdriver.common.by import By


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
    pass

class NavigationMenuLocators:
    Home = (By.CSS_SELECTOR, "nav ul.list-unstyled .sidebar-header:nth-child(1)")
    PROFILE = (By.CSS_SELECTOR, "nav ul.list-unstyled .sidebar-header:nth-child(2)")
    SEARCH_USER = (By.CSS_SELECTOR, "nav ul.list-unstyled .sidebar-header:nth-child(3)")
    COMUNA = (By.CSS_SELECTOR, "nav ul.list-unstyled .sidebar-header:nth-child(4)")
    CONTACT_US = (By.CSS_SELECTOR, "nav ul.list-unstyled .sidebar-header:nth-child(5)")


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

class EventsMenuLocators:
    ''' Events menu object locators '''
    locators_dict = {'FUTURE EVENTS': (By.ID, '#full-width-tab-0'),
                     'ARCHIVE EVENTS': (By.ID, '#full-width-tab-1'),
                     'VISITED EVENTS': (By.ID, '#full-width-tab-2'),
                     'EVENTS TO GO': (By.ID, '#full-width-tab-3'),
                     'ADD_EVENT': (By.ID, '#full-width-tab-3')
    }
    '''User Name:
UserTest
Age:
19
Gender:
Other
Email:
user@gmail.com
Interests:
#Mount
#Golf
#Team-Building
#Swimming
#Gaming
#QC testing event
#Meeting
#Summer'''


class CreateEvent:
    EVENT_TITLE = (By.NAME, "title")
    CALENDAR = (By.CSS_SELECTOR, ".react-datepicker-wrapper")
    CALENDAR_VALUE = (By.CSS_SELECTOR, ".react-datepicker-ignore-onclickoutside")
    # calendar begin date of event
    FROM_DATE = (By.CSS_SELECTOR, ".react-datepicker-popper")
    # description about future event
    DESC_TEXT = (By.CSS_SELECTOR, "[name='description']")
    CATEGORY = (By.CSS_SELECTOR, ".rw-input-reset")



