import hg_player

player = hg_player.Player('juan123', 'jj123', 'Juan', 'Alonso')

def test_firstname():
    assert player.first_name == 'Juan'

def test_lastname():
    assert player.last_name == 'Alonso'

def test_username():
    assert player.username == 'juan123'

def test_pass():
    assert player.password == 'jj123'

def test_lifes():
    assert player.lifes == 3

def test_fullname():
    assert player.fullname == 'Juan Alonso'  
