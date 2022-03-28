import random
from turtle import Turtle,Screen;

screen=Screen();
screen.listen();
isRaceOn=False;
screen.setup(width=500,height=400);
bet=screen.textinput(title="Make your bet",prompt="Who will win the race?");
colors=["blue","red","yellow","green","pink","black"];
turtles=[];
yAxis=90;
for color in colors:
    turtleName=color;
    turtleName=Turtle('turtle');
    turtleName.penup();
    turtleName.goto(x=-230,y=yAxis);
    turtleName.color(color);
    turtles.append(turtleName);
    yAxis-=30
if bet:
    isRaceOn=True;

while isRaceOn:
    for racingTurtle in turtles:
        if racingTurtle.xcor()>220:
            isRaceOn = False;
            if racingTurtle.pencolor()==bet:
                print("You have Won The Bet");
            else:
                print(f"You have lost the bet .The winner is {racingTurtle.pencolor()}")


        distance=random.randint(0,10);
        racingTurtle.forward(distance);
        # print(racingTurtle.position())






screen.exitonclick();

