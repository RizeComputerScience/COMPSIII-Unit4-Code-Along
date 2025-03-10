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
    # Call the `__init__` method in the child class using either `Product`. Set the `name`, `price`, and `sku` properties.
    def __init__(self, name, price, sku, size, color):
        Product.__init__(self, name, price, sku)
        # Set the `size` and `color` to the values that are passed into the constructor.
        self.size = size
        self.color = color
    # Create a `clothing_info` method that returns information about the object.
    def clothing_info(self):
        return f"{self.name} (SKU: {self.sku}) - ${self.price:.2f} - Size: {self.size}, Color: {self.color}"

class ElectronicsProduct(Product):
    # Call the `__init__` method in the child class using `super()` to show you can do either! Set the `name`, `price`, and `sku` properties.
    def __init__(self, name, price, sku, warranty_months):
        super().__init__(name, price, sku)
        # Set the `warranty_months` to the value that are passed into the constructor. 
        self.warranty_months = warranty_months
    
    # Create a method called `electronics_info` that takes the object as an argument. It should return a string.
    def electronics_info(self):
        return f"{self.name} (SKU: {self.sku}) - ${self.price:.2f} - Warranty: {self.warranty_months} months"
    
    # Create a method called `under_warranty` that takes the object and `months` as an argument. If the number of months passed in is less than the `warranty_months`, then return `True`. Otherwise, return `False`.
    def under_warranty(self, months):
        if self.warranty_months > months:
            return True
        else:
            return False