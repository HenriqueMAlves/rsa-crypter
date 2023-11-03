import base64


class Base64Convertion():
    def __init__(self) -> None:
        pass

    def encode(self, data: []) -> str:
        try:
            data_list_str = list(map(str, data))
            data_str = ','.join(data_list_str).encode('utf-8')

            return base64.b64encode(data_str).decode('utf-8')
        except Exception as e:
            print(e)

    def decode(self, data: str) -> list:
        try:
            data_str=base64.b64decode(data.encode('utf-8')).decode('utf-8')
            data_list_str=data_str.split(',')

            return list(map(int, data_list_str))
        except Exception as e:
            print(e)