
from tkinter import Button, Entry, Label
from src.interface.services.utils import FontStyles
from src.interface.services.generic_screen import GenericScreen
from src.interface.theme import input_style, label_style, dropdown_style, title_style, label_response_style
from src.interface.theme import button_convert_style, button_export_style

class mainScreen:
    screen: GenericScreen=GenericScreen(width=800)

    input: Entry
    label: Label
    button: Button
    space: Label

    def button_click(self) -> None:
        text=self.input.get()
        self.label.config(text=text)

    def run(self) -> None:

        ###################################################################################################
        # Coluna 0
        column=0
        row=0
        
        self.screen.space(row, column)
        row+=1

        text="TITLE"
        self.screen.label(row, column, text, title_style)
        row+=1

        self.screen.space(row, column, height=20)
        row+=1

        text="Entre com a string a ser criptografada: "
        self.screen.label(row, column, text, label_style)
        row+=1

        self.input=self.screen.input(row, column, input_style)
        row+=1

        self.screen.space(row, column, height=10)
        row+=1
        
        text="Converter"
        self.button=self.screen.button(row, column, text, self.button_click, button_convert_style)
        text="Criptografar"
        options = ["Criptografar", "Descriptografar"]
        self.screen.dropdown(row, column, text, options=options, style=dropdown_style)
        text="exportar"
        self.button=self.screen.button(row, column, text, self.button_click, button_export_style)
        row+=1

        self.screen.space(row, column, height=10)
        row+=1

        text=""
        self.screen.label(row, column, text, label_response_style)
        row+=1

        self.screen.run()