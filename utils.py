import os
import json
import xml.etree.ElementTree as ET
import zipfile


def clear():
    os.system('cls || clear')

def list_files_by_ext(extensions):
    return [f for f in os.listdir('.') if os.path.isfile(f) and f.lower().endswith(extensions)]   

def check_file(filename):
    while True:
        clear()
        if os.path.isfile(filename):
            return filename
        print("Ошибка! Файл не найден")
        filename = input("Введите имя файла [enter - Выход]: ")
        if filename == '':
            return filename
        
def chek_end(filename, end):
    while True:
        clear()
        if filename.lower().endswith(end):
            return filename
        print(f"Ошибка! Введите файл с расширением {end}")
        filename = input("Введите имя файла [enter - Выход]: ")
        if filename == '':
            return filename

def chek_new_file(filename, end):
    while True:
        clear()
        if filename.lower().endswith(end) and not os.path.isfile(filename):
            return filename
        print(f"Ошибка! Возможно файл с таким именем уже существует или вы забыли указать расширение файла {end}")
        filename = input("Введите имя файла [enter - Выход]: ")
        if filename == '':
            return filename

def load_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Ошибка чтения или парсинга файла {file_path}\nПолная ошибка: {e}")
        return None

def save_data(file_path, data):
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Ошибка записи в файл {file_path}\nПолная ошибка: {e}")
        
def read_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except ET.ParseError as e:
        print(f"Ошибка чтения файла {file_path}\nПолная ошибка: {e}")
        return None

def save_xml(tree, file_path):
    try:
        ET.indent(tree.getroot()) 
        tree.write(file_path, encoding='utf-8', xml_declaration=True)
        print(f"Файл {file_path} успешно сохранен.")
    except IOError as e:
        print(f"Ошибка записи в файл {file_path}\nПолная ошибка: {e}")

def display_xml_tree(element, level=0):

    indent = "  " * level
    attrs = f" (атрибуты: {element.attrib})" if element.attrib else ""
    print(f"{indent}Тег: {element.tag}{attrs}")

    if element.text and element.text.strip():
        print(f"{indent}  Текст: {element.text.strip()}")

    for child in element:
        display_xml_tree(child, level + 1)

def add_to_archive_(file_path, file_to_add):
    try:
        with zipfile.ZipFile(file_path, 'a', compression=zipfile.ZIP_DEFLATED) as zf: 
            zf.write(file_to_add, arcname=os.path.basename(file_to_add))
            print(f"Файл {file_to_add} добавлен в архив {file_path}")
    except Exception as e:
        print(f"Ошибка при добавлении файла в архив: {e}")

def extract(file_path):
    try:
        with zipfile.ZipFile(file_path, 'r') as zf:
            print("Файлы в архиве:")
            zf.printdir()
            file_to_extract = input("\nВведите имя файла для извлечения [Enter - выход]: ")
            if not file_to_extract:
                return
            extract_path = input("Куда извлечь [Enter - текущая директория]: ")
            zf.extract(file_to_extract, path=extract_path or None)
            print(f"Файл {file_to_extract} успешно извлечен.")
            
            full_path = os.path.join(extract_path, file_to_extract)
            if os.path.exists(full_path):
                file_size = os.path.getsize(full_path)
                print(f"Размер извлеченного файла {full_path}: {file_size} байт")
    except KeyError:
        print(f"Ошибка: файла с именем {file_to_extract} нет в архиве")
    except Exception as e:
        print(f"Ошибка при извлечении: {e}")
