print("kodlama.io sitesine hoşgeldiniz.")


#string: harflerle ifade edilen veri türüdür. sayıları string olarak kaydedersek 
#işlemler sırasında hata alırız. çünkü string değerler toplanmaz 
#örn. "13"+13=1313 şeklinde çıktı verecektir veya hata verecektir.
sayi = 13
sayi1 = 13
print(sayi1+sayi)
#integer: genelde rakamlar,sayılar için kullanılır. 
#float: ondalık sayılarda kullanılır.
#boolean: true ve false değerlerini döndüren karşılaştırma değerleridir.

#giriş ekranını şart bloğu gibi tanımlayabiliriz.
isim="deneme"
sifre="deneme"

isim1=input("kullanıcı adı giriniz: ")
sifre1=input("şifre giriniz: ")
if isim==isim1 and sifre==sifre1:
    print("giriş başarılı.")
else:
    print("hatalı bilgi girişi tekrar deneyiniz.")

#pythonda ders adları string değerlere sahiptir.
#dersteki ilerleme ise integer değere sahiptir.
#dersteki ilerlemeyi de şart bloğu gibi düşünebiliriz.
derssayisi=20
bitirilenderssayisi=15
yuzde="75%"
print("ders ilerlemeniz="+yuzde)