import world.text.world
import unittest
from unittest.mock import patch
from io import StringIO


class test_my_module(unittest.TestCase):

    def test_help_function(self):
        self.assertEqual("""I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]
""", world.text.world.help())

    def test_do_forward_out_of_range(self):
        self.assertEqual(world.text.world.do_forward(
            "fly", 300), (True, 'fly: Sorry, I cannot go outside my safe zone.'))

    def test_do_forward_in_range(self):
        self.assertEqual(world.text.world.do_forward(
            "fly", 199), (True, ' > fly moved forward by 199 steps.'))

    def test_do_back(self):
        self.assertEqual(world.text.world.do_back("fly", 199),
                         (True, ' > fly moved back by 199 steps.'))

    def test_do_right(self):
        self.assertEqual(world.text.world.do_right_turn(
            "fly"), (True, ' > fly turned right.'))

    def test_do_left(self):
        self.assertEqual(world.text.world.do_left_turn(
            "fly"), (True, ' > fly turned left.'))

    def test_is_positon_allowed_true_y_value(self):
        self.assertTrue(world.text.world.is_position_allowed(
            0, 199))

    def test_is_positon_allowed_false_y_value(self):
        self.assertFalse(world.text.world.is_position_allowed(
            0, 300))

    def test_is_positon_allowed_true_x_value(self):
        self.assertTrue(world.text.world.is_position_allowed(
            99, 0))

    def test_is_positon_allowed_false_x_value(self):
        self.assertFalse(world.text.world.is_position_allowed(
            200, 0))


if __name__ == "__main__":
    unittest.main()
