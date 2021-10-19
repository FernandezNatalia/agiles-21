from logging import log
import unittest
import hg_game
import numpy as np

class TestHangmanGameGame(unittest.TestCase):

    def test_generate_word(self):
        game = hg_game.Game()
        word = game.generate_word(np.random.randint(len(game.words)))

        self.assertIsNotNone(word)
        self.assertTrue(word.isalpha())

    def test_risk_word_fail(self):
        game = hg_game.Game()

        game.generate_word(1)
        self.assertTrue(game.risk_word('materia'))

        game.generate_word(2)
        self.assertTrue(game.risk_word('facultad'))
        
        game.generate_word(0)
        self.assertTrue(game.risk_word('agiles'))
        
    def test_risk_word_ok(self):
        game = hg_game.Game()
        game.generate_word(1)

        self.assertFalse(game.risk_word('agiles'))        

    def test_select_level(self):
        game = hg_game.Game()
        game.generate_word(1, 1)        
        self.assertTrue(game.risk_word('lavaplatos'))

        game2 = hg_game.Game()
        game2.generate_word(2, 1)        
        self.assertTrue(game2.risk_word('computadora'))        


if __name__ == '__main__':
    unittest.main()
