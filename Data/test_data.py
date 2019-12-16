import random
import os

current_path = os.path.abspath(os.path.dirname(__file__))


class CreateEventData( ):


    # BASE_URL = "http://localhost:3183/home/events?page=1"
    TITLE = random.choice( ['New Year', 'Christmas', 'Malanka'] )
    IMAGE = os.path.join( current_path, 'party.jpg' )
    LOGIN_USER = 'user@gmail.com'
    PASSWORD_USER = '1qaz1qaz'
    DESCRIPTION = {"New Year": "Happy 2020 Year!!!Weclome to the Party"}
    ATT_DATA = "innerHtml"


