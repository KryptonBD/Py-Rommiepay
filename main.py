class Bill:
  '''
  Contains the data for a bill
  amount and period of the bill
  '''

  def __init__(self,amount, period):
    self.amount = amount
    self.period = period


class FlatMate:
  '''
  Creates a flatmate person class and pays a share of the bill
  '''

  def __init__(self, name, days_in_house):
    self.name = name
    self.days_in_house = days_in_house

  def pays(self, bill):
    return bill.amount / 2

class PdfReport:
  '''
  Creates an invoice about the bill
  '''

  def __init__(self, filename):
    self.filename = filename

  def generate(self, f1, fm2, bill):
    pass


bill = Bill(amount=480, period='08/24')

bruce = FlatMate(name='Bruce', days_in_house=21)
oliver = FlatMate(name='Oliver', days_in_house=26)

print(bruce.pays(bill))
