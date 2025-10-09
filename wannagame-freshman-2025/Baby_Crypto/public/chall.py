#!/usr/bin/env python3
import os

message = '???'
FLAG = open("flag.txt").read().encode()
assert FLAG in message


def cauhoi1(text: bytes) -> bytes:
    return ???

def cauhoi2(text: bytes) -> bytes:
    return ???

def cauhoi3(a: bytes, b: bytes) -> bytes:
    return ???

    
enc = cauhoi1(message.encode())
weird = cauhoi2(enc)
key1, key2, key3 = [os.urandom(len(weird)) for _ in range(3)]

ct1 = cauhoi3(weird, key1)
ct2 = cauhoi3(key1, key2)
ct3 = cauhoi3(key2, key3)


with open("output.txt", "w") as o:
    o.write(f'ct1: {ct1.hex()}\nct2: {ct2.hex()}\nct3: {ct3.hex()}\n')
    # I will give you a chance with my last key :D
    o.write(f'key3: {key3.hex()}')