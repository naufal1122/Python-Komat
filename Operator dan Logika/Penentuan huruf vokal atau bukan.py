#Penentuan huruf vokal atau bukan
print('Penentuan huruf vokal atau bukan')
print('--------------------------------')
karakter=input('Karakter = ')
hurufvokal = (karakter=='A','I','U','E','O','a','i','u','e','o')
keterangan='Ini adalah huruf vokal' if karakter in hurufvokal else 'Bukan huruf vokal bro'
print(karakter, keterangan)