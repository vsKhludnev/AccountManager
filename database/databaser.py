import sqlite3

class Databaser():
    def __init__(self, database_name='Database.db'):
        self.connect = sqlite3.connect(database_name)
        self.cursor = self.connect.cursor()

        self.cursor.execute('CREATE TABLE IF NOT EXISTS Notes(id integer, title text, login text, password text, other text)')

    def __close(self):
        self.connect.commit()
        self.connect.close()

    def add_data(self):
        pass

    def delete_data(self):
        pass

    def get_data(self):
        pass