import numpy as np

from vector_operations import VectorOperation


def print_hi(name):
    vector = VectorOperation(np.array([4, 2, 3]), np.array([5, 4, 6]))

    print(vector.square())


if __name__ == '__main__':
    print_hi('PyCharm')
