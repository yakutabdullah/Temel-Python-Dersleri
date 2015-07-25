__author__ = 'abdullahabdullah'



# --- Dictionary ---

iletisim = {
    'Abdullah' : {

        'tel': '053900943',
        'email': 'yakut@gmail.com'
    },

     'yasin' : {

        'tel': '053954354',
        'email': 'yasin@gmail.com'
    }

}

for isimler in iletisim:

    print(iletisim[isimler]['tel'])
    print(iletisim[isimler]['email'])

# --- Exercises ---

"""
fonksiyon tanimliyalim. olusturdugumuz sozlugu foksiyonda ciktisini alalim
"""


muhendisler = {
    'Abdullah': 'Fotograf',
    'Yasin'  : 'Araba',
    'Ali'     : 'Yuzme'
}

def display(gelen):

  for kullanici in muhendisler:
      print('bunlarin hobileri :{}'.format(muhendisler[kullanici]))


display(muhendisler)






