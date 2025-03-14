# product_manager.py

from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        for product in self.products:
            product.display_product_info()

    def display_total_value(self):
        total = sum(product.price * product.quantity for product in self.products)
        print(f"Total Inventory Value: {total}")

    def remove_product(self, product_name):
        self.products = [product for product in self.products if product.name != product_name]