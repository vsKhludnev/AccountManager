from database.databaser import Databaser

if __name__ == '__main__':
    db = Databaser('database\Database_test.db')

    test_data_1 = ('Vk', 'login', 'password', '...')
    test_data_2 = ('Telegramm', 'this login', 'security password', 'other info')
    
    print(db.get_general_data())
    db.add_data(test_data_1)
    db.add_data(test_data_2)
    print(db.get_general_data())
    print(db.get_detail_data(1))
    print(db.get_detail_data(2))
    db.delete_data(5)
    db.delete_data(2)
    print(db.get_general_data())

    db.close()