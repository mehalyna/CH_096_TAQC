import uuid
import pyodbc as pyodbc


class Connection():

    def __init__(self):
        self.server = 'tcp:34.65.101.58'
        self.database = 'EventsExpress'
        self.username = 'SA'
        self.password = '11D3v0ps'
        self.driver = '{ODBC Driver 17 for SQL Server}'
        try:
            self.conn = pyodbc.connect('DRIVER=' + self.driver +
                                    ';SERVER=' + self.server +
                                    ';PORT=1433;DATABASE=' + self.database +
                                    ';UID=' + self.username +
                                    ';PWD=' + self.password)
        except pyodbc.Error as err:
            print('DB Error:', err)
        else:
            print('Connect OK ')
        self.cursor = self.conn.cursor()

    def edit_user_with_name(self, name, newname):
        self.cursor.execute(f"UPDATE Users set Name = '{newname}' where Name like '{name}'")
        self.cursor.commit()

    def edit_user_with_birthday(self, name, birth):
        self.cursor.execute(f"UPDATE Users set Birthday = '{birth}' where Name like '{name}'")
        self.cursor.commit()

    def edit_user_with_gender(self, name, sex):
        """0=Other, 1=Male, 2=Female"""
        self.cursor.execute(f"UPDATE Users set Gender = '{sex}' where Name like '{name}'")
        self.cursor.commit()

    def edit_user_with_email(self, email, newmail):
        self.cursor.execute(f"UPDATE Users set Email = '{newmail}' where Email like '{email}'")
        self.cursor.commit()

    def delete_user_with_email(self, name):
        self.cursor.execute(f"DELETE from Users where Email like '{name}'")
        self.cursor.commit()

    def create_category_with_name(self, name):
        guid = uuid.uuid4()
        self.cursor.execute(f"INSERT INTO Categories(Id, Name) VALUES ('{guid}','{name}')")
        self.cursor.commit()

    def edit_category_with_name(self, name, newname):
        self.cursor.execute(f"UPDATE Categories set Name = '{newname}' where Name like '{name}'")
        self.cursor.commit()

    def delete_category_with_name(self, name):
        self.cursor.execute(f"DELETE from Categories where Name like '{name}'")
        self.cursor.commit()

    def get_token_user_name(self, name):
        self.cursor.execute(f"SELECT Id from Categories where Name = '{name}'")
        return str(self.cursor.fetchone()[0])

    def send_sql(self, execut):
        self.cursor.execute("{}".format(execut))
        self.cursor.commit()

    def close(self):
        self.conn.close()

testdb = Connection()
testdb.send_sql("UPDATE Categories set Name = 22 where Name like 222")
