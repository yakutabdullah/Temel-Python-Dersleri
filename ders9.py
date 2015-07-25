__author__ = 'abdullahabdullah'

# ---list devam---

hayvanlar = ['at', 'tavsan', 'kuzu', 'kedi', 'fare', 'ayi', 'yilan', 'kaplumbaga']

other = ['insan' ,'erkek','kadin']

# --- Sorting List

d_hayvanlar = sorted(hayvanlar)
print(hayvanlar)
print(d_hayvanlar)

evren = hayvanlar + other
print(evren)

# --- Exercises ---

""" bos bir list olusturalim kullanidan listi doldurmasini istewyelim
kullanici entere bastigi zaman program bitsin. ve listi goruntulesin """

listemiz = []

bitti = False

while not bitti:

    giris = input('listeye item ekle :')

    if len(giris) ==0:
        bitti=True

    else:
        listemiz.append(giris)

print(listemiz)









