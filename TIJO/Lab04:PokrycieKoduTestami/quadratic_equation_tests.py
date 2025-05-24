import unittest
from quadratic_equation import QuadraticEquation

class QuadraticEquationTestCase(unittest.TestCase):
    def test_raise_when_a_is_zero(self):
        #arrange
        a,b,c = 0, 2, 4

        # act & assert
        self.assertRaises(ValueError, QuadraticEquation, a, b, c)

    def test_two_solutions(self):
        # arrange
        a, b, c = 1, -3, 2
        eq = QuadraticEquation(a, b, c)
        # act
        result = eq.solve()
        # assert
        self.assertEqual(result, (2.0, 1.0))

    def test_delta_equals_zero(self):
        #arrange
        a,b,c = 1,2,1
        eq = QuadraticEquation(a,b,c)

        #act
        result = eq.solve()

        #assert
        self.assertEqual(result, -1.0)


if __name__ == '__main__':
    unittest.main()