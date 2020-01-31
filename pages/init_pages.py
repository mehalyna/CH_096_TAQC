""" POM init """
from base.base import BaseSetup
from pages.POM.auth import Auth
from pages.POM.home_page import Home
from pages.POM.sign_in import SignInUpClass
from pages.POM.navigationMenu import NavigationMenu
from pages.POM.profile_menu_page import ProfileMenu
from pages.POM.searchPanelPage import SearchEventMenu
from pages.POM.categories import Categories
from pages.ProfileMenu.add_event import CreateEvents
from pages.POM.event_menu_page import EventsMenu
from pages.POM.contact_us_page import ContactUs
from pages.POM.comuna_page import Comunication


class InitPages:
    """
    Instantiate POM pages
    """

    def __init__(self, driver_init):
        """
        Initialize app object which encapsulate pages classes to simplify work with test Framework.
        :param driver_init: webdriver object
        """
        self.base = BaseSetup(driver_init)
        self.auth = Auth(self.base)
        self.signin = SignInUpClass(self.base)
        self.navigation = NavigationMenu(self.base)
        self.categories = Categories(self.base)
        self.prof_menu = ProfileMenu(self.base)
        self.creat_event = CreateEvents(self.base)
        self.search = SearchEventMenu(self.base)
        # page for communication user with admin
        self.contact = ContactUs(self.base)
        # events menu at navigation menu --> profile page
        self.event_menu = EventsMenu(self.base)
        # self.event_carts = EventsMenuCarts(self.base)
        self.home_page = Home(self.base)
        # for comunication with another users
        self.comuna = Comunication(self.base)
