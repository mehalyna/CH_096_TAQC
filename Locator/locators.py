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

class SearchEventPanelLocators():
    #Field search and filter
    SEARCH_FIELD = (By.CSS_SELECTOR, ".MuiInputBase-input")
    SELECT_DATE_FIELD = (By.CSS_SELECTOR, ".react-datepicker-ignore-onclickoutside")
    DATE_FROM = (By.CSS_SELECTOR, "div.form-group:nth-child(2) > div:nth-child(2)")
    DATE_TO = (By.CSS_SELECTOR, "div.form-group:nth-child(3) > div:nth-child(2) > div:nth-child(1)")
    RADIO_BUTTON_BLOCKED = (By.CSS_SELECTOR, "label.MuiFormControlLabel-root:nth-child(1)")
    RADIO_BUTTON_UNBLOCKED = (By.CSS_SELECTOR, "label.MuiFormControlLabel-root:nth-child(2)")
    RADIO_BUTTON_ALL = (By.CSS_SELECTOR, "label.MuiFormControlLabel-root:nth-child(3)")
    HASHTAGS_FIELD = (By.CSS_SELECTOR, "div.form-group:nth-child(4)")
    HASHTAGS_ITEM = (By.CSS_SELECTOR, "li.rw-list-option:nth-child(1)")  # nth-child(NAMBER_FIELD)
    BUTTON_MORE_FILTER = (By.CSS_SELECTOR, ".box > div:nth-child(2) > button:nth-child(1)")
    BUTTON_LESS = (By.CSS_SELECTOR, ".box > div:nth-child(6) > button:nth-child(1)")
    BUTTON_SEARCH = (By.CSS_SELECTOR, "button.MuiButtonBase-root:nth-child(2) > span:nth-child(1)")
    BUTTON_RESET = (By.CSS_SELECTOR, "button.MuiButton-textPrimary:nth-child(1) > span:nth-child(1)")

