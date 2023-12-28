class Customer:
    def __init__(self, customer_id, customer_name, email):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.email = email

    def display_customer_info(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Email: {self.email}")
