import sqlite3
from services.config_log import logger

class Databaser():
    def __init__(self, database_name='database\Database.db'):
        logger.debug('Initial Databaser class')
        self.connect = sqlite3.connect(database_name)
        self.cursor = self.connect.cursor()

        try:
            self.cursor.execute('CREATE TABLE Notes(id integer, title text, login text, password text, other text)')
        except sqlite3.OperationalError:
            logger.warning('Table Notes already exists')
        else:
            logger.info(f'{database_name} is create')

    def __close(self):
        self.connect.commit()
        self.connect.close()

    def add_data(self):
        pass

    def delete_data(self):
        pass

    def get_data(self):
        pass