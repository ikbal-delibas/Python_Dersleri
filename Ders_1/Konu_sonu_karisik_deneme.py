"""
1 - Klavyeden girilen 5 tane sayıyı bir listeye atarak
    bunların karelerinden 20 çıkarıldığında ortaya çıkan sonuca
    göre küçükten büyüğe göre sıralayan
    ve listeyi buna göre yazdıran programı yazınız.
"""
liste = []
for i in range(0, 5):
    liste.append(eval(input()))# 5 komut girilmesi ve listeye atanması sağlandı


def siralama_fonksiyonu(a):
    return a * a - 20 #liste elemanları 20 den çıkarılıyor


liste.sort(key=siralama_fonksiyonu)
print(liste)