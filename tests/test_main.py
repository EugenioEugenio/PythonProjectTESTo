import unittest


class Test(unittest.TestCase):

    def test_split(self):
        s='hello world'
        self.assertEqual(s.split(' '), ['hello','world'])
