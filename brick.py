from turtle import Turtle


class Brick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.resizemode(rmode='user')
        self.turtlesize(stretch_len= 8, stretch_wid = 4, outline=5)
        self.shapesize(stretch_len = 3.4, stretch_wid = 1.6, outline=5)
        self.penup()
        self.goto(position)
        
    def destroy(self):
        self.goto(1200, 1200)
        self.hideturtle()

    
        
    