"""
TEST_MODE set to True, runs rests in silent mode: no UI while testing
"""
import os

URL = {
    'Test_mode': False,
    'URL_HOST': 'http://34.65.101.58:5002',
    'Home_URL': 'http://34.65.101.58:5002/home/events?page=1',
    'Browser': 'Firefox'
}

"""
Test data for logging in us user and admin
"""
CREDENTIALS = {
        'User_name': 'user@gmail.com',
        'User_password': '1qaz1qaz',
        'Admin_name': 'admin@gmail.com',
        'Admin_password': '1qaz1qaz'
        }
"""
Test data for 'Contact us' page
"""
CONTACT_US = {
    'Description_for_contact': 'You have problems with some users and theirs events!'}
"""
Test data for userinfo header from profile menu - events panels page
"""
PROFILE_MENU_INFO = {
    'User_name_label': 'User Name:',
    'User_name_data': 'UserTest',
    'User_age_label': 'Age',
    'User_age_data': '35',
    'User_gender_label': 'Gender:',
    'User_gender_data': 'Other',
    'User_email_label': 'Email:',
    'User_email_data': 'user@gmail.com',
    'User_interests_label': 'Interests:',
    'User_interests_data': {'Mount', 'Golf', '#Team-Building', '#Swimming',
                            '#Gaming', '#Sea', '#Summer'}
    }

"""This test data using for creating event"""
CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
image = 'Data\\imageAddEvent\\EarthGarden.jpg'
image1 = 'Data\\imageAddEvent\\Mysteryland.jpg'
path_to_picture = os.path.join(CURRENT_PATH, image1)
CREATE_EVENT = {'title': 'Sensation WHITE',
                'title1' : 'MYSTERYLAND MUSIC FESTIVAL',
                'image': path_to_picture,
                'description': 'If you want crazy party come to us',
                'description1' : 'We are Mysteryland, the worlds '
                                'longest running electronic music festival',
                'country': 'Austria',
                'city': 'Rio Negro',


                }

"""
Testdata: Locators for event's menu class ProfilePageEventsMenuLocators
"""
PROFILE_PAGE_EVENTS_MENU = {'FUTURE_EVENTS': 'FUTURE EVENTS',
                            'ARCHIVE_EVENTS': 'ARCHIVE EVENTS',
                            'VISITED_EVENTS': 'VISITED EVENTS',
                            'EVENTS_TO_GO': 'EVENTS TO GO',
                            'ADD_EVENT': 'ADD EVENT'
                            }

"""
Events menu -> panel(s) object locators testdata
"""
CART_PANELS_AT_PROFILE_PAGE = {'CART_NTH': 'CART_NTH',
                               'BLANK_CART': 'No Results',
                               'CART_PANEL': 'CART_PANEL',
                               'BLANK_CART_TEXT': 'No Results',
                               'CART_NTH_ID': ''
                               }

"""
edit profile data of user
"""
EDIT_PROFILE_DATA = {'USER_NAME': 'Tester',
                     'CURRENT_PASS': '1qaz1qaz',
                     'NEW_PASS': '2qaz2qaz'
                     }

"""
data for creating and deleting category
"""
CATEGORIESPAGE = {'category_old': 'Hello',
                  'category_new': 'Hello1'
                  }

'''data for create new event'''
CREATE_EVENT_SQL = {
        'UserId': 'f320932e-aac2-4999-32d3-08d79b47df59',
        'PhotoId': 'D1933101-E4B2-4664-2629-08D7A0033B62',
        'CityId': '418ad80a-85da-4033-f8df-08d79b47df2b',
        'DateFrom': '2020-02-08',
        'DateTo': '2020-02-10',
        'Descript': 'Event for testing search',
        'Title': 'Test Event',
        }
