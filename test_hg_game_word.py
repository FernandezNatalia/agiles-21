from parameterized import parameterized
import hg_game
import numpy as np

def test_generate_word():
    game = hg_game.Game()
    word = game.generate_word(np.random.randint(len(game.get_words())))
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

def test_won_game_risk_word():
    
    game = hg_game.Game()
    for number_word, word, wons in [
        [1,"materia",1],
        [0,"agiles",2],
        [2,"botella",2]
    ]:
        game.generate_word(number_word)
        game.risk_word(word)
        assert game.get_won_rounds() == wons


def test_loss_game_risk_word():

    game = hg_game.Game()
    for number_word, word, losts in [
        [1,"materia",0],
        [0,"agiles",0],
        [2,"botella",1],
        [3,"azucar",2],
    ]:
        game.generate_word(number_word)
        game.risk_word(word)
        assert game.get_lost_rounds() == losts