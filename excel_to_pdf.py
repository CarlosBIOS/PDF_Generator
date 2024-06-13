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
    pdf.cell(w=50, h=8, txt=f'Invoice nr. {filepath.strip('Invoices\\.xlsx')[:5]}', align='L', ln=1)
    pdf.set_font(family='Times', style='B', size=16)
    pdf.cell(w=50, h=8, txt=f'Date {filepath.strip('Invoices\\.xlsx')[6:]}', align='L', ln=1)

    all_columns: list = [item.replace('_', ' ').title() for item in list(data.columns)]
    pdf.set_font(family='Times', size=12, style='B')
    pdf.ln()  # Criar parágrafo
    pdf.cell(w=30, h=8, txt=str(all_columns[0]), border=1)
    pdf.cell(w=60, h=8, txt=str(all_columns[1]), border=1)
    pdf.cell(w=40, h=8, txt=str(all_columns[2]), border=1)
    pdf.cell(w=33, h=8, txt=str(all_columns[3]), border=1)
    pdf.cell(w=30, h=8, txt=str(all_columns[4]), border=1, ln=1)
    for index, row in data.iterrows():
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=30, h=8, txt=str(row['product_id']), border=1)
        pdf.cell(w=60, h=8, txt=str(row['product_name']), border=1)
        pdf.cell(w=40, h=8, txt=str(row['amount_purchased']), border=1)
        pdf.cell(w=33, h=8, txt=str(row['price_per_unit']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['total_price']), border=1, ln=1)

    pdf.set_font(family='Times', size=12)
    pdf.cell(w=30, h=8, txt='', border=1)
    pdf.cell(w=60, h=8, txt='', border=1)
    pdf.cell(w=40, h=8, txt='', border=1)
    pdf.cell(w=33, h=8, txt='', border=1)
    pdf.cell(w=30, h=8, txt=str(data['total_price'].sum()), border=1, ln=1)

    pdf.ln()

    pdf.set_font(family='Times', size=15, style='B')
    pdf.cell(w=30, h=8, txt=f'The total price is {data['total_price'].sum()}', ln=1)

    pdf.set_font(family='Times', size=15, style='B')
    pdf.cell(w=30, h=8, txt='PythonHow')
    pdf.image('pythonhow.png', w=10)

    pdf.output(f'PDFs/{filepath[9:].replace('xlsx', 'pdf')}')
