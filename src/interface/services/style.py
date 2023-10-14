from src.interface.services.utils import ComponentAlignment, Colors, TextAlignment, TextJustify


class Style:
    pad_x: int
    pad_y: int
    bg: str
    fg: str
    font: (str, int, str)
    width: int
    height: int
    border: int
    text_alignment: str
    text_justify: str
    component_alignmet: str
    column_span: int

    def __init__(self) -> None:
        self.set_padding()
        self.set_area()
        self.set_text_alignment()
        self.set_text_justify()
        self.set_component_alignmet()
        self.set_column_span()
        
    def set_padding(self, pad_x: int=10, pad_y: int=10) -> None:
        self.pad_x=pad_x
        self.pad_y=pad_y

    def set_color(self, bg: str, fg: str=Colors.BLACK) -> None:
        self.bg=bg
        self.fg=fg if fg else self.fg

    def set_font(self, name: str, size: int, style: str) -> None:
        self.font=(name, size, style)
    
    def set_area(self, width: int=10, height: int=1) -> None:
        self.width=width if width else self.width
        self.height=height if height else self.height
    
    def set_border(self, width: int) -> None:
        self.border=width

    def set_text_alignment(self, alignment: str=TextAlignment.LEFT) -> None:
        self.text_alignment=alignment

    def set_text_justify(self, justify: str=TextJustify.LEFT) -> None:
        self.text_justify=justify

    def set_component_alignmet(self, alignment: str=ComponentAlignment.CENTER) -> None:
        self.component_alignmet=alignment
    
    def set_column_span(self, columns: int=1) -> None:
        self.column_span=columns