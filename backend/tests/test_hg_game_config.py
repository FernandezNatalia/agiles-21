import sys, os
sys.path.append("/".join(os.path.dirname(__file__).split('/')[:-1]))
from parameterized import parameterized
import pytest
from src.hg_game import Game

@parameterized.expand([[1, 1, 'lavaplatos'],[2, 1, 'computadora']])  
def test_select_level(number_word, level, risk_word):
    game = Game()
    game.generate_word(number_word, level)        
    assert game.risk_word(risk_word)

def test_select_level_error():
    game = Game()        

    with pytest.raises(ValueError):
        game.generate_word(1, '*') 

def test_config_opportunities():
    game = Game()

    game.set_max_mistakes(10)
    assert game.get_max_mistakes() == 10

    with pytest.raises(ValueError):
        game.set_max_mistakes('*')