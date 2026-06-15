from fpdf import FPDF
from fpdf.fonts import FontFace
import csv

with open("countries.txt",encoding="utf8") as csv_file:
    data=list(csv.reader(csv_file,delimiter=","))
    """
    data is list of items as rows of the csv file
    """
pdf = FPDF()
pdf.set_font("helvetica",size=14)

#creating a table
pdf.add_page()

#all borders and lines will be orange
pdf.set_draw_color(255,0,0)
pdf.set_line_width(0.3)

#fontface is for styling the heading
heading_style=FontFace(emphasis="BOLD",color=255,fill_color=(255,100,0))

#we can pass parameters to style the table to table()
with pdf.table(
    borders_layout="NO_HORIZONTAL_LINES", #removes all the horizontal lines
    cell_fill_color=(224,235,255), # fill every cell with a colour
    col_widths=(42,39,35,42),
    line_height=6, #controles height of each rows
    headings_style=heading_style,
    text_align=("LEFT","CENTER","RIGHT","RIGHT"),
    width=160, #total width of the table (horizontally it occupies 160mm)

) as table1: #creating a pdf table
    for data_row in data: #acsessing every row csv
        #creating a row inside the table
        row1=table1.row()
        #for every single cell in row
        for cell_1 in data_row:
            row1.cell(cell_1)

pdf.output("table.pdf")