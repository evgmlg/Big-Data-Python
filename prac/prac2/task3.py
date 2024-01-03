import re

regular = r'^[a-zA-Z]+\.(png|jpg|jpeg|gif)$'
file = 'picutre.exe'

def valid(file):
    return re.match(regular, file) is not None

if valid(file) is True:
    print("Правильный формат файла: "+ file)
else:
    print("Неправильный формат файла: "+ file)