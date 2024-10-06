import sqlite3
from services.config_log import logger

class Databaser():
    def __init__(self, database_name='database\Database.db', need_clear_db=False):
        # Логируем инициализацию класса и указанные параметры
        logger.debug('Initial Databaser class')
        logger.trace(f'Database name - {database_name}')
        logger.trace(f'Cleaner database - {need_clear_db}')

        # Инициализируем переменные для работы с БД
        self.connect = sqlite3.connect(database_name)
        self.cursor = self.connect.cursor()
        
        # Удаляем предыдущие таблицы если при создании объекта был указан параметр 'True'
        if need_clear_db == True:
            logger.debug('Clean up database')
            self.__clear_database()

        # Создаем структуру таблиц в БД
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Users (login TEXT, password TEXT)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Accounts (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, login TEXT, password TEXT, other TEXT)')




    # Удаляем все таблицы в БД (использовать только для unit-тестов)
    def __clear_database(self):
        logger.debug('Call cleaning up database')
        self.cursor.execute('DROP TABLE Users')
        self.cursor.execute('DROP TABLE Accounts')




    # Сохраняем внесенные изменения и закрывает соединение объекта с БД (применять после зевершения основного цикла программы)
    def close(self):
        self.connect.commit()
        self.connect.close()




    # Добавление данных в таблицу Accounts
    def add_data(self, data: tuple) -> int:
        # Логируем начало выполнения метода и его параметры
        logger.debug('Call add_data function')
        logger.trace(f'passed data - {data}')
        
        # Делаем запрос на добавление в БД данных из переданного кортежа - (str, str, str, str)
        self.cursor.execute('INSERT INTO Accounts (title, login, password, other) VALUES(?, ?, ?, ?)', data)

        # Получаем id добавленной записи и логируем его значение
        added_id = self.cursor.lastrowid
        logger.trace(f'Data has been added with id - {added_id}')

        return added_id




    # Удаление данных из таблицы
    def delete_data(self, id: int):
        # Логируем начало выполнения метода и его параметры
        logger.debug(f'Call delete_data function')
        logger.trace(f'passed id - {id}')

        # Делаем запрос на удаление строк из БД с указанным значением id
        self.cursor.execute('DELETE FROM Accounts WHERE id=?', (id,))
        



    # Вывод общего списка данных (без логина и пароля)
    def get_general_data(self) -> list:
        # Логируем начало выполнения метода
        logger.debug('Call get_general_data function')

        # Делаем запрос на вывод id, title и other всех строк из БД
        self.cursor.execute('SELECT id, title, other FROM Accounts')

        # Получаем результат вывода и логируем его значение
        output = self.cursor.fetchall()
        logger.trace(f'Output: {output}')
        
        return output




    # Вывод полной информации по одной записи указанному по id
    def get_detail_data(self, id: int) -> list:
        # Логируем начало выполнения метода
        logger.debug(f'Call get_detail_data function')
        logger.trace(f'passed id - {id}')

        # Делаем запрос в БД на вывод всех данных из строки с указанным id
        self.cursor.execute('SELECT * FROM Accounts WHERE id=?', (id,))

        # Получаем результат вывода и логируем его значение
        output = self.cursor.fetchall()
        logger.trace(f'Output: {output}')

        return output