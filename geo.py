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
    d: float
    hx: float
    hy: float
    C: np.ndarray
    U: np.ndarray

    def get_screen_coord(self, P, width, height):
        P_ = self.get_norm_coord(P)
        i = self.get_screen_x_coord(P_[0], width)
        j = self.get_screen_y_coord(P_[1], height)
        return np.array([int(i), int(j)])

    def get_screen_x_coord(self, xs, width):
        return np.floor(((xs + 1) / 2) * width + 0.5)
    
    def get_screen_y_coord(self, ys, height):
        return np.floor(height - ((ys + 1) / 2) * height + 0.5)

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
