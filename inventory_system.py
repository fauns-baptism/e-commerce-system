class InventorySystem:
    def __init__(self):
        self.products = []
        self.orders = []

    def add_product(self, product):
        self.products.append(product)

    def create_order(self, order_id, customer, product_ids):
        order = Order(order_id, customer)
        for product_id in product_ids:
            product = self.find_product_by_id(product_id)
            if product:
                order.add_product(product)
        self.orders.append(order)

    def display_inventory(self):
        print("Current Inventory:")
        for product in self.products:
            product.display_product_info()

    def display_orders(self):
        print("Order History:")
        for order in self.orders:
            order.display_order_info()

    def find_product_by_id(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None
