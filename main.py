# from src.services.rsa import RSA

# service = RSA(17, 23)

# message = "morte ao miojo"
# print("+ original message: ", message)

# coded = service.code(message)
# print("+ message coded: ", coded)

# decoded = service.decode(coded)
# print("+ message decoded: ", decoded)

from src.interface.generic_screen import GenericScreen


screen: GenericScreen = GenericScreen(width=800)

input = screen.input(row=0, column=0)
button = screen.button(row=1, column=0)
label = screen.label(row=2, column=0)

screen.run()