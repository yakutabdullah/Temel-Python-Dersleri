__author__ = 'abdullahabdullah'


# ---  Boleans ---

t_boleans = True
f_boleans = False

print(t_boleans)
print(f_boleans)

# --- Comparators ---
"""
== Esit
> Buyuk
>= Buyuk veya esit
< kucuk
<= kucuk veya esit
!= esit degil
"""

# --- IF ELSE ELIF ---

people = 20

if people >20:
    print('20 den buyuk')

elif people <20:
    print('20 den kucuk')

else:
    print('diger durum')


"""
ucagin anlik hizini kullanicidan al.
girilen hiz 200 den kucuk  ise  bu ucak pistte
200 den buyukse bu ucak havada
3 den kucukse hizi bu ucak hangarda
"""

hizi_string = input('Lutfen hizi giriniz :')
hizi_int = int(hizi_string)

if hizi_int >200:

    print('ucak havada')

elif hizi_int <= 200:
    print('bu ucak pisste')

elif hizi_int <3:
    print('ucak hangarda')








































