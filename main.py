import psutil
from hardcode import line, line_
from utils import clear, list_files_by_ext
from txt_file import file_txt
from json_files import file_json
from xml_file import file_xml
from zip_file import file_zip

txt_ = file_txt()
json_ = file_json()
xml_ = file_xml()
zip_ = file_zip()

 
def get_disk_info():
    info = psutil.disk_partitions()
    for i in info:
        spase = psutil.disk_usage(i.mountpoint)
        disk = i.device
        tom_name = i.mountpoint
        file_system = i.fstype
        total = str(spase.total/(1024**3))[:6] + ' ГБ'
        used = str(spase.used/(1024**3))[:6] + ' ГБ'
        free = str(spase.free/(1024**3))[:6] + ' ГБ'
        percent = spase.percent
        line(disk, tom_name, file_system, total, used, free, percent)
    print("-"*50)



while True:
    clear()
    choice = str(input("1 - Информация о дисках\n2 - Работа с текстовыми файлами\n3 - Работа с json-файлами\n4 - Работа с xml-файлами\n5 - Работа с zip-архивами\n6 - Выход\n"))
    if choice == '1':
        clear()
        get_disk_info()
        input("Для продолжения нажмите Enter...")
    elif choice == '2':
        txt_.menu()
    elif choice == '3':
        json_.menu()
    elif choice == '4':
        xml_.menu()
    elif choice == '5':
        zip_.menu()
    elif choice == '6':
        break