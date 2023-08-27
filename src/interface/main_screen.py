
from tkinter import Entry
from src.interface.services.generic_screen import GenericScreen
from src.interface.theme import button_style, input_style, label_style


class mainScreen:
    screen: GenericScreen=GenericScreen(width=800)

    input: Entry
    label: any
    button: any

    def button_click(self) -> None:
        text=self.input.get()
        self.label.config(text=text)

    def run(self) -> None:
        self.input=self.screen.input(row=0, column=0, style=input_style)
        self.label=self.screen.label(row=2, column=0, style=label_style)
        self.button=self.screen.button(row=1, column=0, command=self.button_click, style=button_style)

        self.screen.run()