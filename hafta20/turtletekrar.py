import turtle # turtle modülünü kodlamak için kendi dosyamıza ekliyoruz.

ekran = turtle.Screen()
kalem = turtle.Turtle()

def haraket_et(x, y):
    kalem.goto(x, y)

ekran.onscreenclick(haraket_et)

ekran.mainloop() # ekranda çizimi sabit tutar exitonclick gibi