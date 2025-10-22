import os
import shutil
from utils import clear, list_files_by_ext, check_file, chek_new_file, load_data, save_data
from hardcode import line_
import json

class file_json:
    def __init__(self):
        self.filename = None
        
        
    def display(self):
        clear()
        print("---Файлы формата json в текущей директории---")
        txt_files = list_files_by_ext(('.json',))
        if not txt_files:
            print("Файлы не найдены.")
        else:
            line_('\n'.join(txt_files))    
            
    def menu(self):
        while True:
            self.display()
            choice = str(input("действия с файлами:\n1 - Создать файл\n2 - Записать данные в файл\n3 - Просмотреть файл\n4 - Удалить файл\n5 - Перемесить файл\n6 - Скопировать файл\n7 - Переименовать файл\n8 - Обновить меню\n9 - Выход\n"))
            if choice == '1':
                self.display()
                self.filename = input("Введите имя файла: ")
                self.create_file()
            elif choice == '2':
                self.display()
                self.filename = input("Введите имя файла: ")
                self.write_to_file()
                input("Для продолжения нажмите Enter...")
            elif choice == '3':
                self.display()
                self.filename = input("Введите имя файла: ")
                self.read_file()
                input("Для продолжения нажмите Enter...")
            elif choice == '4':
                self.display()
                self.filename = input("Введите имя файла: ")
                self.delete_file()
            elif choice == '5':
                self.display()
                self.filename = input("Введите имя файла: ")
                new_name = input("Введите путь к целевой директории: ")
                self.move_file(new_name)
            elif choice == '6':
                self.display()
                self.filename = input("Введите имя файла: ")
                new_name = input("Введите путь к целевой директории: ")
                self.copy_file(new_name)
            elif choice == '7':
                self.display()
                self.filename = input("Введите имя файла: ")
                new_name = input("Введите новое имя файла: ")
                self.rename_file(new_name)
            elif choice == '8':
                self.menu()
            elif choice == '9':
                return
            
    def create_file(self):
        self.global_cheker_2()
        if self.filename == '': 
            return
        with open(self.filename, 'w') as file:
            file.write('')
    
    def write_to_file(self):
        self.global_cheker_1()
        if self.filename == '': 
            return
        data = {}
        while True:
            key = input("Введите ключ [Enter - выход]: ")
            if not key:
                break
            value = input("Введите значение: ")
            data[key] = value
            clear()
            print(f"Текущее состояние: {data}")
        save_data(self.filename, data)
       
        
    def read_file(self):
        self.global_cheker_1()
        if self.filename == '': 
            return
        data = load_data(self.filename)
        if data is None:
            print("Ошибка чтения файла")
            return
        print("Содержимое файла:")
        for key, value in data.items():
            print(f"{key}: {value}")

    def write_file(self, data):
        self.global_cheker_2()
        if self.filename == '': 
            return
        save_data(self.filename, data)
    
    def delete_file(self):
        self.global_cheker_1()
        if self.filename == '': 
            return
        try:
            os.remove(self.filename)
        except Exception as e:
            clear()
            print("Ошибка! Не удалось удалить файл, возможно, вы указали неверный путь\nПолная ошибка: ", e)
            input("Для продолжения нажмите Enter...")

    def copy_file(self, destination):
        self.global_cheker_1()
        try:
            shutil.copy(self.filename, destination)
        except Exception as e:
            clear()
            print("Ошибка! Не удалось скопировать файл, возможно, вы указали неверный путь\nПолная ошибка: ", e)
            input("Для продолжения нажмите Enter...")
            
    def move_file(self, destination):
        self.global_cheker_1()
        if self.filename == '': 
            return
        try:
            shutil.move(self.filename, destination)
        except Exception as e:
            clear()
            print("Ошибка! Не удалось переместить файл, возможно, вы указали неверный путь\nПолная ошибка: ", e)
            input("Для продолжения нажмите Enter...")

    def rename_file(self, new_name):
        self.global_cheker_1()
        if self.filename == '': 
            return
        new_name = chek_new_file(new_name, '.json')
        if new_name == '':
            return
        os.rename(self.filename, new_name)
        
        
    def global_cheker_1(self):
        self.filename = check_file(self.filename)
        if self.filename == '':
            self.menu()
    
    def global_cheker_2(self):
        self.filename = chek_new_file(self.filename, '.json')
        if self.filename == '':
            self.menu()
            
            