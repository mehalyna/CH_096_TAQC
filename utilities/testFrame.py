from Base.base import BaseSetup
from Pages.POM.auth import Auth
from Pages.POM.signIn import SignInUpClass
from Pages.POM.navigationMenu import NavigationMenu
from Pages.POM.profile_menu_page import ProfileMenu
from Pages.POM.searchPanelPage import SearchEventMenu
from Pages.POM.categories import Categories
from Pages.ProfileMenu.add_event import CreateEvents
from Pages.POM.event_menu_page import EventsMenu, EventsMenuCarts
from Pages.POM.contact_us_page import ContactUs
from Pages.POM.comuna_page import ComunaClass


#create class with init driver for testing

class InitPagesDriver():


    def __init__(self, driver_init):
        self.driver_init = driver_init
        #self.base = BaseSetup(self.driver_init)
        self.auth = Auth(self.driver_init)
        self.signin = SignInUpClass(self.driver_init)
        self.navigation = NavigationMenu(self.driver_init)
        self.categories = Categories(self.driver_init)
        # page opended from navigation menu
        self.prof_menu = ProfileMenu(self.driver_init)
        self.creat_event = CreateEvents(self.driver_init)
        # search event panel
        self.search = SearchEventMenu(self.driver_init)
        self.contact = ContactUs(self.driver_init)
        self.event_menu = EventsMenu(self.driver_init)
        self.event_carts = EventsMenuCarts(self.driver_init)
        self.comuna = ComunaClass(self.driver_init)
