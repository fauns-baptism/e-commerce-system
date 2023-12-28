from product import Product
from customer import Customer
from order import Order
from inventory_system import InventorySystem

# Create the inventory system
inventory_system = InventorySystem()

# Add products to the inventory
inventory_system.add_product(Product(1, "Laptop", 999.99))
inventory_system.add_product(Product(2, "Smartphone", 499.99))

# Create customers
customer1 = Customer(101, "Alice", "alice@example.com")
customer2 = Customer(102, "Bob", "bob@example.com")

# Create orders
inventory_system.create_order(201, customer1, [1, 2])
inventory_system.create_order(202, customer2, [2])

# Display the updated inventory and order history
inventory_system.display_inventory()
inventory_system.display_orders()
