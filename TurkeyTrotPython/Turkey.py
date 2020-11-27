import turtle
import random
from PIL import Image


class Turkey:
    window = None
    image_width = 150
    image_height = 109

    imageNum = 1

    def __init__(self, x, y, filename='turkey.gif'):
        self.x = x;
        self.y = y - (Turkey.image_height / 4)
        self.size = 100;
        self.minSpeed = 10;
        self.maxSpeed = 20;
        self.image = Image.open(filename)

#        Turkey.imageNum % 8 => 0, 1, 2, 3, ...7

        if Turkey.imageNum % 7 == 0:
            filename = "cranberrySauce.gif"
        elif Turkey.imageNum % 7 == 1:
            filename = "dinnerRolls.gif"
        elif Turkey.imageNum % 7 == 2:
            filename = "gravy.gif"
        elif Turkey.imageNum % 7 == 3:
            filename = "greenBeanCasserole.gif"
        elif Turkey.imageNum % 7 == 4:
            filename = "mashedPotatoes.gif"
        elif Turkey.imageNum % 7 == 5:
            filename = "stuffing.gif"
        elif Turkey.imageNum % 7 == 6:
            filename = "turkey.gif"
        Turkey.imageNum = Turkey.imageNum + 1

        if Turkey.window is not None:
            print(filename)
            Turkey.window.addshape(filename)

        self.turtleObject = turtle.Turtle()
        self.turtleObject.hideturtle()
        self.turtleObject.shape(filename)
        self.turtleObject.penup()
        self.turtleObject.speed(0)
        self.turtleObject.goto(self.x, self.y)
        self.turtleObject.showturtle()

    def check_finish(self):
        return self.x > (Turkey.window.window_width() / 2)

    def trot(self):
        self.x += random.randint(self.minSpeed, self.maxSpeed)
        self.turtleObject.goto(self.x, self.y)

    def winner(self):
        self.turtleObject.hideturtle()
        self.turtleObject.backward(450)
        self.turtleObject.showturtle()
        self.turtleObject.write(arg="Winner!!!", move=True, align='left', font=('Arial', 24, 'normal'))
        print( "Winner" )
