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
    poop_img = pygame.image.load("assets/poop.png").convert_alpha()
    triceratops_img = pygame.image.load("assets/triceratops.png").convert_alpha()
    pygame.font.init()
    my_font = pygame.font.SysFont("times new roman", 100)
    my_small_font = pygame.font.SysFont("times new roman", 25)
    grass_img.set_colorkey((0, 0, 0))

    map_data = []
    for x in range(12):
        new_map_data = []
        for y in range(12):
            new_map_data.append(1)
        map_data.append(new_map_data)

    dino_x = 0
    dino_y = 0
    cursor = 0
    cursor_down = False
    cursor_up = False
    pause_menu = False
    timer = 0

    dino_data = [dino_x,dino_y]
    poop_data = []

    wallet = 0

    while True:
        screen.fill("black")
        display.fill("black")
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == K_1:
                    if not pause_menu:
                        try:
                            poop_data.pop(0)

                        except IndexError:
                            pass

                    else:
                        if cursor == 0:
                            pause_menu = False

                if event.key == K_2:
                    pause_menu = True

                if event.key == K_DOWN:
                    cursor_down = True

                if event.key == K_UP:
                    cursor_up = True

            if event.type == KEYUP:
                if event.key == K_DOWN:
                    cursor_down = False

                if event.key == K_UP:
                    cursor_up = False

        if pause_menu:
            if cursor_down and cursor < 2:
                cursor += 1
                cursor_down = False

            if cursor_up and cursor > 0:
                cursor -= 1
                cursor_up = False

            if cursor == 0:
                resume_text = my_font.render("resume", True, "red")
                scientist_text = my_font.render("hire scientist", True, "blue")
                market_text = my_font.render("goto market", True, "blue")

            elif cursor == 1:
                resume_text = my_font.render("resume", True, "blue")
                scientist_text = my_font.render("hire scientist", True, "red")
                market_text = my_font.render("goto market", True, "blue")

            elif cursor == 2:
                resume_text = my_font.render("resume", True, "blue")
                scientist_text = my_font.render("hire scientist", True, "blue")
                market_text = my_font.render("goto market", True, "red")

            coin_text = my_font.render(f"coins: {wallet}", True, "yellow")

            screen.blit(resume_text, (200,0))
            screen.blit(scientist_text, (75,100))
            screen.blit(market_text, (100,200))
            screen.blit(coin_text, (25,350))
            pygame.display.flip()
            
        if not pause_menu:
            timer += 1
            if timer == 60:
                timer = 0
                wallet += 1
                    
            # spawn terrain
            for y, row in enumerate(map_data):
                for x, tile in enumerate(row):
                    if tile:
                        display.blit(grass_img, (150 + x * 10 - y * 10, 100 + x * 5 + y * 5))

            # ai
            direction = random.randint(1,4)

            if dino_data[0] == 0 and dino_data[1] == 11:
                dino_data[1] -= 1

            if dino_data[1] == 0 and dino_data[0] == 11:
                dino_data[0] -= 1

            if direction == 1 and dino_data[0] > 0 and dino_data[1] > 0:
                dino_data[0] -= 1

            if direction == 2 and dino_data[0] < 11 and dino_data[1] < 11:
                dino_data[0] += 1

            if direction == 3 and dino_data[0] > 0 and dino_data[1] > 0:
                dino_data[1] -= 1

            if direction == 4 and dino_data[0] < 11 and dino_data[1] < 11:
                dino_data[1] += 1

            # poop
            poop = random.randint(1,60)

            if poop == 1:
                already_pooped = False
                for terd in poop_data:
                    if terd == dino_data:
                        already_pooped = True
                        break
                if not already_pooped:
                    poop_data.append((dino_data[0],dino_data[1]))

            # show coins
            coin_text = my_small_font.render(f"coins: {wallet}", True, "yellow")
            display.blit(coin_text, (25,25))

            # show poop B)
            for y, row in enumerate(map_data):
                for x, tile in enumerate(row):
                    for terd in poop_data:
                        if x == terd[0] and y == terd[1]:
                            display.blit(poop_img, (150 + x * 10 - y * 10  + (grass_img.get_width() - poop_img.get_width()) // 2, 100 + x * 5 + y * 5 - poop_img.get_height() + 15))
            
            # spawn dinosaurs
            for y, row in enumerate(map_data):
                for x, tile in enumerate(row):
                    if [x,y] == dino_data:
                        display.blit(triceratops_img, (150 + x * 10 - y * 10  + (grass_img.get_width() - triceratops_img.get_width()) // 2, 100 + x * 5 + y * 5 - triceratops_img.get_height() + 15))

            screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
            pygame.display.flip()

            time.sleep(1)

main()
