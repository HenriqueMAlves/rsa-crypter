# rsa-crypter
This project aims to be used as an RSA cipher-based encryptor/decryptor. The implementation was done based on information available on the [dcode](https://www.dcode.fr/rsa-cipher) website.

For useful number lookup, you can use the [compoasso](http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php) website.

## Environment
To run the project, you need to have [Python 3.7.2](https://www.python.org/downloads/release/python-372/) or higher. It is also recommended to use [venv](https://docs.python.org/3/library/venv.html) for creating a virtual environment and installing dependencies.

## Installation
>Clone the project:
>```
>git clone https://github.com/HenriqueMAlves/rsa-crypter
>```

>Create a virtual environment:
>```
>python -m venv venv
>```

>Install dependencies:
>```
>pip install -r requirements.txt
>```

>Run project:
>```
>python main.py
>```

>Create an executable:
>```
>pyinstaller --onefile main.py
>```

## Roadmap
- [x] Encrypt data
- [x] Decrypt data
- [x] Tkinter interface
- [x] Data encoding with base64
- [x] Export a report
- [x] Generate an executable
- [ ] Generate error logs
- [ ] Optimize the maximum encryption key range

