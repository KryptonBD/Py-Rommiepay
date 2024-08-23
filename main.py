from flatmate import Bill, FlatMate
from report import PdfReport

# Taking inputs
amount = input('Please Enter Total amount: ')
period = input('Please Enter the period, e.g. April 2024: ')
flat_size = input('How many people live in the flat? ')


bill = Bill(amount=float(amount), period=period)
print(f'{amount} for {period}')

flatmates = []

for _ in range(0, int(flat_size)):
  flatmate_name = input('Please enter the flatemate name: ')
  flatmate_duration = input(f'Please enter the duration {flatmate_name} stayed: ')

  flatmate = FlatMate(name=flatmate_name, days_in_house=int(flatmate_duration))
  print(f'{flatmate.name} stayed for {flatmate.days_in_house}')
  
  flatmates.append(flatmate)


print('Genrating Report....')

report = PdfReport(period)
report.generate(flatmates=flatmates, bill=bill)
