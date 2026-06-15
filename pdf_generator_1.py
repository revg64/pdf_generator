from fpdf import FPDF

#adding a header
#inheriting
class PDF(FPDF):
    #method overriding
    def header(self):
        #adding a logo
        self.image("logo.png",10,8,33)#X #Y #width
        self.set_font("helvetica","B",16)#font family #font style(BOLD)  #font size  #setting font of the page
        #empty cell
        self.cell(80)#width
        
        #adding a cell to the page
        self.cell(40,10,"Hello",border=1,align="C")#width #height #text #border #align to center

        #adding a line break
        self.ln(40)#height

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica","I",16)#font family #font style(BOLD)  #font size  #setting font of the page
        self.cell(0,10,f"Page{self.page_no()}/{{nb}}",align="C")#width #height #nb total no of pages


pdf1=PDF() #creating an object

pdf1.add_page()#adding a page
#writing multiple lines

pdf1.set_font("helvetica","B",16)#font family #font style(BOLD)  #font size  #setting font of the page
for i in range(0,40):
    pdf1.cell(0,10,f"Printing the line number {i}",new_x="LMARGIN",new_y="NEXT")#width(gets max width)  #height #X #Y




#creating an output
pdf1.output("sample.pdf")#path

