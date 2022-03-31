import numpy as np
from scipy.spatial.distance import cdist


class VectorOperation:
    def __init__(self, vectorA, vectorB):
        self.vectorA = vectorA
        self.vectorB = vectorB

    def length(self):
        return np.linalg.norm(self.vectorA)

    def vectorSum(self):
        return self.vectorA + self.vectorB

    def vectorSub(self):
        return self.vectorA - self.vectorB

    def scalarMultiply(self):
        return self.vectorA.dot(self.vectorB)

    def vectorMulti(self):
        return self.vectorA.dot(self.vectorB)

    def vectorCross(self):
        return np.cross(self.vectorA, self.vectorB)

    def angle_between(self):
        dot_pr = self.vectorA.dot(self.vectorB)
        norms = np.linalg.norm(self.vectorA) * np.linalg.norm(self.vectorB)

        return np.rad2deg(np.arccos(dot_pr / norms))

    def distance(self):
        return cdist(self.vectorA, self.vectorB)

    def square(self):
        a = np.cross(self.vectorA, self.vectorB)
        return np.sqrt(np.sum(a**2))
