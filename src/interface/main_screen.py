
from tkinter import Button, Entry, Label
from src.interface.services.generic_screen import GenericScreen
from src.interface.theme import button_style, input_style, label_style, dropdown_style


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
        self.space=self.screen.space(row=0, column=0)
        self.input=self.screen.input(row=1, column=0, style=input_style)
        self.button=self.screen.button(row=2, column=0, command=self.button_click, style=button_style)
        self.label=self.screen.label(row=3, column=0, style=label_style)

        options = ["Opção 1", "Opção 2", "Opção 3", "Opção 4"]
        self.screen.dropdown(row=4, column=0, options=options, style=dropdown_style)
        
        self.screen.run()