import turtle
from Turkey import Turkey
from PIL import Image, ImageDraw


def set_background(filename):
    try:
        image = Image.open(filename)
    except FileNotFoundError:
        print("ERROR: Unable to find file " + filename)
        return

    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(filename)


def draw_lane_markers(num_turkeys):
    lane_maker = turtle.Turtle()
    lane_maker.hideturtle()
    lane_maker.shape(None)
    lane_maker.penup()
    lane_maker.speed(0)
    lane_maker.fillcolor('black')

    for i in range(num_turkeys):
        start_height = -(HEIGHT / 2)
        height = start_height + (i * (HEIGHT / num_turkeys))
        lane_maker.goto(-(WIDTH / 2), height)
        lane_maker.setheading(0)
        lane_maker.begin_fill()
        for k in range(2):
            lane_maker.forward(WIDTH)
            lane_maker.left(90)
            lane_maker.forward(10)
            lane_maker.left(90)
        lane_maker.end_fill()

# ===================== DO NOT EDIT THE CODE ABOVE ============================


if __name__ == '__main__':
    game_over = False
    WIDTH = 1150
    HEIGHT = 600

    # 1. Set the window variable to turtle.Screen()
    window = turtle.Screen()

    # 2. Call the window's setup() method with the WIDTH and HEIGHT variables
    window.setup(width=WIDTH, height=HEIGHT)
    # 3. Call the set_background() method with 'grass.png'
    set_background("grass.png")
    # 4. Run your code. You should see a window with an image of grass

    # 5. Set the Turkey.window variable to the window variable created in step 1
    # Turkey.window = window
    Turkey.window = window
    # 6. Create and set a variable to hold the number of Turkeys you want
    # in the race from 2 to 7
    numberOfTurkeys = 14
    # 5. Call the draw_lane_markers function and pass in the number of turkeys
    draw_lane_markers(numberOfTurkeys)
    # 6. Create and set a variable to hold the width of each lane
    # *HINT* the lane width is the HEIGHT of the window divided by the number of
    #        turkeys in the race
    laneWidth = HEIGHT/numberOfTurkeys
    # 7. Create a variable called start_x and set it to -(WIDTH / 2)
    start_x = -(WIDTH/2)
    # 8. Create a variable called start_y and set it to (HEIGHT / 2)
    start_y = (HEIGHT/2)
    # 9. Create your turkey competitors!
    # gobbler = Turkey(start_x, start_y - (1 * lane_width))
    # *HINT* the (1 * lane_width) part will be different for each turkey
    gobbler = Turkey(start_x, start_y, 'turkey.gif')
    gobbler2 = Turkey(start_x, start_y - laneWidth)
    gobbler3 = Turkey(start_x, start_y - (2 * laneWidth))
    gobbler4 = Turkey(start_x, start_y - (3 * laneWidth))
    gobbler5 = Turkey(start_x, start_y - (4 * laneWidth))
    gobbler6 = Turkey(start_x, start_y - (5 * laneWidth))
    gobbler7 = Turkey(start_x, start_y - (6 * laneWidth))
    gobbler8 = Turkey(start_x, start_y - (7 * laneWidth))
    gobbler9 = Turkey(start_x, start_y - (8 * laneWidth))
    gobbler10 = Turkey(start_x, start_y - (9 * laneWidth))
    gobbler11 = Turkey(start_x, start_y - (10 * laneWidth))
    gobbler12 = Turkey(start_x, start_y - (11 * laneWidth))
    gobbler13 = Turkey(start_x, start_y - (12 * laneWidth))
    gobbler14 = Turkey(start_x, start_y - (13 * laneWidth))

    while not game_over:

        # 10. Call the trot() method for each one of your turkeys!
        gobbler.trot()
        gobbler2.trot()
        gobbler3.trot()
        gobbler4.trot()
        gobbler5.trot()
        gobbler6.trot()
        gobbler7.trot()
        gobbler8.trot()
        gobbler9.trot()
        gobbler10.trot()
        gobbler11.trot()
        gobbler12.trot()
        gobbler13.trot()
        gobbler14.trot()

        # 11. For each turkey, use an 'if' statement and call your turkey's
        # check_finish() method
        # if gobbler.check_finish():
        if gobbler.check_finish() == True:
            gobbler.winner()
            game_over = True
            # 12. If the turkey finished, call that turkey's winner() method,
            # gobbler.winner()
        if gobbler2.check_finish() == True:
            gobbler2.winner()
            game_over = True
        if gobbler3.check_finish() == True:
            gobbler3.winner()
            game_over = True
        if gobbler4.check_finish() == True:
            gobbler4.winner()
            game_over = True
        if gobbler5.check_finish() == True:
            gobbler5.winner()
            game_over = True
        if gobbler6.check_finish() == True:
            gobbler6.winner()
            game_over = True
        if gobbler7.check_finish() == True:
            gobbler7.winner()
            game_over = True
            # 13. set the game_over variable to True


# ===================== DO NOT EDIT THE CODE BELOW ============================

    turtle.done()
