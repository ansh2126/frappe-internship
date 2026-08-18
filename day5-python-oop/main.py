from catalogue import Product, Catalogue

catalogue = Catalogue()

try:
    product1 = Product("Laptop", 50000, 5)
    product2 = Product("Keyboard", 1200, 10)

    catalogue.add_product(product1)
    catalogue.add_product(product2)

    print("\n--- Product Catalogue ---")
    catalogue.show_products()

except ValueError as error:
    print("Error:", error)
