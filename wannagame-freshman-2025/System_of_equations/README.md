# System of Equations

- Category: Crypto
- Score: 472/500
- Solves: 6
- Flag: `W1{y0u_must_b3_th3_m4st3r_0f_3quat1ons_817e31a7ccdbe8fd}`

## Description

Surely you have faced a system of equations in the past, right?

If you are familiar with such challenges, then the path to the solution to this challenge is actually right at your fingertips. The important thing is just perseverance: dare to explore every corner, test every step, and do not hesitate to step into seemingly dead-end paths.

I have been very lenient in giving you only three equations.
The rest depends on your ability and perseverance.

## Solution

The challenge gives us a system of equations with 3 unknowns and our goal is solve this to get the key, decode the AES algorithm and receive the flag.

### Unintended

You can use `sympy` library to construct the system and solve it just by the function @@

P/s: Actually, my purpose is to test the student's ability to apply the knowledge they are learning. So this is still in plannnn 😏

### Intended

The first equation tells us that x is even, then the second equation tells us that y is even.

Let $x=2x_1, y=2y_1$, the system of equations becomes:

$$
\begin{equation}
    \begin{cases}
      x_1^2+2x_1y_1+2z=z^2+2y_1+2\\
      2x_1^2+y_1+z=2(2p+1)
    \end{cases}\
\end{equation}
$$

Continuing, equation 1 tells us: $x_1\equiv z\pmod{2}$, and equation 2 also gives $x_1\equiv z\pmod{2}$. If $x_1, y_1, z$ were all even, the first equation would not hold because the left-hand side would be divisible by 4 while the right-hand side is $\equiv 2\pmod{4}$.

Therefore, they are all odd. Let $x_1=2u+1$, $y_1 = 2v-1$, $z=2w+1$. The system becomes:

$$
\begin{equation}
    \begin{cases}
      u^2+2uv=w^2\\
      4u^2+4u+v+w=2p
    \end{cases}\
\end{equation}
$$

1. If $u=0$
   Then $w=0$ and $v=2p$, which yields the solution $(x, y, z) = (2, 8p-2, 1)$.

2. If $u\ne 0$

The first equation implies $u\mid w^2$, so we can write $u=a b^2$ and $w=a b c$ for some square-free positive integer $a$ and nonzero integers $b,c$.
The system becomes:

$$
\begin{equation}
    \begin{cases}
      v=\dfrac{a(c^2-b^2)}{2}\\
      v=2p-4a^2b^4-4ab^2-abc
    \end{cases}\
\end{equation}
$$

From this we see that $a(c^2-b^2)$ is even, and $a(c^2-b^2)=4p-8a^2b^4-8ab^2-2abc$

Rearranging gives $a(b+c)^2=4p-8a^2b^4-8ab^2 \ \ (1)$

Since $a$ is square-free and divides the right-hand side, and $a>0$, we have $a\in\{1,2,p,2p\}$. Let $N=b+c$.

Then the equation can be rewritten as $(8ab^2+3)^2+8aN=32p+9$.

Because $a>0$ we get the bound $8ab^2+3\le\sqrt{32p+9}$, hence $1\le b^2\le\dfrac{\sqrt{32p+9}-3}{8a}$.

This implies $a\le\dfrac{\sqrt{32p+9}-3}{8}$.

One checks that for all $p>1$ the right-hand side is less than $p$, so $a<p$. Therefore $a$ can only be $1$ or $2$.

- If $a=1$ then from (1) we need $-8b^4-6b^2+4p$ to be a perfect square.
- If $a=2$ then from (1) we need $-16b^4-6b^2+2p$ to be a perfect square.

A small brute-force search over these cases is easy and yields the solution family $(x,y,z)=(4ab^2+2,\;2a(c^2-b^2)-2,\;2abc+1)$ with $c$ chosen so that the perfect-square condition holds (in the original derivation $c=\sqrt{k}-b$ for some integer $k$).

[Full script](./solution.py)...
