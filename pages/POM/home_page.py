from locators.locators import HomePageLocators


class Home():
    """
    class for
    """

    def __init__(self, browser):
        self.browser = browser
        self.locator = HomePageLocators

    def check_pagination(self, *locator):
        """
        Function for checking  if pagination and element "last"
        are existed
        :param locator: css selector or xpath
        :return: None
        """
        try:
            self.browser.scroll_to_element(*locator)
            self.browser.click_on_element(*locator)
        except BaseException as e:
            print(e)

    def choose_last_event_title(self, title, *locator):
        """
        Function for choose last event title
        :param title: text for checking
        :param locator: css selector or xpath
        :return:
        """
        lst = self.browser.get_list_element('innerHTML', *locator)
        if lst[-1] == title:
            print('YEP')
        else:
            print('No title')

    def choose_last_event_p(self, msg, *locator):
        """
        Function for choose last event description
        :param msg: text for checking
        :param locator: css selector or xpath
        :return:
        """
        lst = self.browser.get_list_element('innerHTML', *locator)
        if msg in str(lst[-1]).strip('., '):
            print('YEP')
        else:
            print('No description')

    def choose_last_event_country(self, *locator):
        """
        Method for checking if country match
        :param locator: css selector or xpath
        :return:
        """
        lst = self.browser.get_list_element('innerHTML', *locator)
        country = str(lst[-1]).split(" ")[0]
        print(country)

    def choose_last_event_city(self, *locator):
        """
        Method for checking if country match
        :param locator: css selector or xpath
        :return:
        """
        lst = self.browser.get_list_element('innerHTML', *locator)
        city = str(lst[-1]).split(" ")[1]
        print(city)
