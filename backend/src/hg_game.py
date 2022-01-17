class Game:

    def __init__(self):
        self._words = ["vaca", "pato", "perro", "mate", "hola"]
        self._hits = 0
        self._mistakes = 0
        self._won_rounds = 0
        self._lost_rounds = 0
        self._total_letters = 0
        self._count_correct_letters = 0
        self._max_mistakes = 5
        self._correct_letters = []
        self._incorrect_letters = []

    def get_words(self):
        return self._words

    def get_hits(self):
        return self._hits

    def get_mistakes(self):
        return self._mistakes

    def get_won_rounds(self):
        return self._won_rounds

    def get_lost_rounds(self):
        return self._lost_rounds

    def get_total_letter(self):
        return self._total_letters

    def get_count_correct_letters(self):
        return self._count_correct_letters

    def get_max_mistakes(self):
        return self._max_mistakes
    
    def get_correct_letters(self):
        return self._correct_letters

    def get_incorrect_letters(self):
        return self._incorrect_letters

    def set_max_mistakes(self, max_mistakes):
        if not int(max_mistakes) or not max_mistakes:
            raise ValueError('The number of mistakes must be a number')    

        self._max_mistakes = max_mistakes

    def generate_word(self, point, level=2):      
        if not int(level) or not level:
            raise ValueError('The level must be a number')  

        if level == 1:
            Game._words = ["ornitorrinco", "lavaplatos", "computadora", "aceitunas", "resaltadores"]            

        if level == 2:
            Game._words = ["agiles", "materia", "facultad", "mejora", "discord"]

        self._word = Game._words[point]

        self._total_letters = len(self._word)    
        return self._word

    def risk_word(self, word):
        if word == self._word:
            self._won_rounds += 1
            return True
        else:
            self._lost_rounds += 1
            return False

    def risk_letter(self, letter):
        if not letter.isalpha() or not letter:
            raise ValueError('The character must be a letter')
        try:
            poss_letters = []
            for pos, char in enumerate(self._word):
                if(char == letter):
                    poss_letters.append(pos)
                    self._hits += 1                    

            if not poss_letters:
                self._mistakes += 1
                self._incorrect_letters.append(letter)
                if self._max_mistakes <= self._mistakes:
                    self._lost_rounds += 1                
            else:
                self._correct_letters.append(letter)
            
            self._count_correct_letters += len(poss_letters)            
            
            if self._count_correct_letters == self._total_letters:
                self._won_rounds += 1

            return poss_letters
        except ValueError as ve:            
            return False
