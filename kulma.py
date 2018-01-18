import time, math
from graphics import *

CENTER = [320, 240]

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x + CENTER[0]
        self.y = y + CENTER[1]


win = GraphWin('Kello', 640, 480)


while(True):
    print(time.localtime())
    hours = time.localtime().tm_hour
    hours = 5
    minutes = time.localtime().tm_min
    seconds = time.localtime().tm_sec
    hours %= 12 # Convert the hours to the 12-hour scale so that they can be divided for the clock face.
    seconds_hand_angle = 6 * seconds
    minutes_hand_angle = 6 * minutes
    hours_hand_angle = hours * 30 + minutes_hand_angle / 12
    angles = [str(hours_hand_angle), str(minutes_hand_angle), str(seconds_hand_angle)]
    #print('\n'.join(angles))

    hours_hand_length = 100
    minutes_hand_length = 200
    seconds_hand_length = 225

    hours_x_coordinate = math.sin(math.radians(hours_hand_angle)) * hours_hand_length
    hours_y_coordinate = math.cos(math.radians(hours_hand_angle)) * hours_hand_length
    hours_coordinates = Coordinate(hours_x_coordinate, hours_y_coordinate)
    hours_hand = Line(Point(CENTER[0], CENTER[1]), Point(hours_coordinates.x, -hours_coordinates.y))
    hours_hand.setWidth(3)
    hours_hand.draw(win)
    minutes_x_coordinate = math.sin(math.radians(minutes_hand_angle)) * minutes_hand_length
    minutes_y_coordinate = math.cos(math.radians(minutes_hand_angle)) * minutes_hand_length
    minutes_coordinates = Coordinate(minutes_x_coordinate, minutes_y_coordinate)

    seconds_x_coordinate = math.sin(math.radians(seconds_hand_angle)) * seconds_hand_length
    seconds_y_coordinate = math.cos(math.radians(seconds_hand_angle)) * seconds_hand_length
    seconds_coordinates = Coordinate(seconds_x_coordinate, seconds_y_coordinate)
    time.sleep(1)
