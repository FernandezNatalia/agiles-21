import pytest
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

@parameterized.expand([
    [0, 2, 'a', [0]],
    [0, 2, 's', [5]],
    [2, 1, 'c', [0]],
    [2, 1, 'r', [9]],
    [1, 1, 'p', [4]],
    [1, 1, 's', [9]],
])  
def test_risk_letter_poss_ok(number_word, level, risk_letter, position_letter):
    game = hg_game.Game()
    game.generate_word(number_word, level) #agiles, computadora, lavaplatos

    assert game.risk_letter(risk_letter) == position_letter

@parameterized.expand([
    [0, 2, 'h'],
    [0, 2, 'j'],
    [2, 1, 'z'],
    [2, 1, 'i'],
    [2, 1, 'y'],
    [1, 1, 'w'],
    [1, 1, 'd'],
    [1, 1, 'e']
])  
def test_risk_letter_fail(number_word, level, risk_letter):
    game = hg_game.Game()
    game.generate_word(number_word, level) #agiles, computadora, lavaplatos

    assert not game.risk_letter(risk_letter)

@parameterized.expand([
    [0, 2, '@'],
    [0, 2, '*'],
    [2, 1, '1'],
    [2, 1, '-'],
    [1, 1, '.'],
    [1, 1, '0']
])  
def test_risk_letter_error(number_word, level, risk_letter):
    game = hg_game.Game()
    game.generate_word(number_word, level) #agiles, computadora, lavaplatos

    with pytest.raises(ValueError):
        game.risk_letter(risk_letter)


