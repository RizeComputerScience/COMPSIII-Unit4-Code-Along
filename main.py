from app import Product, ShoppingCart, ClothingProduct, ElectronicsProduct

def main():
    # Code from last week's code along
    laptop = Product("MacBook Pro", 1299.99, "123456")
    headphones = Product("AirPods", 159.99, "789012")

    cart = ShoppingCart()
    cart.add_items(laptop)
    cart.add_items(headphones, 2)
    # End code from last week's code along


# Call the main() function. See bash.sh for directions on how to run in your terminal.
main()