__author__ = 'abdullahabdullah'

# -- Functions ---

"""
def fonk():
    print('Merhaba')


fonk()

def fonk2(name):
    print(name)


fonk2('Abdullah')

def fonk3(name):
    print('{}'.format(name))

fonk3('Yakut')


def fonk4(first,last):
    print('my name is {} and my sourname {}'.format(first,last))

fonk4('Abdullah','Yakut')

def fonk5(first,last):
    print('my name is {} and my sourname {}'.format(first,last))

fonk5(first ='Abdullah',last='Yakut')

"""


# fonksiyona  gonderecegimiz rakamin tek mi ciftmi
# ciktisini gosteren kod yazalim.


def tek_cift(rakam):

    if rakam %2 ==0:
        return 'Cift'

    if rakam %2 ==1:
        return 'Tek'

# sonuc = 'cift'
# sonuc = 'tek'

sonuc = tek_cift(8)

print(sonuc)








































