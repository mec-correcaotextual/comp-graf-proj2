from abc import ABC, abstractmethod
from typing import List

import numpy as np

from geo import Camera, Triangle
from calc import Matrix, Vector


class Loader(ABC):

    @abstractmethod
    def load(self, file):
        pass


class TriangleLoader(Loader):

    def load(self, file) -> List[Triangle]:
        try:
            triangles = []

            with open(file, 'r') as f:
                lines = f.readlines()
                number_vertices = self._get_number_of_vertices(lines)
                vertices = []

                for line in lines[1:number_vertices+1]:
                    x, y, z = line.split()
                    vertices.append(np.array([x, y, z]))

                for line in lines[number_vertices+1:]:
                    a, b, c = line.split()
                    selected_vertices = self._select_vertices(vertices, [int(a), int(b), int(c)])
                    triangles.append(self._init_triangle(selected_vertices))
            
            return triangles

        except FileNotFoundError:
            print("File doesn't exist")

    def _get_number_of_vertices(self, lines: List[str]) -> int:
        number_vertices, _ = lines[0].split()
        return int(number_vertices)
    
    def _init_triangle(self, vertices) -> Triangle:
        return Triangle(*vertices)

    def _select_vertices(self, vertices, idxs):
        selected_vertices = []
        for i in idxs:
            selected_vertices.append(vertices[i-1])
        return selected_vertices


class CameraLoader(Loader, Matrix, Vector):

    def load(self, file):
        N, V, d, hx, hy, C = self.get_values(file)
        V_ = self.orth(N, V)
        V_norm = self.normalize(V_)
        N_norm = self.normalize(N)        
        U = self.cross_prod(N, V_)
        U_norm = self.normalize(U)
        return Camera(N_norm, V_norm, d, hx, hy, C, U_norm)


    def get_values(self, file):
        try:
            with open(file, 'r') as f:
                lines = f.readlines()
                N = np.array([int(e) for e in lines[0].split()])
                V = np.array([int(e) for e in lines[1].split()])
                d = int(lines[2])
                hx = int(lines[3])
                hy = int(lines[4])
                C = np.array([int(e) for e in lines[5].split()])
            return N, V, d, hx, hy, C
        except FileNotFoundError:
            print('Camera file was not found')


if __name__ == '__main__':
    tl = TriangleLoader()
    triangles = tl.load('data/input.txt')
    for t in triangles:
        print(t)

    cl = CameraLoader()
    camera = cl.load('data/camera_test.txt')
    print(camera)
    print(camera.world2sight(np.array([1, -3, -5])))
