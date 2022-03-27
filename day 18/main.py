# import colorgram;
# colors=colorgram.extract('hirst.jpg',30);
# new_colors=[];
# for color in colors:
#     r=color.rgb.r;
#     g=color.rgb.g;
#     b=color.rgb.b;
#     new_colors.append((r,g,b));
import turtle
from turtle import Turtle,Screen;
import random;
timmy=Turtle();
turtle.colormode(255);
extract_colors=[(247, 241, 232), (236, 242, 248), (239, 248, 244), (248, 239, 243), (142, 165, 191), (211, 156, 117), (24, 37, 56), (193, 142, 152), (147, 68, 59), (61, 102, 133), (231, 212, 109), (143, 177, 163), (137, 71, 78), (45, 35, 32), (46, 33, 37), (144, 30, 35), (66, 109, 96), (29, 51, 44), (132, 34, 29), (226, 169, 176), (232, 171, 163), (189, 98, 106), (195, 93, 79), (176, 188, 216), (21, 90, 68), (112, 122, 158), (35, 58, 102), (173, 203, 194), (22, 78, 99), (55, 150, 190)];
print(random.choice(extract_colors));
timmy.speed("fastest");
timmy.penup();
timmy.hideturtle();
timmy.setposition(-200, -200);
timmy.pendown()
for j in range(10):
    for i in range(10):
        timmy.dot(20,random.choice(extract_colors));
        timmy.penup();
        timmy.forward(50);
        timmy.pendown();
    timmy.penup();
    timmy.setposition(-200,-200);
    timmy.left(90);
    for _ in range(j+1):
        timmy.forward(50);
    timmy.pendown();
    timmy.right(90);



screen=Screen();
screen.exitonclick();
