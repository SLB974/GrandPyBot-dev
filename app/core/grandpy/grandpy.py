from random import choice

from .utils import grandpy_intro
from .utils import grandpy_nickname
from .utils import grandpy_catch_phrase
from .utils import grandpy_catch_wiki
from .utils import grandpy_response
from .utils import grandpy_error
from .utils import grandpy_none
from .utils import grandpy_next


class GrandPy:

    """Manage grandpy interactions"""

    def empty_response(self):
        return choice(grandpy_none)

    def catch_phrase(self):
        return choice(grandpy_catch_phrase)

    def positive_response(self):
        return choice(grandpy_response)

    def error_response(self):
        return choice(grandpy_error)

    def anecdote(self):
        return choice(grandpy_catch_wiki)

    def intro_phrase(self):
        return choice(grandpy_intro) + choice(grandpy_nickname) + choice(grandpy_catch_phrase)

    def next_query(self):
        return choice(grandpy_next)
