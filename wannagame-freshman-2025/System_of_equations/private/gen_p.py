from Crypto.Util.number import getPrime
from sympy import nextprime
import math

def check_scp(n: int) -> bool:
    if n < 0:
        return False
    root = int(math.isqrt(n))  # căn bậc hai nguyên (Python 3.8+)
    return root * root == n

p = getPrime(56)
mode = True
while mode:
    for b in range(2**13):
        t1 = -8*b**4-6*b**2 + 4*p
        t2 = -16*b**4-6*b**2 + 2*p
        if check_scp(t1):
            print(f"Bộ: {p, b, t1, 1}")
            print(f'N = {8*p+4}')
            mode = False
        if check_scp(t2):
            print(f"Bộ: {p, b, t2, 2}")
            print(f'N = {8*p+4}')
            mode = False
    p = nextprime(p)
    print(p)