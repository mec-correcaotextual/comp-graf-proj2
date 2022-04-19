import pygame

import settings

from drawing import Drawer, TriangleDrawer
from datastructures import Triangle
from loaders import TriangleLoader, CameraLoader


def main():
    pygame.init()
    window = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    run = True

    tl = TriangleLoader()
    cl = CameraLoader()

    triangles = tl.load(settings.INPUT_FILE)
    camera = cl.load(settings.CAMERA_FILE)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                triangles = tl.load(settings.INPUT_FILE)
                camera = cl.load(settings.CAMERA_FILE)
        
        window.fill('black')

        for t in triangles:
            v1 = camera.get_screen_coord(t.v1, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
            v2 = camera.get_screen_coord(t.v2, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
            v3 = camera.get_screen_coord(t.v3, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)

            Drawer.draw_pixel(window, v1[0], v1[1], pygame.Color(255, 255, 255))
            Drawer.draw_pixel(window, v2[0], v2[1], pygame.Color(255, 255, 255))
            Drawer.draw_pixel(window, v3[0], v3[1], pygame.Color(255, 255, 255))

            TriangleDrawer.draw(window, Triangle(v1, v2, v3), pygame.Color(255, 255, 255))

            # pygame.draw.polygon(surface=window, color=pygame.Color(255, 255, 255), points=[
            #     (v1[0], v1[1]),
            #     (v2[0], v2[1]),
            #     (v3[0], v3[1])
            # ])
            # Drawer.draw_line(window, v1, v2, pygame.Color(255, 255, 255))
            # Drawer.draw_line(window, v2, v3, pygame.Color(255, 255, 255))
            # Drawer.draw_line(window, v3, v1, pygame.Color(255, 255, 255))

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
