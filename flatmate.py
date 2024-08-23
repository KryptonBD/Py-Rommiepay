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

  def pays(self, bill: Bill, flatmates: list[Self]) -> float | int:
    total_days = sum(flatmate.days_in_house for flatmate in flatmates)

    return bill.amount * (self.days_in_house / total_days)