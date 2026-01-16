from fpdf import FPDF
from PIL import Image, ImageOps

def main():
    name = input("Name: ")
    
	# Instantiation of inherited class
    img = crop("./shirtificate.png")
    pdf = PDF()
    pdf.add_page()
    pdf.image(img, 15, 60)
    pdf.set_font("helvetica", size=24)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, 200, f"{name} took CS50", align="C", center=True)
    pdf.output("new-tuto2.pdf")

class PDF(FPDF):
    def header(self):
        self.set_auto_page_break(margin=0, auto=0)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", style="B", size=40)
        self.cell(30, 40, "CS50 Shirtificate", align="C", center=True)
        # Performing a line break:
        self.ln(5)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:


def crop(img):
    shirt = Image.open(img)
    resized = ImageOps.fit(
        shirt,
        size=(500, 500),
        method=Image.Resampling.BICUBIC,
        bleed=0.0,
        centering=(0.5, 0.5),
    )
    return resized


if __name__ == "__main__":
    main()