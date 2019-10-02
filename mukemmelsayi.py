sayi = int(input("Sayi Girin: "))
# Önce kontrol etmek için kullanıcıdan bir sayı istiyoruz. Bunu sayi değişkenine integer olarak alıyoruz.
sonuc = 0
# Sonuc değişkenini daha sonra, kullanıcıdan aldığımız sayıyı bölen tüm sayıları toplamak için kullanacağız.
for i in range(1, sayi):
# Şimdi 1'den başlayarak verilen sayıya kadar olan sayıları sıralıyoruz.
    kalan = float(sayi % i)
# 1'den başlayarak her bir sayıyı verilen sayıya bölüp kalanı 0 olanları kalan değişkenine atıyoruz.
    if kalan == 0:
# Eğer kalan 0 ise yukarıda daha önce tanımladığımız sonuc değişkeni ile her defasında toplayarak, en sonunda tüm
# bölenlerin bu değişkende toplanmasını sağlayacağız.
        sonuc = sonuc + i

# Aşağıdaki kontrol satırlarında, ilk başta girilen sayı ile bölenlerin toplamının eşit olma durumunu kontrol ediyoruz.
if sonuc==sayi:
    print("Sayı Mükemmeldir.")
else:
    print("Sayi Mükemmel Değildir.")
