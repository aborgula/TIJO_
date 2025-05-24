import unittest


# Implementacja klasy Calc
class Calc:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b


# Testy dla klasy Calc
class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_add(self):
        # Arrange
        a, b = 3, 5
        expected_result = 8

        # Act
        result = self.calc.add(a, b)

        # Assert
        self.assertEqual(result, expected_result)

    def test_subtract(self):
        # Arrange
        a, b = 10, 4
        expected_result = 6

        # Act
        result = self.calc.subtract(a, b)

        # Assert
        self.assertEqual(result, expected_result)

    def test_multiply(self):
        # Arrange
        a, b = 3, 7
        expected_result = 21

        # Act
        result = self.calc.multiply(a, b)

        # Assert
        self.assertEqual(result, expected_result)


# Implementacja klasy ShoppingCart
class ShoppingCart:
    def __init__(self):
        self.products = {}

    def add_product(self, product_name: str, price: int, quantity: int) -> bool:
        if price < 0 or quantity <= 0:
            return False
        if product_name in self.products:
            self.products[product_name]['quantity'] += quantity
        else:
            self.products[product_name] = {'price': price, 'quantity': quantity}
        return True

    def remove_product(self, product_name: str) -> bool:
        return self.products.pop(product_name, None) is not None

    def update_quantity(self, product_name: str, new_quantity: int) -> bool:
        if new_quantity <= 0 or product_name not in self.products:
            return False
        self.products[product_name]['quantity'] = new_quantity
        return True

    def get_products(self):
        return list(self.products.keys())

    def count_products(self) -> int:
        return sum(item['quantity'] for item in self.products.values())

    def get_total_price(self) -> int:
        return sum(item['price'] * item['quantity'] for item in self.products.values())

    def apply_discount_code(self, discount_code: str) -> bool:
        if discount_code == "DISCOUNT10":
            for product in self.products.values():
                product['price'] *= 0.9
            return True
        return False

    def checkout(self) -> bool:
        if self.products:
            self.products.clear()
            return True
        return False


# Testy dla klasy ShoppingCart
class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_product(self):
        # Arrange
        product_name = "Laptop"
        price = 3000
        quantity = 1

        # Act
        result = self.cart.add_product(product_name, price, quantity)

        # Assert
        self.assertTrue(result)
        self.assertIn(product_name, self.cart.get_products())

    def test_remove_product(self):
        # Arrange
        self.cart.add_product("Mouse", 150, 1)

        # Act
        result = self.cart.remove_product("Mouse")

        # Assert
        self.assertTrue(result)
        self.assertNotIn("Mouse", self.cart.get_products())

    def test_update_quantity(self):
        # Arrange
        self.cart.add_product("Keyboard", 200, 1)

        # Act
        result = self.cart.update_quantity("Keyboard", 3)

        # Assert
        self.assertTrue(result)
        self.assertEqual(self.cart.count_products(), 3)

    def test_get_total_price(self):
        # Arrange
        self.cart.add_product("Monitor", 500, 2)
        self.cart.add_product("Speaker", 300, 1)
        expected_total = 1300

        # Act
        result = self.cart.get_total_price()

        # Assert
        self.assertEqual(result, expected_total)

    def test_apply_discount_code(self):
        # Arrange
        self.cart.add_product("Tablet", 1000, 1)
        expected_price_after_discount = 900

        # Act
        result = self.cart.apply_discount_code("DISCOUNT10")

        # Assert
        self.assertTrue(result)
        self.assertEqual(self.cart.get_total_price(), expected_price_after_discount)

    def test_checkout(self):
        # Arrange
        self.cart.add_product("Headphones", 250, 1)

        # Act
        result = self.cart.checkout()

        # Assert
        self.assertTrue(result)
        self.assertEqual(self.cart.count_products(), 0)


if __name__ == "__main__":
    unittest.main()
