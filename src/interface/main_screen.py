
from tkinter import Button, Label
from src.services.rsa import RSA
from src.interface.services.generic_screen import GenericScreen
from src.interface.theme import input_style, label_style, dropdown_style, title_style, label_response_style
from src.interface.theme import button_convert_style, button_export_style, key_input_style, key_2_input_style
from src.interface.theme import key_2_label_style

class option:
    encrypt: str="Criptografar"
    decrypt: str="Descriptografar"

class mainScreen:
    screen: GenericScreen=GenericScreen(width=900)

    # Genericos (não usados para obter ou manipular dados)
    label: Label
    button: Button
    space: Label

    # Específicos (usados para obter e manipular dados)
    input_string: Label
    input_key_1: Label
    input_key_2: Label
    label_response: Label
    mode: str=''

    rsa_service: RSA

    def encrypt(self) -> None:
        string: str=self.input_string.get()
        key_1: int=self.input_key_1.get()
        key_2: int=self.input_key_2.get()

        if (not string) or (not key_1) or (not key_2):
            pass

        self.rsa_service=RSA(int(key_1), int(key_2))
        (public_keys, private_keys)=self.rsa_service.generate_keys(int(key_1), int(key_2))
        encrypted_message=self.rsa_service.code(string)

        self.label_response.config(text=f"public keys={public_keys}\nprivate key=[{private_keys[2]}] \nmessage: \n{encrypted_message}")

    def convert(self) -> None:
        try: 
            if self.mode == option.decrypt:
                pass
            else:
                self.encrypt()
                
        except Exception as err:
            print(err)
    
    def select_mode(self, event):
        self.mode=event

    def export(self):
        pass

    def run(self) -> None:
        ###########################################################
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
        self.input_string=self.screen.input(row, column, input_style)
        row+=1
        self.screen.space(row, column, height=5)
        row+=1
        
        #####
        # Chaves de criptografia
        text="Key 1"
        self.screen.label(row, column, text, label_style)
        self.input_key_1=self.screen.input(row, column, key_input_style)
        text="Key 2"
        self.screen.label(row, column, text, key_2_label_style)
        self.input_key_2=self.screen.input(row, column, key_2_input_style)
        row+=1
        self.screen.space(row, column, height=10)
        row+=1

        #####
        # Opções
        text="Converter"
        self.button=self.screen.button(row, column, text, self.convert, button_convert_style)
        text="Criptografar"
        options=[option.encrypt, option.decrypt]
        self.screen.dropdown(row, column, text, options, self.select_mode ,dropdown_style)
        text="exportar"
        self.button=self.screen.button(row, column, text, self.export, button_export_style)
        row+=1
        self.screen.space(row, column, height=10)
        row+=1

        #####
        # Resultado
        text=""
        self.label_response=self.screen.label(row, column, text, label_response_style)
        row+=1

        ###########################################################
        # Coluna 1
        row=0
        column+=1
        self.screen.space(row, column)
        row+=1
        
        self.screen.run()