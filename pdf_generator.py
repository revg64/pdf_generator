from fpdf import FPDF


#inheriting
class PDF(FPDF):
    #method overriding
    def header(self):
        #adding a logo
        self.image("logo.png",10,8,33)#X #Y #width


pdf1=PDF() #creating an object

pdf1.add_page()#adding a page
pdf1.set_font("helvetica","B",16)#font family #font style(BOLD)  #font size  #setting font of the page

#adding a cell to the page
pdf1.cell(40,10,"Hello world")#width #height #text

#creating an output
pdf1.output("sample.pdf")#path

#adding a header

