import play # dosyama kütüphaneyi ekliyorum

play.set_backdrop("white")

karakter = play.new_circle(color="red",
                           x=0,
                           y=0,
                           radius=85,
                           border_color="black",
                           border_width=5)

hedef = play.new_box(color="green",
                     x=250,
                     y=200,
                     width=60,
                     height=60)

@play.when_key_pressed("d","a")
def haraket(tus):
    if tus == "d":
        karakter.x += 5

    elif tus == "a":
        karakter.x -= 5

play.start_program()

# play.new_box oluşturun değişkeni hedef olsun | hedef = play.new_box()