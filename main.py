# main.py

from product import Product
from product_manager import ProductManager
from cart import Cart

# Crearea instanței ProductManager
manager = ProductManager()

# Adăugarea unor produse
manager.add_product(Product("Laptop", 3500, 5))
manager.add_product(Product("Telefon", 2000, 10))

# Afișarea produselor
manager.display_products()

# Afișarea valorii totale
manager.display_total_value()

# Crearea instanței Cart
cart = Cart()

# Adăugarea produselor în coș
cart.add_to_cart(Product("Laptop", 3500, 1))
cart.add_to_cart(Product("Telefon", 2000, 2))

# Afișarea conținutului coșului și valoarea totală
cart.display_cart()
print(f"Total Cart Value: {cart.calculate_total()}")