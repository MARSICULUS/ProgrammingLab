from vero import conversione
from vero import AidaError
import unittest

class TestVero(unittest.TestCase):

    def test_1(self):
        self.assertEqual(10, 10)
        print('fine test1')

    def test_convertitore(self):
        self.assertEqual(conversione('lol'), None)

    def test_convertitore_migliorato(self):
        self.assertEqual(1, 1)
        print('fine test 2')