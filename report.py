from fpdf import FPDF
from flatmate import Bill, FlatMate


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