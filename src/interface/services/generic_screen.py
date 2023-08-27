import tkinter as tk

from src.interface.services.style import Style

class GenericScreen():
    root=None
    width: int=0
    height: int=0
    title: str=""
    default_style: Style=Style()

    def __init__(
            self, 
            width: int=1200, 
            height: int=500,
            title: str="rsa code / decode"
            ) -> None:
        self.width=width
        self.height=height
        self.title=title
        self.root=tk.Tk()
        self.root.title(self.title)
        self.root.geometry(f"{self.width}x{self.height}")

    def run(self) -> None:
        '''
            Executa a tela com todos os componentes
            **deve ser utilizado após posicionar todos os componentes
        '''
        self.root.mainloop()

    def resize(self, width_resize: bool=True, height_resize: bool=True) -> None:
        '''
            Habilita / Desabilita o redimensionmento da janela
        '''
        self.root.resizable(width_resize, height_resize)
    
    def generic_click() -> None:
        '''
            função padrão de click dos botões
        '''
        print("clicked")

    def input(self, row: int, column: int, style: Style=default_style) -> tk.Entry:
        entry=tk.Entry(self.root)
        entry.grid(
            row=row,
            column=column,
            padx=style.pad_x,
            pady=style.pad_y
        )
        entry.config(
            font=style.font,
            borderwidth=style.border,
            bg=style.bg,
            fg=style.fg,
            width=style.width,
        )
        return entry

    def button(self, row: int, column: int, text: str="click", command: callable=generic_click, style: Style=default_style) -> tk.Button:
        button=tk.Button(self.root, text=text, command=command)
        button.grid(
            row=row, 
            column=column, 
            padx=style.pad_x, 
            pady=style.pad_y
        )
        button.config(
            font=style.font,
            borderwidth=style.border,
            bg=style.bg,
            fg=style.fg,
            width=style.width,
            height=style.height
        )

        return button
    
    def label(self, row: int, column: int, text: str="label", style: Style=default_style) -> tk.Label:
        label=tk.Label(self.root, text=text)
        label.grid(
            row=row, 
            column=column, 
            padx=style.pad_x, 
            pady=style.pad_y
        )

        return label