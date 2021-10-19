from logging import log
import unittest
import hg_login


class TestHangmanGameLoginPlayer(unittest.TestCase):

    def test_login_firstname_with_number(self):

        with self.assertRaises(ValueError):
            hg_login.Login('juan123', 'jj123', 'Ju1an', 'Alonso')

    def test_login_lastname_with_number(self):

        with self.assertRaises(ValueError):
            hg_login.Login('juan123', 'jj123', 'Juan', 'Al0nso')

    def test_login_max_30(self):

        with self.assertRaises(ValueError):
            hg_login.Login('juan123', 'jj123',
                               'JuanJuanJuanJuanJuanJuanJuanJuan', 'Alonso')

        with self.assertRaises(ValueError):
            hg_login.Login('juan123', 'jj123', 'Juan',
                               'AlonsoAlonsoAlonsoAlonsoAlonsoAlonso')

        with self.assertRaises(ValueError):
            hg_login.Login(
                'juan123juan123juan123juan123juan123', 'jj123', 'Juan', 'Alonso')

    def test_login_min_3(self):

        with self.assertRaises(ValueError):
            hg_login.Login('juan123', 'jj123', 'Ju', 'Alonso')

        with self.assertRaises(ValueError):
            hg_login.Login('juan123', 'jj123', 'Juan', 'AA')

        with self.assertRaises(ValueError):
            hg_login.Login('23', 'jj123', 'Juan', 'Alonso')

    def test_input_null(self):

        with self.assertRaises(ValueError):
            hg_login.Login('', 'jj123', 'Juan', 'Alonso')

        with self.assertRaises(ValueError):
            hg_login.Login('juan123', '', 'Juan', 'Alonso')

        with self.assertRaises(ValueError):
            hg_login.Login('juan123', 'jj123', '', 'Alonso')

        with self.assertRaises(ValueError):
            hg_login.Login('juan123', 'jj123', 'Juan', '')


if __name__ == '__main__':
    unittest.main()
