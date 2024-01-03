import re

regular = r'^\d{6}$'
p_code = '123456'

def valid(p_code):
    return re.match(regular, p_code) is not None

if valid(p_code) is True:
    print("Правильный почтовый индекс: "+ p_code)
else:
    print("Неправильный почтовый индекс: "+ p_code)