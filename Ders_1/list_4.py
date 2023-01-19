liste = ["Elma", "Armut", "Ayva"]

liste.sort() #listeyi küçükten büyüğe doğru sıraladık
print(liste)

liste.reverse() # listeyi büyükten küçüğe doğru sıraladık
print(liste)

def fonksiyon(n):
  return abs(n - 50) # sayıların mutlak değerini hesaplamak için kullanılır :abs 

sayi_listesi = [100, 50, 65, 82, 23]
sayi_listesi.sort(key=fonksiyon)#burada yaptığımız şey şudur: 
"""
Listenin elemanlarını fonksiyona gönderdik ve çıkan sonuçların küçükten büyüğe doğru sıralanmasını alarak dizinin elemanlarını ona göre sıraladık.
100 50 65 82 23 dizisi fonksiyondan sonra şöyle değerler alır
50  0  15 32 27 buradaki 27 abs fonksiyonundan dolayı pozitif işaretlidir. bunları küçükten büyüğe doğru sıraladığımızda
0   15 27 32 50 ve bunların dizideki karşılıklarını sıraya soktuğumuzda:
50 65  23 82 100 yani çıktı bu şekildedir
"""
print(sayi_listesi)