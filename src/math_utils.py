from typing import List
import sympy

class Prime():
    def is_prime(self, num: int) -> bool:
        return sympy.isprime(num)
    
    def prime_quantitie(self, num: int) -> int:
        return sympy.primepi(num)
    
    def prev_prime(self, num: int) -> int:
        return sympy.prevprime(num)
    
    def next_prime(self, num: int) -> int:
        return sympy.nextprime(num)
    
    def prime_range(self, start: int, end: int) -> List[int]:
        return sympy.primerange(start, end)
    
    def prime(num: int) -> int:
        return sympy.prime(num)

class MultiplicativeInverse():
    def extended_gcd(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = self.extended_gcd(b % a, a)
            return gcd, y - (b // a) * x, x

    def multiplicative_inverse(self, a: int, m: int):
        '''
            d * a ≡ 1 mod(m)
        '''
        gcd, x, y = self.extended_gcd(a, m)
        if gcd != 1:
            raise ValueError("O inverso multiplicativo não existe.")
        else:
            return (x % m + m) % m