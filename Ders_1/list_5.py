sayi_listesi = [3, 5, 10, -8, 9, 15]
a = sayi_listesi
print(a) #sayi_listesinin a ya kopyalanması sonucu çıktı sayi_listesindeki gibidir

sayi_listesi.sort() #liste küçükten büyüğe doğru sıralanır
print(a) # a da aynı şekilde sıralanacağından aynı işlem olur

# yani yukarıda sayi_listesi ne yapılan her işlem a için de geçerli olmaktadır

##############################
sayi_listesi = [3, 5, 10, -8, 9, 15]
a = sayi_listesi.copy()
print(a)

sayi_listesi.sort()
print(a)
"""
son yapılan işlemlerde sayi_listesi ne yapılan herhangi bir işlem a listesini etkilemez
"""