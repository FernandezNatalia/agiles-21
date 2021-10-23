import hg_login
from parameterized import parameterized
import pytest

def test_login_firstname_with_number():

    with pytest.raises(ValueError):
        hg_login.Login('juan123', 'jj123', 'Ju1an', 'Alonso')

def test_login_lastname_with_number():

    with pytest.raises(ValueError):
        hg_login.Login('juan123', 'jj123', 'Juan', 'Al0nso')

@parameterized.expand([
    ['juan123', 'jj123','juan'*6, 'Alonso'],
    ['juan123', 'jj123','Juan', 'Alonso'*5],
    ['juan123'*5, 'jj123','Juan', 'Alonso']
])
def test_login_max_30(user, password, name, lastname):
    with pytest.raises(ValueError):
        hg_login.Login(user, password, name, lastname)

@parameterized.expand([
    ['juan123', 'jj123','Ju', 'Alonso'],
    ['juan123', 'jj123','Juan', 'AA'],
    ['JA', 'jj123','Juan', 'Alonso']
])
def test_login_min_3(user, password, name, lastname):

    with pytest.raises(ValueError):
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
def test_input_null(user, password, name, lastname):

    with pytest.raises(ValueError):
        hg_login.Login(user, password, name, lastname)

