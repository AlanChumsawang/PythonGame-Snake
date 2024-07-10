import turtle
from turtle import Turtle,Screen
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-5, 250)
        self.color('white')
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f'Score:{self.score} ', False, align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0,0)
        self.write('Game Over', False, align=ALIGNMENT, font=FONT)
    def add_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()



