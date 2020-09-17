import numpy as np
from matplotlib import pyplot as plt

def main():

    # define your vector
    v1 = np.array([-3, 6])

    # define mu
    mu = 1/np.linalg.norm(v1)

    # "normalize" the vector
    v1n = v1*mu

    # plot them
    plt.plot([0, v1n[0]], [0, v1n[1]], 'r', label='v1-norm', linewidth=5)
    plt.plot([0, v1[0]],  [0, v1[1]], 'b', label='v1')

    # axis square
    plt.axis('square')
    plt.axis((-6, 6, -6, 6))
    plt.grid()
    plt.legend()
    plt.show()

main()