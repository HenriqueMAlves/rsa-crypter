from typing import List
from src.services.base64 import Base64Convertion
from src.services.math_utils import Prime, MultiplicativeInverse


class RSA():
    # public key=[N, E]       *positions
    __N: int=0
    __E: int=1
    # private key=[P, Q, D]   *positions
    __P: int=0
    __Q: int=1
    __D: int=2
    prime_service: Prime=Prime()
    mi_service: MultiplicativeInverse=MultiplicativeInverse()
    base64_service: Base64Convertion=Base64Convertion()
    private_keys: List[int]=[]
    public_keys: List[int]=[]

    def __init__(self, p=7, q=13) -> None:
        (self.public_keys, self.private_keys)=self.generate_keys(p, q)

    def generate_keys(self, p, q) -> tuple:
        n=p * q
        totiente=(p - 1) * (q - 1)                
        e=self.prime_service.prev_prime(totiente)
        
        # 𝑑 ∗ 𝑒 ≡ 1 mod(𝜑𝑛)
        d=self.mi_service.multiplicative_inverse(e, totiente)

        public_keys=[n, e]
        private_keys=[p, q, d]

        return (public_keys, private_keys)
    
    def code(self, message: str, public_keys: List[int]=None) -> List: 
        (public_keys, private_keys)=self.verify_keys(public_keys, None)
        
        ascii_message=[ord(char) for char in message]
        
        encrypted_message=[]
        for character in ascii_message:
            encrypted_message.append((character ** public_keys[self.__E]) % public_keys[self.__N])

        return self.base64_service.encode(encrypted_message)

    def decode(self, encrypted_base64_message: str, private_keys: List[int]=None, public_keys: List[int]=None) -> str:
        (public_keys, private_keys)=self.verify_keys(public_keys, private_keys)

        encrypted_message=self.base64_service.decode(encrypted_base64_message)

        ascii_message=[]
        for character in encrypted_message:
            ascii_message.append((character ** private_keys[self.__D]) % public_keys[self.__N])

        decoded_message=''.join([chr(value) for value in ascii_message])

        return decoded_message
        
    def verify_keys(self, public: List[int]=None, private: List[int]=None) -> tuple:
        if not public:
            public=self.public_keys
        if not private:
            private=self.private_keys
        
        return (public, private)


        
