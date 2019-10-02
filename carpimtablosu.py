print("""*********

Çarpım Tablosu

***********""")

a = 1

for x in range(1,11):
    for i in range(1,11):
        birler = a * i
        print(a,"*",i,"=",birler)
    a += 1
