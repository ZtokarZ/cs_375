from graphics import*


def main():
    win = GraphWin("Face Drawing", 1000, 1000)
    win.setCoords(0,50,50,0)
    win.setBackground(color_rgb(32,111,215))

    draw_sun(win)
    draw_rectangle(win)
    draw_mast(win)
    draw_stick(win)
    draw_left(win)
    draw_right(win)

    input("Press any key to quit")


def draw_sun(win):
    sun = Circle (Point(4,4),2)
    sun.setFill(color_rgb(255,230,0))
    sun.setOutline('black')
    sun.draw(win)


def draw_rectangle(win):
    rectangle = Rectangle(Point(22,26), Point (26,28))
    rectangle.setFill('brown')
    rectangle.setOutline('black')
    rectangle.draw(win)


def draw_mast(win):
    mast = Polygon (Point(24,18),Point(26,24),Point(22,24))
    mast.setFill('white')
    mast.setOutline('black')
    mast.draw(win)


def draw_right(win):
    right = Polygon (Point(28,26),Point(26,26),Point(26,28))
    right.setFill ('brown')
    right.setOutline ('black')
    right.draw(win)


def draw_left(win):
    left = Polygon (Point(22,26), Point(20,26),Point(22,28))
    left.setFill('brown')
    left.setOutline('black')
    left.draw(win)


def draw_stick(win):
    stick = Polygon (Point(24,18),Point(24,26))
    stick.setFill('black')
    stick.setOutline('black')
    stick.draw(win)

main()
