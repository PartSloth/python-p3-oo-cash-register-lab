#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []

  def add_item(self, title, price, quantity=1):
    self.last_transaction = (price * quantity)
    i = 0
    while i < quantity:
      self.items.append(title)
      i += 1
    self.total += price * quantity

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else: 
      discount_decimal = (100 - self.discount)/100
      self.total = int(self.total * discount_decimal)
      print(f'After the discount, the total comes to ${self.total}.')

  def void_last_transaction(self):
    self.total -= self.last_transaction
