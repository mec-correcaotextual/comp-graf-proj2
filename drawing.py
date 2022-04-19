import warnings

import numpy as np
from pygame import gfxdraw

from datastructures import Triangle


warnings.filterwarnings('ignore')


class Drawer:
    @classmethod
    def draw_pixel(cls, surface, x, y, color):
        gfxdraw.pixel(surface, x, y, color)

    @classmethod
    def draw_line(cls, surface, x: np.ndarray, y: np.ndarray, color):
        delta_x = y[0] - x[0]
        delta_y = y[1] - x[1]

        error = 0

        if delta_x == 0:
            delta_error = 1
        else:
            delta_error = abs(delta_y / delta_x)

        if delta_x > 0:
            y_ = x[1]
            x_ = x[0]
            while x_ <= y[0]:
                cls.draw_pixel(surface, x_, y_, color)
                error += delta_error

                while error >= 0.5:
                    y_ += 1
                    error -= 1

                x_ += 1
        elif delta_x < 0:
            y_ = x[1]
            x_ = x[0]

            while x_ >= y[0]:
                cls.draw_pixel(surface, x_, y_, color)

                error += delta_error

                while error >= 0.5:
                    y_ += 1
                    error -= 1

                x_ -= 1
        else:
            if delta_y > 0:
                y_ = x[1]
                while y_ <= y[1]:
                    cls.draw_pixel(surface, x[0], y_, color)
                    y_ += 1
            else:
                y_ = x[1]

                while y_ >= y[1]:
                    cls.draw_pixel(surface, x[0], y_, color)
                    y_ -= 1


class TriangleDrawer(Drawer):

    @classmethod
    def draw(cls, surface, triangle: Triangle, color):
        triangle = cls.sort_triangle_vertices_asc(triangle)

        if triangle.v2[1] == triangle.v3[1]:
            cls.draw_bottom_flat(surface, triangle, color)
        elif triangle.v1[1] == triangle.v2[1]:
            cls.draw_top_flat(surface, triangle, color)
        else:
            aux1 = (triangle.v2[1] - triangle.v1[1]) / \
                (triangle.v3[1] - triangle.v1[1])
            aux2 = triangle.v1[0] + (aux1 * (triangle.v3[0] - triangle.v1[0]))
            v4 = np.array([aux2, triangle.v2[1]])
            cls.draw_bottom_flat(surface, Triangle(
                triangle.v1, triangle.v2, v4), color)
            cls.draw_top_flat(surface, Triangle(
                triangle.v2, v4, triangle.v3), color)

    @classmethod
    def draw_bottom_flat(cls, surface, triangle: Triangle, color):
        try:
            inv_slope1 = (triangle.v2[0] - triangle.v1[0]) / \
                (triangle.v2[1] - triangle.v1[1])
            inv_slope2 = (triangle.v3[0] - triangle.v1[0]) / \
                (triangle.v3[1] - triangle.v1[1])

            curx1 = triangle.v1[0]
            curx2 = triangle.v1[0]

            scanline_y = triangle.v1[1]

            while scanline_y <= triangle.v2[1]:
                cls.draw_line(surface, [int(curx1), int(scanline_y)], [
                              int(curx2), int(scanline_y)], color)
                curx1 += inv_slope1
                curx2 += inv_slope2
                scanline_y += 1
        except:
            print(f'Error (bottom): {triangle}')

    @classmethod
    def draw_top_flat(cls, surface, triangle: Triangle, color):
        try:
            inv_slope1 = (triangle.v3[0] - triangle.v1[0]) / \
                (triangle.v3[1] - triangle.v1[1])
            inv_slope2 = (triangle.v3[0] - triangle.v2[0]) / \
                (triangle.v3[1] - triangle.v1[1])

            curx1 = int(triangle.v3[0])
            curx2 = int(triangle.v3[0])

            scanline_y = triangle.v3[1]
            while scanline_y > triangle.v1[1]:
                cls.draw_line(surface, [int(curx1), int(scanline_y)], [
                              int(curx2), int(scanline_y)], color)
                curx1 -= inv_slope1
                curx2 -= inv_slope2
                scanline_y -= 1
        except:
            print(f'Error (top): {triangle}')

    @classmethod
    def _draw(cls, surface, triangle: Triangle, color):
        try:
            inv_slope1 = (triangle.v2[0] - triangle.v1[0]) / \
                (triangle.v2[1] - triangle.v1[1])
            inv_slope2 = (triangle.v3[0] - triangle.v1[0]) / \
                (triangle.v3[1] - triangle.v1[1])

            curx1 = triangle.v1[0]
            curx2 = triangle.v1[0]

            scanline_y = triangle.v1[1]

            while scanline_y <= triangle.v2[1]:
                cls.draw_line(surface, [int(curx1), int(scanline_y)], [
                              int(curx2), int(scanline_y)], color)

                if curx1 == curx2:
                    cls.draw_top_flat(surface, Triangle(triangle.v2, np.array(
                        [curx2, triangle.v3[1] + (curx1 - scanline_y)]), triangle.v3), color)

                curx1 += inv_slope1
                curx2 += inv_slope2
                scanline_y += 1
        except:
            print(triangle)

    @classmethod
    def sort_triangle_vertices_asc(cls, triangle: Triangle):
        aux = [triangle.v1, triangle.v2, triangle.v3]
        return Triangle(*list(sorted(aux, key=lambda x: x[1])))


if __name__ == '__main__':
    t = Triangle(np.array([4, 5]), np.array([2, 15]), np.array([1, 2]))
    print(TriangleDrawer.sort_triangle_vertices_asc(t))
