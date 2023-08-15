import tkinter as tk

class GenericScreen():
    root = None
    width: int = 0
    height: int = 0
    title: str = ""

    def __init__(
            self, 
            width: int = 1200, 
            height: int = 500,
            title: str = "rsa code / decode"
            ) -> None:
        self.width = width
        self.height = height
        self.title = title
        self.root = tk.Tk()
        self.root.title(self.title)
        self.root.geometry(f"{self.width}x{self.height}")

    def run(self) -> None:
        '''
            Executa a tela com todos os componentes
            **deve ser utilizado após posicionar todos os componentes
        '''
        self.root.mainloop()

    def resize(self, width_resize: bool = True, height_resize: bool = True) -> None:
        '''
            Habilita / Desabilita o redimensionmento da janela
        '''
        self.root.resizable(width_resize, height_resize)
    
    def generic_click() -> None:
        '''
            função padrão de click dos botões
        '''
        print("clicked")

    def input(self) -> tk.Entry:
        return tk.Entry(self.root).grid(row=0, column=0, padx=10, pady=10)

    def button(self, text: str = "click", command: callable = generic_click) -> tk.Button:
        return tk.Button(self.root, text=text, command=command).grid(row=1, column=0, padx=10, pady=10)
    
    def label(self, text: str = "label") ->tk.Label:
        return tk.Label(self.root, text=text).grid(row=2, column=0, padx=10, pady=10)