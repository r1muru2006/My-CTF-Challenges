import base64, re

def rot13(text: bytes) -> bytes:
    return bytes(
        (c + 13 - 65) % 26 + 65 if 65 <= c <= 90 else
        (c + 13 - 97) % 26 + 97 if 97 <= c <= 122 else c
        for c in text
    )
   
def base85decode(text: bytes) -> bytes:
    return base64.b85decode(text) 

def xor(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))


with open("output.txt", "r") as f:
    ct1 = bytes.fromhex(f.readline().strip().split(": ")[1])
    ct2 = bytes.fromhex(f.readline().strip().split(": ")[1])
    ct3 = bytes.fromhex(f.readline().strip().split(": ")[1])
    key3 = bytes.fromhex(f.readline().strip().split(": ")[1])
    

weird = xor(ct1, xor(ct2, xor(ct3, key3)))
enc = base85decode(weird)
message = rot13(enc)

match = re.search(rb"W1\{.*?\}", message)
flag = match.group(0).decode(errors="ignore")
print("Flag:", flag)