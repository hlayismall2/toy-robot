import sys
import random
import itertools


import world.text.world


module_to_use = False
mazerun_mode = False
counter = 0


if len(sys.argv) > 1 and sys.argv[1] == "turtle":
    import world.turtle.world
    print('fucken shit')
    module_to_use = True
    mode = 'turtle'
    counter = 0


# list of valid command names
valid_commands = ['off', 'help', 'replay',
                  'forward', 'back', 'right', 'left', 'sprint', "mazerun"]
move_commands = valid_commands[3:]


# commands history
history = []


def get_robot_name():
    """Asks the user for the robot name."""

    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """

    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    while len(command) == 0 or not valid_command(command):
        world.text.world.output(
            robot_name, "Sorry, I did not understand '"+command+"'.") if module_to_use is False else world.turtle.world.output(
            robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)

    return command.lower()


def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''


def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """

    (command_name, arg1) = split_command_input(command)

    if command_name.lower() == 'replay':
        if len(arg1.strip()) == 0:
            return True
        elif (arg1.lower().find('silent') > -1 or arg1.lower().find('reversed') > -1) and len(arg1.lower().replace('silent', '').replace('reversed', '').strip()) == 0:
            return True
        else:
            range_args = arg1.replace('silent', '').replace('reversed', '')
            if is_int(range_args):
                return True
            else:
                range_args = range_args.split('-')
                return is_int(range_args[0]) and is_int(range_args[1]) and len(range_args) == 2
    elif command_name.lower() == "mazerun":
        if arg1.lower() == "top" or arg1 == "" or arg1.lower() == "bottom" or arg1.lower() == "left" or arg1 == "right":
            return True
    else:
        return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1))


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, world.text.world.help() if module_to_use is False else world.turtle.world.help()


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return world.text.world.do_forward(robot_name, 1) if module_to_use == False else world.turtle.world.do_forward(robot_name, 1)
    else:
        (do_next, command_output) = world.text.world.do_forward(robot_name,
                                                                steps) if module_to_use is False else world.turtle.world.do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


# mazerun
def left():
    '''
    Mazerun fuction 
    : checks the left side if it is available it returns True else False
    '''

    global counter

    x = world.text.world.position_x if module_to_use is False else world.turtle.world.position_x
    y = world.text.world.position_y if module_to_use is False else world.turtle.world.position_y

    if (world.text.world.obstacles.is_path_blocked(x, y, x, y-20) is False and world.text.world.obstacles.is_path_blocked(x, y, x+20, y) is False and world.text.world.obstacles.is_path_blocked(x, y, x, y+20) is False and world.text.world.obstacles.is_path_blocked(x, y, x, y-20) is False if module_to_use is False else world.turtle.world.obstacles.is_path_blocked(x, y, x-20, y) is False and world.turtle.world.obstacles.is_path_blocked(x, y, x+20, y) is False and world.turtle.world.obstacles.is_path_blocked(x, y, x, y+20) is False and world.turtle.world.obstacles.is_path_blocked(x, y, x, y-20) is False):
        if (world.text.world.obstacles.is_path_blocked(x, y, x, y-20) is False if module_to_use is False else world.turtle.world.obstacles.is_path_blocked(x, y, x, y-20) is False):
            return False

    if counter == 0:
        if (world.text.world.obstacles.is_path_blocked(x, y, x-20, y) if module_to_use is False else world.turtle.world.obstacles.is_path_blocked(x, y, x-20, y)) or ((world.text.world.is_position_allowed(x-20, y) is False) if module_to_use is False else (world.turtle.world.is_position_allowed(x-20, y) is False)):
            return False

    if counter == 3:
        if (world.text.world.obstacles.is_path_blocked(x, y, x, y+20) if module_to_use is False else world.turtle.world.obstacles.is_path_blocked(x, y, x, y+20)) or ((world.text.world.is_position_allowed(x, y+20) is False) if module_to_use is False else (world.turtle.world.is_position_allowed(x, y+20) is False)):
            return False

    if counter == 2:
        if (world.text.world.obstacles.is_path_blocked(x, y, x+20, y) if module_to_use is False else world.turtle.world.obstacles.is_path_blocked(x, y, x+20, y)) or ((world.text.world.is_position_allowed(x+20, y) is False) if module_to_use is False else (world.turtle.world.is_position_allowed(x+20, y) is False)):
            return False

    if counter == 1:
        if (world.text.world.obstacles.is_path_blocked(x, y, x, y-20) if module_to_use is False else world.turtle.world.obstacles.is_path_blocked(x, y, x, y-20)) or ((world.text.world.is_position_allowed(x, y-20) is False) if module_to_use is False else (world.turtle.world.is_position_allowed(x, y-20) is False)):
            return False
    return True


