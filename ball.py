from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid = 0.8, stretch_len = 0.8)
        self.x_move = 10
        self.y_move = 10
        self.goto(0, -360)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_from_side_wall(self):
        self.x_move *= -1
    
    def bounce(self):
        self.y_move *= -1

