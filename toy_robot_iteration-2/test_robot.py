import unittest
import robot
from io import StringIO
from unittest.mock import patch


class myTestCase(unittest.TestCase):

    @patch("sys.stdin", StringIO("ofF\nOff\nOFF\n"))
    def test_off_command(self):
        with patch("sys.stdout", StringIO()) as output:
            robot.get_command_input("fly")
            self.assertEqual(
                "fly: What must I do next? fly: Shutting down..", output.getvalue().strip())

        with patch("sys.stdout", StringIO()) as output:
            robot.get_command_input("fly")
            self.assertEqual(
                "fly: What must I do next? fly: Shutting down..", output.getvalue().strip())

        with patch("sys.stdout", StringIO()) as output:
            robot.get_command_input("fly")
            self.assertEqual(
                "fly: What must I do next? fly: Shutting down..", output.getvalue().strip())

    @patch("sys.stdin", StringIO("of\noff\n"))
    def test_incorrect_command(self):

        with patch("sys.stdout", StringIO()) as output:
            robot.get_command_input("fly")

        self.assertEqual("""fly: What must I do next? fly: Sorry, I did not understand 'of'.
fly: What must I do next? fly: Shutting down..""", output.getvalue().strip())

    @patch("sys.stdin", StringIO("help\noff\n"))
    def test_help_command_correctness(self):

        with patch("sys.stdout", StringIO()) as output:
            robot.get_command_input("fly")

        self.assertEqual("""fly: What must I do next? I can understand these commands:
OFF  - Shut down robot\nHELP - provide information about commands
FORWARD STEP - move the robot forward
BACK STEP- move the robot back
RIGHT - turn the robot to the right
LEFT - move your robot to left
SPRINT STEP - sprint the robot by selected steps

fly: What must I do next? fly: Shutting down..""", output.getvalue().strip())

    @patch("sys.stdin", StringIO("forward 10\nforward 20\noff\n"))
    def test_forward_command(self):

        with patch("sys.stdout", StringIO()) as output:
            robot.get_command_input("fly")

        self.assertEqual("""fly: What must I do next?  > fly moved forward by 10 steps.
 > fly now at position (0,10).
fly: What must I do next?  > fly moved forward by 20 steps.
 > fly now at position (0,30).
fly: What must I do next? fly: Shutting down..""", output.getvalue().strip())

    @patch("sys.stdin", StringIO("back 10\nback 10\noff\n"))
    def test_back_command(self):

        with patch("sys.stdout", StringIO()) as output:
            robot.get_command_input("fly")

        self.assertEqual("""fly: What must I do next?  > fly moved back by 10 steps.
 > fly now at position (0,-10).
fly: What must I do next?  > fly moved back by 10 steps.
 > fly now at position (0,-20).
fly: What must I do next? fly: Shutting down..""", output.getvalue().strip())

    @patch("sys.stdin", StringIO("sprint 5\noff\n"))
    def test_sprint_command(self):
        with patch("sys.stdout", StringIO()) as output:
            robot.get_command_input("s")

        self.assertEqual("""s: What must I do next?  > s moved forward by 5 steps.
 > s moved forward by 4 steps.
 > s moved forward by 3 steps.
 > s moved forward by 2 steps.
 > s moved forward by 1 steps.
 > s now at position (0,15).
s: What must I do next? s: Shutting down..""", output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
