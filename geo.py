from dataclasses import dataclass

import numpy as np

from calc import Vector


@dataclass
class Triangle:
    v1: np.ndarray
    v2: np.ndarray
    v3: np.ndarray


@dataclass
class Camera(Vector):
    N: np.ndarray
    V: np.ndarray
    d: int
    hx: int
    hy: int
    C: np.ndarray
    U: np.ndarray

    def world2sight(self, camera, P):
        I_e_alpha = np.array([camera.U, camera.V, camera.N])
        P_ = self.sub_vecs(P, camera.C)
