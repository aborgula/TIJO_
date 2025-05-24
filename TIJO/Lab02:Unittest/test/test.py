import unittest

class Calc:
    def add(self, a,b):
        return a+b

    def divide(self,a,b):
        if b ==0:
            raise ValueError("nie mozna dzielic przez zeo")
        return a/b

class TestCalc(unittest.TestCase):

    def setUp(self):
        print("* setUp()")
        self.calc = Calc()

    def test_add(self):
        print(" test_add()")
        result = self.calc.add(3,2)
        self.assertEqual(result,5)

    def test_divide_by_zero(self):
        print("test_divide_by_zero()")
        with self.assertRaises(ValueError):
            self.calc.divide(10,0)

    def tearDown(self):
        print("* tearDown()")
        self.calc = None


if __name__ == "__main__":
    unittest.main()