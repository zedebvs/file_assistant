import os
from utils import clear, list_files_by_ext, check_file, chek_new_file, read_xml, save_xml, display_xml_tree
from hardcode import line_
import xml.etree.ElementTree as ET




class file_xml():
    def __init__(self):
        self.filename = None
        
    def display(self):
        clear()
        print("---Файлы формата xml в текущей директории---")
        txt_files = list_files_by_ext(('.xml',))
        if not txt_files:
            print("Файлы не найдены.")
        else:
            line_('\n'.join(txt_files))       
        
    def create_file(self):
        self.global_cheker_2()
        if self.filename == '': 
            return
        with open(self.filename, 'w') as file:
            file.write('')
    
    def read_file(self):
        self.global_cheker_1()
        if self.filename == '': 
            return
            
        root = read_xml(self.filename)
        if root is None:
            print("Ошибка чтения файла")
            return
    
        print(f"Структура файла {self.filename}")
        display_xml_tree(root)
        print("-" * 50)

    def write_to_file(self):
        self.global_cheker_2() 
        if self.filename == '':
            return

        root_tag = input("Введите имя корневого тега (например, 'data'): ")
        root = ET.Element(root_tag)

        while True:
            clear()
            print("Добавление нового элемента (оставьте имя тега пустым для завершения).")
            elem_tag = input("Имя тега дочернего элемента: ")
            if not elem_tag:
                break
            
            elem_text = input(f"Текст для тега <{elem_tag}>: ")
            child = ET.SubElement(root, elem_tag)
            child.text = elem_text
            
            while True:
                attr_name = input("Имя атрибута (оставьте пустым, чтобы пропустить): ")
                if not attr_name:
                    break
                attr_value = input(f"Значение для атрибута '{attr_name}': ")
                child.set(attr_name, attr_value)

        tree = ET.ElementTree(root)
        save_xml(tree, self.filename)
    
    def menu(self):
        while True:
            self.display()
            choice = str(input("Действия с файлами:\n1 - Создать пустой файл\n2 - Записать данные в новый файл\n3 - Просмотреть файл\n4 - Удалить файл\n5 - Добавить данные в существующий файл\n6 - Выход\n"))
            if choice == '1':
                self.display()
                self.filename = input("Введите имя файла: ")
                self.create_file()
            elif choice == '2':
                self.display()
                self.filename = input("Введите имя нового файла: ")
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
                self.filename = input("Введите имя файла для изменения: ")
                self.add_data_to_file()
                input("Для продолжения нажмите Enter...")
            elif choice == '6':
                return
    
    def add_data_to_file(self):
        self.global_cheker_1()
        if self.filename == '':
            return

        try:
            tree = ET.parse(self.filename)
            root = tree.getroot()
        except (ET.ParseError, FileNotFoundError) as e:
            print(f"Ошибка! Не удалось прочитать файл: {e}")
            return

        print("Добавление нового элемента")
        elem_tag = input("Введите имя тега для нового элемента: ")
        if not elem_tag:
            print("Имя тега не может быть пустым.")
            return
        
        elem_text = input(f"Введите текст для тега <{elem_tag}>: ")
        
        new_element = ET.Element(elem_tag)
        new_element.text = elem_text

        while True:
            attr_name = input("Имя атрибута (оставьте пустым, чтобы закончить): ")
            if not attr_name:
                break
            attr_value = input(f"Значение для атрибута '{attr_name}': ")
            new_element.set(attr_name, attr_value)
            
        root.append(new_element)

        save_xml(tree, self.filename)

    def delete_file(self):
        self.global_cheker_1()
        try:
            os.remove(self.filename)
        except Exception as e:
            clear()
            print("Ошибка! Не удалось удалить файл, возможно, вы указали неверный путь\nПолная ошибка: ", e)
            input("Для продолжения нажмите Enter...")
            
    
    def global_cheker_1(self):
        self.filename = check_file(self.filename)
        if self.filename == '':
            self.menu()
    
    def global_cheker_2(self):
        self.filename = chek_new_file(self.filename, '.xml')
        if self.filename == '':
            self.menu()