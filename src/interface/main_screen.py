
from tkinter import Button, Entry, Label
from src.interface.services.utils import FontStyles
from src.interface.services.generic_screen import GenericScreen
from src.interface.theme import input_style, label_style, dropdown_style, title_style, label_response_style
from src.interface.theme import button_convert_style, button_export_style, key_input_style, key_2_input_style
from src.interface.theme import key_2_label_style


class mainScreen:
    screen: GenericScreen=GenericScreen(width=900)

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
        
        #####
        # Título
        self.screen.space(row, column)
        row+=1
        text="TITLE"
        self.screen.label(row, column, text, title_style)
        row+=1
        self.screen.space(row, column, height=10)
        row+=1

        #####
        # String de entrada
        text="Entre com a string a ser criptografada: "
        self.screen.label(row, column, text, label_style)
        row+=1
        self.input=self.screen.input(row, column, input_style)
        row+=1
        self.screen.space(row, column, height=5)
        row+=1
        
        #####
        # Chaves de criptografia
        text="Key 1"
        self.screen.label(row, column, text, label_style)
        self.input=self.screen.input(row, column, key_input_style)
        text="Key 2"
        self.screen.label(row, column, text, key_2_label_style)
        self.input=self.screen.input(row, column, key_2_input_style)
        row+=1
        self.screen.space(row, column, height=10)
        row+=1

        #####
        # Opções
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

        #####
        # Resultado
        text=""
        self.screen.label(row, column, text, label_response_style)
        row+=1

        row=0
        column+=1
        self.screen.space(row, column)
        row+=1
        
        self.screen.run()