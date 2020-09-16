'''
    Determine whether the dot product sign is invariant to scalar multiplication.

    1. Generate 2 vectors in R3.
    2. Generate 2 scalars.
    3. Compute the dot product between vectors.
    4. Compute the dot product between the scaled vectors.

    Answer: The scalar multiplication has an effect on the dot product.
'''

import numpy as np

def main():

    # define the m rows and n columns.
    m = 1
    n = 3

    # generate 2 vectors
    v1 = np.array([4,7,1])
    v2 = np.array([2,8,9])

    # generate 2 scalars
    s1 = -3
    s2 = 8

    # compute the dot product between vectors
    dp = np.dot(v1,v2)

    # compute the dot product between the scaled vectors
    dps = np.dot(v1*s1, v2*s2)

    print(dp,dps)

main()