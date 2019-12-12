from selenium.webdriver.common.by import By

#main page EventExpress
class MainLoginPageLocators():

    SIGNIN  = (By.CLASS_NAME, 'MuiButton-label')


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