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
    scientist_img = pygame.image.load("assets/scientist.png").convert_alpha()
    triceratops_img = pygame.image.load("assets/triceratops.png").convert_alpha()
    trex_img = pygame.image.load("assets/trex.png").convert_alpha()
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
    flask = 0
    main_menu = True
    pause_menu = False
    scientist_x = 11
    scientist_y = 11
    timer = 0

    dino_data = []
    poop_data = []
    scientist_data = [scientist_x,scientist_y]

    while True:
        screen.fill("black")
        display.fill("black")
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause_menu = True

                if event.key == K_SPACE:
                    if main_menu:
                        main_menu = False
                        if cursor == 0:
                            dino_data.append([dino_x,dino_y,"triceratops"])

                        elif cursor == 1:
                            dino_data.append([dino_x,dino_y,"trex"])

                        elif cursor == 2:
                            pygame.quit()
                            sys.exit()

                        cursor = 0

                    if pause_menu:
                        if cursor == 0:
                            pause_menu = False

                        elif cursor == 2:
                            pygame.quit()
                            sys.exit()

                        cursor = 0

                if event.key == K_DOWN:
                    cursor_down = True

                if event.key == K_UP:
                    cursor_up = True

            if event.type == KEYUP:
                if event.key == K_DOWN:
                    cursor_down = False

                if event.key == K_UP:
                    cursor_up = False

        if main_menu:
            if cursor_down and cursor < 2:
                cursor += 1
                cursor_down = False

            if cursor_up and cursor > 0:
                cursor -= 1
                cursor_up = False

            if cursor == 0:
                triceratops_text = my_font.render("triceratops", True, "red")
                trex_text = my_font.render("t-rex", True, "blue")
                exit_text = my_font.render("exit game", True, "blue")

            elif cursor == 1:
                triceratops_text = my_font.render("triceratops", True, "blue")
                trex_text = my_font.render("t-rex", True, "red")
                exit_text = my_font.render("exit game", True, "blue")

            elif cursor == 2:
                triceratops_text = my_font.render("triceratops", True, "blue")
                trex_text = my_font.render("t-rex", True, "blue")
                exit_text = my_font.render("exit game", True, "red")

            research_text = my_small_font.render(f"research points: {flask}", True, "yellow")

            screen.blit(triceratops_text, (125,0))
            screen.blit(trex_text, (225,100))
            screen.blit(exit_text, (125,200))
            pygame.display.flip()
        
        elif pause_menu:
            if cursor_down and cursor < 2:
                cursor += 1
                cursor_down = False

            if cursor_up and cursor > 0:
                cursor -= 1
                cursor_up = False

            if cursor == 0:
                resume_text = my_font.render("resume", True, "red")
                market_text = my_font.render("goto market", True, "blue")
                exit_text = my_font.render("exit game", True, "blue")

            elif cursor == 1:
                resume_text = my_font.render("resume", True, "blue")
                market_text = my_font.render("goto market", True, "red")
                exit_text = my_font.render("exit game", True, "blue")

            elif cursor == 2:
                resume_text = my_font.render("resume", True, "blue")
                market_text = my_font.render("goto market", True, "blue")
                exit_text = my_font.render("exit game", True, "red")

            research_text = my_small_font.render(f"research points: {flask}", True, "yellow")

            screen.blit(resume_text, (200,0))
            screen.blit(market_text, (75,100))
            screen.blit(exit_text, (125,200))
            screen.blit(research_text, (25,400))
            pygame.display.flip()
            
        else:
            timer += 1
            if timer == 60:
                timer = 0
                    
            # draw terrain
            for y, row in enumerate(map_data):
                for x, tile in enumerate(row):
                    if tile:
                        display.blit(grass_img, (150 + x * 10 - y * 10, 100 + x * 5 + y * 5))

            # dino ai
            direction = random.randint(1,4)

            for dino in dino_data:
                if dino[0] == 0 and dino[1] == 11:
                    dino[1] -= 1

                if dino[1] == 0 and dino[0] == 11:
                    dino[0] -= 1

                if direction == 1 and dino[0] > 0 and dino[1] > 0:
                    dino[0] -= 1

                if direction == 2 and dino[0] < 11 and dino[1] < 11:
                    dino[0] += 1

                if direction == 3 and dino[0] > 0 and dino[1] > 0:
                    dino[1] -= 1

                if direction == 4 and dino[0] < 11 and dino[1] < 11:
                    dino[1] += 1

            # scientist ai
            if len(poop_data) > 0:
                if poop_data[0][0] < scientist_data[0]:
                    scientist_data[0] -= 1
                elif poop_data[0][1] < scientist_data[1]:
                    scientist_data[1] -= 1
                elif poop_data[0][0] > scientist_data[0]:
                    scientist_data[0] += 1
                elif poop_data[0][1] > scientist_data[1]:
                    scientist_data[1] += 1
                elif list(poop_data[0]) == scientist_data and len(poop_data) > 0:
                    poop_data.pop(0)
                    flask += 1

            elif len(poop_data) == 0:
                direction = random.randint(1,4)

                if scientist_data[0] == 0 and scientist_data[1] == 11:
                    scientist_data[1] -= 1

                if scientist_data[1] == 0 and scientist_data[0] == 11:
                    scientist_data[0] -= 1

                if direction == 1 and scientist_data[0] > 0 and scientist_data[1] > 0:
                    scientist_data[0] -= 1

                if direction == 2 and scientist_data[0] < 11 and scientist_data[1] < 11:
                    scientist_data[0] += 1

                if direction == 3 and scientist_data[0] > 0 and scientist_data[1] > 0:
                    scientist_data[1] -= 1

                if direction == 4 and scientist_data[0] < 11 and scientist_data[1] < 11:
                    scientist_data[1] += 1

            # poop
            for dino in dino_data:
                poop = random.randint(1,15)
                if poop == 1:
                    already_pooped = False
                    for terd in poop_data:
                        if terd == dino:
                            already_pooped = True
                            break
                    if not already_pooped:
                        poop_data.append((dino[0],dino[1]))
            
            # draw research points
            research_text = my_small_font.render(f"research points: {flask}", True, "yellow")
            display.blit(research_text, (25,25))

            # draw poop B)
            for y, row in enumerate(map_data):
                for x, tile in enumerate(row):
                    for terd in poop_data:
                        if x == terd[0] and y == terd[1]:
                            display.blit(poop_img, (150 + x * 10 - y * 10  + (grass_img.get_width() - poop_img.get_width()) // 2, 100 + x * 5 + y * 5 - poop_img.get_height() + 15))

            # draw scientist
            for y, row in enumerate(map_data):
                for x, tile in enumerate(row):
                    if [x,y] == scientist_data:
                        display.blit(scientist_img, (150 + x * 10 - y * 10  + (grass_img.get_width() - scientist_img.get_width()) // 2, 100 + x * 5 + y * 5 - scientist_img.get_height() + 15))
            
            # draw dinosaurs
            for y, row in enumerate(map_data):
                for x, tile in enumerate(row):
                    for dino in dino_data:
                        if [x,y,"triceratops"] == dino:
                            display.blit(triceratops_img, (150 + x * 10 - y * 10  + (grass_img.get_width() - triceratops_img.get_width()) // 2, 100 + x * 5 + y * 5 - triceratops_img.get_height() + 15))
                        
                        if [x,y,"trex"] == dino:
                            display.blit(trex_img, (150 + x * 10 - y * 10  + (grass_img.get_width() - trex_img.get_width()) // 2, 100 + x * 5 + y * 5 - trex_img.get_height() + 15))

            screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
            pygame.display.flip()

            time.sleep(1)

    pygame.quit()
    sys.exit()

main()
