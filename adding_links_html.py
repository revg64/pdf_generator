from fpdf import FPDF

pdf=FPDF()

#first page
pdf.add_page()
pdf.set_font("helvetica",size=20)

#creting a link

pdf.write(5,"what's next ")#height #text #this is a matter in the page
pdf.set_font("helvetica", size=20,style="U") #underling text
link1=pdf.add_link(page=2)#after clicking link it is redirected to page 2 in the same pdf
pdf.write(5,"click here",link=link1) #this is the link in the page

#secound page
pdf.add_page()
#adding an image
#after clicking image it is redirected to google
pdf.image("logo.png",10,10,50,0,"","https://www.google.com")#name #X #Y #width #height #type #link

#writing html
pdf.set_left_margin(60)
#pdf.write_html("<b>This is a text</b>") #single line of html
#multi line html
pdf.write_html("""  You can add any html code here <b> This is a bold text </b>
               <h1>This is a heading</h1>
               <a href="https://www.google.com">Click here to go to google </a>
               """)


pdf.output("link.pdf")