from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, 0)

    def up(self):
        new_y = self.ycor() + 25
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 25
        self.goto(self.xcor(), new_y)

    def goback(self, x):
        self.goto(x, 0)

    def line(self):
        line = Turtle(shape="square")
        line.speed(0)
        line.color("white")
        line.penup()
        line.pensize(5)
        line.goto(0, -290)
        for _ in range(0, 15):
            line.pendown()
            line.setheading(90)
            line.forward(20)
            line.penup()
            line.forward(20)
