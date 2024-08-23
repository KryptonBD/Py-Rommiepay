from typing import Self

class Bill:
  '''
  Contains the data for a bill
  amount and period of the bill
  '''

  def __init__(self, amount: int, period: str):
    self.amount = amount
    self.period = period


class FlatMate:
  '''
  Creates a flatmate person class and pays a share of the bill
  '''

  def __init__(self, name: str, days_in_house: int):
    self.name = name
    self.days_in_house = days_in_house

  def pays(self, bill: Bill, other_flat_mate: Self) -> float | int:
    total_days = self.days_in_house + other_flat_mate.days_in_house

    return bill.amount * (self.days_in_house / total_days)

class PdfReport:
  '''
  Creates an invoice about the bill
  '''

  def __init__(self, filename):
    self.filename = filename

  def generate(self, fm1: FlatMate, fm2: FlatMate, bill: Bill):
    pass


bill = Bill(amount=480, period='08/24')

bruce = FlatMate(name='Bruce', days_in_house=21)
oliver = FlatMate(name='Oliver', days_in_house=26)

print(bruce.pays(bill, oliver))
