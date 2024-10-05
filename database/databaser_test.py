def unit_test(test_name, expect, actual):
    if expect == actual:
        print(f'\033[32m{test_name}: PASS\033[0m')
    else:
        print(f'\033[31m{test_name}: FAIL\033[0m')
        print(f'expect: {expect}')
        print(f'actual: {actual}')

from database.databaser import Databaser

if __name__ == '__main__':
    db = Databaser('database\Database_test.db')

    test_data_1 = ('Vk', 'login', 'password', '...')
    test_data_2 = ('Telegramm', 'this login', 'security password', 'other info')

    # Проверка вывода из пустой БД
    received_data = db.get_general_data()
    unit_test('Receive general data from emty database', received_data, [])

    receive_detail_data = db.get_detail_data(1)
    unit_test('Receive detail data by id from empty database', receive_detail_data, [])


    # Проверка добавления данных


    # Проверка вывода данных после добавления


    # Проверка удаления данных


    # Проверка вывода данных после удаления