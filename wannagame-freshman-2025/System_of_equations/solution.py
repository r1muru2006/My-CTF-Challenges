from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from tqdm import trange
import hashlib, math

def check_scp(n: int) -> bool:
    if n < 0:
        return False
    root = int(math.isqrt(n))  # căn bậc hai nguyên (Python 3.8+)
    return root * root == n

ans = 23128165544962556
p = (ans - 4) // 8
print("Voi a = 1: ")
a = 1
for b in trange(2**12):
    k = -8*b**4 - 6*b**2+4*p
    if check_scp(k):
        cp = math.isqrt(k)
        c = cp - b
        x, y, z = 4*a*b**2+2, 2*a*(c**2-b**2) - 2, 2*a*b*c + 1
        print(f'Bộ nghiệm: {x, y, z}')
        
print("Voi a = 2: ")
a = 2
for b in trange(2**12):
    k = -16*b**4 - 6*b**2+2*p
    if check_scp(k):
        cp = math.isqrt(k)
        c = cp - b
        x, y, z = 4*a*b**2+2, 2*a*(c**2-b**2) - 2, 2*a*b*c + 1
        print(f'Bộ nghiệm: {x, y, z}')
        
secret = (str(x**10) + str(y**10) + str(z**10)).encode()
key = hashlib.sha256(secret).digest()
iv = b'\x8d\r\x19\xbc\xfd\x84\x13N,\xf85\xdb\xd3\x92i\x93'
ciphertext = b'\xe9\xa2\x8c\x8b\xc3\xb4\x88\xe2\xbb\x96\xc6\xac`\x1c}\xd1\xca\xc1ZB\xf1@\x01\x92\xca\xc4Z[\x96o\xdeFv\xdf\r\x13u+\x89\xac3\xa3\xc9X\xfb\x07u\x1bO\x9c\xb0\xbdN\xa4\xb6\xca&T\xabmx\xdb\xae\xc2'

FLAG = unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(ciphertext), 16)
print("Flag: ", FLAG.decode())