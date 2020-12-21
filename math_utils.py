import numpy as np
import math

##  Find gcd for of a and b ##
'''
Arguments: int a: an integer
           int b: an integer 
Returns: int gcd of a and b
'''


def gcd(b, a):
    if b == a:
        return b
    if b > a:
        r = b % a
    else:
        r = a % b
    if r == 0:
        return min(a, b)

    return gcd(min(a, b), r)


def printDivision(b, a):
    q, r = b // a, b % a
    print(f"{b} = {a} x {q} + {r}")
    return q, r


def gcdEuclidean(b, a):
    text = []
    if b == a:
        text += printDivision(b, a)
        return a
    if b < a:
        text += gcdEuclideanHelper(a, b, (a, b))
    else:
        text += gcdEuclideanHelper(b, a, (b, a))
    return text


def gcdEuclideanHelper(b, a, init_values):
    if a == 0:
        return f"\nTherefore, gcd{init_values} is {b}\n\n"

    _, r = printDivision(b, a)
    return gcdEuclideanHelper(a, r, init_values)


def gcdMatrix(b, a, matrix=None, init_values=None):
    if init_values is None:
        init_values = (b, a)
    if matrix is None:
        print(f"Find gcd{init_values} = {b} x s + {a} x t ")
        matrix = np.array([[1, 0, b],
                           [0, 1, a]])
    print(matrix, "\n")
    if b == 0 or a == 0:
        if b == 0:
            s, t, gcd = matrix[1][0], matrix[1][1], a
        else:
            s, t, gcd = matrix[0][0], matrix[0][1], b
        print(f'Therefore, {init_values[0]} x {s} + {init_values[1]} x {t} = {gcd}')
        return None
    if b >= a:
        q = b // a
        matrix[0] -= q * matrix[1]
    else:
        q = a // b
        matrix[1] -= q * matrix[0]

    return gcdMatrix(matrix[0, 2], matrix[1, 2], matrix, init_values)


def m(a, b):
    gcdEuclidean(a, b)

    gcdMatrix(a, b)

    print(gcd(a, b))


def caesar_encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        if text[i].isupper():
            # 65 is to make A as 1, B as 2 ...etc.
            result += chr((ord(text[i]) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(text[i]) + shift - 97) % 26 + 97)
    print(f"encrypted text:  {result}")
    return (result, shift)


def caesar_decrypt(result_tuple):
    cipher_text = result_tuple[0]
    shift = result_tuple[1]
    result = ""

    for i in range(len(cipher_text)):
        if cipher_text[i].isupper():
            # 65 is to make A as 1, B as 2 ...etc.
            result += chr((ord(cipher_text[i]) - shift - 65) % 26 + 65)
        else:
            result += chr((ord(cipher_text[i]) - shift - 97) % 26 + 97)
    print(f"decrypted text:  {result}")
    return result


def pigeonHole(pigeon, holes):
    if pigeon > holes:
        print(f"There is at least one pigeonhole with at least {math.ceil(pigeon / holes)} pigeons")
    else:
        print(f"There is at least one pigeonhole with at least {math.floor(pigeon / holes)} pigeons")


"""
format in parameters
x == a1 (mod m1)
x == a2 (mod m2)
x == a3 (mod m3)
m must be relatively prime
"""


def CRT(a1, a2, a3, m1, m2, m3):
    m = m1 * m2 * m3
    z1 = m2 * m3
    z2 = m1 * m3
    z3 = m2 * m1
    y1 = modularReciprocal(z1, m1)
    y2 = modularReciprocal(z2, m2)
    y3 = modularReciprocal(z3, m3)
    x = (a1 * z1 * y1 + a2 * z2 * y2 + a3 * z3 * y3) % m
    return x


'''
format:
Want to find r such that  x*r == y (mod m)
'''


def linearCongruence(x, y, m):
    if gcd(x, m) == 1:
        inverse = modularReciprocal(x, m)
        r = y * inverse % m
    # this is the exception case
    elif isinstance(y / gcd(x, m), int):
        linearCongruence(x / gcd(x, m), y / gcd(x, m), m / gcd(x, m))
    return r


# https://www.dcode.fr/extended-gcd
def extended_gcd(a, b):
    r1, r2, u1, v1, u2, v2 = a, b, 1, 0, 0, 1
    while r2 != 0:
        q = r1 // r2
        r3, u3, v3 = r1, u1, v1
        r1, u1, v1 = r2, u2, v2
        r2, u2, v2 = r3 - q * r2, u3 - q * u2, v3 - q * v2
    print(f"{r1} = {a} * {u1} + {b} * {v1}")
    return (r1, u1, v1)


# calculate modular inverse of x mod y (i.e. x^-1)
# this method is based on Extended Euclid Algo (CMPSC 360)
def modularReciprocal(x, y):
    if gcd(x, y) == 1:
        return extended_gcd(x, y)[1]
    else:
        return "gcd != 1, so the given modulus is not invertible"


if __name__ == '__main__':
    pass
