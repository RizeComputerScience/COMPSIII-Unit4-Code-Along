# COMPS III: Unit 3 Code Along

## Overview
This unit we'll be continuing to build out our e-commerce store by incorporating inheritance into our system. Last unit we created `Product` and `ShoppingCart` classes. However, there are many different types of products that our store could have that require special information. 

![Inheritance in E-Commerce Store](./E-Store_W2.png)

This unit we'll be adding classes for `ClothingProduct` and `ElectronicProduct` using inheritance. You can use the code you completed last week, but we have included the completed unit 2 code in `app.py`.

## VS Code - app.py has syntax instructions
1. Define a `ClothingProduct` class that is a child of the `Product` class.
2. Call the `__init__` method in the child class using either `Product` or `super()`. Set the `name`, `price`, and `sku` properties.
3. Set the `size` and `color` to the values that are passed into the constructor.
4. Finally, create a `clothing_info` method that returns information about the object in the form `"[NAME] (SKU: [SKU]) - $[PRICE] - Size: [SIZE], Color: [COLOR]""`
5. Run the tests! `test_clothing_product`, `test_clothing_product_attributes`, and `test_clothing_info` tests should now be passing!

## VS Code - main.py has syntax instructions
6. Import the `ClothingProduct` class into the file. The `Product` and `ShoppingCart` class was imported last week.
7. Inside the `main()` function that was created last week, create an instance of the `ClothingProduct` class and `print()` out the object. Show how it inherited the `__str__` method from the `Product` class. 
    - **NOTE**: Polymorphism is covered next week, so we're explicitly not adding `__str__` method this week.
8. Call the `clothing_info()` method to see the information about the items that you created. 
9. Add both items the cart using `add_items`. Print out the new cart info.

## VS Code - app.py has syntax instructions
10. Define a `ElectronicsProduct` class that is a child of the `Product` class.
11. Call the `__init__` method in the child class using either `Product` or `super()`. Set the `name`, `price`, and `sku` properties.
12. Set the `warranty_months` to the value that are passed into the constructor. 
13. Create a method called `electronics_info` that takes the object as an argument. It should return a string in the format `"[NAME] (SKU: [SKU]) - $[PRICE] - Warranty: [WARRANTY_MONTHS] months"`.
14. Run the tests! `test_electronics_product`, `test_electronics_product_attributes`, and `test_electronics_info` should now be passing.
15. Create a method called `under_warranty` that takes the object and `months` as an argument. If the number of months passed in is less than the `warranty_months`, then return `True`. Otherwise, return `False`.
16. Run the tests! `test_under_warranty` should now be passing.

## VS Code - main.py has syntax instructions
17. Import the `ElectronicsProduct` class into the file.
18. Inside the `main()` function, create an instance of the `ElectronicsProduct` class and `print()` out the object. Show how it also inherited the `__str__` method from the `Product` class.
19. Call `electronics_info()` to see the additional information about the object.
20. Call the `under_warranty()` method and print out the resulting boolean.
21. Finally, add both items the cart using `add_items`. Print out the new cart info.