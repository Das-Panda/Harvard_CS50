from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'CS50 Shirtificate', 0, 1, 'C')

def create_shirtificate(name):
    pdf = PDF()
    pdf.add_page()

    # Add the shirt image
    pdf.image('shirtificate.png', x=0, y=60, w=210)

    # Add the user's name on top of the shirt
    pdf.set_font('Arial', 'B', 24)
    pdf.set_text_color(255, 255, 255)
    pdf.text(x=55, y=140, txt=name)

    # Save the PDF
    pdf.output('shirtificate.pdf')

if __name__ == "__main__":
    name = input("What's your name? ")
    create_shirtificate(name)