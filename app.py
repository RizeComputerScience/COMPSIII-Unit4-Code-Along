# Code from Week 2 code along
class Product:
    def __init__(self, name, price, sku):
        self.name = name
        self.price = price
        self.sku = sku
    
    def __str__(self):
        return f"{self.name} (SKU: {self.sku}) - ${self.price:.2f}"

class ShoppingCart:
    def __init__(self):
        self.items = []

    def __str__(self):
        return f"Shopping Cart with {len(self.items)} items."
    
    def add_items(self, product, quantity=1):
        self.items.append({"product": product, "quantity": quantity})
    
    def get_total(self):
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total
    
    def display_cart(self):
        for item in self.items:
            print(f'{item["product"]} - Quantity: {item["quantity"]}')
        print(f"Total: ${self.get_total():.2f}")

# Create ClothingProduct and ElectronicsProduct classes here
class ClothingProduct(Product):
    pass

class ElectronicsProduct(Product):
    pass