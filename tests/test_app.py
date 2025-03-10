from app import Product, ShoppingCart, ClothingProduct, ElectronicsProduct

# Test that you can create a ClothingProduct that is a child of Product
def test_clothing_product():
    shirt = ClothingProduct("T-Shirt", 9.99, "345678", "M", "Red")
    assert isinstance(shirt, ClothingProduct)
    assert isinstance(shirt, Product)

# Test that you can create a ClothingsProduct with the correct attributes
def test_clothing_product_attributes():
    shirt = ClothingProduct("T-Shirt", 9.99, "345678", "M", "Red")
    assert shirt.name == "T-Shirt"
    assert shirt.price == 9.99
    assert shirt.sku == "345678"
    assert shirt.size == "M"
    assert shirt.color == "Red"

# Test that ClothingProduct has a method called clothing_info
def test_clothing_info():
    shirt = ClothingProduct("T-Shirt", 9.99, "345678", "M", "Red")
    assert shirt.clothing_info() == "T-Shirt (SKU: 345678) - $9.99 - Size: M, Color: Red"

# Test that you can create a ElectronicsProduct that is a child of Product
def test_electronics_product():
    phone = ElectronicsProduct("iPhone 12", 799.99, "567890", 12)
    assert isinstance(phone, ElectronicsProduct)
    assert isinstance(phone, Product)

# Test that you can create a ElectronicsProduct with the correct attributes
def test_electronics_product_attributes():
    phone = ElectronicsProduct("iPhone 12", 799.99, "567890", 12)
    assert phone.name == "iPhone 12"
    assert phone.price == 799.99
    assert phone.sku == "567890"
    assert phone.warranty_months == 12

# Test that ElectronicsProduct has a method called electronics_info
def test_electronics_info():
    phone = ElectronicsProduct("iPhone 12", 799.99, "567890", 12)
    assert phone.electronics_info() == "iPhone 12 (SKU: 567890) - $799.99 - Warranty: 12 months"

# Test ElectronicsProduct under_warranty method
def test_under_warranty():
    phone = ElectronicsProduct("iPhone 12", 799.99, "567890", 12)
    tv = ElectronicsProduct("Samsung TV", 999.99, "345678", 24)
    assert phone.under_warranty(6) == True
    assert tv.under_warranty(25) == False