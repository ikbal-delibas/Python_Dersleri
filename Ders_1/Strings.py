name="İkbal"
surname="Delibaş"
age=22
greeting='My name is ' + name + ' ' + surname + ' and\nI am ' + str(age)+ ' years old.'
print(greeting)
print(greeting[0]) # ilk karakterini veriyor
print(len(greeting)) # uzunluğunu verecek
print(greeting[0:5]) # 0. karakterden 5. karaktere kadar yazar
print(greeting[0:20:2]) # 0. karakterden 20. karaktere kadar 2 karakterden birini alır
###############
print('My name is {} {}'.format(name,surname))
print('My name is {0} {1}'.format(name,surname))
print('My name is {1} {0}'.format(name,surname))
print('My name is {n} {s}'.format(n=name,s=surname))
print(f'My name is {name} {surname}')