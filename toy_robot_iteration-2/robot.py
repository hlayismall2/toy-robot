
counter = 0


def robot_start():
    """This is the entry function, do not change"""
    name = name_the_robot()
    get_command_input(name)


def name_the_robot():
    '''getting a name of a robot from the user'''

    name = input('What do you want to name your robot? ')
    print(f"{name}: Hello kiddo!")
    return name


def get_command_input(name):
    '''Tgetting commands input from the user and validate'''
    global counter
    try:
        x, y, counter = 0, 0, 0  # counter declared to move the robot based on a cartesian plane
        get_input = input(f"{name}: What must I do next? ")
        while True:
            if get_input.lower() == "off":  # off command
                print(f"{name}: Shutting down..")
                break
            elif get_input.lower() == "help":  # help command
                help_result()
            elif get_input[:7].lower() == "forward":  # forward command
                x, y = move_forward(name, counter, get_input[8:], x, y)
            elif get_input[:4].lower() == "back":  # back command
                x, y = move_back(name, counter, get_input[5:], x, y)
            elif get_input.lower() == "right":  # right command
                right(name, x, y)
                counter += 1
                if counter == 4:
                    counter = 0
            elif get_input.lower() == "left":  # left command
                left(name, x, y)
                counter -= 1
                if counter == -5:
                    counter = 0
            elif get_input.split()[0].lower() == "sprint":  # sprint command
                x, y = sprint(name, counter, int(get_input.split()[1]), x, y)
            else:
                # for unknown command
                print(f"{name}: Sorry, I did not understand '{get_input}'.")
            # prompting the input each and everytime
            get_input = input(f"{name}: What must I do next? ")
    except ValueError:
        # handle exceptions if the users enter incomplete command
        get_command_input(name)


def help_result():
    '''This function display all commands'''
    print("I can understand these commands:\nOFF  - Shut down robot")
    print("HELP - provide information about commands")
    print("FORWARD STEP - move the robot forward\nBACK STEP- move the robot back")
    print("RIGHT - turn the robot to the right\nLEFT - move your robot to left")
    print("SPRINT STEP - sprint the robot by selected steps\n")


def move_forward(name, counter, get_input, x, y):
    '''This function move the robot forward in a specified step'''
    if counter == 0 or counter == -4:
        y += int(get_input)
        if y > -200 and y < 200:  # y -axis range
            forward(name, get_input, x, y)
        else:
            y = abs(y - int(get_input))
            range_result(name, x, y)
    if counter == 1 or counter == -3:
        x += int(get_input)
        if x > -100 and x < 100:  # x -axis range
            forward(name, get_input, x, y)
        else:
            x = abs(x - int(get_input))
            range_result(name, x, y)
    if counter == 2 or counter == -2:
        y -= int(get_input)
        if y > -200 and y < 200:  # y -axis range
            forward(name, get_input, x, y)
        else:
            y = abs(y + int(get_input))
            range_result(name, x, y)
    if counter == 3 or counter == -1:
        x -= int(get_input)
        if x > -100 and x < 100:  # x -axis range
            forward(name, get_input, x, y)
        else:
            x = abs(x + int(get_input))
            range_result(name, x, y)
    return (x, y)


def move_back(name, counter, get_input, x, y):
    '''This function move the robot back with a specified step'''
    if counter == 0 or counter == -4:
        y -= int(get_input)
        if y > -200 and y < 200:  # y -axis range
            back(name, get_input, x, y)
        else:
            y = abs(y + int(get_input))
            range_result(name, x, y)
    if counter == 1 or counter == -3:
        x -= int(get_input)
        if x > -100 and x < 100:  # x -axis range
            back(name, get_input, x, y)
        else:
            x = abs(x + int(get_input))
            range_result(name, x, y)
    if counter == 2 or counter == -2:
        y += int(get_input)
        if y > -200 and y < 200:  # y -axis range
            back(name, get_input, x, y)
        else:
            y = abs(y - int(get_input))
            range_result(name, x, y)
    if counter == 3 or counter == -1:
        x += int(get_input)
        if x > -100 and x < 100:  # x -axis range
            back(name, get_input, x, y)
        else:
            x = abs(x - int(get_input))
            range_result(name, x, y)
    return (x, y)


def sprint(name, counter, input, x, y):
    '''This function move the robot in a sprinted motion'''
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
    '''This function display thes range result if the specified step is out of range'''
    print(f"{name}: Sorry, I cannot go outside my safe zone.")
    print(" > {} now at position {}".format(name, "("+str(x)+","+str(y)+")."))


def forward(name, steps, x, y):
    '''This function display moving forward outcome'''
    print(f" > {name} moved forward by {steps} steps.")
    print(" > {} now at position {}".format(name, "("+str(x)+","+str(y)+")."))


def back(name, steps, x, y):
    '''This function display moving back outcome'''
    print(f" > {name} moved back by {steps} steps.")
    print(" > {} now at position {}".format(name, "("+str(x)+","+str(y)+")."))


def right(name, x, y):
    '''This function display turn right outcome'''
    print(f" > {name} turned right.")
    print(" > {} now at position {}".format(name, "("+str(x)+","+str(y)+")."))


def left(name, x, y):
    '''This function display turn left outcome'''
    print(f" > {name} turned left.")
    print(" > {} now at position {}".format(
        name, "(" + str(x) + "," + str(y) + ")."))


def show_sprint_result(name, x, y):
    print(" > {} now at position {}".format(name, "("+str(x)+","+str(y)+")."))


if __name__ == "__main__":
    robot_start()
