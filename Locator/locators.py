from selenium.webdriver.common.by import By

#main page EventExpress
class MainLoginPageLocators():

    SIGNIN  = (By.CLASS_NAME, 'MuiButton-label')
    CATEGORIES = (By.CSS_SELECTOR, '.sidebar-header:nth-child(5) .nav-item-text')
    PROFILE = (By.CSS_SELECTOR, '.sidebar-header:nth-child(2) .nav-item-text')


# form of signin /signup


    EMAIL    = (By.NAME, 'email')
    PASSWORD  = (By.NAME, 'password')
    BUTTON_SIGIN = (By.CSS_SELECTOR, ".auth .MuiButtonBase-root.MuiButton-root.MuiButton-text.MuiButton-textPrimary.MuiButton-fullWidth:nth-child(2)")


# home page. page is availabled after log in
class HomePageLocators():
    CONFIG_PROFILE = (By.CSS_SELECTOR, "div a[href='/profile']" )

    PROFILE = (By.CSS_SELECTOR, "nav ul.list-unstyled .sidebar-header:nth-child(2)")

#page with personal info and with possibility to manage events
class ProfilePageLocators():
    ADD_EVENT = (By.CSS_SELECTOR,".MuiTabs-scroller.MuiTabs-fixed [type='button']:nth-child(5)")

# page for creating events
class AddEventPageLocators():
    #FROM DATE
    UPLOAD_PICTURE = (By.CSS_SELECTOR, ".placeholder-preview > input " )
    TITLE_EVENT = (By.NAME, 'title')
    FROM_DATE = (By.CSS_SELECTOR, ".react-datepicker-wrapper" )
    DATE_DATA = (By.CSS_SELECTOR, ".react-datepicker-ignore-onclickoutside") #month/day/year
    CALENDAR = (By.CSS_SELECTOR,".react-datepicker-popper")

#page for communication users with admins
class ContactUsPageLocators():

    CONTACT_US = (By.CSS_SELECTOR, '#root > div.left-sidebar-closed.left-sidebar > nav > ul > li:nth-child(5) > a > span > span')
    DESCRIPTION = (By.CSS_SELECTOR, 'textarea')
    SUBMIT = (By.CSS_SELECTOR, 'button:nth-child(3)')
    MESSAGE = (By.CSS_SELECTOR, '#root > div.MuiSnackbar-root.MuiSnackbar-anchorOriginBottomLeft > div')
    CLEAR = (By.CSS_SELECTOR, 'button:nth-child(4) > span.MuiButton-label')
    REQUIRED = (By.CSS_SELECTOR, 'p')

class ComunaPageLocators():

    COMUNA = (By.CSS_SELECTOR, 'li:nth-child(4)')
    SELECT_CORRESPONDENCE = (By.CSS_SELECTOR, 'button > div')
    SEND_MESSAGE = (By.CSS_SELECTOR, '.card-footer > form > div > div > input')
    SEND = (By.CSS_SELECTOR, '.MuiButton-label')
    OUR_MESSAGE = (By.CSS_SELECTOR, '.msg_card_body > div:nth-child(4) > div')
    MESSAGE = (By.CSS_SELECTOR, '.msg_card_body > div:nth-child(3) > div')







