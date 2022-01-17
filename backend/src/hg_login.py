from src.hg_player import Player

class Login:

    def __init__(self, *args):
        if self.login(args):
            self.player = Player(args)

    def login(self, *args):
        username, _, first_name, last_name = args
        if not(args):
            raise ValueError('One or more fields are null')

        if not first_name.isalpha():
            raise ValueError('The first name must contain only letters')

        if not last_name.isalpha():
            raise ValueError('The last name must contain only letters')

        self.validate_len_min3_max30(first_name)
        self.validate_len_min3_max30(last_name)
        self.validate_len_min3_max30(username)

        return True

    def validate_len_min3_max30(self, string):
        if len(string) < 3 or len(string) > 30:
            raise ValueError(
                'The username must contain at least 3 letters and a maximum of 30')