import turtle as tom
import random


kame = tom.Turtle()
tom.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
kame.width(10)
kame.speed("fast")

for _ in range(200):
    kame.color(random_color())
    kame.forward(40)
    kame.setheading(random.choice(directions))
    kame.heading()


