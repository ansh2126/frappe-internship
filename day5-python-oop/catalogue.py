class Product:
    def __init__(self, name, price, quantity):
        if price < 0:
            raise ValueError("Price cannot be negative")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self._price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    def display(self):
        return f"{self.name} - ₹{self.price} - Stock: {self.quantity}"


def log_action(func):
    def wrapper(*args, **kwargs):
        print("Action:", func.__name__)
        return func(*args, **kwargs)

    return wrapper


class Catalogue:
    def __init__(self):
        self.products = []

    @log_action
    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        if not self.products:
            raise ValueError("Catalogue is empty")

        for product in self.products:
            print(product.display())
