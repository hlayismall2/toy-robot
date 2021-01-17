history = []
track = False  # for silent replay option
counter = 0


def robot_start():
    """This is the entry function, do not change."""
    name = name_the_robot()
    get_command_input(name)


def name_the_robot():
    '''Asks the user to name the robot.'''
    name = input('What do you want to name your robot? ')
    print(f"{name}: Hello kiddo!")
    return name


def history_(result):
    '''Add comands to a global history container.'''
    history.append(result)
    return history


def replay_normal(name, x, y, counter, range_):
    '''Replay the moving commands in the history container
       and limit range of commands in history if specified.'''
    move = ["forward", "right", "back", "left", "sprint"]
    filtered_list = list(
        filter(lambda x: x.split()[0].lower() in move, history))
    co = 0
    if range_ == None:
        pass
    elif type(range_) == list:
        n = int(range_[0])
        m = int(range_[1])
        filtered_list = filtered_list[len(filtered_list) - n:-m]
    else:
        n = int(range_)
        filtered_list = filtered_list[len(filtered_list) - n:]

    for i in filtered_list:
        co += 1
        x, y, counter = validate(name, i, x, y, counter)
    if track == False:
        print(f" > {name} replayed {co} commands.")
        print(" > {} now at position {}".format(
            name, "("+str(x)+","+str(y)+")."))
    else:
        print(f" > {name} replayed {co} commands silently.")
        print(" > {} now at position {}".format(
            name, "("+str(x)+","+str(y)+")."))

    return x, y, counter


def replay_reversed(name, x, y, counter, range_):
    '''Replay the moving commands in the history container in a reverse
       and limit range of commands in history if it is specified.'''
    move = ["forward", "right", "back", "left", "sprint"]
    filtered_list = list(
        filter(lambda x: x.split()[0].lower() in move, history))
    filtered_list = filtered_list[::-1]
    co = 0
    if range_ == None:
        pass
    elif range_.isdigit():
        n = int(range_)
        filtered_list = filtered_list[len(filtered_list) - n:]

    for i in filtered_list:
        co += 1
        x, y, counter = validate(name, i, x, y, counter)
    if track == False:
        print(f" > {name} replayed {co} commands in reverse.")
    else:
        print(f" > {name} replayed {co} commands in reverse silently.")
    print(" > {} now at position {}".format(name, "("+str(x)+","+str(y)+")."))
    return x, y, counter


def replay(name, input, x, y, counter):
    '''Validates all the replay commands :Replay :Replay silent :Replay reversed
       :Replay reversed silent
       :Limit range of commands.'''
    global track
    track = False
    range_ = None
    if len(input.split()) == 3:
        if input.split()[1].isalpha() and input.split()[2].lower() == 'silent':
            track = True
            x, y, counter = replay_reversed(name, x, y, counter, range_)
            track = False
        # range with only one digit and in a reverse
        elif input.split()[1].isdigit() and input.split()[2].lower() == 'reversed':
            x, y, counter = replay_reversed(
                name, x, y, counter, input.split()[1])
        # range with only one digit and in a reverse
        elif input.split()[1].isdigit() and input.split()[2].lower() == 'silent':
            track = True
            x, y, counter = replay_normal(
                name, x, y, counter, input.split()[1])
            track = False
        else:
            # for unknown command
            print(f"{name}: Sorry, I did not understand '{input}'.")
        return x, y, counter

    if len(input.split()) == 1:
        x, y, counter = replay_normal(name, x, y, counter, range_)
    elif input.split()[1].isnumeric():
        x, y, counter = replay_normal(name, x, y, counter, input.split()[
                                      1])  # range with only one digit
    elif input.split()[1].count("-") == 1:
        x, y, counter = replay_normal(name, x, y, counter, input.split()[
                                      1].split("-"))  # a range with a dash
    elif input.split()[1].lower() == "silent":
        track = True
        x, y, counter = replay_normal(name, x, y, counter, range_)
        track = False
    elif input.split()[1].lower() == "reversed":
        x, y, counter = replay_reversed(name, x, y, counter, range_)
    else:
        # for unknown command
        print(f"{name}: Sorry, I did not understand '{input}'.")
    return x, y, counter


