import turtle
from turtle import Turtle,Screen;
import random;


timm=Turtle();

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    timm.color(R, G, B)

timm.pensize(15);
for _ in range(100):
    change_color();
    timm.speed("fastest");
    timm.right(random.randint(0,360));
    distance=random.randint(1,100);
    timm.forward(distance);
screen=Screen();
screen.exitonclick();