from ast import List
import tkinter as tk

from src.interface.services.utils import Colors, TextAlignment
from src.interface.services.style import Style
from src.interface.theme import space_style

class GenericScreen():
    root=None
    width: int=0
    height: int=0
    title: str=""
    default_style: Style=Style()
    background_color: str

    def __init__(
            self, 
            width: int=1200, 
            height: int=500,
            title: str="rsa code / decode",
            bg: str=Colors.SILVER_LIGHT
            ) -> None:
        self.width=width
        self.height=height
        self.title=title
        self.root=tk.Tk()
        self.root.title(self.title)
        self.root.geometry(f"{self.width}x{self.height}")
        self.background_color=bg
        self.root.config(bg=self.background_color)

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
    
    def generic_select(event) -> None:
        print(event)

    def input(self, row: int, column: int, style: Style=default_style) -> tk.Entry:
        entry=tk.Entry(self.root)
        entry.grid(
            row=row,
            column=column,
            padx=style.pad_x,
            pady=style.pad_y,
            columnspan=style.column_span,
            sticky=style.component_alignmet
        )
        entry.config(
            font=style.font,
            borderwidth=style.border,
            bg=style.bg,
            fg=style.fg,
            width=style.width*style.column_span,
        )
        return entry

    def button(self, row: int, column: int, text: str="click", command: callable=generic_click, style: Style=default_style) -> tk.Button:
        button=tk.Button(self.root, text=text, command=command)
        button.grid(
            row=row, 
            column=column, 
            padx=style.pad_x, 
            pady=style.pad_y,
            stick=style.component_alignmet,
            columnspan=style.column_span
        )
        button.config(
            font=style.font,
            borderwidth=style.border,
            bg=style.bg,
            fg=style.fg,
            width=style.width*style.column_span,
            height=style.height,
            anchor=style.text_alignment
        )

        return button
    
    def label(self, row: int, column: int, text: str="label", style: Style=default_style) -> tk.Label:
        label=tk.Label(self.root, text=text)
        label.grid(
            row=row, 
            column=column, 
            padx=style.pad_x, 
            pady=style.pad_y,
            columnspan=style.column_span,
            sticky=style.component_alignmet
        )
        label.config(
            font=style.font,
            borderwidth=style.border,
            bg=style.bg,
            fg=style.fg,
            width=style.width*style.column_span,
            height=style.height,
            anchor=style.text_alignment,
            justify=style.text_justify,
            wraplength=850 # Tamanho total da janela
        )

        return label
    
    def space(self, row: int, column: int, height: int=space_style.height) -> tk.Label:
        '''
            Usado como um limitador do tamanho de cada coluna
            para manter o mesmo espaço mesmo que os componentes 
            da coluna sejam menores
        '''

        space=tk.Label(self.root, text="")
        space.grid(
            row=row, 
            column=column, 
            padx=space_style.pad_x, 
            pady=space_style.pad_y
        )
        space.config(
            font=space_style.font,
            bg=self.background_color,
            width=space_style.width,
            height=height
        )

        return space
    
    def dropdown(self, row: int, column: int, text: str="Converter", options: List=['1', '2'], command: callable=generic_select, style: Style=default_style) -> tk.Button:
        selected_option=tk.StringVar(value=text)
        dropdown=tk.OptionMenu(self.root, selected_option, *options, command=command)
        dropdown.grid(
            padx=style.pad_x, 
            pady=style.pad_y,
            row=row, 
            column=column,
            sticky=style.component_alignmet,
            columnspan=style.column_span
        )
        dropdown.configure(
            font=style.font,
            borderwidth=style.border,
            bg=style.bg,
            fg=style.fg,
            width=style.width*style.column_span,
            height=style.height,
            anchor=style.text_alignment
        )

        return selected_option

    def text(self, row: int, column: int, text: str="label", style: Style=default_style) -> tk.Label:
        text=tk.Label(self.root, text=text)
        text.grid(
            row=row, 
            column=column, 
            padx=style.pad_x, 
            pady=style.pad_y,
            columnspan=style.column_span,
            sticky=style.component_alignmet
        )
        text.config(
            font=style.font,
            borderwidth=style.border,
            bg=style.bg,
            fg=style.fg,
            width=style.width*style.column_span,
            height=style.height,
            anchor=style.text_alignment,
            justify=style.text_justify,
            wraplength=850 # Tamanho total da janela
        )

        return text