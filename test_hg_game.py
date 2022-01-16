# import pytest
# import hg_game
# import numpy as np
# from parameterized import parameterized

# def test_generate_word():
#     game = hg_game.Game()
#     word = game.generate_word(np.random.randint(len(game.words)))
#     assert word is not None
#     assert word.isalpha()

# @parameterized.expand([[1, 'materia'],[2, 'facultad'],[0, 'agiles']])
# def test_risk_word_fail(word_number, input_word):
#     game = hg_game.Game()
#     game.generate_word(word_number)
#     assert game.risk_word(input_word)

# @parameterized.expand([[1, 'facultad'],[2, 'materia'],[0, 'ag1les']])       
# def test_risk_word_ok(word_number, input_word):
#     game = hg_game.Game()
#     game.generate_word(word_number)
#     assert not game.risk_word(input_word)     

# @parameterized.expand([[1, 1, 'lavaplatos'],[2, 1, 'computadora']])  
# def test_select_level(number_word, level, risk_word):
#     game = hg_game.Game()
#     game.generate_word(number_word, level)        
#     assert game.risk_word(risk_word)   

# @parameterized.expand([
#     [0, 2, 'a', [0]],
#     [0, 2, 's', [5]],
#     [2, 1, 'c', [0]],
#     [2, 1, 'r', [9]],
#     [1, 1, 'p', [4]],
#     [1, 1, 's', [9]],
# ])  
# def test_risk_letter_poss_ok(number_word, level, risk_letter, position_letter):
#     game = hg_game.Game()
#     game.generate_word(number_word, level) #agiles, computadora, lavaplatos

#     assert game.risk_letter(risk_letter) == position_letter

# @parameterized.expand([
#     [0, 2, 'h'],
#     [0, 2, 'j'],
#     [2, 1, 'z'],
#     [2, 1, 'i'],
#     [2, 1, 'y'],
#     [1, 1, 'w'],
#     [1, 1, 'd'],
#     [1, 1, 'e']
# ])  
# def test_risk_letter_fail(number_word, level, risk_letter):
#     game = hg_game.Game()
#     game.generate_word(number_word, level) #agiles, computadora, lavaplatos

#     assert not game.risk_letter(risk_letter)

# @parameterized.expand([
#     [0, 2, '@'],
#     [0, 2, '*'],
#     [2, 1, '1'],
#     [2, 1, '-'],
#     [1, 1, '.'],
#     [1, 1, '0']
# ])  
# def test_risk_letter_error(number_word, level, risk_letter):
#     game = hg_game.Game()
#     game.generate_word(number_word, level) #agiles, computadora, lavaplatos

#     with pytest.raises(ValueError):
#         game.risk_letter(risk_letter)

# def test_risk_letter_hits():
#     game = hg_game.Game()
#     game.generate_word(0) #agiles
#     [game.risk_letter(i) for i in ['a','g','l']]
#     assert game.hits == 3

# def test_risk_letter_mistakes():
#     game = hg_game.Game()
#     game.generate_word(0) #agiles
#     [game.risk_letter(i) for i in ['k','p','r']]
#     assert game.mistakes == 3

# def test_risk_letter_hits_and_mistakes():
#     game = hg_game.Game()
#     game.generate_word(0) #agiles
    
#     for i in ['k','p','@','*','-','e','g','l']:
#         try:
#             game.risk_letter(i)
#         except ValueError as ve:
#             pass

#     assert game.mistakes == 2
#     assert game.hits == 3

# def test_win_game_risk_word():
    
#     game = hg_game.Game()
#     for number_word, word, wins in [
#         [1,"materia",1],
#         [0,"agiles",2],
#         [2,"botella",2]
#     ]:
#         game.generate_word(number_word)
#         game.risk_word(word)
#         assert game.win_rounds == wins


# def test_loss_game_risk_word():

#     game = hg_game.Game()
#     for number_word, word, losts in [
#         [1,"materia",0],
#         [0,"agiles",0],
#         [2,"botella",1],
#         [3,"azucar",2],
#     ]:
#         game.generate_word(number_word)
#         game.risk_word(word)
#         assert game.lost_rounds == losts

# def test_win_game_risk_letters():
#     game = hg_game.Game()
#     game.generate_word(0) #agiles
#     [game.risk_letter(i) for i in ['a','g','l','i','e','s']]
#     assert game.win_rounds == 1

# def test_loss_game_risk_letters():
#     game = hg_game.Game()
#     game.generate_word(0) #agiles

#     [game.risk_letter(i) for i in ['k','o','w','q','r']]

#     assert game.lost_rounds == 1