def forward():
    '''
    Mazerun function
    : checks the forward path if it is available
    : return: True if path is available else False 
    '''

    global counter

    x = world.text.world.position_x if module_to_use is False else world.turtle.world.position_x
    y = world.text.world.position_y if module_to_use is False else world.turtle.world.position_y

    if counter == 0:
        if (world.text.world.obstacles.is_path_blocked(x, y, x, y+20) if module_to_use is False else world.turtle.world.obstacles.is_path_blocked(x, y, x, y+20)) or ((world.text.world.is_position_allowed(x, y+20) is False) if module_to_use is False else (world.turtle.world.is_position_allowed(x, y+20) is False)):
            return False

    if counter == 1:
        if (world.text.world.obstacles.is_path_blocked(x, y, x-20, y) if module_to_use is False else world.turtle.world.obstacles.is_path_blocked(x, y, x-20, y)) or (world.text.world.is_position_allowed(x-20, y) is False if module_to_use is False else world.turtle.world.is_position_allowed(x-20, y) is False):
            return False

    if counter == 2:
        if (world.text.world.obstacles.is_path_blocked(x, y, x, y-20) if module_to_use is False else world.turtle.world.obstacles.is_path_blocked(x, y, x, y-20)) or (world.text.world.is_position_allowed(x, y-20) is False if module_to_use is False else world.turtle.world.is_position_allowed(x, y-20) is False):
            return False

    if counter == 3:
        if (world.text.world.obstacles.is_path_blocked(x, y, x+20, y) if module_to_use is False else world.turtle.world.obstacles.is_path_blocked(x, y, x+20, y)) or (world.text.world.is_position_allowed(x+20, y) is False if module_to_use is False else world.turtle.world.is_position_allowed(x+20, y) is False):
            return False
    return True


def maze_runner(robot, arg):
    '''
    solve the maze on a specified edge command
    : consist of all four edges.
    '''
    global mazerun_mode
    mazerun_mode = True

    if arg == '':
        arg = 'top'

    print(f' > {robot} starting maze run..')

    if arg.lower().strip() == "top" or arg.lower().strip() == "":
        # solve the maze to the top edge.
        for x in itertools.repeat(1):
            if (world.text.world.position_y == 200 if module_to_use is False else world.turtle.world.position_y == 200):
                break
            if left():
                handle_command(robot, "left")
            if forward():
                handle_command(robot, "forward 20")
            else:
                handle_command(robot, "right")

    if arg.lower().strip() == "bottom":
        return bottom_edge(robot, arg)

    if arg.lower().strip() == "right":
        handle_command(robot, "right")
        return right_edge(robot, arg)

    if arg.lower().strip() == "left":
        handle_command(robot, "left")
        return left_edge(robot, arg)

    mazerun_mode = False
    return True, " > " + robot+" I am at the "+arg+" edge."


def bottom_edge(robot, arg):
    '''
    solve the maze to the bottom edge.
    '''

    for x in itertools.repeat(1):
        if (world.text.world.position_y == -200 if module_to_use is False else world.turtle.world.position_y == -200):
            return True, " > " + robot+" I am at the "+arg+" edge."
        if left():
            handle_command(robot, "left")
        if forward():
            handle_command(robot, "forward 20")
        else:
            handle_command(robot, "right")
    return


def right_edge(robot, arg):
    '''
    solve the maze to the right edge.
    '''

    for x in itertools.repeat(1):
        if (world.text.world.position_x == 100 if module_to_use is False else world.turtle.world.position_x == 100):
            return True, " > " + robot+" I am at the "+arg+" edge."
        if left():
            handle_command(robot, "left")
        if forward():
            handle_command(robot, "forward 20")
        else:
            handle_command(robot, "right")
    return


def left_edge(robot, arg):
    '''
    solve the maze to the left edge.
    '''

    for x in itertools.repeat(1):
        if (world.text.world.position_x == -100 if module_to_use is False else world.turtle.world.position_x == -100):
            return True, " > " + robot+" I am at the "+arg+" edge."
        if left():
            handle_command(robot, "left")
        if forward():
            handle_command(robot, "forward 20")
        else:
            handle_command(robot, "right")
    return

# end of mazerun


