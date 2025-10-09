import base64
import os

message = "In March 2007, the first trailer for the highly anticipated Grand Theft Auto IV was released onto the Rockstar Games website. Viewership was so high that it crashed Rockstar's site. Several users helped to post mirrors of the video on different sites, but one user on 4chan, Shawn Cotter, had linked to the Never Gonna Give You Up video claiming to be the trailer, tricking numerous readers into the bait-and-switch. Here is the flag: W1{D1d_y0U_GeT_r1Ck_r0lL3d?} In 2022, Shawn Cotter was interviewed by Vice Media. He said the reason of using Never Gonna Give You Up was because he found a list about songs that were popular at the time he was born using the Internet, and this song is on the top of 1987, which was his year of birth. This practice quickly replaced duck rolling for other alluring links, all generally pointing to Astley's video, and thus creating the practice of rickrolling. The bait-and-switch to Never Gonna Give You Up greatly expanded on 4chan on April Fools' Day in 2007, and led to the trick expanding to other sites like Fark and Digg later that year, quickly adding the name rickrolling based on the prior duck rolling."
FLAG = open("flag.txt").read().strip()

assert FLAG in message

def rot13(text: bytes) -> bytes:
    return bytes(
        (c + 13 - 65) % 26 + 65 if 65 <= c <= 90 else
        (c + 13 - 97) % 26 + 97 if 97 <= c <= 122 else c
        for c in text
    )
    
def base85encode(text: bytes) -> bytes:
    return base64.b85encode(text)

def xor(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))

enc = rot13(message.encode())
weird = base85encode(enc)

key1, key2, key3 = [os.urandom(len(weird)) for _ in range(3)]

ct1 = xor(weird, key1)
ct2 = xor(key1, key2)
ct3 = xor(key2, key3)

with open("output.txt", "w") as o:
    o.write(f'ct1: {ct1.hex()}\nct2: {ct2.hex()}\nct3: {ct3.hex()}\n')
    # I will give you a chance with my last key :D
    o.write(f'key3: {key3.hex()}')