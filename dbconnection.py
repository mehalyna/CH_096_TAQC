import uuid
import pyodbc as pyodbc
from config import CREATE_EVENT_SQL as event


class Connection:
    def __init__(self):
        self.server = "34.65.101.58"
        self.database = "EventsExpress"
        self.username = "SA"
        self.password = ""
        self.driver = "ODBC Driver 17 for SQL Server"
        self.conn = pyodbc.connect(
                                "DRIVER=" + self.driver + 
                                ";SERVER=" + self.server + 
                                ";PORT=1433;DATABASE=" + self.database + 
                                ";UID=" + self.username + 
                                ";PWD=" + self.password
                                )   
        self.cursor = self.conn.cursor()

    def delete_user_with_email(self, email):
        self.cursor.execute(f"Delete from Users where Email like '{email}'")
        self.cursor.commit()

    def edit_user_with_name(self, name, newname):
        self.cursor.execute(
            f"UPDATE Users set Name = '{newname}' where Name like '{name}'"
        )
        self.cursor.commit()

    def edit_user_with_birthday(self, name, birth):
        self.cursor.execute(
            f"UPDATE Users set Birthday = '{birth}' where Name like '{name}'"
        )
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
                            '{event['PhotoId']}', '{event['UserId']}');
                            """
                            )
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
            f"Update Categories set Name ='{newname}' where Name like '{name}'"
        )
        self.cursor.commit()

    def create_category_with_name(self, name):
        guid = uuid.uuid4()
        self.cursor.execute(
            f"INSERT INTO Categories(Id, Name) VALUES ('{guid}','{name}');"
        )
        self.cursor.commit()

    def get_id_using_name(self, name):
        self.cursor.execute(f"select Id from Categories where Name = '{name}'")
        return str(self.cursor.fetchone()[0])

    def confirm_useremail_on_register(self, email):
        self.cursor.execute(
            f"UPDATE Users SET EmailConfirmed = 1 WHERE Email like '{email}'"
        )
        self.cursor.commit()

    def send_sql(self, execute):
        self.cursor.execute("{}".format(execute))
        self.cursor.commit()

    def close(self):
        self.conn.close()


Connection().delete_event_with_name('Test Event')
