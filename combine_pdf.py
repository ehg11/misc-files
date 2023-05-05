from pypdf import PdfWriter
from os import listdir
from os.path import isfile, join

merger = PdfWriter()
pdf_dir = 'merging_pdfs'

pdf_files = sorted(
    [join(pdf_dir, f) for f in listdir('merging_pdfs') if isfile(join(pdf_dir, f))]
)

for pdf in pdf_files:
    merger.append(pdf)

merger.write('merged_pdf.pdf')
merger.close()




