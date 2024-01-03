import re

regular = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$'
email = 'stud12-751@vyatsu.ru'

def valid(email):
    return re.match(regular, email) is not None

if valid(email) is True:
    print("Правильная почта: "+ email)
else:
    print("Неправильная почта: "+ email)