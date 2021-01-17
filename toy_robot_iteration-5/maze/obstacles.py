import robot
import random
import turtle
import sys

random_position = []

def draw():
    turtle.Screen()
    robot = turtle.Turtle()
    robot.pen(pencolor="red", pensize=1, speed=10)
    # make turtle to draw constraints
    robot.up()
    robot.goto(-110, -210)
    robot.down()

    for i in range(2):
        robot.fd(220)
        robot.lt(90)
        robot.fd(420)
        robot.lt(90)
    robot.up()

    # draw obstacles using turtle
    for i in random_position:
        x, y = i
        robot.goto(x, y)
        robot.down()
        robot.begin_fill()
        for j in range(4):
            robot.fillcolor("red")
            robot.fd(5)
            robot.lt(90)
        robot.end_fill()
        robot.up()
        robot.hideturtle()


def is_positon_blocked(x, y):
    for i in random_position:
        x2, y2 = i
        if (x, y) in [(x2 + i, y2) for i in range(5)]:
            return True
        elif (x, y) in [(x2 + 4, y2 + i) for i in range(5)]:
            return True
        elif (x, y) in [(x2 + 4 - i, y2 + 4) for i in range(5)]:
            return True
        elif (x, y) in [(x2, y2 + 4 - i) for i in range(5)]:
            return True
        else:
            continue
    return False


def is_path_blocked(x1, y1, x2, y2):
    global random_position
    final_x = x2
    final_y = y2
    if x1 > x2:
        x1, x2 = x2, x1
    elif y1 > y2:
        y1, y2 = y2, y1

    # print(random_position)
    for x, y in random_position:
        for i in range(x1, x2+1):
            if i == x and final_y == y or is_positon_blocked(i, final_y):
                return True
    for x, y in random_position:
        for i in range(y1, y2+1):
            if i == y and final_x == x or is_positon_blocked(final_x, i):
                return True
    return False


def get_obstacles():
    "returns a list randomly selscted obstacles positions"
    global random_position
    random_position = []
    number = random.randint(1, 10)
    for i in range(number):
        x = random.randint(-100, 100)
        y = random.randint(-200, 200)
        if y == 0 and x == 0:
            pass
        else:
            random_position.append((x, y))
    return random_position


get_obstacles()


draw() if len(sys.argv) > 1 and sys.argv[1] == 'turtle' else ''


if __name__ == "__main__":
    print(is_path_blocked(1, 3, 1, -4))
    print(is_positon_blocked(12, 17))
    print(get_obstacles())
    print(random_position)
    draw()
