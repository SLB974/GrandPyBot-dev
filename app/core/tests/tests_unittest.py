import unittest

from . import test_grandpy as grandpy
from . import test_parser as parser
from . import test_google as google
from . import test_wiki as wiki
from . import test_fetcher as fetcher

loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTests(loader.loadTestsFromModule(grandpy))
suite.addTests(loader.loadTestsFromModule(parser))
suite.addTests(loader.loadTestsFromModule(google))
suite.addTests(loader.loadTestsFromModule(wiki))
suite.addTests(loader.loadTestsFromModule(fetcher))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
