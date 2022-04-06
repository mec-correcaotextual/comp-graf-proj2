import math

import numpy as np


class Matrix:
    def mult_matrix_vec(M, V):
        aux = []
        for i in range(M.shape[0]):
            sum = 0.0
            for j in range(M.shape[1]):
                sum += M[i][j] * V[j]
            aux.append(sum)
        return np.array(aux)

class Vector:
    @classmethod
    def cross_prod(cls, X, Y):
        return np.array(
            [
                (X[1]*Y[2] - X[2]*Y[1]),
                -1 * (X[0]*Y[2] - X[2]*Y[0]),
                (X[0]*Y[1] - X[1]*Y[0])
            ]
        )

    @classmethod
    def dot_product(cls, x, y):
        assert len(x) == len(y)
        return sum(x * y)

    @classmethod
    def get_magnitude(cls, vec):
        sum = 0.0
        for s in vec:
            sum += math.pow(s, 2)
        return math.sqrt(sum)

    @classmethod
    def normalize(cls, vec):
        magnitude = cls.get_magnitude(vec)
        aux = []
        for s in vec:
            r = s / magnitude
            aux.append(r)
        return np.array(aux)
    
    @classmethod
    def sub_vecs(cls, X, Y):
        assert len(X) == len(Y)
        aux = []
        for i in range(len(X)):
            aux.append(X[i] - Y[i])
        return np.array(aux)

    @classmethod
    def prod_scaler_vec(cls, V, scaler):
        aux = []
        for s in V:
            aux.append(s * scaler)
        return np.array(aux)

    @classmethod
    def orth(cls, N, V):
        return cls.sub_vecs(V, cls.prod_scaler_vec(N, cls.dot_product(V, N) / cls.dot_product(N, N)))

if __name__ == '__main__':
    import numpy as np

    M = np.array([[1, -1, 2], [0, -3, 1]])
    V = np.array([2, 1, 0])
    print(Matrix.mult_matrix_vec(M, V))
