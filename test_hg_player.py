from logging import log
import unittest
import hg_player

class TestHangmanGameLoginPlayer(unittest.TestCase):

    def setUp(self):
        self.player = hg_player.Player('juan123', 'jj123', 'Juan', 'Alonso')

    def test_firstname(self):
        self.assertEqual(self.player.first_name, 'Juan')

    def test_lastname(self):
        self.assertEqual(self.player.last_name, 'Alonso')

    def test_username(self):
        self.assertEqual(self.player.username, 'juan123')

    def test_pass(self):
        self.assertEqual(self.player.password, 'jj123')

    def test_lifes(self):
        self.assertEqual(self.player.lifes, 3)

    def test_fullname(self):
        self.assertEqual(self.player.fullname, 'Juan Alonso')   

if __name__ == '__main__':
    unittest.main()
