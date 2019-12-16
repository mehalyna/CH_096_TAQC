from Base.base import Base
from Pages.POM.auth import Auth
from Pages.POM.signIn import SignInUpClass
from Pages.POM.navigationMenu import NavigationMenu
from Pages.POM.profile_menu_page import ProfileMenu
from Pages.ProfileMenu.add_event import CreateEvents


class InitPagesDriver():
    '''Instantiating a class by making a composition'''

    def __init__(self, driver_init):
        self.driver_init = driver_init
        self.base = Base(self.driver_init)
        self.auth = Auth(self.base)
        self.signin = SignInUpClass( self.base )
        self.navigation = NavigationMenu(self.base)
        # page opended from navigation menu
        self.prof_menu = ProfileMenu(self.base)
        self.creat_event = CreateEvents(self.base)