def get_commands_history(reverse, relativeStart, relativeEnd):
    """
    Retrieve the commands from history list, already breaking them up into (command_name, arguments) tuples
    :param reverse: if True, then reverse the list
    :param relativeStart: the start index relative to the end position of command, e.g. -5 means from index len(commands)-5; None means from beginning
    :param relativeEnd: the start index relative to the end position of command, e.g. -1 means from index len(commands)-1; None means to the end
    :return: return list of (command_name, arguments) tuples
    """

    commands_to_replay = [(name, args) for (name, args) in list(map(
        lambda command: split_command_input(command), history)) if name in move_commands]
    if reverse:
        commands_to_replay.reverse()

    range_start = len(commands_to_replay) + relativeStart if (
        relativeStart is not None and (len(commands_to_replay) + relativeStart) >= 0) else 0
    range_end = len(commands_to_replay) + relativeEnd if (relativeEnd is not None and (len(
        commands_to_replay) + relativeEnd) >= 0 and relativeEnd > relativeStart) else len(commands_to_replay)
    return commands_to_replay[range_start:range_end]


def do_replay(robot_name, arguments):
    """
    Replays historic commands
    :param robot_name:
    :param arguments a string containing arguments for the replay command
    :return: True, output string
    """

    silent = arguments.lower().find('silent') > -1
    reverse = arguments.lower().find('reversed') > -1
    range_args = arguments.lower().replace('silent', '').replace('reversed', '')

    range_start = None
    range_end = None

    if len(range_args.strip()) > 0:
        if is_int(range_args):
            range_start = -int(range_args)
        else:
            range_args = range_args.split('-')
            range_start = -int(range_args[0])
            range_end = -int(range_args[1])

    commands_to_replay = get_commands_history(reverse, range_start, range_end)

    for (command_name, command_arg) in commands_to_replay:
        (do_next, command_output) = call_command(
            command_name, command_arg, robot_name)
        if not silent:
            print(command_output)
            world.text.world.show_position(
                robot_name) if module_to_use is False else world.turtle.world.show_position(robot_name)

    return True, ' > '+robot_name+' replayed ' + str(len(commands_to_replay)) + ' commands' + (' in reverse' if reverse else '') + (' silently.' if silent else '.')


def call_command(command_name, command_arg, robot_name):
    ''' calls the command if it is valid'''

    global counter

    if command_name == 'help':
        return do_help()
    elif command_name == 'forward':
        return world.text.world.do_forward(robot_name, int(command_arg)) if module_to_use is False else world.turtle.world.do_forward(robot_name, int(command_arg))
    elif command_name == 'back':
        return world.text.world.do_back(robot_name, int(command_arg)) if module_to_use is False else world.turtle.world.do_back(robot_name, int(command_arg))
    elif command_name == 'right':
        if counter == 0:
            counter = 3
        else:
            counter -= 1
        return world.text.world.do_right_turn(robot_name) if module_to_use is False else world.turtle.world.do_right_turn(robot_name)
    elif command_name == 'left':
        counter += 1
        if counter == 4:
            counter = 0
        return world.text.world.do_left_turn(robot_name) if module_to_use is False else world.turtle.world.do_left_turn(robot_name)
    elif command_name == 'sprint':
        return do_sprint(robot_name, int(command_arg))
    elif command_name == 'replay':
        return do_replay(robot_name, command_arg)
    elif command_name == "mazerun":
        add_to_history(command_name + " "+command_arg)
        return maze_runner(robot_name, command_arg)
    return False, None


def handle_command(robot_name, command):
    """
    Handles a command by asking different functions to handle each command.

    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """

    (command_name, arg) = split_command_input(command)

    if command_name == 'off':
        return False
    else:
        (do_next, command_output) = call_command(command_name, arg, robot_name)

    print(command_output)
    world.text.world.show_position(
        robot_name) if module_to_use is False else world.turtle.world.show_position(robot_name)
    if mazerun_mode:
        pass
    else:
        add_to_history(command)
    return do_next


def add_to_history(command):
    """
    Adds the command to the history list of commands
    :param command:
    :return:
    """
    history.append(command)


def robot_start():
    """This is the entry point for starting my robot"""

    global history

    robot_name = get_robot_name()

    world.text.world.output(robot_name, "Hello kiddo!")if module_to_use is False else world.turtle.world.output(
        robot_name, "Hello kiddo!")

    world.text.world.obstacles_positions(
        robot_name) if module_to_use is False else ""

    world.text.world.position_x = 0
    world.text.world.position_y = 0
    world.text.world.current_direction_index = 0
    history = []

    command = get_command(robot_name)
    while handle_command(robot_name, command):
        command = get_command(robot_name)

    world.text.world.output(robot_name, "Shutting down..") if module_to_use is False else world.turtle.world.output(
        robot_name, "Shutting down..")


if __name__ == "__main__":
    robot_start()
