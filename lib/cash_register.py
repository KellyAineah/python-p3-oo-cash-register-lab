#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * self.discount / 100
            self.total -= discount_amount
            return f"After the discount, the total comes to ${self.total:.2f}."
        else:
            return "There is no discount to apply."

    def void_last_transaction(self):
        if self.items:
            last_item_price = self.total - self._price_of_last_transaction()
            self.total -= last_item_price
            self.items.pop()

    def _price_of_last_transaction(self):
        # Assuming the last item added is the last transaction
        last_item_index = -1
        last_item_title = self.items[last_item_index]
        last_item_price = self._price_of_item(last_item_title)
        return last_item_price

    def _price_of_item(self, title):
        # Dummy implementation - replace with actual logic to get price of an item
        return 0  # Placeholder until we implement a proper price lookup

    def reset_register(self):
        self.total = 0
        self.items = []



