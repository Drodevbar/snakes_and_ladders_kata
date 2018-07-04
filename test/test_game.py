import unittest

from game import SnakesLadders


class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = SnakesLadders()

    def test_player_one_wins(self):
        self.assertEqual(self.game.play(50, 50), "Player 1 Wins!")

    def test_player_two_wins(self):
        self.game.play(1, 2)
        self.assertEqual(self.game.play(50, 50), "Player 2 Wins!")

    def test_game_over_after_player_one_wins(self):
        self.assertEqual(self.game.play(50, 50), "Player 1 Wins!")
        self.assertEqual(self.game.play(1, 1), "Game over!")

    def test_ladder_square(self):
        self.assertTrue("square 38" in self.game.play(1, 1))

    def test_snake_square(self):
        self.assertTrue("square 6", self.game.play(10, 6))

    def test_extra_move_when_both_dies_values_are_the_same(self):
        self.assertTrue("Player 1" in self.game.play(1, 1))
        self.assertTrue("Player 1" in self.game.play(1, 1))
        self.assertTrue("Player 1" in self.game.play(5, 6))
        self.assertTrue("Player 2" in self.game.play(1, 2))

    def test_single_game(self):
        self.assertEqual(self.game.play(1, 1), "Player 1 is on square 38")
        self.assertEqual(self.game.play(1, 5), "Player 1 is on square 44")
        self.assertEqual(self.game.play(6, 2), "Player 2 is on square 31")
        self.assertEqual(self.game.play(1, 1), "Player 1 is on square 25")
        self.assertEqual(self.game.play(6, 6), "Player 1 is on square 37")
        self.assertEqual(self.game.play(3, 5), "Player 1 is on square 45")
        self.assertEqual(self.game.play(1, 3), "Player 2 is on square 35")
        self.assertEqual(self.game.play(3, 3), "Player 1 is on square 67")
        self.assertEqual(self.game.play(2, 2), "Player 1 is on square 91")
        self.assertEqual(self.game.play(6, 5), "Player 1 is on square 98")
        self.assertEqual(self.game.play(1, 5), "Player 2 is on square 41")
        self.assertEqual(self.game.play(1, 1), "Player 1 Wins!")
        self.assertEqual(self.game.play(1, 1), "Game over!")
        self.assertEqual(self.game.play(1, 1), "Game over!")
