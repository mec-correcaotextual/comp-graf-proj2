from dataclasses import dataclass

import numpy as np

from calc import Vector, Matrix


@dataclass
class Triangle:
    v1: np.ndarray
    v2: np.ndarray
    v3: np.ndarray


@dataclass
class Camera(Vector, Matrix):
    N: np.ndarray
    V: np.ndarray
    d: int
    hx: int
    hy: int
    C: np.ndarray
    U: np.ndarray

    def world2sight(self, P):
        I_e_alpha = np.array([self.U, self.V, self.N])
        P_ = self.mult_matrix_vec(I_e_alpha, self.sub_vecs(P, self.C))
        return P_
