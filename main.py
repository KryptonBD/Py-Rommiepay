from typing import Self
from fpdf import FPDF 

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
    pdf = FPDF(unit='pt')
    pdf.add_page()

    # Title
    pdf.set_font(family='Times', size=24, style='B')
    pdf.cell(w=0, h=80, txt='Py Bill Share', align='C', ln=1)

    # Period Label
    pdf.set_font_size(20)
    pdf.cell(w=100, h=40, txt='Period')
    pdf.cell(w=0, h=40, align='R', txt=bill.period, ln=1)

    pdf.set_font(family='Times', size=16)

    # Person 1 bill
    fm1_bill = round(fm1.pays(bill, fm2), 2)
    pdf.cell(w=100, h=40, txt=fm1.name)
    pdf.cell(w=150, h=40, txt=str(fm1_bill), ln=1)

    # Person 2 bill
    fm2_bill = round(fm2.pays(bill, fm1), 2)
    pdf.cell(w=100, h=40, txt=fm2.name)
    pdf.cell(w=150, h=40, txt=str(fm2_bill), ln=1)


    # Output
    pdf.output(f'{self.filename}.pdf')


# Taking inputs
amount = input('Please Enter Total amount: ')
period = input('Please Enter the period, e.g. April 2024: ')

bill = Bill(amount=float(amount), period=period)
print(f'{amount} for {period}')

flat_mate1_name = input('Please Enter the name of first flatmate: ')
flat_mate1_duration = input(f'Please enter the duration {flat_mate1_name} stayed: ')

flat_mate1 = FlatMate(name=flat_mate1_name, days_in_house=float(flat_mate1_duration))
print(f'{flat_mate1.name} stayed for {flat_mate1.days_in_house} days')

flat_mate2_name = input('Please enter the name of second flatmate: ')
flat_mate2_duration = input(f'Please enter the duration {flat_mate2_name} stayed: ')

flat_mate2 = FlatMate(name=flat_mate2_name, days_in_house=float(flat_mate2_duration))
print(f'{flat_mate2.name} stayed for {flat_mate2.days_in_house} days')

print('Genrating Report....')

report = PdfReport(period)
report.generate(flat_mate1, flat_mate2, bill)
