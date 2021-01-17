import unittest
from world import obstacles


class test_my_obstacles(unittest.TestCase):

    def test_position_is_blocked(self):
        obstacles.random_position = [(7, 10)]
        self.assertTrue(obstacles.is_positon_blocked(9, 10))

    def test_position_is_not_blocked(self):
        obstacles.random_position = [(7, 10)]
        self.assertFalse(obstacles.is_positon_blocked(9, 12))

    def test_path_is_blocked_1(self):
        obstacles.random_position = [(1, 11)]
        self.assertEqual(obstacles.is_path_blocked(2, 0, 2, 17), True)

    def test_not_path_is_block_1(self):
        obstacles.random_position = [(1, 11)]
        self.assertEqual(obstacles.is_path_blocked(-1, 7, 10, 1), False)

    def test_path_is_blocked_2(self):
        obstacles.random_position = [(1, 11)]
        self.assertEqual(obstacles.is_path_blocked(-1, 12, 10, 12), True)

    def test_not_path_is_block_2(self):
        obstacles.random_position = [(1, 11)]
        self.assertEqual(obstacles.is_path_blocked(7, 0, 7, 20), False)


if __name__ == "__main__":
    unittest.main()
