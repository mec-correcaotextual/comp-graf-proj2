from abc import ABC, abstractmethod
from typing import List

from geo import Camera, Triangle, Vertice


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
                    vertices.append(Vertice(x, y, z))

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


class CameraLoader(Loader):

    def load(self, file):
        try:
            with open(file, 'r') as f:
                lines = f.readlines()
                N = Vertice(*[int(e) for e in lines[0].split()])
                V = Vertice(*[int(e) for e in lines[1].split()])
                d = int(lines[2])
                hx = int(lines[3])
                hy = int(lines[4])
                C = Vertice(*[int(e) for e in lines[5].split()])
                camera = Camera(N, V, d, hx, hy, C)
            return camera
        except FileNotFoundError:
            print('Camera file was not found')



if __name__ == '__main__':
    tl = TriangleLoader()
    triangles = tl.load('data/input.txt')
    for t in triangles:
        print(t)

    cl = CameraLoader()
    camera = cl.load('data/camera.txt')
    print(camera)
