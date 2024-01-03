from collections import Counter
from bs4 import BeautifulSoup as bs
import codecs

doc = bs(codecs.open('sad.html', encoding='utf-8', mode='r').read(), 'html.parser')

#Извлечение цен из списка
lot = []
for node in doc.select('div.list-item'):
    price = node.select('div.item-price span')[0].decode_contents().strip()
    lot.append(price)
lot_int = [int(float(x)) for x in lot]
print("Min price: ", min(lot_int))
print("Max price: ", max(lot_int))

avg_price = sum(lot_int) / len(lot_int)
print("AVG price: ",avg_price)

otz = bs(codecs.open('dromOTZ.html', encoding='utf-8', mode='r').read(), 'html.parser')
otz_lot = []
for k in otz.find_all('a', class_= 'username offline popupctrl'):
    names = k.select('strong')[0].decode_contents().strip()
    otz_lot.append(names)
#print(otz_lot)
c = Counter(otz_lot).most_common(1)
print("Most active: ",c[0][0], " with ", c[0][1], " comments\n")


unique = set(otz_lot)
print("All names in page:\n", otz_lot,'\n')
print("Names quantity before : ", len(otz_lot), "\n")
print("Unique name:\n", unique,'\n')
print("Names quantity after : ", len(unique))