# from src.services.rsa import RSA

# service=RSA(17, 23)

# message="morte ao miojo"
# print("+ original message: ", message)

# coded=service.code(message)
# print("+ message coded: ", coded)

# decoded=service.decode(coded)
# print("+ message decoded: ", decoded)

from src.interface.main_screen import mainScreen


screen1=mainScreen()
screen1.run()