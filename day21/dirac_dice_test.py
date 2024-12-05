import unittest

from day21.dirac_dice import Player, DeterministicDie, play_game


class DiracDiceTest(unittest.TestCase):

    def test_play_game(self):
        player1 = Player(4)
        player2 = Player(8)
        die = DeterministicDie()
        result = play_game(player1, player2, die)
        self.assertEqual(739785, result)

    def test_part_1_solution(self):
        player1 = Player(7)
        player2 = Player(8)
        die = DeterministicDie()
        result = play_game(player1, player2, die)
        self.assertEqual(556206, result)
