__author__ = 'abdullahabdullah'

# --- Dictionaries ---


adres = {'Abdullah': 'yenisehir','Feride':'Uskudar'}
print(adres)

adresi = adres['Abdullah']
print(adresi)
print('Adresi : {}'.format(adresi))
#degisiklik
adres['Abdullah'] = 'Kadikoy'

print(adres)
# ekleme
adres['Ali'] = 'Uskudar'
print(adres)

# silme

del adres['Ali']
print(adres)

#print(adres['Abdullah'])

if 'Abdullah' in adres:
    print(adres['Abdullah'])

print('beyoglu' in adres.values())

for liste in  adres:

    print('Kisi adi : {} ve adresi {}'.format(liste,adres[liste]))

    # adres['Abdullah'] = Kadikoy
    # liste = Abdullah

