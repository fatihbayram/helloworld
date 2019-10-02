print("""***********************
Girilen 4 basamaklı sayının Armstrong Sayısı Kontrolünü Yapalım

**************************""")

sayi = input("Sayi Gir: ")

if len(sayi) == 4:
    a = int(sayi[0])
    b = int(sayi[1])
    c = int(sayi[2])
    d = int(sayi[3])
else:
    print("4 Basamaklı sayı giriniz.")

toplam = pow(a,4) + pow(b,4) + pow(c,4) + pow(d,4)
print("Girdiğiniz Sayıların Her Basamağının Dördüncü Kuvveti Toplamı= ",toplam)
if int(toplam) == int(sayi):
    print("Armstrong Sayısıdır.")
else:
    print("Armstrong Sayısı Değildir.")
