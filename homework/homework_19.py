import sqlite3

# sqlite3.connect('data.db') as conn - создание базы данных.
# cur = conn.cursor() - создание переменной для взаимодействия с базой данных.
# cur.execute - создание таблицы базы данных.
# conn.commit() - сохранение.

"""
Задача 1
Создайте таблицу "Книги" со следующими полями:
id (целое число, первичный ключ)
название (строка)
автор (строка)
жанр (строка)
год издания (целое число)
"""

with sqlite3.connect('data.db') as conn:
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Книги (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                 'название' TEXT,
                 'автор' TEXT,
                 'жанр' TEXT,
                 'год издания' INTEGER
                 )''')
    conn.commit()

"""
Задача 2
Создайте таблицу "Задачи" со следующими полями:
id (целое число, первичный ключ)
название (строка)
описание (строка)
дата начала (дата)
дата окончания (дата)
статус (строка)
"""

with sqlite3.connect('data.db') as conn:
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Задачи (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                 'название' TEXT,
                 'описание' TEXT,
                 'дата начала' DATE,
                 'дата окончания' DATE,
                 'статус' TEXT
                 )''')
    conn.commit()

"""Задача 3
Создайте таблицу "Фильмы" со следующими полями:
id (целое число, первичный ключ)
название (строка)
режиссер (строка)
год выпуска (целое число)
рейтинг (десятичное число)
длительность (целое число)
"""

with sqlite3.connect('data.db') as conn:
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Фильмы (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                 'название' TEXT,
                 'режиссёр' TEXT,
                 'год выпуска' INTEGER,
                 'рейтинг' FLOAT,
                 'длительность' INTEGER
                 )''')
    conn.commit()
