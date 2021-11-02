import pytest
from app.core.grandpy.grandpy import GrandPy
from app.core.grandpy.utils import grandpy_response, grandpy_none, grandpy_catch_phrase
from app.core.grandpy.utils import grandpy_catch_wiki, grandpy_error, grandpy_next


@pytest.fixture
def grandpy():
    return GrandPy()


def test_constructor():
    g = GrandPy()
    assert isinstance(g, GrandPy)


def test_empty_response(grandpy):
    assert grandpy.empty_response() in grandpy_none


def test_catch_phrase(grandpy):
    assert grandpy.catch_phrase() in grandpy_catch_phrase


def test_error_response(grandpy):
    assert grandpy.error_response() in grandpy_error


def test_anecdote(grandpy):
    assert grandpy.anecdote() in grandpy_catch_wiki


def test_positive_response(grandpy):
    assert grandpy.positive_response() in grandpy_response


def test_next_query(grandpy):
    assert grandpy.next_query() in grandpy_next
