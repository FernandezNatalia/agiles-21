import sys, os
sys.path.append("/".join(os.path.dirname(__file__).split('/')[:-1]))
from parameterized import parameterized
from src.hg_game import Game
import pytest

@parameterized.expand([
    [0, 2, 'a', [0]],
    [0, 2, 's', [5]],
    [2, 1, 'c', [0]],
    [2, 1, 'r', [9]],
    [1, 1, 'p', [4]],
    [1, 1, 's', [9]],
])  
def test_risk_letter_poss_ok(number_word, level, risk_letter, position_letter):
    game = Game()
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
    game = Game()
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
    game = Game()
    game.generate_word(number_word, level) #agiles, computadora, lavaplatos

    with pytest.raises(ValueError):
        game.risk_letter(risk_letter)

def test_risk_letter_hits():
    game = Game()
    game.generate_word(0) #agiles
    [game.risk_letter(i) for i in ['a','g','l']]
    assert game.get_hits() == 3

def test_risk_letter_mistakes():
    game = Game()
    game.generate_word(0) #agiles
    [game.risk_letter(i) for i in ['k','p','r']]
    assert game.get_mistakes() == 3

def test_risk_letter_hits_and_mistakes():
    game = Game()
    game.generate_word(0) #agiles
    
    for i in ['k','p','@','*','-','e','g','l']:
        try:
            game.risk_letter(i)
        except ValueError as ve:
            pass

    assert game.get_mistakes() == 2
    assert game.get_hits() == 3

def test_won_game_risk_letters():
    game = Game()
    game.generate_word(0) #agiles
    [game.risk_letter(i) for i in ['a','g','l','i','e','s']]
    assert game.get_won_rounds() == 1

def test_loss_game_risk_letters():
    game = Game()
    game.generate_word(0) #agiles

    [game.risk_letter(i) for i in ['k','o','w','q','r']]

    assert game.get_lost_rounds() == 1

def test_consult_correct_letters():
    game = Game()
    game.generate_word(0) #agiles
    [game.risk_letter(i) for i in ['a','g','l','i']]

    assert game.get_correct_letters() == ['a','g','l','i']

def test_consult_incorrect_letters():
    game = Game()
    game.generate_word(0) #agiles
    [game.risk_letter(i) for i in ['a','k','p','i']]

    assert game.get_correct_letters() == ['a','i']
    assert game.get_incorrect_letters() == ['k','p']