def get_command_input(name):
    '''Asks the user to enter a command.'''
    global counter
    x, y, counter = 0, 0, 0  # counter declared to move the robot based on a cartesian plane
    global history
    history = []
    get_input = input(f"{name}: What must I do next? ")
    while get_input.lower() != "off":  # off command:
        x, y, counter = validate(name, get_input, x, y, counter)
        history_(get_input)
        # prompting the input each and everytime
        get_input = input(f"{name}: What must I do next? ")
    print(f"{name}: Shutting down..")


def validate(name, get_input, x, y, counter):
    '''Getting the command input and validates it.'''
    if get_input == "help":  # help command
        help_result()
    elif get_input[:7].lower() == "forward" and get_input.split()[1].isnumeric():  # forward command
        x, y = move_forward(name, counter, get_input, x, y)
    elif get_input[:4].lower() == "back" and get_input.split()[1].isnumeric():  # back command
        x, y = move_back(name, counter, get_input, x, y)
    elif get_input.lower() == "right":  # right command
        counter = right(name, counter, x, y)
    elif get_input.lower() == "left":  # left command
        counter = left(name, counter, x, y)
    # sprint command
    elif get_input.split()[0].lower() == "sprint" and get_input.split()[1].isnumeric():
        x, y = sprint(name, counter, int(get_input.split()[1]), x, y)
    elif get_input.split()[0].lower() == "replay":  # replay command
        x, y, counter = replay(name, get_input, x, y, counter)
    else:
        # for unknown command
        print(f"{name}: Sorry, I did not understand '{get_input}'.")
    return (x, y, counter)


def help_result():
    '''This function display all the commands that the robot allow.'''
    print("I can understand these commands:\nOFF  - Shut down robot")
    print("HELP - provide information about commands")
    print("FORWARD STEP - move the robot forward\nBACK STEP- move the robot back")
    print("RIGHT - turn the robot to the right\nLEFT - turn your robot to left")
    print("SPRINT STEP - sprint the robot by selected steps\nREPLAY - replay the previous commands in history")
    print("REPLAY SILENT - replay the previous commands in history in silence")
    print("""REPLAY REVERSED - replay the prvious commands in reverse
REPLAY SIZE - replay the last size commands""")
    print("""REPLAY N-M - replay the previous commands in range of n and m, n must be bigger than m!
REPLAY SIZE SILENT - replay the last size commands silent\n""")


def move_forward(name, counter, get_input, x, y):
    '''This function move the robot in a forward direction
       by a specified step  and direction.'''
    if counter == 0 or counter == -4:
        y += int(get_input[8:])
        if y > -200 and y < 200:  # y -axis range
            forward(name, get_input[8:], x, y)
        else:
            y = abs(y - int(get_input[8:]))
            range_result(name, x, y)
    if counter == 1 or counter == -3:
        x += int(get_input[8:])
        if x > -100 and x < 100:  # x -axis range
            forward(name, get_input[8:], x, y)
        else:
            x = abs(x - int(get_input[8:]))
            range_result(name, x, y)
    if counter == 2 or counter == -2:
        y -= int(get_input[8:])
        if y > -200 and y < 200:  # y -axis range
            forward(name, get_input[8:], x, y)
        else:
            y = abs(y + int(get_input[8:]))
            range_result(name, x, y)
    if counter == 3 or counter == -1:
        x -= int(get_input[8:])
        if x > -100 and x < 100:  # x -axis range
            forward(name, get_input[8:], x, y)
        else:
            x = abs(x + int(get_input[8:]))
            range_result(name, x, y)
    return (x, y)


