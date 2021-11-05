import pytest
from app.core.parser.parser import Parser


question = "Bonjour GrandPy, tu connais la tour eiffel ?"


@pytest.fixture
def parser():
    return Parser(question)


def test_constructor():
    p = Parser(question)
    assert isinstance(p, Parser)
    assert p.user_query == question


def test_clean_string(parser):
    assert parser.clean_string() == ["tour", "eiffel"]
