

class Style:
    pad_x: int
    pad_y: int

    def __init__(self) -> None:
        self.set_padding()

    def set_padding(self, pad_x: int = 10, pad_y: int = 10) -> None:
        self.pad_x = pad_x
        self.pad_y = pad_y