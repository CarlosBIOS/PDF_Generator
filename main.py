# O módulo FPDF (Free PDF) é uma biblioteca de código aberto para gerar documentos PDF em Python. É uma portação da
# biblioteca FPDF para PHP, conhecida por sua simplicidade e facilidade de uso. O FPDF oferece uma variedade de recursos
# para criar PDFs ricos em conteúdo, incluindo:
# Formatação de texto: Definir fontes, tamanhos de fonte, estilos de fonte (negrito, itálico, sublinhado), cores de
# texto e espaçamento entre linhas.
# Layout de página: Criar páginas com margens personalizadas, cabeçalhos e rodapés, e controlar a quebra de página.
# Inserção de imagens: Incorporar imagens PNG, JPG e GIF nos seus PDFs, com suporte para transparência e canal alfa.
# Criação de tabelas: Gerar tabelas com bordas, células formatadas e conteúdo multilinha.
# Suporte a Unicode: Embutir fontes TrueType Unicode para gerar texto em vários idiomas.
# Códigos de barras: Incluir códigos de barras I2of5 e code39 nos seus documentos.
# Suporte a HTML: Converter conteúdo HTML básico em elementos PDF usando o módulo html2pdf opcional.
# O FPDF é uma ferramenta leve e versátil para criar PDFs em Python. Não requer nenhuma dependência externa ou
# compilação, tornando-o ideal para projetos de desenvolvimento rápido. O módulo também oferece uma ampla gama de
# exemplos e documentação para facilitar o aprendizado e o uso.

# Se você precisa de recursos mais avançados para criar PDFs complexos, como interatividade ou formulários, pode
# considerar outras bibliotecas PDF como o ReportLab ou o WeasyPrint.
from fpdf import FPDF
import pandas

pdf = FPDF(orientation='P', unit='mm', format='A4')

data = pandas.read_csv('topics.csv')

for index, value in data.iterrows():
    add = 0
    while add != value['Pages']:
        pdf.add_page()

        pdf.set_font(family='Times', style='B', size=24)
        pdf.set_text_color(0, 0, 0)
# w (float): Largura da célula em milímetros. Se w for 0, a célula se estende até a margem direita da página.
# h (float): Altura da célula em milímetros. No exemplo, h=12 define a altura da célula como 12 milímetros.
# txt (str): Texto a ser impresso dentro da célula. No exemplo, txt='Hello There!' define o texto que será exibido
# dentro da célula.
# align (str): Alinhamento do texto dentro da célula. Pode ser: L(esquerda), C(centro), R(direita) e J(justificado)
# ln (int): Indica a quebra de linha após a célula.Pode ser:0(sem quebra de linha), 1(quebra de linha para a próxima
# célula na linha seguinte) e 2 (quebra de linha e inicia uma nova página)
# border (int or str): Define a borda da célula. Pode ser: 0(sem borda) e 1(borda completa)
        pdf.cell(w=0, h=12, txt=value['Topic'], align='L', ln=1, border=0)
        pdf.line(10, 20, 200, 20)
        # pdf.set_font(family='Times', size=10)
        # pdf.cell(w=0, h=12, txt='Hi There!', align='L', ln=1, border=1)
        add += 1

pdf.output('output.pdf')
