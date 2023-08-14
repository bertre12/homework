from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

"""Создать программу для создания заметок, где пользователь может вводить текст и сохранять его в файле.
Программа должна иметь возможность открывать сохраненные заметки и редактировать их.
"""


# Подключение модуля и диалогового окна.

def open_file():
    """Открывает файл для редактирования"""
    # Создание переменной, и открытие диалогового окна.
    file_path = askopenfilename(
        filetypes=[('Текстовые файлы', '*.txt'), ('Все файлы', '*.*')]
    )
    if not file_path:
        return
    # Удаление текста.
    text_edit.delete('1.0', END)
    # Открытие файла для редактирования.
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        # Добавление текста с конца файла.
        text_edit.insert(END, text)


def save_file():
    """Сохраняем текущий файл как новый файл."""
    # Создание переменной, и открытие диалогового окна, сохранение файла по умолчанию, шаблоны файлов.
    file_path = asksaveasfilename(
        defaultextension="txt",
        filetypes=[('Текстовые файлы', '*.txt'), ('Все файлы', '*.*')],
    )
    # Проверка есть ли такой файл, и создание его.
    if not file_path:
        return
    with open(file_path, 'w', encoding='utf-8') as file:
        text = text_edit.get('1.0', END)
        file.write(text)


# Создание окна программы.
window = Tk()

# Переименования окна.
window.title('Заметки')

# Установка размеров окна и положение от левого края.
window.geometry('400x500+200+100')

# Запрет на изменение открытого окна.
window.resizable(False, False)

# Создание переменной текстового поля, цвет, перенос слов.
text_edit = Text(bg='#eeefea', wrap='word')

# Заполнение текстового поля в окне программы, отступ.
text_edit.pack(fill=BOTH, expand=1)

# Создание кнопок, цвет, привязка к выполнению команды.
button_open = Button(text='Открыть', bg='#b6b9a3', command=open_file)
button_save = Button(text='Сохранить', bg='#b6b9a3', command=save_file)

# Расположение кнопок внизу и заполнение всего пространства.
button_open.pack(anchor=S, fill=X)
button_save.pack(anchor=S, fill=X)

# Запуск приложения.
window.mainloop()
