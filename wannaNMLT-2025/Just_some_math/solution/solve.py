from sage.all import gcd, ecm, crt
from Crypto.Util.number import inverse, long_to_bytes
from pwn import *


def get_data():
    io = remote('160.25.233.64', 31217)
    # io = process(['python3', 'chall.py'])
    lst = []
    for i in range(7):
        io.recvuntil(" = ")
        lst.append(int(io.recvline().decode().split("\n")[0]))
    io.close()
    return lst

ct1, e1, a2, a3, a4, a5, a6 = get_data()
ct2, e2, b2, b3, b4, b5, b6 = get_data()

k1p = a2 * a2 - a4
k2p = a2 * a3 - a6
p1 = gcd(k1p, k2p)
p1 = ecm.factor(p1)[-1]
d1 = inverse(e1, p1 - 1)
pt1 = pow(ct1, d1, p1)

t1p = b2 * b2 - b4
t2p = b2 * b3 - b6
p2 = gcd(t1p, t2p)
p2 = ecm.factor(p2)[-1]
d2 = inverse(e2, p2 - 1)
pt2 = pow(ct2, d2, p2)

pt = crt(pt1, pt2, p1, p2)
flag = long_to_bytes(pt)
print(flag)
