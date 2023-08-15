from src.rsa import RSA

service = RSA(17, 23)

message = "morte ao miojo"
print("+ original message: ", message)

coded = service.code(message)
print("+ message coded: ", coded)

decoded = service.decode(coded)
print("+ message decoded: ", decoded)