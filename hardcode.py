def line(disk,tom_name,file_system,total,used,free,percent):
    print(f'{"-"*50}\nдиск: {disk}\nНазвание метки: {tom_name}\nФайловая система: {file_system}\nРазмер диска: {total}\nЗанятое место: {used}\nСвободное место: {free}\nПроцент занятости: {percent}')

def line_(string):
    print(f'{"-"*50}\n{string}\n{"-"*50}')