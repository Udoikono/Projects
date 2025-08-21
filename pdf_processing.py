# import PyPDF2
# with open('recrystallization_of_acetanilide.pdf', 'rb') as file:
#
#   print(len(reader.pages))
#
#   #Define the page to rotate
#   new = reader.pages[0]
#   new.rotate(90)
#   writer = PyPDF2.PdfWriter()
#   writer.add_page(new)
#   with open('tilted.pdf', 'wb') as file1:
#         writer.write(file1)

#
# import PyPDF2
#
# # Path to your PDF file
# pdf_path = 'recrystallization_of_acetanilide.pdf'
#
# # Open the PDF file in read-binary mode
# with open(pdf_path, 'rb') as file:
#     reader = PyPDF2.PdfReader(file)
#
#     # Print total number of pages
#     print(f'Total pages: {len(reader.pages)}\n')
#
#     # Loop through each page and print text
#     for page_num in range(len(reader.pages)):
#         page = reader.pages[page_num]
#         text = page.extract_text()
#         print(f'--- Page {page_num + 1} ---\n{text}\n')



# from pdf2docx import Converter
# import os
# # pdf_file = "recrystallization_of_acetanilide.pdf"
# # docx_file = "recrystallization.docx"
# # converter = Converter(pdf_file, docx_file)
# # converter.convert()
# # converter.close()
#
# pdf_path = './'
# docx_path = './new_document'
#
# os.makedirs(docx_path, exist_ok=True)
#
# for filename in os.listdir(pdf_path):
#     if filename.lower().endswith('.pdf'):
#
#         p_path = os.path.join(pdf_path, filename)
#         p_pathsplit = os.path.splitext(filename)[0]
#         d_path = os.path.join(docx_path, p_pathsplit + '.docx')
#
#         converter = Converter(p_path)
#         converter.convert(d_path)
#
#         converter.close()
#
#     print('Done')
#

# from PyPDF2 import PdfMerger
# from docx2pdf import convert
#
# convert('GENERAL_MOTORS.docx')

#
from PyPDF2 import PdfReader, PdfWriter
input_file = 'recrystallization_of_acetanilide.pdf'
watermark_file = 'signature.pdf'
output_file = 'WM.pdf'

file1 = PdfReader(input_file)
file2 = PdfReader(watermark_file)
watermark_page = file2.pages[0]

writer = PdfWriter()
for page in file1.pages:
    page.merge_page(watermark_page)
    writer.add_page(page)


with open(output_file, 'wb') as output:
    writer.write(output)


print('The file has been watermarked')

# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter
#
# def create_watermark(output="watermark.pdf"):
#     c = canvas.Canvas(output, pagesize=letter)
#
#     # Set transparency — note: this is a trick using PDF blend mode
#     c.setFillAlpha(0.1)  # 0.0 = fully transparent, 1.0 = fully opaque
#
#     # Draw rotated watermark
#     c.setFont("Helvetica-Bold", 30)
#     c.saveState()
#     c.translate(300, 400)
#     c.rotate(45)
#     c.drawCentredString(0, 0, "GENERAL MOTORS, MICHIGAN")
#     c.restoreState()
#     c.save()
#
# create_watermark('Signature.pdf')


