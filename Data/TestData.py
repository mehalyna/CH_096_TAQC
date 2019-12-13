import random
import os

current_path = os.path.abspath(os.path.dirname(__file__))


class TestData():

    TITLE = random.choice( ['New Year', 'Christmas', 'Malanka'] )
    IMAGE = os.path.join( current_path, 'party.jpg' )
    LOGIN_USER = 'user@gmail.com'
    PASSWORD_USER = '1qaz1qaz'
    LOGIN_ADMIN = 'admin@gmail.com'
    DESCRIPTION = 'very nice!!!'



