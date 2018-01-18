import time, math
from graphics import *

CENTER = [320, 240]

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x + CENTER[0]
        self.y = y + CENTER[1]

asd = [-123]

win = GraphWin('Kello', 640, 480)
lines = [[[0, 250], [0, 275]],
         [[125, 216.5063509], [137.5, 238.156986]],
         [[216.5063509, 125], [238.156986, 137.5]],
         [[250, 0], [275, 0]],
         [[216,5063509, -125], [238.156986, -137.5]],
         [[125, -216.5063509], [137.5, -238.156986]],
         [[0, -250], [0, -275]],
         [[-125, -216.5063509], [-137.5, -238.156986]],
         [[-216.5063509, -125], [-238.156986, -137.5]],
         [[-250, 0], [-275, 0]],
         [[-216.5063509, 125], [-238.156986, 137.5]],
         [[-125, 216.5063509], [-137.5, 238.156986]],
         [[0, 250], [0, 275]]]
for i in lines:
    p1 = i[0]
    p2 = i[1]
    a = Line(Point(i[0][0] + CENTER[0], i[0][1] + CENTER[1]), Point(i[1][0] + CENTER[0], i[1][1] + CENTER[1]))
    a.draw(win)

while(True):
    print(time.localtime())
    hours = time.localtime().tm_hour
    minutes = time.localtime().tm_min
    seconds = time.localtime().tm_sec


    minutes = 30

    #hours = 20
     # Convert the hours to the 12-hour scale so that they can be divided for the clock face.
    print(hours)
    #minutes = 40
    seconds_hand_angle = -6 * seconds
    minutes_hand_angle = -6 * minutes
    hours_hand_angle = hours * 30 - minutes_hand_angle // 30 #360 / 12
    #hours_hand_angle = 360 - hours_hand_angle
    angles = [str(hours_hand_angle), str(minutes_hand_angle), str(seconds_hand_angle)]
    print('\n'.join(angles))

    hours_hand_length = 300
    minutes_hand_length = 200
    seconds_hand_length = 225

    hours_x_coordinate = math.sin(math.radians(hours_hand_angle)) * hours_hand_length
    hours_y_coordinate = -math.cos(math.radians(hours_hand_angle)) * hours_hand_length
    hours_coordinates = Coordinate(hours_x_coordinate, hours_y_coordinate)

    minutes_x_coordinate = -math.sin(math.radians(minutes_hand_angle)) * minutes_hand_length
    minutes_y_coordinate = -math.cos(math.radians(minutes_hand_angle)) * minutes_hand_length
    minutes_coordinates = Coordinate(minutes_x_coordinate, minutes_y_coordinate)

    seconds_x_coordinate = -math.sin(math.radians(seconds_hand_angle)) * seconds_hand_length
    seconds_y_coordinate = -math.cos(math.radians(seconds_hand_angle)) * seconds_hand_length
    seconds_coordinates = Coordinate(seconds_x_coordinate, seconds_y_coordinate)
    try:
        seconds_hand.undraw()
        minutes_hand.undraw()
        hours_hand.undraw()
    except NameError:
        print('moi')
    seconds_hand = Line(Point(CENTER[0], CENTER[1]), Point(seconds_coordinates.x, seconds_coordinates.y))
    minutes_hand = Line(Point(CENTER[0], CENTER[1]), Point(minutes_coordinates.x, minutes_coordinates.y))
    hours_hand = Line(Point(CENTER[0], CENTER[1]), Point(hours_coordinates.x, hours_coordinates.y))
    seconds_hand.setWidth(3)
    minutes_hand.setWidth(3)
    hours_hand.setWidth(3)
    seconds_hand.draw(win)
    minutes_hand.draw(win)
    hours_hand.draw(win)
    time.sleep(1)
