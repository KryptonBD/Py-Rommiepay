from flatmate import Bill, FlatMate
from report import PdfReport

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