def move_back(name, counter, get_input, x, y):
    '''This function move the robot in a backward direction
        by a specified step and direction.'''
    if counter == 0 or counter == -4:
        y -= int(get_input[5:])
        if y > -200 and y < 200:  # y -axis range
            back(name, get_input[5:], x, y)
        else:
            y = abs(y + int(get_input[5:]))
            range_result(name, x, y)
    if counter == 1 or counter == -3:
        x -= int(get_input[5:])
        if x > -100 and x < 100:  # x -axis range
            back(name, get_input[5:], x, y)
        else:
            x = abs(x + int(get_input[5:]))
            range_result(name, x, y)
    if counter == 2 or counter == -2:
        y += int(get_input[5:])
        if y > -200 and y < 200:  # y -axis range
            back(name, get_input[5:], x, y)
        else:
            y = abs(y - int(get_input[5:]))
            range_result(name, x, y)
    if counter == 3 or counter == -1:
        x += int(get_input[5:])
        if x > -100 and x < 100:  # x -axis range
            back(name, get_input[5:], x, y)
        else:
            x = abs(x - int(get_input[5:]))
            range_result(name, x, y)
    return (x, y)


def sprint(name, counter, input, x, y):
    '''This function move the robot in a sprint motion.'''
    if input == 0:
        show_sprint_result(name, x, y)
        return (x, y)
    else:
        if counter == 2 or counter == -2:
            y -= input
            if y > -200 and y < 200:  # y -axis range
                print(f" > {name} moved forward by {input} steps.")
                return sprint(name, counter, input - 1, x, y)
            else:
                y = abs(y - input)
                range_result(name, x, y)

        if counter == 1 or counter == -3:
            x += input
            if x > -100 and y < 100:  # y -axis range
                print(f" > {name} moved forward by {input} steps.")
                return sprint(name, counter, input - 1, x, y)
            else:
                x = abs(x - input)
                range_result(name, x, y)

        if counter == 0 or counter == -4:
            y += input
            if y > -200 and y < 200:  # y -axis range
                print(f" > {name} moved forward by {input} steps.")
                return sprint(name, counter, input - 1, x, y)
            else:
                y = abs(y - input)
                range_result(name, x, y)

        if counter == 3 or counter == -1:
            x -= input
            if x > -100 and y < 100:  # y -axis range
                print(f" > {name} moved forward by {input} steps.")
                return sprint(name, counter, input - 1, x, y)
            else:
                x = abs(x - input)
                range_result(name, x, y)
    return (x, y)


def range_result(name, x, y):
    '''This function display thes range result if the specified step is out of range.'''
    if track == True:
        pass
    else:
        print(f"{name}: Sorry, I cannot go outside my safe zone.")
        print(" > {} now at position {}".format(
            name, "("+str(x)+","+str(y)+")."))


def forward(name, steps, x, y):
    '''This function display moving forward outcomes.'''
    if track == True:
        pass
    else:
        print(f" > {name} moved forward by {steps} steps.")
        print(" > {} now at position {}".format(
            name, "("+str(x)+","+str(y)+")."))


def back(name, steps, x, y):
    '''This function display moving back outcomes.'''
    if track == True:
        pass
    else:
        print(f" > {name} moved back by {steps} steps.")
        print(" > {} now at position {}".format(
            name, "("+str(x)+","+str(y)+")."))


def right(name, counter, x, y):
    '''This function display turn right outcomes and turn the robot by 90 degress.'''
    if track == True:
        pass
    else:
        print(f" > {name} turned right.")
        print(" > {} now at position {}".format(
            name, "("+str(x)+","+str(y)+")."))
    counter += 1
    if counter == 4:
        counter = 0
    return counter


def left(name, counter, x, y):
    '''This function display turn left outcomes and turn the robot by -90 degress.'''
    if track == True:
        pass
    else:
        print(f" > {name} turned left.")
        print(" > {} now at position {}".format(
            name, "("+str(x)+","+str(y)+")."))
    counter -= 1
    if counter == -5:
        counter = 0
    return counter


def show_sprint_result(name, x, y):
    print(" > {} now at position {}".format(name, "("+str(x)+","+str(y)+")."))


if __name__ == "__main__":
    robot_start()
