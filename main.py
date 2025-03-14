# main.py

from product import Product
from product_manager import ProductManager

# Crearea instanței ProductManager
manager = ProductManager()

# Adăugarea unor produse
manager.add_product(Product("Laptop", 3500, 5))
manager.add_product(Product("Telefon", 2000, 10))

# Afișarea produselor
manager.display_products()

# Afișarea valorii totale
manager.display_total_value()
