import unittest
from application.calc import calculator

calc = calculator()

class TestCalc(unittest.TestCase):

    def setUp(self):

        self.calc = calculator()

    
    def tearDown(self):

        pass

    def test_add(self):

        self.assertEqual(self.calc.add(2,2), 4)

        self.assertEqual(self.calc.add(-2,2), 0)
        
        self.assertEqual(self.calc.add(1,-2), -1)
        
        self.assertEqual(self.calc.add(-50,-50), -100)

        with self.assertRaises(TypeError):

            self.calc.add("this is a string",-1)

    def test_subtract(self):
        
        self.assertEqual(self.calc.subtract(10, 5), 5)
        
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        
        self.assertEqual(self.calc.subtract(-1, -1), 0)

        with self.assertRaises(TypeError):

            self.calc.add("this is a string",-1)

    def test_multiply(self):
        
        self.assertEqual(self.calc.multiply(10, 5), 50)
        
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        
        self.assertEqual(self.calc.multiply(-1, -1), 1)

        with self.assertRaises(TypeError):

            calc.add("this is a string",-1)

    def test_divide(self):

        self.assertEqual(self.calc.divide(10, 5), 2)
        
        self.assertEqual(self.calc.divide(-1, 1), -1)
        
        self.assertEqual(self.calc.divide(-1, -1), 1)
        
        self.assertEqual(self.calc.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            
            self.calc.divide(10, 0)

        with self.assertRaises(TypeError):

            self.calc.add("this is a string",-1)

if __name__ == '__main__':

    unittest.main()