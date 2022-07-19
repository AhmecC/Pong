from turtle import Turtle
import random
direction = random.choice([0,180])

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.goto(0,0)
        self.setheading(direction)

    def move(self):
        self.forward(25)

    def bounce_wall(self):
        if self.ycor() > 280 or self.ycor() < -280:
            head = self.heading()
            self.setheading(360 - head)


    def bounce_paddle(self):
        head = self.heading()
        print(head)
        X = random.choice([25, 30, 35,40])
        if head < 360 and head >= 270:
            if head == 270:
                self.setheading(head - 90 + X) #good logic
            else:
                if head - 90 - X <= 180:
                    self.setheading(head - 90)
                else:
                    self.setheading(head - 90 - X) #good logic

        if head <= 90 and head >= 0:
            if head == 90:
                self.setheading(head+90-X) #good logic
            elif head == 0:
                self.setheading(head+180-X)
            else:
                if head + 90 + X >= 180:
                    self.setheading(head + 90 + 0)
                else:
                    self.setheading(head+90+X) #good logic


        if head > 90 and head <= 180:
            if head == 180:
                self.setheading(head-180+X)
            else:
                if head - 90 - X <= 0:
                    self.setheading(head-90)
                else:
                    self.setheading(head-90-X)

        if head > 180 and head < 270:
            if head+90+X >= 360:
                self.setheading(head + 90 )
            else:
                self.setheading(head+90+X)


        self.forward(20)

    def rebound(self, position):
        list = []
        y = position[1] - 40
        for _ in range(0,5):
            list.append(y)
            y+=20
        if self.distance(380,list[2]) < 15: #RHS PLAYER
            self.bounce_paddle()
        elif self.distance(380,list[0]) < 15 or self.distance(380,list[1]) < 15:
            self.bounce_paddle()
        elif self.distance(380,list[3]) < 15 or self.distance(380,list[4]) < 15:
            self.bounce_paddle()

        if self.distance(-380,list[2]) < 15: #RHS PLAYER
            self.bounce_paddle()
        elif self.distance(-380,list[0]) < 15 or self.distance(-380,list[1]) < 15:
            self.bounce_paddle()
        elif self.distance(-380,list[3]) < 15 or self.distance(-380,list[4]) < 15:
            self.bounce_paddle()

    def scorer(self):
        if self.xcor() > 390: #Left Player Gets Point
            self.ht()
            return 1
        if self.xcor() < -390: #RIGHT Player Gets Point
            self.ht()
            return 2


