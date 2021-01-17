import robot

def left():
    global counter
    x = world.text.world.position_x if robot.module_to_use is False else world.turtle.world.position_x
    y = world.text.world.position_y if robot.module_to_use is False else world.turtle.world.position_y
    if (world.text.world.obstacles.is_path_blocked(x, y, x, y-20) is False and world.text.world.obstacles.is_path_blocked(x, y, x+20, y) is False and world.text.world.obstacles.is_path_blocked(x, y, x, y+20) is False and world.text.world.obstacles.is_path_blocked(x, y, x, y-20) is False if robot.module_to_use is False else world.turtle.world.obstacles.is_path_blocked(x, y, x-20, y) is False and world.turtle.world.obstacles.is_path_blocked(x, y, x+20, y) is False and world.turtle.world.obstacles.is_path_blocked(x, y, x, y+20) is False and world.turtle.world.obstacles.is_path_blocked(x, y, x, y-20) is False):
        # if (world.text.world.obstacles.is_path_blocked(x, y, x, y-20) is False or world.text.world.obstacles.is_path_blocked(x, y, x+20, y) is False or world.text.world.obstacles.is_path_blocked(x, y, x, y+20) is False or world.text.world.obstacles.is_path_blocked(x, y, x, y-20) is False if robot.module_to_use is False else world.turtle.world.obstacles.is_path_blocked(x, y, x-20, y) is False or world.turtle.world.obstacles.is_path_blocked(x, y, x+20, y) is False or world.turtle.world.obstacles.is_path_blocked(x, y, x, y+20) is False or world.turtle.world.obstacles.is_path_blocked(x, y, x, y-20) is False):

        if (world.text.world.obstacles.is_path_blocked(x, y, x, y-20) is False if robot.module_to_use is False else world.turtle.world.obstacles.is_path_blocked(x, y, x, y-20) is False):

            return False
    if counter == 0:
        if (world.text.world.obstacles.is_path_blocked(x, y, x-20, y) if robot.module_to_use is False else world.turtle.world.obstacles.is_path_blocked(x, y, x-20, y)) or ((world.text.world.is_position_allowed(x-20, y) is False) if robot.module_to_use is False else (world.turtle.world.is_position_allowed(x-20, y) is False)):
            return False
    if counter == 3:
        if (world.text.world.obstacles.is_path_blocked(x, y, x, y+20) if robot.module_to_use is False else world.turtle.world.obstacles.is_path_blocked(x, y, x, y+20)) or ((world.text.world.is_position_allowed(x, y+20) is False) if robot.module_to_use is False else (world.turtle.world.is_position_allowed(x, y+20) is False)):
            return False
    if counter == 2:
        if (world.text.world.obstacles.is_path_blocked(x, y, x+20, y) if robot.module_to_use is False else world.turtle.world.obstacles.is_path_blocked(x, y, x+20, y)) or ((world.text.world.is_position_allowed(x+20, y) is False) if robot.module_to_use is False else (world.turtle.world.is_position_allowed(x+20, y) is False)):
            return False
    if counter == 1:
        if (world.text.world.obstacles.is_path_blocked(x, y, x, y-20) if robot.module_to_use is False else world.turtle.world.obstacles.is_path_blocked(x, y, x, y-20)) or ((world.text.world.is_position_allowed(x, y-20) is False) if robot.module_to_use is False else (world.turtle.world.is_position_allowed(x, y-20) is False)):
            return False
    return True


def forward():
    global counter
    x = world.text.world.position_x if robot.module_to_use is False else world.turtle.world.position_x
    y = world.text.world.position_y if robot.module_to_use is False else world.turtle.world.position_y
    if counter == 0:
        if (world.text.world.obstacles.is_path_blocked(x, y, x, y+20) if robot.module_to_use is False else world.turtle.world.obstacles.is_path_blocked(x, y, x, y+20)) or ((world.text.world.is_position_allowed(x, y+20) is False) if robot.module_to_use is False else (world.turtle.world.is_position_allowed(x, y+20) is False)):
            return False
    if counter == 1:
        if (world.text.world.obstacles.is_path_blocked(x, y, x-20, y) if robot.module_to_use is False else world.turtle.world.obstacles.is_path_blocked(x, y, x-20, y)) or (world.text.world.is_position_allowed(x-20, y) is False if robot.module_to_use is False else world.turtle.world.is_position_allowed(x-20, y) is False):
            return False
    if counter == 2:
        if (world.text.world.obstacles.is_path_blocked(x, y, x, y-20) if robot.module_to_use is False else world.turtle.world.obstacles.is_path_blocked(x, y, x, y-20)) or (world.text.world.is_position_allowed(x, y-20) is False if robot.module_to_use is False else world.turtle.world.is_position_allowed(x, y-20) is False):
            return False
    if counter == 3:
        if (world.text.world.obstacles.is_path_blocked(x, y, x+20, y) if robot.module_to_use is False else world.turtle.world.obstacles.is_path_blocked(x, y, x+20, y)) or (world.text.world.is_position_allowed(x+20, y) is False if robot.module_to_use is False else world.turtle.world.is_position_allowed(x+20, y) is False):
            return False
    return True


def maze_runner(robot, arg):
    global mazerun_mode
    mazerun_mode = True

    if arg == '':
        arg = 'top'

    print(f' > {robot} starting maze run..')
    if arg.lower().strip() == "top" or arg.lower().strip() == "":
        for x in itertools.repeat(1):
            # if arg.lower().strip() == "top" or arg.lower().strip() == "":
            if (world.text.world.position_y == 200 if robot.module_to_use is False else world.turtle.world.position_y == 200):
                break
            if left():
                robot.handle_command(robot, "left")
            if forward():
                robot.handle_command(robot, "forward 20")
            else:
                robot.handle_command(robot, "right")
    if arg.lower().strip() == "bottom":
        return bottom_side(robot, arg)

    if arg.lower().strip() == "right":
        return right_side(robot, arg)
    if arg.lower().strip() == "left":
        return left_side(robot, arg)

    mazerun_mode = False
    return True, " > " + robot+" I am at the "+arg+" edge."


def bottom_side(robot, arg):
    # for x in itertools.repeat(1):
    if (world.text.world.position_y == -200 if robot.module_to_use is False else world.turtle.world.position_y == -200):
        return True, " > " + robot+" I am at the "+arg+" edge."
    if left():
        robot.handle_command(robot, "left")
    if forward():
        robot.handle_command(robot, "forward 20")
    else:
        robot.handle_command(robot, "right")
    return bottom_side(robot, arg)


def right_side(robot, arg):
    # for x in itertools.repeat(1):
    if (world.text.world.position_x == 100 if robot.module_to_use is False else world.turtle.world.position_x == 100):
        return True, " > " + robot+" I am at the "+arg+" edge."
    if left():
        robot.handle_command(robot, "left")
    if forward():
        robot.handle_command(robot, "forward 20")
    else:
        robot.handle_command(robot, "right")
    return right_side(robot, arg)


def left_side(robot, arg):
    # for x in itertools.repeat(1):
    # while True:
    if (world.text.world.position_x == -100 if robot.module_to_use is False else world.turtle.world.position_x == -100):
        return True, " > " + robot+" I am at the "+arg+" edge."
    if left():
        robot.handle_command(robot, "left")
    if forward():
        robot.handle_command(robot, "forward 20")
    else:
        robot.handle_command(robot, "right")
    return left_side(robot, arg)
