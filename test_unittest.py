import inc_dec    # The code to test
import unittest   # The test framework

class Test_TestIncrementDecrement(unittest.TestCase):
    #Este es cierto y deber ser correcto
    def test_true(self):
        self.assertEqual(inc_dec.check(51000), 40800)

    #Este es falso no y debe pasar el test
    def test_false(self):
        self.assertEqual(inc_dec.check(10000), 9500)

if __name__ == '__main__':
    unittest.main()