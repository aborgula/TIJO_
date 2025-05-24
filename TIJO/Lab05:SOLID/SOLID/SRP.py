# Naruszona zasada SRP

class Order:
    def __init__(self, id, items, customer):
        self.id = id
        self.items = items
        self.customer = customer

class OrderProcessor:
    def __init__(self, orderValidator, orderSave, orderConfirmator):
        self.ordervalidator = orderValidator
        self.ordersave = orderSave
        self.orderconfirmator = orderConfirmator

    def process_order(self, order):
        self.ordervalidator.validate(order)
        self.ordersave.save_order(order)
        self.orderconfirmator.send_confirmation_email(order)


class OrderValidator:
    def validate(self, order):
        self.order= order
        print("Wysylanie zamowienia.")

class OrderSave:
    def save_order(self, order):
        self.order = order
        print("Zapisywanie zamowienia do bazy danych.")

class SendConfirmator:
    def send_confirmation_email(self, order):
        self.order = order
        print("Wysylanie e-maila potwierdzajacego.")


order = Order("123", ["Produkt A", "Produkt B"], "Jan Kowalski")
validator = OrderValidator()
saver = OrderSave()
confirmator = SendConfirmator()
processor = OrderProcessor(validator, saver, confirmator)
processor.process_order(order)