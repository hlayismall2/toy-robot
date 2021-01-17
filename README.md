# toy_robot

* Given a prototype program that is intended to simulate a basic toy robot. Using an iterative programming approach to evolve this prototype into a much more capable robot simulator and controller.

# Implematations

* Split the project into 4 iterations.

# Program

* Get command input from the user and handle it.
* Use variables to keep state of the robot’s position and direction
* keep a history of all commands given to it.
* on a replay command it must filter out all non-movement commands and redo only the movement commands, providing the full output.
* on a replay silent command it must not show the full output, but only show the resulting updated position.
* support a replay reversed command that redo movement commands in reverse order.
* possible to specify the range of commands to replay.
* movements on a graphical user interface, as an alternative to the terminal output.
* robot move on randomized maze and being able to solve the maze
