#Değişkenleri tutarken tipini belirtmemize gerek yoktur.
#Belli bir maaştan belli bir KDV oranını çıkararak gerçek maaşı bulmayı deneyelim.
from importlib.abc import MetaPathFinder


maas=5000
print(maas)
kdvTutari=maas*0.27
maas=maas-kdvTutari
print(maas)
x=1 # int
y=2.5 # float
z="Metin" #string
a=True # bool


sayi1=10
sayi2=20

print(sayi1+sayi2) #30
metin1= "İkbal"
metin2=" DELİBAŞ"
print(metin1+metin2) # İkbal DELİBAŞ

b,c,d=1,2,3 # b=1 , c=2 , d=3 değerleri sırayla atanabilir
