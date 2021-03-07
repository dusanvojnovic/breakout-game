from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-450, 350)
        self.write(f"Score: {self.score}", align = "left", font = ("Courier", 20, "normal"))


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = "center", font = ("Courier", 40, "bold"))

    def win_game(self):
        self.goto(0, 0)
        self.write("YOU WIN, CONGRATULATIONS!", align = "center", font = ("Courier", 40, "bold"))