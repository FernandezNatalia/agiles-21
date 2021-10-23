class TestHangmanGameGame(unittest.TestCase):

    def test_generate_word(self):
        game = hg_game.Game()
        word = game.generate_word(1)
        self.assertIsNotNone(word)
        self.assertTrue(word.isalpha())

    @parameterized.expand([[1, 'materia'],[2, 'facultad'],[0, 'agiles']])
    def test_risk_word_fail(self, word_number, input_word):
        game = hg_game.Game()
        game.generate_word(word_number)
        self.assertTrue(game.risk_word(input_word))

    @parameterized.expand([[1, 'facultad'],[2, 'materia'],[0, 'ag1les']])       
    def test_risk_word_ok(self, word_number, input_word):
        game = hg_game.Game()
        game.generate_word(word_number)
        self.assertFalse(game.risk_word(input_word))        

    @parameterized.expand([[1, 1, 'lavaplatos'],[2, 1, 'computadora']])  
    def test_select_level(self, number_word, level, risk_word):
        game = hg_game.Game()
        game.generate_word(number_word, level)        
        self.assertTrue(game.risk_word(risk_word))     


if __name__ == '__main__':
    from logging import log
    import unittest
    import hg_game
    import pytest
    from parameterized import parameterized
    unittest.main()

