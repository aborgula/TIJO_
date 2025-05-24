import unittest
from bankomat import InsufficientFundsException, InvalidPinException, ATM

class ATMTestCase(unittest.TestCase):
    def test_check_balance_wrong_pin(self):
        # arrange
        pin = 1111
        konto = ATM()

        # assert
        with self.assertRaises(ValueError):
            konto.check_balance(pin)

    def test_check_balance_right_pin(self):
        #arrange
        pin = 1234
        konto = ATM()

        # act and asert
        self.assertEqual(konto.check_balance(pin), 0)

    def test_deposit_wrong_pin(self):
        #arrange
        pin = 1111
        konto = ATM()

        #assert
        with self.assertRaises(ValueError):
            konto.deposit(pin, 200)

    def test_deposit_proper_pin(self):
        #arrange
        pin = 1234
        konto = ATM()

        #assert
        self.assertEqual(konto.deposit(pin, 200), 200)

    def test_withdraw_wrong_pin(self):
        #arrange
        pin = 1111
        konto = ATM()

        #assert
        with self.assertRaises(InvalidPinException):
            konto.withdraw(pin, 200)

    def test_withraw_insufficient_balance(self):
        #arrange
        konto = ATM()
        pin = 1234

        #assert
        with self.assertRaises(InsufficientFundsException):
            konto.withdraw(pin, 200)

    def test_withdraw(self):
        #arrange
        pin = 1234
        konto = ATM()
        konto.deposit(pin, 200)

        #assert
        self.assertEqual(konto.withdraw(pin, 200), 0)

if __name__ == "__main__":
    unittest.main()
