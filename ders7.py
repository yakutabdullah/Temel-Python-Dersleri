__author__ = 'abdullahabdullah'

# --- Functions Exercises ---


#1. soru. verilen not 60 dan buyukse dersi gecti. degilse kaldi.

def sonuc(d_not):

    if d_not >=60:
        return 'Dersi gectin'

    else:
        return 'Dersten kaldin'


durum = sonuc(40)

print(durum)


# --- 2 ----

def gumruk(adi,soyadi,adres,sehir):

    print('LEfkosa Gumruk Mudurlugu'
          ''
          ''
          'Sayin {} {} satin aldiginiz urunler gumruge taabidir.'
          ''
          'gumruk mudurlugumuzden vergisini odeyerek urunlerinizi'
          'alabilirsiniz...'
          ''
          ''
          'Adres : {}'
''
          'Sehir : {}'.format(adi,soyadi,adres,sehir))

adi_g = input('Kisinin Adi:')
soyadi_g =input('Kisinin Soyadi :')
adres_g = input('adresi')
sehir_g = input('sehir')

gumruk(adi_g,soyadi_g,adres_g,sehir_g)













