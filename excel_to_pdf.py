from fpdf import FPDF
import pandas as pd
import glob

filepaths = glob.glob('Invoices/*.xlsx')
# ['Invoices\\10001-2023.1.18.xlsx', 'Invoices\\10002-2023.1.18.xlsx', 'Invoices\\10003-2023.1.18.xlsx']

for filepath in filepaths:
    data = pd.read_excel(filepath, sheet_name='Sheet 1')  # Só dá quando instalar openpyxl!!!
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=16)
    pdf.cell(w=50, h=8, txt=f'Invoice nr. {filepath.strip('Invoices\\.xlsx')[:5]}', align='L', ln=1, border=0)
    pdf.set_font(family='Times', style='B', size=16)
    pdf.cell(w=50, h=8, txt=f'Date {filepath.strip('Invoices\\.xlsx')[6:]}', align='L', ln=1, border=0)

    pdf.output(f'PDFs/{filepath[9:].replace('xlsx', 'pdf')}')
