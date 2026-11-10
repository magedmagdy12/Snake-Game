#snake class:
#method: create snake
#method: move snake

from turtle import Turtle


class Snake:
    def __init__(self): #لما بعمل اوبجيكت من الكلاس دا كاني بقول يا اوبجيكت او مثلا يا سام انزل اعمل اللي تحت
        self.turtles=[]# سيلف هنا راحت ل الاوبجيكت اللي هو ماي سنيك 
        self.positions=[(-20,0),(-40,0),(0,0),(20,0),(40,0),(60,0)]
        self.create_snake()
    
    def create_snake(self):
        
        for i in range(len(self.positions)): #for i in (self.positions):
            new_turtle=Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(self.positions[i])# طالما جوا الكلاس يبقى نحط سيلف انما لما كانت برا الكلاس كنا بنحطها من غير سيلف
            self.turtles.append(new_turtle)
    def move(self):
        for i in range(len(self.turtles)-1):
            self.turtles[i].goto(self.turtles[i+1].pos())
        self.turtles[-1].forward(20)
    def up(self):
        self.turtles[-1].setheading(90)# اتجاه للاتجاه اللي عايزينه
    def down(self):
        self.turtles[-1].setheading(270)
    def left(self):
        self.turtles[-1].setheading(180)
    def right(self):
        self.turtles[-1].setheading(0)
