import base64


class Base64Convertion():
    def __init__(self) -> None:
        pass

    def encode(self, data: []) -> str:
        try:
            formated_data=[]
            for num in data:
                hexadecimal=hex(num)[2:]
                hexadecimal=hexadecimal.zfill(6)
                formated_data.append(int(hexadecimal[:2], 16))
                formated_data.append(int(hexadecimal[2:4], 16))
                formated_data.append(int(hexadecimal[4:6], 16))
                
            return base64.b64encode(bytes(formated_data)).decode('utf-8')
        except Exception as e:
            print(e)

    def decode(self, data: str) -> list:
        try:
            data_list=list(base64.b64decode(data))

            formated_data=[]
            for index in range(0, len(data_list), 3):
                hex_data=f'{hex(data_list[index])[2:]}' + \
                         f'{hex(data_list[index+1])[2:]}' + \
                         f'{hex(data_list[index+2])[2:]}'
                formated_data.append(int(hex_data, 16))

            return formated_data
        except Exception as e:
            print(e)