from dataclasses import dataclass


@dataclass
class Vertice:
    x: int
    y: int
    z: int


@dataclass
class Triangle:
    v1: Vertice
    v2: Vertice
    v3: Vertice
