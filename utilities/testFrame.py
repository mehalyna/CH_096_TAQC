from Base.base import BaseSetup
from Pages.POM.auth import Auth
from Pages.POM.signIn import SignInUpClass
from Pages.POM.navigationMenu import NavigationMenu
from Pages.POM.profile_menu_page import ProfileMenu
<<<<<<< HEAD
from Pages.POM.searchPanelPage import SearchEventMenu
=======
from Pages.POM.categories import Categories
>>>>>>> 6e87498f1edd1e4c1240586e9ca9d0dd50f4e7d9
from Pages.ProfileMenu.add_event import CreateEvents



#create class with init driver for testing

class InitPagesDriver():


    def __init__(self, driver_init):
        self.driver_init = driver_init
        self.base = BaseSetup(self.driver_init)
        self.auth = Auth(self.base)
        self.signin = SignInUpClass(self.base)
        self.navigation = NavigationMenu(self.base)
        self.categories = Categories( self.base )
        # page opended from navigation menu
        self.prof_menu = ProfileMenu(self.base)
        self.creat_event = CreateEvents(self.base)
        # search event panel
        self.search = SearchEventMenu(self.base)
