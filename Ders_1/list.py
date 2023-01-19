from re import M


message="My name is İkbal Delibaş".split()
#mesajın her kelimesi bir karakter olarak algılanır ve listenin bir elemanı gibi gözükür
my_list=[1,2,3,4,5,6,7,8,9]

my_list_2=["bir",2,3,True]
toplam_list=my_list+my_list_2#listeleri birleştirdik

toplam_list_2=[my_list,my_list_2]#2 elemanlı listedir ama listenin elemanları da listedir
print(toplam_list_2)# çıktısı :[[1, 2, 3, 4, 5, 6, 7, 8, 9], ['bir', 2, 3, True]]

result=len(my_list)#listenin uzunluğunu verir

ilkdeger=my_list[0]
sondeger=my_list[-1]
elemanVarMı=9 in my_list#9 değeri my_list listesinde var ise true döndürür yoksa false döndürür
ilkUcEleman=my_list[0:3]#ilk üç eleman


