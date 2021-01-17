import unittest
import robot
from io import StringIO
from unittest.mock import patch
from world import obstacles


class myTestCase(unittest.TestCase):

    @patch("sys.stdin", StringIO("fly\nofF\nfly\nOff\nfly\nOFf\n"))
    def test_off_command(self):
        with patch("sys.stdout", StringIO()) as output:

            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()
        self.assertEqual(
            "What do you want to name your robot? fly: Hello kiddo!\nfly: What must I do next? fly: Shutting down..", output.getvalue().strip())

        with patch("sys.stdout", StringIO()) as output:
            robot.robot_start()
        self.assertEqual(
            "What do you want to name your robot? fly: Hello kiddo!\nfly: What must I do next? fly: Shutting down..", output.getvalue().strip())

        with patch("sys.stdout", StringIO()) as output:
            robot.robot_start()
        self.assertEqual(
            "What do you want to name your robot? fly: Hello kiddo!\nfly: What must I do next? fly: Shutting down..", output.getvalue().strip())

    @patch("sys.stdin", StringIO("fly\nof\noff\n"))
    def test_incorrect_command(self):

        with patch("sys.stdout", StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()

        self.assertEqual("""What do you want to name your robot? fly: Hello kiddo!\nfly: What must I do next? fly: Sorry, I did not understand 'of'.
fly: What must I do next? fly: Shutting down..""", output.getvalue().strip())

    @patch("sys.stdin", StringIO("fly\nforward 10\nforward 20\noff\n"))
    def test_forward_command(self):

        with patch("sys.stdout", StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()

        self.assertEqual("""What do you want to name your robot? fly: Hello kiddo!\nfly: What must I do next?  > fly moved forward by 10 steps.
 > fly now at position (0,10).\nfly: What must I do next?  > fly moved forward by 20 steps.
 > fly now at position (0,30).\nfly: What must I do next? fly: Shutting down..""", output.getvalue().strip())

    @patch("sys.stdin", StringIO("fly\nback 10\nback 10\noff\n"))
    def test_back_command(self):

        with patch("sys.stdout", StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()

        self.assertEqual("""What do you want to name your robot? fly: Hello kiddo!\nfly: What must I do next?  > fly moved back by 10 steps.
 > fly now at position (0,-10).\nfly: What must I do next?  > fly moved back by 10 steps.
 > fly now at position (0,-20).\nfly: What must I do next? fly: Shutting down..""", output.getvalue().strip())

    @patch("sys.stdin", StringIO("s\nsprint 5\noff\n"))
    def test_sprint_command(self):
        with patch("sys.stdout", StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? s: Hello kiddo!\ns: What must I do next?  > s moved forward by 5 steps.
 > s moved forward by 4 steps.
 > s moved forward by 3 steps.
 > s moved forward by 2 steps.
 > s moved forward by 1 steps.
 > s now at position (0,15).
s: What must I do next? s: Shutting down..""", output.getvalue().strip())

    @patch("sys.stdin", StringIO("fly\nforward 10\nforward 5\nreplay\noff\n"))
    def test_replay_command_then_off(self):

        with patch("sys.stdout", StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()

        self.assertEqual("""What do you want to name your robot? fly: Hello kiddo!\nfly: What must I do next?  > fly moved forward by 10 steps.
 > fly now at position (0,10).
fly: What must I do next?  > fly moved forward by 5 steps.
 > fly now at position (0,15).
fly: What must I do next?  > fly moved forward by 10 steps.
 > fly now at position (0,25).
 > fly moved forward by 5 steps.
 > fly now at position (0,30).
 > fly replayed 2 commands.
 > fly now at position (0,30).
fly: What must I do next? fly: Shutting down..""", output.getvalue().strip())

    @patch("sys.stdin", StringIO("fly\nforward 10\nforward 5\nreplay silent\noff\n"))
    def test_repaly_silent_then_off(self):

        with patch("sys.stdout", StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()

        self.assertEqual("""What do you want to name your robot? fly: Hello kiddo!\nfly: What must I do next?  > fly moved forward by 10 steps.
 > fly now at position (0,10).
fly: What must I do next?  > fly moved forward by 5 steps.
 > fly now at position (0,15).
fly: What must I do next?  > fly replayed 2 commands silently.
 > fly now at position (0,30).
fly: What must I do next? fly: Shutting down..""", output.getvalue().strip())

    @patch("sys.stdin", StringIO("fly\nforward 10\nforward 5\nreplay reversed\noff\n"))
    def test_replay_reversed_then_off(self):

        with patch("sys.stdout", StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()

        self.assertEqual("""What do you want to name your robot? fly: Hello kiddo!\nfly: What must I do next?  > fly moved forward by 10 steps.
 > fly now at position (0,10).
fly: What must I do next?  > fly moved forward by 5 steps.
 > fly now at position (0,15).
fly: What must I do next?  > fly moved forward by 5 steps.
 > fly now at position (0,20).
 > fly moved forward by 10 steps.
 > fly now at position (0,30).
 > fly replayed 2 commands in reverse.
 > fly now at position (0,30).
fly: What must I do next? fly: Shutting down..\n""", output.getvalue())

    @patch("sys.stdin", StringIO("fly\nforward 10\nright\nforward 10\nright\nforward 5\nreplay 2\noff\n"))
    def test_replay_range_then_off(self):

        with patch("sys.stdout", StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()

        self.assertEqual("""What do you want to name your robot? fly: Hello kiddo!\nfly: What must I do next?  > fly moved forward by 10 steps.
 > fly now at position (0,10).
fly: What must I do next?  > fly turned right.
 > fly now at position (0,10).
fly: What must I do next?  > fly moved forward by 10 steps.
 > fly now at position (10,10).
fly: What must I do next?  > fly turned right.
 > fly now at position (10,10).
fly: What must I do next?  > fly moved forward by 5 steps.
 > fly now at position (10,5).
fly: What must I do next?  > fly turned right.
 > fly now at position (10,5).
 > fly moved forward by 5 steps.
 > fly now at position (5,5).
 > fly replayed 2 commands.
 > fly now at position (5,5).
fly: What must I do next? fly: Shutting down..""", output.getvalue().strip())

    @patch("sys.stdin", StringIO("fly\nforward 10\nright\nforward 10\nright\nforward 5\nreplay 2 silent\noff\n"))
    def test_replay_range_silently(self):

        with patch("sys.stdout", StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? fly: Hello kiddo!\nfly: What must I do next?  > fly moved forward by 10 steps.
 > fly now at position (0,10).
fly: What must I do next?  > fly turned right.
 > fly now at position (0,10).
fly: What must I do next?  > fly moved forward by 10 steps.
 > fly now at position (10,10).
fly: What must I do next?  > fly turned right.
 > fly now at position (10,10).
fly: What must I do next?  > fly moved forward by 5 steps.
 > fly now at position (10,5).
fly: What must I do next?  > fly replayed 2 commands silently.
 > fly now at position (5,5).
fly: What must I do next? fly: Shutting down..""", output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
