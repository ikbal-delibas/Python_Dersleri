a = [1, 6]
print(a)
a.append(5) #a listesinin son elemanı olarak eleman ekledi
print(a)

a.pop() # a nın son elemanını listeden sildi
print(a)

a.append(5)
print(a)
a.remove(1) # a nın 1 olan elemanını sildik
print(a)

a.insert(1, 100) # a nın 1. elemanı 100 olacak şekilde eleman ekledik. buna göre diğer elemanların sırası kaydı
print(a)

print(a.pop())
print(a)

a.clear() #bütün listenin içini sildik
print(a)