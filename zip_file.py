import os
import zipfile
from utils import clear, list_files_by_ext, check_file, chek_new_file, add_to_archive_, extract
from hardcode import line_

class file_zip:
    def __init__(self):
        self.filename = None

    def display(self):
        clear()
        print("---Архивы формата .zip в текущей директории---")
        zip_files = list_files_by_ext(('.zip',))
        if not zip_files:
            print("Архивы не найдены")
        else:
            line_('\n'.join(zip_files))

    def display_full(self):
        clear()
        print("Файлы в текущей директории:")
        zip_files = list_files_by_ext(('',))
        if not zip_files:
            print("файлы не найдены")
        else:
            line_('\n'.join(zip_files))
    
    def menu(self):
        while True:
            self.display()
            choice = input("Действия с архивами:\n1 - Создать архив\n2 - Добавить файл в архив\n3 - Разархивировать файл\n4 - Показать информацию об архиве\n5 - Уделить архив\n6 - Выход\n")
            if choice == '1':
                self.filename = input("Введите имя нового архива: ")
                self.create_archive()
            elif choice == '2':
                self.filename = input("Введите имя архива: ")
                self.add_to_archive()
            elif choice == '3':
                self.filename = input("Введите имя архива: ")
                self.extract_from_archive()
                input("\nДля продолжения нажмите Enter...")
            elif choice == '4':
                self.filename = input("Введите имя архива: ")
                self.get_archive_info()
                input("\nДля продолжения нажмите Enter...")
            elif choice == '5':
                self.filename = input("Введите имя архива: ")
                self.delete_archive()
            elif choice == '6':
                return
    '''            if choice in '2345':
                input("\nДля продолжения нажмите Enter...")'''

    def create_archive(self):
        self.filename = chek_new_file(self.filename, '.zip')
        if not self.filename:
            return
        with zipfile.ZipFile(self.filename, 'w') as zf:
            pass

    def add_to_archive(self):
        self.filename = check_file(self.filename)
        if not self.filename:
            return
        self.display_full()
        file_to_add = input("Введите имя файла, который нужно добавить в архив: ")
        file_to_add = check_file(file_to_add)
        if not file_to_add:
            return
        add_to_archive_(self.filename, file_to_add)

    def extract_from_archive(self):
        self.filename = check_file(self.filename)
        if not self.filename:
            return
        extract(self.filename)
        
    def get_archive_info(self):
        self.filename = check_file(self.filename)
        if not self.filename:
            return
        try:
            size = os.path.getsize(self.filename)
            print(f"Размер архива {self.filename}: {size} байт")
            with zipfile.ZipFile(self.filename, 'r') as zf:
                print("\nСодержимое архива:")
                zf.printdir()
        except Exception as e:
            print(f"Ошибка при получении информации: {e}")

    def delete_archive(self):
        self.filename = check_file(self.filename)
        if not self.filename:
            return
        try:
            os.remove(self.filename)
            print(f"Архив {self.filename} успешно удален")
        except Exception as e:
            print(f"Ошибка при удалении архива: {e}")
