"""TEST_MODE set to True, runs rests in silent mode: no UI while testing"""
URL = {
    'Test_mode': False,
    'Home_URL': 'http://localhost:57690/',
    'Browser': 'Firefox'}
"""Test data for logging in us user and admin"""
CREDENTIALS = {'User_name': 'user@gmail.com', 'User_password': '1qaz1qaz',
               'Admin_name': 'admin@gmail.com', 'Admin_password': '1qaz1qaz'}
"""Test data for Contact us page"""
CONTACT_US = {'Description_for_contact': 'very nice!!!'}
"""Test data for userinfo header from profile menu - events panels page"""
PROFILE_MENU_PAGE_HEADER = {
    'User_name_label': 'User Name:',
    'User_name_data': 'UserTest',
    'User_age_label': 'Age',
    'User_age_data': '19',
    'User_gender_label': 'Gender:',
    'User_gender_data': 'Other',
    'User_email_label': 'Email:',
    'User_email_data': 'user@gmail.com',
    'User_interests_label': 'Interests:'}


'''This test data using for creating event'''
CREATE_EVENT = {'title': 'Home Party',
                'image': 'Data/imageAddEvent/party.jpg',
                'description': 'cool party',

                }

'''Testdata: Locators for event's menu class ProfilePageEventsMenuLocators'''
PROFILE_PAGE_EVENTS_MENU = {'FUTURE_EVENTS': 'FUTURE EVENTS',
                            'ARCHIVE_EVENTS': 'ARCHIVE EVENTS',
                            'VISITED_EVENTS': 'VISITED EVENTS',
                            'EVENTS_TO_GO': 'EVENTS_TO_GO',
                            'ADD_EVENT': 'ADD_EVENT'
                            }

"""Events menu -> panel(s) object locators testdata"""
CART_PANELS_AT_PROFILE_PAGE = {'CART_NTH': 'CART_NTH',
                               'BLANK_CART': 'No Results',
                               'CART_PANEL': 'CART_PANEL',
                               'BLANK_CART_TEXT': 'No Results',
                               'CART_NTH_ID': ''
                               }

'''edit profile data of user'''
EDIT_PROFILE_DATA = {'USER_NAME': 'Tester',
                     'CURRENT_PASS': '1qaz1qaz',
                     'NEW_PASS': '2qaz2qaz'
                     }

'''data for creating and deleting category'''
CATEGORIESPAGE = {'category_old': 'Hello',
                  'category_new': 'Hello1'
                  }
