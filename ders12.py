__author__ = 'abdullahabdullah'


# --- Tuples ---

gunler = ('p.tesi','sali','carsamba','persembe','cuma')
print(gunler)
"""
for gun in gunler:
    print(gun)

gunler[0] = 'yeni gun'



(ptesi,sal,car,per,cum) = gunler

print(ptesi)
print(sal)
"""


""" turkiyedeki havalimanlarin adlarini ve kodlarini list icinde tubles olsun.
ve bunu
listeleyelim """

havalimani = [('Anakara','ESB'),('malatya','MLX'),('istanbul','AHL')]

for (isim,kod) in havalimani:
    print('sehrin adi : {} ve kodu : {}'.format(isim,kod))















