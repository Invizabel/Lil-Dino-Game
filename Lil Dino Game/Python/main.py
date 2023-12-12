import random
import sys
import time
import pygame
from pygame.locals import *

def main():
    pygame.init()
    pygame.display.set_caption("Lil Dino Game")
    screen = pygame.display.set_mode((640, 480),0,32)
    display = pygame.Surface((300, 300))

    grass_img = pygame.image.load("assets/grass.png").convert_alpha()
    triceratops_img = pygame.image.load("assets/triceratops.png").convert_alpha()
    grass_img.set_colorkey((0, 0, 0))

    map_data = []
    for x in range(12):
        new_map_data = []
        for y in range(12):
            new_map_data.append(1)
        map_data.append(new_map_data)

    dino_data = []
    spawned_bool = True
    for x in range(12):
        new_dino_data = []
        for y in range(12):
            if spawned_bool:
                spawned_bool = False
                new_dino_data.append(1)
            else:
                new_dino_data.append(0)
        dino_data.append(new_dino_data)
    
    while True:
        display.fill((0,0,0))
        for y, row in enumerate(map_data):
            for x, tile in enumerate(row):
                if tile:
                    display.blit(grass_img, (150 + x * 10 - y * 10, 100 + x * 5 + y * 5))

        screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        for y, row in enumerate(dino_data):
            for x, tile in enumerate(row):
                if tile:
                    display.blit(triceratops_img, (150 + x * 10 - y * 10  + (grass_img.get_width() - triceratops_img.get_width()) // 2, 100 + x * 5 + y * 5 - triceratops_img.get_height() + 15))

        screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))

        pygame.display.update()

main()
