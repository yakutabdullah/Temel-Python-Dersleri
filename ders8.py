__author__ = 'abdullahabdullah'


# --- List ---

hayvanlar = ['kopek','kedi','fare']
#print(hayvanlar[0])
# degistirme
hayvanlar[0] = 'tavsan'
#print(hayvanlar[0])

#index ekleme .append()

hayvanlar.append('Ayi')
#print(hayvanlar)


# birlestirme .extend()
hayvanlar.extend(['yilan','kaplumbaga'])

#print(hayvanlar)

# ekleme insert()

hayvanlar.insert(0,'at')
hayvanlar.insert(2,'kuzu')

print(hayvanlar)
print(hayvanlar[2:4])


# indexi bul.
"""
indexbul = hayvanlar.index('Ayi')
print(indexbul) """

try:
    indexbul = hayvanlar.index('sinek')
except:
    indexbul = 'boyle bir hayvan yok'

print(indexbul)


for hayvan in hayvanlar:

    print(hayvan.upper())

index =0

while index < len(hayvanlar):
    print(hayvanlar[index])

    index +=1
















