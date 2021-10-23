from logging import log
import unittest
import hg_login
from parameterized import parameterized

class TestHangmanGameLoginPlayer(unittest.TestCase):

    def test_login_firstname_with_number(self):

        with self.assertRaises(ValueError):
            hg_login.Login('juan123', 'jj123', 'Ju1an', 'Alonso')

    def test_login_lastname_with_number(self):

        with self.assertRaises(ValueError):
            hg_login.Login('juan123', 'jj123', 'Juan', 'Al0nso')

    @parameterized.expand([
        ['juan123', 'jj123','juan'*6, 'Alonso'],
        ['juan123', 'jj123','Juan', 'Alonso'*5],
        ['juan123'*5, 'jj123','Juan', 'Alonso']
    ])
    def test_login_max_30(self, user, password, name, lastname):
        with self.assertRaises(ValueError):
            hg_login.Login(user, password, name, lastname)

    @parameterized.expand([
        ['juan123', 'jj123','Ju', 'Alonso'],
        ['juan123', 'jj123','Juan', 'AA'],
        ['JA', 'jj123','Juan', 'Alonso']
    ])
    def test_login_min_3(self, user, password, name, lastname):

        with self.assertRaises(ValueError):
            hg_login.Login(user, password, name, lastname)

    @parameterized.expand([
        ['', 'jj123','juan', 'Alonso'],
        ['juan123', '','Juan', 'Alonso'],
        ['juan123', 'jj123','', 'Alonso'],
        ['juan123', 'jj123','Juan', ''],
        ['juan123', 'jj123','', ''],
        ['juan123', '','', ''],
        ['', '','', '']
    ])
    def test_input_null(self, user, password, name, lastname):

        with self.assertRaises(ValueError):
            hg_login.Login(user, password, name, lastname)


if __name__ == '__main__':
    unittest.main()
