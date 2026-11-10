# 1 -DEĞİLİ YÖNTEM

dongu1 = 0

while dongu1 != 10:
    print("Burak")
    dongu1 += 1 # dongu1 = dongu1 + 1

# 2 - SAYAÇ YÖNETİMİ

dongu2 = 0

while dongu2 <= 10:
    print("Kerem")
    dongu2 += 1 #

# 3 - For

for i in range(5,10): # FOR i değişkenine belirlenen aralğıa kadaar 0 dan başlayarak değer atar ve kodunu o şekilde çalıştırır.
    print("Kodlama!", i)

# FOR TEKRAR SAYISINI BİLDİĞİMİZ GÖREVLERDE KULLANILIR. WHİLE İSE TEKRAR SAYISINDAN EMİN OLMADIĞIMIZ GÖREVLERDE KULLANILIR.

puanlar = [10,50,100,50,100,50,100,50,100,50,100,50,100,50,100,50,100,50,100,50,100,50,100,50,100,50,100]
print(len(puanlar))
for x in puanlar:
    print("Puanım:", x)