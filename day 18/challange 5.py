from turtle import Turtle,Screen;
import random;


timm=Turtle();

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    timm.color(R, G, B)

timm.speed("fastest")
for _ in range(180):
    change_color();
    timm.circle(100);
    timm.left(2);


screen=Screen();
screen.exitonclick();