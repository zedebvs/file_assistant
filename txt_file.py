import os
import shutil
from utils import clear, list_files_by_ext, chek_end, check_file, chek_new_file
from hardcode import line_


class file_txt:
    def __init__(self):
        self.filename = None

    def create_file(self):
        self.global_cheker_2()
        if self.filename == '': 
            return
        with open(self.filename, 'w') as file:
            file.write('')

    def write_to_file(self, text):
        self.global_cheker_1()
        if self.filename == '': 
            return
        with open(self.filename, 'a') as file:
            file.write(text + '\n')
    
    def write_to_file_full(self, text):
        self.global_cheker_1()
        if self.filename == '': 
            return
        with open(self.filename, 'w') as file:
            file.write(text + '\n')

    def view_file_contents(self):
        self.global_cheker_1()
        if self.filename == '': 
            return
        with open(self.filename, 'r') as file:
            return file.read()

    def ifase(self):
        clear()
        print("---Текстовые файлы в текущей директории---")
        txt_files = list_files_by_ext(('.txt',))
        if not txt_files:
            print("Файлы не найдены.")
        else:
            line_('\n'.join(txt_files))
        
    
    def menu(self):
        while True:
            self.ifase()
            choice = str(input('Действие с файлами:\n1 - Создать файл\n2 - Удалить файл\n3 - Скопировать файл\n4 - Переместить файл\n5 - Переименовать файл\n6 - Добавление записи в файл\n7 - Перезапись файла\n8 - Просмотреть файл\n9 - Обновить меню\n10 - Выход\n'))
            if choice == '1':
                self.ifase()
                self.filename = input("Введите имя файла: ")
                self.create_file()
            elif choice == '2':
                self.ifase()
                self.filename = input("Введите имя файла: ")
                self.delete_file()
            elif choice == '3':
                self.ifase()
                self.filename = input("Введите имя файла: ")
                destination = input("Введите имя целевой директории: ")
                self.copy_file(destination)
            elif choice == '4':
                self.ifase()
                self.filename = input("Введите имя файла: ")
                destination = input("Введите имя целевой директории: ")
                self.move_file(destination)
            elif choice == '5':
                self.ifase()
                self.filename = input("Введите имя файла: ")
                new_name = input("Введите новое имя файла: ")
                self.rename_file(new_name)
            elif choice == '6':
                self.ifase()
                self.filename = input("Введите имя файла: ")
                text = input("Введите текст для записи в файл: ")
                self.write_to_file(text)
            elif choice == '7':
                self.ifase()
                self.filename = input("Введите имя файла: ")
                text = input("Введите текст для записи в файл: ")
                self.write_to_file_full(text)
            elif choice == '8':
                self.ifase()
                self.filename = input("Введите имя файла: ")
                print(f'Содержимое файла {self.filename}:\n{self.view_file_contents()}')
                input("Для продолжения нажмите Enter...")
            elif choice == '9':
                continue
            elif choice == '10':
                return
            
    def delete_file(self):
        self.global_cheker_1()
        if self.filename == '': 
            return
        try:
            os.remove(self.filename)
        except Exception as e:
            clear()
            print("Ошибка! Не удалось удалить файл, возможно вы указали неверный путь\nПолная ошибка: ", e)
            input("Для продолжения нажмите Enter...")

    def copy_file(self, destination):
        self.global_cheker_1()
        if self.filename == '': 
            return
        try:
            shutil.copy(self.filename, destination)
        except Exception as e:
            clear()
            print("Ошибка! Не удалось скопировать файл, возможно вы указали неверный путь\nПолная ошибка: ", e)
            input("Для продолжения нажмите Enter...")
            
    def move_file(self, destination):
        self.global_cheker_1()
        if self.filename == '': 
            return
        try:
            shutil.move(self.filename, destination)
        except Exception as e:
            clear()
            print("Ошибка! Не удалось переместить файл, возможно вы указали неверный путь\nПолная ошибка: ", e)
            input("Для продолжения нажмите Enter...")

    def rename_file(self, new_name):
        self.global_cheker_1()
        if self.filename == '': 
            return
        new_name = chek_new_file(new_name, '.txt')
        if new_name == '':
            return
        os.rename(self.filename, new_name)
        
    def global_cheker_1(self):
        self.filename = check_file(self.filename)
        if self.filename == '':
            self.menu()
    
    def global_cheker_2(self):
        self.filename = chek_new_file(self.filename, '.txt')
        if self.filename == '':
            self.menu()