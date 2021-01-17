import turtle
from .. import obstacles

# get the turtle screen and customize my turtle pen
turtle.Screen()
robot = turtle.Turtle()
robot.pen(pencolor="red", pensize=1, speed=10)

# make turtle to draw constraints
robot.up()
robot.goto(-110, -210)
robot.down()

for i in range(2):
    robot.fd(210)
    robot.lt(90)
    robot.fd(410)
    robot.lt(90)
robot.up()

# draw obstacles using turtle
pos = obstacles.get_obstacles()
for i in pos:
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

robot.up()
robot.home()
robot.down()
robot.lt(90)
robot.up()
robot.fillcolor('black')


# variables tracking position and directionsubmission_002
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0
output_of_obstacles = False

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100


def help():
    """display all the commands to help you see which commands the robots allows"""
    return """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]
"""


def do_forward(robot_name, steps):
    """submission_002
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        robot.forward(steps)
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.' if output_of_obstacles is False else ''+robot_name +': Sorry, there is an obstacle in the way.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps):
        robot.bk(steps)
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.' if output_of_obstacles is False else ''+robot_name +': Sorry, there is an obstacle in the way.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0
    robot.rt(90)
    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3
    robot.lt(90)
    return True, ' > '+robot_name+' turned left.'


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y, output_of_obstacles
    new_x = position_x
    new_y = position_y
    output_of_obstacles = False

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if obstacles.is_path_blocked(position_x, position_y, new_x, new_y):
        output_of_obstacles = True
        return False

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def show_position(robot_name):
    """shows the position of the robot after it updates"""
    print(' > '+robot_name+' now at position (' +
          str(position_x)+','+str(position_y)+').')


def output(name, message):
    """output the result of the robot"""
    print('' + name + ": " + message)
