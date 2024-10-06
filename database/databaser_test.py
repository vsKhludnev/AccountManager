from database.databaser import Databaser
from services.custom_tester import Tester

if __name__ == '__main__':
    tester = Tester()
    db = Databaser('database\Database_test.db', need_clear_db=True)

    test_data_1 = ('Vk', 'login', 'password', '...')
    test_data_2 = ('Telegramm', 'this login', 'security password', 'other info')

    # Проверка вывода из пустой БД
    received_data = db.get_general_data()
    tester.basic_test('Receive general data from emty database', received_data, [])

    receive_detail_data = db.get_detail_data(1)
    tester.basic_test('Receive detail data by id from empty database', receive_detail_data, [])


    # Проверка добавления данных
    first_id = db.add_data(test_data_1)
    second_id = db.add_data(test_data_2)


    # Проверка вывода данных после добавления
    received_data = db.get_general_data()
    tester.basic_test('Receive general added data', received_data, [test_data_1, test_data_2])  # Тут надо отредактировать ожидаемый результат, т.к. запрос лишь на общие данные
    

    # Проверка удаления данных


    # Проверка вывода данных после удаления


    # Закрываем связь с БД
    db.close()