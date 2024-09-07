import sqlite3
from services.config_log import logger

class Databaser():
    def __init__(self, database_name='database\Database.db'):
        logger.debug('Initial Databaser class')
        self.connect = sqlite3.connect(database_name)
        self.cursor = self.connect.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Notes(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, login TEXT, password TEXT, other TEXT)')
        

    def close(self):
        self.connect.commit()
        self.connect.close()

    # Добавление данных в таблицу
    def add_data(self, data):
        logger.debug('Initial add_data function')
        logger.trace(f'passed data: {data}')
        self.cursor.execute('INSERT INTO Notes (title, login, password, other) VALUES(?, ?, ?, ?)', data)


    # Удаление данных из таблицы
    def delete_data(self, id):
        logger.debug(f'Initial delete_data by id={id}')
        self.cursor.execute('DELETE FROM Notes WHERE id=?', (id,))
        

    # Вывод общего списка данных (только id и названия)
    def get_list_data(self):
        logger.debug('Initial output general information')
        self.cursor.execute('SELECT id, title FROM Notes')
        return self.cursor.fetchall()

    # Вывод конкретных данных по id
    def get_definite_data(self, id):
        logger.debug(f'Initial output data by id={id}')
        self.cursor.execute('SELECT * FROM Notes WHERE id=?', (id,))
        return self.cursor.fetchall()