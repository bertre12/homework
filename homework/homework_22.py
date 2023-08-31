import sqlite3


"""
В вашей базе данных есть таблица "Books" со следующими столбцами: "id" (целое число, первичный ключ),
 "title" (текстовый тип), "author" (текстовый тип), "year" (целое число) и "price" (вещественный тип). 
 Вам необходимо выполнить следующие действия:
- вставьте несколько записей в таблицу "Books" с информацией о различных книгах, включая название, 
автора, год издания и цену.
- выберите все записи из таблицы "Books", отсортированные по году издания в порядке возрастания.
- выберите книги, у которых цена выше определенного значения.
- обновите цену книги с определенным ID.
- удалите книги, у которых год издания меньше определенного значения.
"""

# Создание таблицы.

with sqlite3.connect('books_data.db') as conn:
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                year INTEGER,
                price REAL
                )''')
    conn.commit()

# Заполнение таблицы и вывод через переменную.

cur.execute('''INSERT INTO Books (title, author, year, price) VALUES
                ('Война и мир', 'Толстой', 1869, 29.70),
                ('Идиот', 'Достоевский', 1868, 35.60),
                ('Евгений Онегин', 'Пушскин', 1833, 19.10),
                ('Мцыри', 'Лермонтов', 1840, 25.00)
                ''')
conn.commit()

print(f'---------- Начальная таблица. ----------')

cur.execute('''SELECT * FROM Books''')

formers = cur.fetchall()

for former in formers:
    print(*former)

# Сортировка таблицы по возрастанию и вывод результата через переменную.

print(f'---------- Таблица после сортировки данных. ----------')

cur.execute('''SELECT * FROM Books ORDER BY year''')

years = cur.fetchall()

for year in years:
    print(*year)

# Выбор значений из таблицы по заданному условию и вывод результата через переменную.

print(f'---------- Выборка значений из таблицы. ----------')

cur.execute('''SELECT title, price FROM Books WHERE price > 25.00''')

cost = cur.fetchall()

for price in cost:
    print(*price)

# Изменение данных в таблице по id и вывод изменённой таблицы через переменнную.

print(f'---------- Таблица после изменения данных. ----------')

cur.execute('''UPDATE Books SET price = 22.50 WHERE id = 3''')
conn.commit()

cur.execute('''SELECT * FROM Books''')

repls = cur.fetchall()

for repl in repls:
    print(*repl)

# Удаление данных из таблицы по заданному условию и вывод изменённой таблицы через переменнную.

print(f'---------- Таблица после удаления данных. ----------')

cur.execute('''DELETE FROM Books WHERE year < 1840''')
conn.commit()

cur.execute('''SELECT * FROM Books''')

totals = cur.fetchall()

for total in totals:
    print(*total)

# Закрытие соединения с базой данных.
cur.close()
