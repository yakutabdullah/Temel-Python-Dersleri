__author__ = 'abdullahabdullah'


# --- Exercises ---


"""
serverin saatlik ucreti $0.10

1. bu serverin gunluk ucreti nekadardir ?

2. bu serverin aylik ucreti nekadardir ?

3. bu serverin yillik ucreti nekadardir ?

"""
server_saatlik = 0.10
server_gunluk = server_saatlik * 24
server_aylik =  server_gunluk * 30
server_yillik =  server_aylik *12

print('server saatlik ucreti : {:.2f}'.format(server_saatlik))
print('server gunluk ucreti : {:.2f}'.format(server_gunluk))
print('server aylik ucreti : {:.2f}'.format(server_aylik))
print('server yillik ucreti : {:.2f}'.format(server_yillik))


""" saatlik $0.10
20 tane server kiraliyoruz. ve butcemiz $3500
1. 20 serverin gunluk ucreti nedir
2. 20 serveri kac gun kiralayabiliriz. """

butce = 3500

server_20_saatlik = server_saatlik *20
server_20_gunluk =  server_20_saatlik * 24

gun_sayisi = butce / server_20_gunluk

print('20 server saatlik ucreti : {:.2f}'.format(server_20_saatlik))
print('20 server gunluk ucreti : {:.2f}'.format(server_20_gunluk))
print('kiralanabilir gun sayisi : {:.0f}'.format(gun_sayisi))































