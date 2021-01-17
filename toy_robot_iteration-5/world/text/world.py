
import import_helper
import sys


# obstacles = import_helper.dynamic_import('maze.obstacles')
if len(sys.argv) == 1 or len(sys.argv) == 2 and sys.argv[1] == 'text':
    obstacles = import_helper.dynamic_import('maze.obstacles')
elif len(sys.argv) == 3 and sys.argv[1] == 'text':
    obstacles = import_helper.dynamic_import('maze.'+sys.argv[2])
elif 'turtle' in sys.argv:
    pass
else:
    obstacles = import_helper.dynamic_import('maze.obstacles')


# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0
output_of_obstacles = False

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100


def help():
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
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.' if output_of_obstacles is False else ''+robot_name + ': Sorry, there is an obstacle in the way.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.' if output_of_obstacles is False else ''+robot_name + ': Sorry, there is an obstacle in the way.'


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


def obstacles_positions(robot_name):
    """display the list of obstacles if there's any"""
    obstacles.get_obstacles()
    obstacles_list = obstacles.random_position

    if len(obstacles_list) == 0:
        pass
    else:

        if len(sys.argv) == 2 and sys.argv[1] == 'text' or len(sys.argv) == 1:
            print(f"{robot_name}: Loaded obstacles.")
        elif len(sys.argv) == 3 and sys.argv[1] == 'text':
            print(f'{robot_name}: Loaded {sys.argv[2]}')
        else:
            print(f"{robot_name}: Loaded obstacles.")

        print("There are some obstacles:")
        for i in obstacles_list:
            x, y = i
            print("- At position "+str(x)+","+str(y) +
                  " (to "+str(x+4)+","+str(y+4)+")")
