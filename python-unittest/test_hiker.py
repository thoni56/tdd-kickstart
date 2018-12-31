import hiker
import unittest

class HikerTest(unittest.TestCase):

    def test_life_the_universe_and_everything(self):
        '''a simple example to start you off'''
        douglas = hiker.Hiker()
        self.assertEqual(douglas.answer(), 42)

if __name__ == "__main__":
    unittest.main()
