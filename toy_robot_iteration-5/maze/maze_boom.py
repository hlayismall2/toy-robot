import turtle
import random


turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.color("red")


stack = []
all_obs = []
paths = []
openinings = []

# all the position of x and y
position = [[(x, y) for y in range(-210, 210, 20)]
            for x in range(-110, 110, 20)]

# matching x and  y coordinates to use in drawing a grid
position = [[position[col][row]
             for col in range(len(position))]for row in range(len(position[0]))]


unvisted = [[(j, i) for i in range(len(position[0]))]
            for j in range(len(position))]

# drawing a grid 10*20
turtle.tracer(False)
for c in position:
    for x, y in c:
        t.up()
        t.goto(x, y)
        t.down()
        for i in range(4):
            t.fd(20)
            t.lt(90)
turtle.tracer(True)
t.hideturtle()


def left(x, y):
    '''this function checks the left side in the grid that it exist by the defined position'''
    
    try:
        y = y - 1
        if y < 0 or (x, y) in stack:
            return False
        else:
            position[x][y]
            return True
    except IndexError:
        return False


def up(x, y):
    '''this function checks the top side in the grid that it exist by the defined position'''
    
    try:
        if (x+1, y) in stack:
            return False
        else:
            position[x+1][y]
            return True
    except IndexError:
        return False


def right(x, y):
    '''this function checks the right side in the grid that it exist by the defined position'''
   
    try:
        if (x, y+1) in stack:
            return False
        else:
            position[x][y+1]
            return True
    except IndexError:
        return False


def down(x, y):
    '''this function checks the down side in the grid that it exist by the defined position'''

    try:
        x = x - 1
        if x < 0 or (x, y) in stack:
            return False
        else:
            position[x][y]
            return True
    except IndexError:
        return False


def convert_2D_to_list(multi_dime):
    '''convert 2-d array to a list'''

    new_list = []
    for i in multi_dime:
        for j in i:
            new_list.append(j)
    return new_list

# recursive_backtracking


def recursive_backtracking(initial, unvisted):
    '''this function is a recursive bactracking'''

    global stack
    for i in unvisted:
        if len(i):
            del i
    if len(unvisted) == 0:
        return 0
    else:
        direction = []
        x, y = initial

        # checking the availability of all the four side
        if up(x, y):
            if (x+1, y) in convert_2D_to_list(unvisted):
                direction.append(((x+1, y), position[x+1][y], 90))
        if down(x, y):
            if (x-1, y) in convert_2D_to_list(unvisted):
                x1, y1 = position[x - 1][y]
                direction.append(((x-1, y), (x1, y1+20), 270))
        if left(x, y):
            if (x, y-1) in convert_2D_to_list(unvisted):
                x1, y1 = position[x][y-1]
                direction.append(((x, y-1), (x1+20, y1), 180))
        if right(x, y):
            if (x, y+1) in convert_2D_to_list(unvisted):
                direction.append(((x, y + 1), position[x][y + 1], 0))

        if len(direction) == 0:
            for i in unvisted:
                for j in range(len(i)):
                    if (x, y) == i[j]:
                        del i[j]
                        break
            stack.pop()
            if len(stack) == 0:
                return 0
            xx, yy = stack[-1]
            new_initial = (xx, yy)
        else:
            for i in unvisted:
                for j in range(len(i)):
                    if (x, y) == i[j]:
                        del i[j]
                        break
            data = random.choice(direction)
            new_initial = data[0]
            go_to = data[1]
            facing = data[2]
            structure(go_to, facing)
            paths.append((go_to, facing))
            stack.append((x, y))

        return recursive_backtracking(new_initial, unvisted)


def structure(pos, direct):
    '''this function structure the maze by deleting one side of each block by using a different color'''

    t.color("white")

    if direct == 0:
        t.setheading(90)
        t.up()
        t.goto(pos)
        t.down()
        t.fd(20)
    elif direct == 90:
        t.setheading(0)
        t.up()
        t.goto(pos)
        t.down()
        t.fd(20)
    elif direct == 180:
        t.setheading(90)
        t.up()
        t.goto(pos)
        t.down()
        t.fd(20)
    elif direct == 270:
        t.setheading(0)
        t.up()
        t.goto(pos)
        t.down()
        t.fd(20)
    return True


initial = (5, 5)
recursive_backtracking(initial, unvisted)

# add all the obstacles to the all_obs empty list


def get_obstacles():
    '''returns a list of the obstacles positions'''

    global all_obs
    all_obs = []
    for i in position:
        for j in i:
            for k in range(22):
                all_obs.append((j[0] + k, j[1]))
                all_obs.append((j[0] + 20, j[1] + k))
                all_obs.append((j[0] + 20 - k, j[1] + 20))
                all_obs.append((j[0], j[1] + 20 - k))
    return all_obs


# append oppenings coordinates to a oppenings empty list
for co, fc in paths:
    for i in range(1, 21):
        if fc == 0:
            openinings.append((co[0], co[1] + i))
        elif fc == 90:
            openinings.append((co[0]+20-i, co[1]))
        elif fc == 180:
            openinings.append((co[0], co[1]+i))
        elif fc == 270:
            openinings.append((co[0]+20-i, co[1]))

get_obstacles()

# filter out openings from the list of the whole of obstacles
random_position = list(
    set(list(filter(lambda a: a not in openinings, all_obs))))

# implement the obstacles by drawing them in the maze
turtle.tracer(False)
t.color("red")
for i in random_position:
    x, y = i
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    for j in range(4):
        t.fillcolor("red")
        t.fd(5)
        t.rt(90)
    t.end_fill()
    t.up()
turtle.tracer(True)

# hiding the turtle from this file after the maze has been generated
t.hideturtle()


def is_positon_blocked(x, y):
    '''checks if the position is blocked or not : if it is blocked it returns True else: returns False'''

    if (x, y) in random_position:
        return True
    return False


def is_path_blocked(x1, y1, x2, y2):
    '''checks the whole path if it is blocked or not linked to *is_position_blocked()* : returns True if the path is blocked and False if it is not blocked'''
    
    global random_position
    final_x = x2
    final_y = y2
    if x1 > x2:
        x1, x2 = x2, x1
    elif y1 > y2:
        y1, y2 = y2, y1

    if y1 == y2:
        for i in range(x1, x2+1):
            if i == x and final_y == y or is_positon_blocked(i, final_y):
                return True

    if x1 == x2:
        for i in range(y1, y2+1):
            if i == y and final_x == x or is_positon_blocked(final_x, i):
                return True
    return False


t.hideturtle()
