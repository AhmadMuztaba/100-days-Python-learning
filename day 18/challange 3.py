from turtle import Turtle,Screen;
timm=Turtle();
timm.shape("turtle");
timm.color("red");

def shape(sides):
   degree=360/sides;
   for _ in range(sides):
      timm.right(degree);
      timm.forward(100);

color=['red','green','blue','yellow'];
for i in range(3,11):
   shape(i);
   timm.color(color[i % 4]);

screen=Screen();
screen.exitonclick();