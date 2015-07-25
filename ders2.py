__author__ = 'abdullahabdullah'

# --- Repeating String ---

print('python'*3)

ders = 'python'*6

print(ders)

# -- str() Function ---

yil = 2015
ay = 'Eylul'
gun = 23
# print(gun+ ' ' + ay) hatali
print(str(gun)+ ' ' + ay)

# --- Format String ---

print('aylardan {}'.format('Eylul'))

print('bu ay {0} yil {1}'.format('eylul','2015'))

ders = 'Python'
konu = 'Format'

print('Dersin adi {} konusu {}'.format(ders,konu))

# --- Input ---

ders = input('Dersin Adi :')
print(ders)
