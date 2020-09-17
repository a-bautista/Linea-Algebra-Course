'''
    Determine whether the dot product is commutative.

    1. Generate two 100 elements random row vectors, compute the dot product a with b, b with a.
    2. Generate two 2-element integer row vectors.

    Answer:Yes, the dot product is commutative.
'''

import numpy as np

def main():
    A = np.random.rand(1,100)
    B = np.random.rand(1,100)

    integerMatrixA = np.array([2, 1, 4])
    integerMatrixB = np.array([6, 2, 7])

    dpsBA = dpsAB = np.zeros(100)
    for i in range(100):
        dpsAB[i] = np.dot(A[:,i],B[:,i])

    for i in range(100):
        dpsBA[i] = np.dot(B[:,i],A[:,i])

    for i in range(100):
        if dpsAB[i]!=dpsBA[i]:
            print(i)
            print("Not commutative")

    integerDPAB = np.dot(integerMatrixA, integerMatrixB)
    integerDPBA = np.dot(integerMatrixB, integerMatrixA)

    print(integerDPAB, integerDPBA)

main()