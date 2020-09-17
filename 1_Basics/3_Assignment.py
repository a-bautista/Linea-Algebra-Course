'''
    1. Create two random-integer vectors in R3.
    2. Compute the length of the individual vectors (norm) and magnitude of
       their dot product.
    3. "Normalize" the vectors (unit vector).
    4. Compute the magnitude of that dot product.

'''

import numpy as np
from matplotlib import pyplot as plt

def main():
    # Create the 2 random integer vectors in R3.
    v1 = np.array([1, 3, -5])
    v2 = np.array([2, 8, 1])

    # Compute the length of each vector (norm)
    normv1 = np.linalg.norm(v1)
    normv2 = np.linalg.norm(v2)

    # Compute the dot product
    dp = np.dot(v1,v2)

    print("These are the norms or lengths:", normv1, normv2)
    print("This is the dot product:", dp)

    # Normalize the vectors (unit vectors)
    muv1 = 1/np.linalg.norm(v1)
    muv2 = 1/np.linalg.norm(v2)

    normalizedv1 = muv1 * v1
    normalizedv2 = muv2 * v2

    # Calculate the dot products of the normalized vectors
    dpNormalized = np.abs(np.dot(normalizedv1, normalizedv2))
    print("This is the normalized dot product:",dpNormalized)

    illustrate(v1, v2, normalizedv1, normalizedv2)

def illustrate(v1, v2, v1n, v2n):
    # plot them

    plt.plot([0, v1[0]], [0, v1[1]], 'y', label='v1')
    plt.plot([0, v1n[0]], [0, v1n[1]], 'r', label='v1-norm', linewidth=5)

    # plt.plot([0, v2[0]], [0, v2[1]], 'b', label='v2')
    # plt.plot([0, v2n[0]], [0, v2n[1]], 'g', label='v2-norm', linewidth=5)

    # axis square
    plt.axis('square')
    plt.axis((-6, 6, -6, 6))
    plt.grid()
    plt.legend()
    plt.show()

main()