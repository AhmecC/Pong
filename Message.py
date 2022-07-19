from turtle import Turtle

class Message(Turtle):
    def __init__(self):
        super().__init__()

    def repeat(self):
        self.penup()
        self.color("white")
        self.ht()

    def intro(self):
        self.repeat()
        self.goto(0,0)
        self.write(f"WELCOME TO PONG", True, align="center", font=("Calibri", 40, "normal"))


    def score(self,score,X):
        self.repeat()
        self.clear()
        self.goto(X, 240)
        self.write(f"{score}", True, align="center", font=("Calibri", 40, "normal"))

    def player_name(self,x,r):
        self.repeat()
        self.goto(x,270)
        self.write(f"Player {r}", True, align="center", font=("Calibri", 20, "normal"))


    def winner(self,x,r):
        self.repeat()
        self.clear()
        self.goto(x,-30)
        self.write(f"Player {r} WINS!", True, align="center", font=("Calibri", 30, "normal"))

    def clean(self):
        self.clear()