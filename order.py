class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        total = sum(product.price for product in self.products)
        return total

    def display_order_info(self):
        print(f"Order ID: {self.order_id}")
        self.customer.display_customer_info()
        print("Products in the order:")
        for product in self.products:
            product.display_product_info()
        print(f"Total: ${self.calculate_total()}")
