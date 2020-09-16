import numpy as np
from math import sqrt
from matplotlib import pyplot as plt

def main():

    ### Define you m rows and n columns
    m = 3
    n = 2

    ### Random numbers from a random distribution
    # from m rows and n columns
    A = np.random.randn(m,n)
    B = np.random.randn(m,n)

    # the output of A and B in m*n is:
    #    x     y
    # [[2.54, 9.03],
    # [-0.34, 9.23],
    # [9.21,-0.23]]

    # [[-1.24, 2.13],
    # [2.31, 2.21],
    # [8.11,-0.56]]

    print(A)
    print(B)

    ### Compute the dot product
    # (2.54*-1.24) + (-0.34*2.31) + (9.21*8.11) = some number
    # (9.03*2.13)  + (9.23*2.21)  + (-0.23*-0.56) = another number

    dps = np.zeros(n)
    for i in range(n):
        dps[i] = np.dot(A[:,i], B[:,i])

    # display the computed dot product
    print("\nThis is the dot product:")
    print(dps)

    ### Calculating the norm of a vector in 5D
    v = np.array([1,2,3,4,5])
    norm = sqrt(sum(np.multiply(v,v)))

    # display the norm
    print("\nThis is the norm of a vector:")
    print(norm)

    # Define two vectors in 3D
    # v1 = np.array([2, 4, -3])
    # v2 = np.array([0, -3, -3])

    v1 = np.array([16, -2, 4])
    v2 = np.array([0.5, 2, -1])

    dp = np.dot(v1,v2)
    print(dp)

    # Compute the angle (radians) between two vectors
    theta = np.arccos( np.dot(v1,v2) / (np.linalg.norm(v1)*np.linalg.norm(v2)))
    print("\nThis is the angle between these two vectors: ")
    print(theta)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot([0, v1[0]], [0, v1[1]], [0, v1[2]], 'b')
    ax.plot([0, v2[0]], [0, v2[1]], [0, v2[2]], 'r')

    plt.axis((-6, 6, -6, 6))
    plt.title('Angle between vectors: %s rad. '%theta)
    plt.show()

main()
