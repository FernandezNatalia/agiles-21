import hg_game
import numpy as np
from parameterized import parameterized

def test_generate_word():
    game = hg_game.Game()
    word = game.generate_word(np.random.randint(len(game.words)))
    assert word is not None
    assert word.isalpha()

@parameterized.expand([[1, 'materia'],[2, 'facultad'],[0, 'agiles']])
def test_risk_word_fail(word_number, input_word):
    game = hg_game.Game()
    game.generate_word(word_number)
    assert game.risk_word(input_word)

@parameterized.expand([[1, 'facultad'],[2, 'materia'],[0, 'ag1les']])       
def test_risk_word_ok(word_number, input_word):
    game = hg_game.Game()
    game.generate_word(word_number)
    assert not game.risk_word(input_word)     

@parameterized.expand([[1, 1, 'lavaplatos'],[2, 1, 'computadora']])  
def test_select_level(number_word, level, risk_word):
    game = hg_game.Game()
    game.generate_word(number_word, level)        
    assert game.risk_word(risk_word)   


