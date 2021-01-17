import unittest
import robot
from io import StringIO
from unittest.mock import patch

class myTestCase(unittest.TestCase):

    # @patch("sys.stdin",StringIO("HAL\nfly_lettuce\n"))
    # def test_name_the_robot(self):
    #     with patch("sys.stdout",StringIO()) as output:
    #         robot.name_the_robot()
    #         self.assertEqual("What do you want to name your robot? HAL: Hello kiddo!",output.getvalue().strip())

    #     with patch("sys.stdout",StringIO()) as output:
    #         robot.name_the_robot()
    #         self.assertEqual("What do you want to name your robot? fly_lettuce: Hello kiddo!",output.getvalue().strip())

   

    @patch("sys.stdin",StringIO("ofF\nOff\nOFF\n"))
    def test_off_command(self):   
        with patch("sys.stdout",StringIO()) as output:
            robot.get_command_input("fly")
            self.assertEqual("fly: What must I do next? fly: Shutting down..",output.getvalue().strip())
        
        with patch("sys.stdout",StringIO()) as output:
            robot.get_command_input("fly")
            self.assertEqual("fly: What must I do next? fly: Shutting down..",output.getvalue().strip())
        
        with patch("sys.stdout",StringIO()) as output:
            robot.get_command_input("fly")
            self.assertEqual("fly: What must I do next? fly: Shutting down..",output.getvalue().strip())


    @patch("sys.stdin",StringIO("of\noff\n"))
    def test_incorrect_command(self):
       
        with patch("sys.stdout",StringIO()) as output:
            robot.get_command_input("fly")
        
        self.assertEqual("""fly: What must I do next? fly: Sorry, I did not understand 'of'.
fly: What must I do next? fly: Shutting down..""",output.getvalue().strip())

    @patch("sys.stdin",StringIO("help\noff\n"))          
    def test_help_command_correctness(self):
    
        with patch("sys.stdout",StringIO()) as output:
            robot.get_command_input("fly")    
       
        self.assertEqual("""fly: What must I do next? I can understand these commands:
OFF  - Shut down robot\nHELP - provide information about commands
FORWARD STEP - move the robot forward
BACK STEP- move the robot back
RIGHT - turn the robot to the right
LEFT - turn your robot to left
SPRINT STEP - sprint the robot by selected steps
REPLAY - replay the previous commands in history
REPLAY SILENT - replay the previous commands in history in silence
REPLAY REVERSED - replay the prvious commands in reverse
REPLAY SIZE - replay the last size commands
REPLAY N-M - replay the previous commands in range of n and m, n must be bigger than m!
REPLAY SIZE SILENT - replay the last size commands silent

fly: What must I do next? fly: Shutting down..""",output.getvalue().strip())
    
    @patch("sys.stdin",StringIO("forward 10\nforward 20\noff\n"))
    def test_forward_command(self):

        with patch("sys.stdout",StringIO()) as output:
            robot.get_command_input("fly")
      
        self.assertEqual("""fly: What must I do next?  > fly moved forward by 10 steps.
 > fly now at position (0,10).\nfly: What must I do next?  > fly moved forward by 20 steps.
 > fly now at position (0,30).\nfly: What must I do next? fly: Shutting down..""",output.getvalue().strip())

    @patch("sys.stdin",StringIO("back 10\nback 10\noff\n"))
    def test_back_command(self):
    
        with patch("sys.stdout",StringIO()) as output:
            robot.get_command_input("fly")
       
        self.assertEqual("""fly: What must I do next?  > fly moved back by 10 steps.
 > fly now at position (0,-10).\nfly: What must I do next?  > fly moved back by 10 steps.
 > fly now at position (0,-20).\nfly: What must I do next? fly: Shutting down..""",output.getvalue().strip())

    @patch("sys.stdin",StringIO("sprint 5\noff\n"))
    def test_sprint_command(self):
        with patch("sys.stdout",StringIO()) as output:
            robot.get_command_input("s")
        
        self.assertEqual("""s: What must I do next?  > s moved forward by 5 steps.
 > s moved forward by 4 steps.
 > s moved forward by 3 steps.
 > s moved forward by 2 steps.
 > s moved forward by 1 steps.
 > s now at position (0,15).
s: What must I do next? s: Shutting down..""",output.getvalue().strip())
    
 
    # def test_history_function(self):
    #     tests = ["hal","wow","picanto","ford"]
    #     for i in tests:
    #         result = robot.history_(i)
    #     self.assertEqual(result,["help","hal","wow","picanto","ford"])

    @patch ("sys.stdin",StringIO("forward 10\nforward 5\nreplay\noff\n"))
    def test_replay_command_then_off(self):

        with patch ("sys.stdout",StringIO()) as output:
            robot.get_command_input("fly")
            
        self.assertEqual("""fly: What must I do next?  > fly moved forward by 10 steps.
 > fly now at position (0,10).
fly: What must I do next?  > fly moved forward by 5 steps.
 > fly now at position (0,15).
fly: What must I do next?  > fly moved forward by 10 steps.
 > fly now at position (0,25).
 > fly moved forward by 5 steps.
 > fly now at position (0,30).
 > fly replayed 2 commands.
 > fly now at position (0,30).
fly: What must I do next? fly: Shutting down..""",output.getvalue().strip())

    @patch ("sys.stdin",StringIO("forward 10\nforward 5\nreplay silent\noff\n"))
    def test_repaly_silent_then_off(self):

        with patch ("sys.stdout",StringIO()) as output:
            robot.get_command_input("fly")

        self.assertEqual("""fly: What must I do next?  > fly moved forward by 10 steps.
 > fly now at position (0,10).
fly: What must I do next?  > fly moved forward by 5 steps.
 > fly now at position (0,15).
fly: What must I do next?  > fly replayed 2 commands silently.
 > fly now at position (0,30).
fly: What must I do next? fly: Shutting down..""",output.getvalue().strip())

    @patch ("sys.stdin",StringIO("forward 10\nforward 5\nreplay reversed\noff\n"))
    def test_replay_reversed_then_off(self):

        with patch("sys.stdout",StringIO()) as output:
            robot.get_command_input("fly")
    
        self.assertEqual("""fly: What must I do next?  > fly moved forward by 10 steps.
 > fly now at position (0,10).
fly: What must I do next?  > fly moved forward by 5 steps.
 > fly now at position (0,15).
fly: What must I do next?  > fly moved forward by 5 steps.
 > fly now at position (0,20).
 > fly moved forward by 10 steps.
 > fly now at position (0,30).
 > fly replayed 2 commands in reverse.
 > fly now at position (0,30).
fly: What must I do next? fly: Shutting down..\n""",output.getvalue())

    @patch ("sys.stdin",StringIO("forward 10\nright\nforward 10\nright\nforward 5\nreplay 2\noff\n"))
    def test_replay_range_then_off(self):

        with patch("sys.stdout",StringIO()) as output:
            robot.get_command_input("fly")

        self.assertEqual("""fly: What must I do next?  > fly moved forward by 10 steps.
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
fly: What must I do next? fly: Shutting down..""",output.getvalue().strip())

    @patch ("sys.stdin",StringIO("forward 10\nright\nforward 10\nright\nforward 5\nreplay 2 silent\noff\n"))
    def test_replay_range_silently(self):

        with patch("sys.stdout",StringIO()) as output:
            robot.get_command_input('fly')
        self.assertEqual("""fly: What must I do next?  > fly moved forward by 10 steps.
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
fly: What must I do next? fly: Shutting down..""",output.getvalue().strip())

if __name__ == "__main__":
    unittest.main()