import numpy as np

class Game:
    words = ["vaca", "pato", "perro", "mate", "hola"]
    def generate_word(self, point, level=2):      

        if level == 1:
            Game.words = ["ornitorrinco", "lavaplatos", "computadora", "aceitunas", "resaltadores"]            

        if level == 2:
            Game.words = ["agiles", "materia", "facultad", "mejora", "discord"]

        self.word = Game.words[point]            
        return self.word

    def risk_word(self, word):
        if word == self.word:
            return True
        return False