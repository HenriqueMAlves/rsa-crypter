import datetime
import random
from fpdf import FPDF

class Pdf:
    MARGIN=20
    PAGE_WIDTH=210
    PAGE_HEIGHT=297

    def __init__(self) -> None:
        pass

    def file_name(self) -> str:
        prefix="gold" + datetime.datetime.now().strftime("_%Y%m%d%H%M%S_")
        suffix="".join(random.choice("0123456789") for _ in range(4))
        return prefix + suffix + ".pdf"

    def create(self, text):
        pdf=FPDF()

        pdf.set_left_margin(self.MARGIN)
        pdf.set_top_margin(self.MARGIN)
        pdf.set_right_margin(self.MARGIN)
        pdf.add_page()

        usable_width=self.PAGE_WIDTH-(self.MARGIN*2)

        pdf.set_font("Arial", size=12)
        text_width=pdf.w-self.MARGIN*2
        text_height=pdf.font_size

        x_centered=self.MARGIN+(usable_width-text_width)/2
        y_centered=self.MARGIN

        pdf.set_xy(x_centered, y_centered)
        pdf.multi_cell(usable_width, text_height, text, align='L')

        name=self.file_name()
        pdf.output(name)
