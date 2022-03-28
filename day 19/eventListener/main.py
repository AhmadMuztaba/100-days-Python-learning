from turtle import Turtle,Screen;

timmy=Turtle();
def move_forward():
    timmy.forward(10);

def move_left():
    timmy.left(10);

def move_right():
    timmy.right(10);

def move_back():
    timmy.back(10)

def clear():
    timmy.clear()

screen=Screen();
screen.listen();
screen.onkey(move_forward,"w");
screen.onkey(move_back,"s");
screen.onkey(move_right,"d");
screen.onkey(move_left,"a");
screen.onkey(clear,"c");

screen.exitonclick();
