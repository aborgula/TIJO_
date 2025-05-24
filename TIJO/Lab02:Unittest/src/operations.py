class ShoppingCard:

    def __init__(self):
        self.products = {}
        self.discount = 0

    def add_product(self, product_name: str, price: int, quantity: int) -> bool:
        if price < 0 or quantity < 0 or product_name in self.products:
            return False
        else:
            self.products[product_name] = {"price": price, "quantity": quantity}
        return True

    def remove_product(self, product_name: str) -> bool:
        if product_name in self.products:
            del self.products[product_name]
            return True
        return False

    def update_quantity(self, product_name: str, new_quantity: int) -> bool:
        if product_name in self.products and new_quantity >= 0:
            self.products[product_name]["quantity"] = new_quantity
            return True
        return False

    def get_products(self):
        return list(self.products.keys())


    def count_products(self) -> int:
        return sum(item["quantity"] for item in self.products.values())

    def get_total_price(self) -> int:
        return sum(item["price"] * item["quantity"] for item in  self.products.values())

    def apply_discount_code(self, discount_code: str) -> bool:
        valid_discounts = {"SAVE10": 10, "SAVE20": 20}
        if discount_code in valid_discounts:
            self.discount = valid_discounts[discount_code]
            return True
        return False


    def checkout(self) -> bool:
        if self.products:
            self.products.clear()
            self.discount = 0
            return True
        return False


#zrobic kombinacje funkcje o nazwie co robie np usuniecie zwiekszenie dodanie i czy sie zgadza cena