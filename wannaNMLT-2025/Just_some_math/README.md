# System of Equations
- Category: Crypto
- Score: 1000/1000
- Solves: 1
- Flag: `W1{I_hdpe_you_did_not_need_so_many_samples}`
- Port: port: 3636
## Description
Hope you have fun without modulo.
## Solution
Analyzing the `chall.py` file reveals the following information:
- The flag is converted into an integer `pt` with a length exceeding 800 bits.
```python
assert pt.bit_length() > 800
```
- The RSA system employs two primes $p, q$ (512 bits each) and a public exponent $e$ (256 bits).
- The system prints the values of $i^e \pmod p$ for $i$ ranging from 2 to 6.

```python
def try_gen():
    p = getPrime(512)
    q = getPrime(512)
    e = getPrime(256)
    N = p * q

    phi = (p - 1) * (q - 1)
    if math.gcd(phi, e) != 1:
        try_gen()

    ct = pow(pt, e, N)
    print('ct =', ct)
    print('e =', e)
    for i in [2, 3, 4, 5, 6]:
        print(f'{i}^e mod p =', pow(i, e, p))
```

Since `pt` (800+ bits) is larger than $p$ (512 bits), we cannot recover the full flag simply by decrypting modulo $p$. Therefore, we must collect more data from runs to utilize the Chinese Remainder Theorem (CRT).


First we recover prime $p$ based on the provided values:
$$R_2 = 2^e \pmod p, R_3 = 3^e \pmod p, R_4 = 4^e \pmod p, R_6 = 6^e \pmod p$$
We observe the following mathematical properties: $ R_4 \equiv R_2^2 \pmod p, R_6 \equiv R_2 \cdot R_3 \pmod p$

This implies that: $p \mid (R_2^2 - R_4), p \mid (R_2 \cdot R_3 - R_6)$

By calculating the Greatest Common Divisor (GCD) of these differences, we can recover the prime $p$:$$p = \text{gcd}(|R_2^2 - R_4|, |R_2 \cdot R_3 - R_6|)$$

On the other hand, we notice that p has 512 bits, while the other two values ​​are less than or equal to 1024 bits, so when taking GCD, the largest prime factor is p.

Then, we calculate $d_p = e^{-1} \pmod{p-1}$. And we have the value of the flag modulo $p$ is:$pt' = ct^{d_p} \pmod p$

Using CRT with two pairs $(pt_1, p_1), (pt_2, p_2)$ is enough for us to recover the flag.

[Full solution script](./solution/solve.py)