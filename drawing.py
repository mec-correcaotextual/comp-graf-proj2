from dataclasses import astuple
from pygame import gfxdraw

from geo import Triangle


def draw_pixel(surface, x, y, color):
    gfxdraw.pixel(surface, x, y, color)


class Drawer:
    @classmethod
    def draw_pixel(cls, surface, x, y, color):
        gfxdraw.pixel(surface, x, y, color)
