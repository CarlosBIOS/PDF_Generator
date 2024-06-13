from fpdf import FPDF
import glob

filepaths = glob.glob('TextFiles/*.txt')

for filepath in filepaths:
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    title = filepath.replace('TextFiles\\', '').replace('.txt', '').title()
    pdf.cell(w=50, h=10, txt=f'{title}', align='L', border=0, ln=1)
    pdf.ln()
    pdf.set_font(family='Times', size=12)
    with open(filepath, encoding='utf-8') as file:
        for line in file:
            pdf.multi_cell(w=180, h=8, txt=f'{line.strip()}')

    pdf.output(f'TextFiles/{filepath[9:].replace('txt', 'pdf')}')
