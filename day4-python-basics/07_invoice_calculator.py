customer_name = input("Enter customer name: ")
item_name = input("Enter item name: ")
price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))

subtotal = price * quantity
tax = subtotal * 0.18
total = subtotal + tax

print("\n--- Invoice ---")
print("Customer:", customer_name)
print("Item:", item_name)
print("Price:", price)
print("Quantity:", quantity)
print("Subtotal:", subtotal)
print("GST (18%):", tax)
print("Total:", total)
