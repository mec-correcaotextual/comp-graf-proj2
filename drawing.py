from pygame import gfxdraw


def draw_pixel(surface, x, y, color):
    gfxdraw.pixel(surface, x, y, color)
