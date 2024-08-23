from fpdf import FPDF
from flatmate import Bill, FlatMate


class PdfReport:
  '''
  Creates an invoice about the bill
  '''

  def __init__(self, filename):
    self.filename = filename

  def generate(self, flatmates: list[FlatMate], bill: Bill):
    pdf = FPDF(unit='pt')
    pdf.add_page()

    # Title
    pdf.set_font(family='Times', size=24, style='B')
    pdf.cell(w=0, h=80, txt='RoomiePay', align='C', ln=1)

    # Period Label
    pdf.set_font_size(20)
    pdf.cell(w=100, h=40, txt='Period')
    pdf.cell(w=0, h=40, align='R', txt=bill.period, ln=1)

    pdf.set_font(family='Times', size=16)

    for flatmate in flatmates:
      flatmate_bill = round(flatmate.pays(bill, flatmates), 2)

      print(f'{flatmate.name} pays: {flatmate_bill}')

      pdf.cell(w=100, h=40, txt=flatmate.name)
      pdf.cell(w=150, h=40, txt=str(flatmate_bill), ln=1)

    # Output
    pdf.output(f'{self.filename}.pdf')