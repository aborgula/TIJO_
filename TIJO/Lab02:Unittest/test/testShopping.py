from src.operations import ShoppingCard
import unittest

class testShopping(unittest.TestCase):

    def setUp(self):
        print("set up")
        self.calc = ShoppingCard()

    def test_add_products(self):

        #arrange
        product_name = "bed"
        price = 200
        quantity = 3
        expected = True

        #act
        result = self.calc.add_product(product_name, price, quantity)

        #assert
        assert expected == result, f"expected {expected}, got {result}"

    def test_below_zero_price(self):

        #arrange
        product_name = "flower"
        price = -3
        quantity = 2
        expected = False

        #act
        result = self.calc.add_product(product_name, price, quantity)

        #assert
        assert expected == result, f"expected {expected}, got {result}"

    def test_remove_none_product(self):

        #arrange
        product_name = "flower"
        expected = False

        #act
        result = self.calc.remove_product(product_name)

        #assert
        assert expected == result, f"expected {expected}, got {result}"



    def test_remove_product(self):

        #arrange
        self.calc.add_product("bed", 300, 1)
        product_name = "bed"
        expected = True

        #act
        result = self.calc.remove_product(product_name)

        #assert
        assert expected == result, f"expected {expected}, got {result}"


    def test_update_quantity(self):

        #arrange
        self.calc.update_quantity("flower", 4)
        expected = False

        #act
        result = self.calc.update_quantity("flower", 4)

        #assert
        assert expected == result, f"expected {expected}, got {result}"


    def test_update_quantity(self):

        #arrange
        self.calc.add_product("wardrobe", 300, 1)
        expected = True

        #act
        result = self.calc.update_quantity("wardrobe", 4)

        #assert
        assert expected == result, f"expected {expected}, got {result}"

    def test_remove_product(self):

        #arrange
        expected = False
        
        #act
        result = self.calc.remove_product("armchair")
        
        #assert
        assert expected == result, f"expected {expected}, got {result}"
    
    def test_update_quantity(self):
        
        #arrange
        self.calc.add_product("picture", 20, 2)
        expected = True
        
        #act
        result = self.calc.update_quantity("picture", 5)
        
        #assert
        assert expected == result, "expected {}, got {}".format(expected, result)
        
    def test_get_products_empty(self):
        
        #arrange
        expected = []
        
        #act
        result = self.calc.get_products()
        
        #assert
        assert expected == result, "expected {}, got {}".format(expected, result)
        
    def test_count_products(self):
        
        #arrange
        self.calc.add_product("bath", 500, 1)
        self.calc.add_product("bed", 300, 3)
        expected = 4
        
        #act
        result = self.calc.count_products()
        
        #assert
        assert expected == result, f"expected {expected}, got {result}"
        
    def test_total_price(self):
        
        #arrange
        self.calc.add_product("bath", 500, 1)
        self.calc.add_product("bed", 300, 3)
        expected = 1400
        
        #act
        result = self.calc.get_total_price()
        
        #assert
        assert result == expected, "expected {}, got {}".format(expected, result) 
        
    def test_apply_discount_code(self):
        
        #arrange
        expected = False
        
        #act
        result = self.calc.apply_discount_code("SAVE30")
        
        #assert
        assert expected == result, "expected {}, got {}".format(expected, result)
        
    def test_overall(self):
        
        #arrange
        self.calc.add_product("flower", 50, 3)
        self.calc.update_quantity("flower", 6)
        self.calc.add_product("bin", 20, 2)
        self.calc.remove_product("bin")

        expected1 = 6
        expected2 = 300
        expected3 = ["flower"]
        
        #act
        result1 = self.calc.count_products()
        result2 = self.calc.get_total_price()
        result3 = self.calc.get_products()
        
        #assert
        assert expected1 == result1 and expected2 == result2 and expected3 == result3, "error here"
        
    
    def tearDown(self):
        print("tear down")
        self.calc = None



if __name__ == "__main__":
    unittest.main()