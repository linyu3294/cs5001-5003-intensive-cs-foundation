'''
    CS5001
    Spring 2019
    Sample code -- writing unittests for coffee using the TestCase class
'''

from coffee import Coffee
import unittest

class TestCoffee(unittest.TestCase):
    def test_init(self):
        coffee = Coffee("PSL")

        self.assertEqual(coffee.name, "PSL")
        self.assertAlmostEqual(coffee.price, 2.49)
        self.assertTrue(coffee.is_hot)
        self.assertTrue(coffee.is_caff)

    def test_add_on(self):
        coffee = Coffee("Black Coffee")

        coffee.add_on('shot')
        self.assertAlmostEqual(coffee.price, 3.48)

        coffee.add_on('flavor')
        self.assertAlmostEqual(coffee.price, 3.98)

        coffee.add_on('whatever')
        self.assertAlmostEqual(coffee.price, 3.98)

def main():
    unittest.main(verbosity = 3)

main()
        
