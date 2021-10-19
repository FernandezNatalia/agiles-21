class Player:

    def __init__(self, username, password, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    @property
    def lifes(self):
        return 3

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'
