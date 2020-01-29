import uuid
import pyodbc as pyodbc
from config import CREATE_EVENT_SQL as event
from credentials import CredentDb as Db
from config import SEND_MESSAGE_SQL as message
from datetime import datetime


class Connection:

    def __init__(self):
        self.server = Db.server
        self.database = Db.database
        self.username = Db.username
        self.password = Db.password
        self.driver = Db.driver
        self.conn = pyodbc.connect('DRIVER=' + self.driver +
                                   ';SERVER=' + self.server +
                                   ';PORT=1433;DATABASE=' + self.database +
                                   ';UID=' + self.username +
                                   ';PWD=' + self.password)
        self.cursor = self.conn.cursor()

    def delete_user_with_email(self, email):
        self.cursor.execute(f"Delete from Users where Email like '{email}'")
        self.cursor.commit()

    def edit_user_with_name(self, name, newname):
        self.cursor.execute(
            f"UPDATE Users set Name = '{newname}' where Name like '{name}'")
        self.cursor.commit()

    def edit_user_with_birthday(self, name, birth):
        self.cursor.execute(
            f"UPDATE Users set Birthday = '{birth}' where Name like '{name}'")
        self.cursor.commit()

    def edit_user_with_gender(self, name, sex):
        """
        sex: 0=Other, 1=Male, 2=Female
        """
        self.cursor.execute(
            f"UPDATE Users set Gender = '{sex}' where Name like '{name}'"
        )
        self.cursor.commit()

    def create_event(self,
                     title=event["Title"],
                     disc=event["Descript"],
                     date_from=event["DateFrom"],
                     date_to=event["DateTo"]):

        guid = uuid.uuid4()
        self.cursor.execute(f"""
                            INSERT INTO EventsExpress.dbo.Events
                            (Id,IsBlocked, Title, Description,
                            DateFrom, DateTo, CityId, PhotoId, OwnerId)
                            VALUES('{guid}', 0, '{title}', '{disc}',
                            '{date_from}', '{date_to}', '{event['CityId']}', 
                            '{event['PhotoId']}', '{Connection().
                            get_userId_by_name('Admin')}');
                            """)
        self.cursor.commit()

    def get_id_event_by_name(self, name):
        self.cursor.execute(f"SELECT Id FROM Events WHERE Name = '{name}'")
        return str(self.cursor.fetchone()[0])

    def delete_event_with_name(self, name):
        self.cursor.execute(f"Delete from Events where Title like '{name}'")
        self.cursor.commit()

    def delete_category_with_name(self, name):
        self.cursor.execute(f"Delete from Categories where Name like '{name}'")
        self.cursor.commit()

    def edit_category_with_name(self, name, newname):
        self.cursor.execute(
            f"Update Categories set Name = '{newname}' where Name like '{name}'")
        self.cursor.commit()

    def create_category_with_name(self, name):
        guid = uuid.uuid4()
        self.cursor.execute(
            f"INSERT INTO Categories(Id, Name) VALUES ('{guid}','{name}');")
        self.cursor.commit()

    def get_id_using_name(self, name):
        self.cursor.execute(f"select Id from Categories where Name = '{name}'")
        return str(self.cursor.fetchone()[0])

    def get_userId_by_name(self, name):
        self.cursor.execute(f"SELECT Id from Users where Name = '{name}'")
        return str(self.cursor.fetchone()[0])

    def get_name_of_category_using_id(self, id):
        self.cursor.execute(
            f"select Name from Categories where Id like '{id}'")
        return str(self.cursor.fetchone()[0])

    def get_count_of_category_on_name(self, name):
        self.cursor.execute(
            f"SELECT COUNT(1) FROM Categories WHERE Name like '{name}'")
        return str(self.cursor.fetchone()[0])

    def confirm_useremail_on_register(self, email):
        self.cursor.execute(
            f"UPDATE Users SET EmailConfirmed = 1 WHERE Email like '{email}'")
        self.cursor.commit()

    def send_message(self, id_sender=message['id_sender'],
                     date_created=datetime.now(),
                     edited=0, text=message['text'],
                     chat_room_id=message['chat_room_id'],
                     seen=0):
        guid = uuid.uuid4()
        self.cursor.execute(f"""
                            INSERT INTO EventsExpress.dbo.Message
                            (Id, SenderId, DateCreated, Edited,
                            Text, ChatRoomId, Seen)
                            VALUES ('{guid}', '{id_sender}', '{date_created}',
                            '{edited}', '{text}', '{chat_room_id}', '{seen}');
                            """)
        self.cursor.commit()

    def delete_mes_with_text(self, mes=message['text']):
        self.cursor.execute(
            f"Delete from EventsExpress.dbo.Message where Text like '{mes}'")
        self.cursor.commit()

    def send_sql(self, execute):
        self.cursor.execute("{}".format(execute))
        self.cursor.commit()

    def close(self):
        self.conn.close()

