import base64


class Base64Convertion():
    def __init__(self) -> None:
        pass

    def encode(self, data: []) -> str:
        try:
            return base64.b64encode(bytes(data)).decode('utf-8')
        except Exception as e:
            print(e)

    def decode(self, data: str) -> list:
        try:
            return list(base64.b64decode(data))
        except Exception as e:
            print(e)