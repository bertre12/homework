import sqlite3


"""
Задание 1
Необходимо выполнить операцию вставки данных в несколько таблиц базы данных и убедиться, что эти операции 
выполняются все или ни одна. Используйте транзакцию, чтобы обеспечить атомарность операций. 
Если хотя бы одна из операций не выполнится успешно, все изменения должны быть отменены.
"""

with sqlite3.connect('data_1.db') as conn:
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS table_1 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 start_date DATE,
                 status TEXT
                 )''')
    conn.commit()

with sqlite3.connect('data_1.db') as conn:
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS table_2 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 start_date DATE,
                 status TEXT
                 )''')
    conn.commit()

with sqlite3.connect('data_1.db') as conn:
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS table_3 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 start_date DATE,
                 status TEXT
                 )''')
    conn.commit()

try:
    # Начало транзакции.
    conn.execute('BEGIN TRANSACTION')

    # Вставка данных в таблицу 1, 2, 3.
    cur.execute("INSERT INTO table_1 (name, start_date, status) VALUES (?, ?, ?)", ('value_1', 'value_2', 'value_3'))
    cur.execute("INSERT INTO table_2 (name, start_date, status) VALUES (?, ?, ?)", ('value_4', 'value_5', 'value_6'))
    cur.execute("INSERT INTO table_3 (name, start_date, status) VALUES (?, ?, ?)", ('value_7', 'value_8', 'value_9'))

    # Подтверждение транзакции.
    cur.execute('COMMIT')
    print('Операция выполнены успешно.')

except:
    # Откат транзакции в случае ошибки.
    cur.execute('ROLLBACK')
    print('Операция не выполнялась.')

finally:
    # Закрытие соединения с базой данных.
    cur.close()

"""
Задание 2
Вам предоставлена база данных со множеством записей. Необходимо оптимизировать производительность запроса, 
который выполняет поиск записей по определенному столбцу. Создайте подходящий индекс для этого столбца, 
чтобы ускорить выполнение запроса и снизить нагрузку на базу данных.
"""

with sqlite3.connect('data_2.db') as conn:
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS table_1 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                column_1 INTEGER,
                column_2 INTEGER,
                column_3 INTEGER,
                column_4 INTEGER
                 )''')
    conn.commit()

# Создание индекса.
cur.execute('''CREATE INDEX index_name ON table_1 (column_2)''')

# Использование индекса в запросе.
cur.execute('''SELECT * FROM table WHERE column_2 = ?''', ('value',))

# Закрытие соединения с базой данных.
cur.close()

"""
Задание 3
Необходимо выполнить операцию обновления данных в нескольких связанных таблицах базы данных. 
Также нужно убедиться, что данные остаются целостными и в случае сбоя можно выполнить откат изменений. 
Используйте транзакцию для группировки операций обновления и создайте необходимые индексы для улучшения 
производительности запросов.
"""

with sqlite3.connect('data_3.db') as conn:
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS table_1 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                column_1 INTEGER,
                column_2 INTEGER
                 )''')
    conn.commit()

with sqlite3.connect('data_3.db') as conn:
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS table_2 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                column_1 INTEGER,
                column_2 INTEGER
                 )''')
    conn.commit()

try:
    # Начало транзакции.
    cur.execute('BEGIN TRANSACTION')

    # Выполнение операций обновления данных.
    cur.execute('''UPDATE table_1 SET column_1 = 'new_value' WHERE condition''')
    cur.execute('''UPDATE table_2 SET column_2 = 'new_value' WHERE condition''')

    # Подтверждение транзакции.
    cur.execute('COMMIT')

except:
    # Откат транзакции в случае ошибки.
    cur.execute('ROLLBACK')

# Создание индекса на таблицу table1

cur.execute('''CREATE INDEX index_name ON table_1 (column_1)''')

# Закрытие соединения с базой данных.
cur.close()
