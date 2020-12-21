import numpy as np

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
    if b == a:
        printDivision(b, a)
        return a
    if b < a:
        return gcdEuclideanHelper(a, b, (a, b))
    else:
        return gcdEuclideanHelper(b, a, (b, a))


def gcdEuclideanHelper(b, a, init_values):
    if a == 0:
        print(f"\nTherefore, gcd{init_values} is {b}\n\n")
        return
    _, r = printDivision(b, a)
    return gcdEuclideanHelper(a, r, init_values)


def gcdMatrix(b, a, matrix = None, init_values = None):
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
        matrix[1]-= q * matrix[0]

    return gcdMatrix(matrix[0, 2], matrix[1, 2], matrix, init_values)

def m(a, b):
    gcdEuclidean(a, b)

    gcdMatrix(a, b)

    print(gcd(a, b))



if __name__ == '__main__':
    pass