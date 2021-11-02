class Game:
    words = ["vaca", "pato", "perro", "mate", "hola"]
    hits = 0
    mistakes = 0
    win_rounds = 0
    lost_rounds = 0
    total_letters = 0
    correct_letters = 0
    max_mistakes = 5

    def generate_word(self, point, level=2):      

        if level == 1:
            Game.words = ["ornitorrinco", "lavaplatos", "computadora", "aceitunas", "resaltadores"]            

        if level == 2:
            Game.words = ["agiles", "materia", "facultad", "mejora", "discord"]

        self.word = Game.words[point]

        self.total_letters = len(self.word)    
        return self.word

    def risk_word(self, word):
        if word == self.word:
            self.win_rounds += 1
            return True
        else:
            self.lost_rounds += 1
            return False

    def risk_letter(self, letter):
        if not letter.isalpha() or not letter:
            raise ValueError('The character must be a letter')
        try:
            poss_letters = []
            for pos, char in enumerate(self.word):
                if(char == letter):
                    poss_letters.append(pos)
                    self.hits += 1

            if not poss_letters:
                self.mistakes += 1
                if self.max_mistakes <= self.mistakes:
                    self.lost_rounds += 1
            
            self.correct_letters += len(poss_letters)

            if self.correct_letters == self.total_letters:
                self.win_rounds += 1

            return poss_letters
        except ValueError as ve:            
            return False
