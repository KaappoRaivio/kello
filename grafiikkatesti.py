from graphics import *

def main():
    win = GraphWin('testi', 200, 150)
    suora = Line(Point(20, 30), Point(40, 20))
    suora.setWidth(3)
    suora.draw(win)
    win.getMouse()
    win.quit()
if __name__ == '__main__':
    main()
