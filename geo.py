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

    def get_norm_coord(self, P):
        vec = self.p_(P)
        xs_norm = vec[0] / self.hx
        ys_norm = vec[1] / self.hy
        return np.array([xs_norm, ys_norm])

    def p_(self, P):
        P_ = self.world2sight(P)
        xs = self.d * P_[0] / P_[2]
        ys = self.d * P_[1] / P_[2]
        return np.array([xs, ys])

    def world2sight(self, P):
        I_e_alpha = np.array([self.U, self.V, self.N])
        P_ = self.mult_matrix_vec(I_e_alpha, self.sub_vecs(P, self.C))
        return P_
