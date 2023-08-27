

class Style:
    pad_x: int
    pad_y: int
    bg: str
    fg: str
    font: (str, int, str)
    width: int
    height: int
    border: int

    def __init__(self) -> None:
        self.set_padding()
        
    def set_padding(self, pad_x: int=10, pad_y: int=10) -> None:
        self.pad_x=pad_x
        self.pad_y=pad_y

    def set_color(self, bg: str, fg: str=None) -> None:
        self.bg=bg
        self.fg=fg if fg else self.fg

    def set_font(self, name: str, size: int, style: str) -> None:
        self.font=(name, size, style)
    
    def set_area(self, width: int=None, height: int=None) -> None:
        self.width=width if width else self.width
        self.height=height if height else self.height
    
    def set_border(self, width: int) -> None:
        self.border=width