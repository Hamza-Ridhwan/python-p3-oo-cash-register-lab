class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.last_transaction = 0.0

    def add_item(self, title, price, quantity=1):
        """Add item(s) to the cash register."""
        self.total += price * quantity
        self.last_transaction = price * quantity
        self.items.extend([title] * quantity)

    def apply_discount(self):
        """Apply a discount to the total if available."""
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """Void the last transaction and update the total."""
        self.total -= self.last_transaction
        self.last_transaction = 0.0
        if self.total < 0:
            self.total = 0.0
