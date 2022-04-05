from abc import ABC, abstractmethod
from typing import List

from geo import Vertice, Triangle


class Loader(ABC):

    @abstractmethod
    def load(self, file):
        pass


class InputLoader(Loader):

    def load(self, file):
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


if __name__ == '__main__':
    tl = InputLoader()
    triangles = tl.load('input.txt')
    for t in triangles:
        print(t)
