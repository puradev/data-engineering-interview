import pytest 
from hello_there import obiwan

@pytest.fixture
def jedi_master():
    new_jedi = obiwan()
    return new_jedi

def test_hello_there_returns_str_greeting(jedi_master):
    message = jedi_master.get_text()
    assert message == "general kenobi, best get after it"