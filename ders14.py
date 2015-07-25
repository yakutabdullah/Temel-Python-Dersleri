__author__ = 'abdullahabdullah'


# --- Exercises ---

""" birinci.txt dosyayi oku. alfabatik siraya gore duzenle
2. dosyaya at...."""

birincidosya = 'C:/birinci.txt'
ikincidosya = 'C:/Users/abdullahabdullah/Desktop/ikinci.txt'

evren = []

with open(birincidosya) as birincikelime:

    for kelime in birincikelime :
        evren.append(kelime)

#print(evren)

evren.sort()

with open(ikincidosya,'w') as duzenlenmis:

    for kelimeler in evren:

        duzenlenmis.write(kelimeler)






