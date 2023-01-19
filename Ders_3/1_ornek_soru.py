"""
kendisine gönderilen sayılardan sadece palindrom
olanları toplayan
diğerlerini de bu toplamdan çıkaran ve geri
döndüren python fonksiyonunu yazınız.
palindrom sayı: tersten okunuşu kendisine eşit olan sayı demektir. 1221,1223221,44,555...
"""


def polinDROM(*drom):
    toplam = 0
    for sayi in drom:
        if str(sayi) == str(sayi)[::-1]: #sayıyı string hale çevirip tersinin kendisine eşit olup olmadığına bakıyoruz
            toplam += sayi
        else:
            toplam -= sayi
    return toplam


print(polinDROM(10, 101, 55, 40, 9009))