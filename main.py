import pygame

import drawing
import settings

def main():
    pygame.init()
    window = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        window.fill('black')

        drawing.draw_pixel(window, 100, 100, pygame.Color(255, 255, 255))

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
