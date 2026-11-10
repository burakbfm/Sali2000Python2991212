import turtle

ekran = turtle.Screen()
ekran.title("Dijital Çizim Tahtası")

kalem = turtle.Turtle()
kalem.speed(0)
kalem.pensize(3)

# Görev 1: Fareyle çizim fonksiyonu oluştur.

# Görev 2: Renk değiştirme fonksiyonları ekle.
def kirmizi():
    kalem.pencolor("red")

# Görev 3: Ekranı temizleme özelliği ekle.

# Görev 4: Klavye olaylarını tanımla.
ekran.onkey(kirmizi, "r")

# bonus Görev: 1, 2 ve 3 tuşlarına basıldığında kalemin kalınlığını değiştiren özellik ekle.
ekran.mainloop()