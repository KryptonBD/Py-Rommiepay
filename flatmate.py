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