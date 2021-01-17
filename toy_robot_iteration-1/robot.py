

# TODO: Decompose into functions
def move_square(size):
    'moving the robot in square'
    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")
    return


def move_rectangle(length, width):
    '''moving the robot in the rectangle shape'''
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")
    return


def move_circle(length):
    '''moving robot in circle shape'''
    print("Moving in a circle")
    degrees = 1
    for i in range(360):
        length = 1
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
    return


def square_dancing(lemgth):
    '''moving robot in a square dancing motion'''
    degrees = 90
    size = 20
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        length = 20
        print("* Move Forward "+str(length))
        print("Moving in a square of size 20")
        for j in range(4):
            print("* Move Forward " + str(size))
            print("* Turn Right " + str(degrees) + " degrees")
    return


def crop_circles():
    '''moving robot in crop circle motion'''
    degrees = 1
    print("Crop circles - 4 circles")
    for i in range(4):
        length = 20
        print("* Move Forward "+str(length))
        print("Moving in a circle")
        length = 1
        for k in range(360):
            print("* Move Forward " + str(length))
            print("* Turn Right " + str(degrees) + " degrees")
    return


def move():
    ''' moving_in_shapes -  chose it because as the code base is dealing with shapes'''
    size = 10
    length = 20
    width = 10

    move_square(size)
    move_rectangle(length, width)
    move_circle(length)
    square_dancing(length)
    crop_circles()


def robot_start():
    move()


if __name__ == "__main__":
    robot_start()
