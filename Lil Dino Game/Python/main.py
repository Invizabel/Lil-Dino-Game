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

    dino_x = 0
    dino_y = 0
    dino_data = [dino_x,dino_y]

    while True:
        display.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # spawn terrain
        for y, row in enumerate(map_data):
            for x, tile in enumerate(row):
                if tile:
                    display.blit(grass_img, (150 + x * 10 - y * 10, 100 + x * 5 + y * 5))

        screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))

        # generate movement
        direction = random.randint(1,4)

        if direction == 1 and dino_data[0] > 0:
            dino_data[0] -= 1

        if direction == 2 and dino_data[0] < 15:
            dino_data[0] += 1

        if direction == 3 and dino_data[0] > 0:
            dino_data[1] -= 1

        if direction == 4 and dino_data[0] < 15:
            dino_data[1] += 1
                
        
        # spawn dinosaurs
        for y, row in enumerate(map_data):
            for x, tile in enumerate(row):
                if [x,y] == dino_data:
                    display.blit(triceratops_img, (150 + x * 10 - y * 10  + (grass_img.get_width() - triceratops_img.get_width()) // 2, 100 + x * 5 + y * 5 - triceratops_img.get_height() + 15))
                    
        screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))

        pygame.display.update()
        time.sleep(1)

main()
