from fpdf import FPDF


def create_pdf(header, footer, pages, name, folder):
    path = f"{folder}{'/' + name + '.pdf'}"
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(margin=0, auto=False)
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=header, align="L", ln=1)

    pdf.ln(265)

    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=footer, align="R")

    for i in range(pages - 1):
        pdf.add_page()

        # Set the header
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=header, align="L", ln=1)

        # Set the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=footer, align="R")

    pdf.output(name=path, dest='f')


def create_pdf_line(header, footer, pages, name, folder):
    path = f"{folder}{'/' + name + '.pdf'}"
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(margin=0, auto=False)
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=header, align="L", ln=1)

    for y in range(20, 288, 10):
        pdf.line(10, y, 200, y)

    pdf.ln(265)

    pdf.set_font(family="Times", style="I", size=12)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=footer, align="R")

    for i in range(pages - 1):
        pdf.add_page()

        # Set the header
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=header, align="L", ln=1)

        for y in range(20, 288, 10):
            pdf.line(10, y, 200, y)

        # Set the footer
        pdf.ln(265)
        pdf.set_font(family="Times", style="I", size=12)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=footer, align="R")


    pdf.output(name=path, dest='f')



if __name__ == "__main__":
    create_pdf_line("zion", "sdsdsd", 3, "fffff", "C:/Users/András/Desktop")
