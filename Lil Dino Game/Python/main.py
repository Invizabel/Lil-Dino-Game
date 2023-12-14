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

    cursor_img = pygame.image.load("assets/cursor.png").convert_alpha()
    fence_img = pygame.image.load("assets/fence.png").convert_alpha()
    grass_img = pygame.image.load("assets/grass.png").convert_alpha()
    keeper_img = pygame.image.load("assets/dino_keeper.png").convert_alpha()
    pizza_img = pygame.image.load("assets/pizza.png").convert_alpha()
    poop_img = pygame.image.load("assets/poop.png").convert_alpha()
    rainbow_poop_img = pygame.image.load("assets/rainbow_poop.png").convert_alpha()
    soda_img = pygame.image.load("assets/soda.png").convert_alpha()
    triceratops_img = pygame.image.load("assets/triceratops.png").convert_alpha()
    trex_img = pygame.image.load("assets/trex.png").convert_alpha()
    pygame.font.init()
    my_font = pygame.font.SysFont("times new roman", 50)
    my_small_font = pygame.font.SysFont("times new roman", 25)
    grass_img.set_colorkey((0, 0, 0))
    pygame.mouse.set_visible(False)

    # generate map data
    map_data = []
    for x in range(12):
        new_map_data = []
        for y in range(12):
            new_map_data.append(1)

        map_data.append(new_map_data)

    # generate fence data
    fence_data = []
    for x in range(12):
        new_fence_data = []
        for y in range(12):
            if y == 6 and x <= 6:
                new_fence_data.append(1)

            elif x == 6 and y <= 6:
                new_fence_data.append(1)

            else:
                new_fence_data.append(0)

        fence_data.append(new_fence_data)

    dino_keeper = False
    dino_x = 0
    dino_y = 0
    cursor = 0
    cursor_down = False
    cursor_up = False
    flask = 100
    keeper_x = 0
    keeper_y = 0
    pizza_stand = False
    soda_stand = False
    timer = 0
  
    main_menu = True
    pause_menu = False
    market_menu = False

    dino_data = []
    keeper_data = [keeper_x,keeper_y]
    pizza_data = []
    player_data = [0,0]
    poop_data = []
    soda_data = []

    player_up = False
    player_down = False
    player_left = False
    player_right = False

    while True:
        # timer
        timer += 1
        move_ai = False
        if timer == 10:
            timer = 0
            move_ai = True

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
                            dino_data.append([dino_x, dino_y, "triceratops"])

                        elif cursor == 1:
                            dino_data.append([dino_x, dino_y, "trex"])

                        elif cursor == 2:
                            pygame.quit()
                            sys.exit()

                        cursor = 0

                    elif pause_menu:
                        if cursor == 0:
                            pause_menu = False

                        if cursor == 1:
                            dino_keeper = True
                            pause_menu = False

                        if cursor == 2:
                            market_menu = True
                            pause_menu = False

                        elif cursor == 3:
                            pygame.quit()
                            sys.exit()

                        cursor = 0

                    elif market_menu:
                        if cursor == 0:
                            market_menu = False

                        if cursor == 1 and flask >= 25:
                            pizza_stand = True
                            market_menu = False
                            flask -= 25

                        if cursor == 2 and flask >= 25:
                            soda_stand = True
                            market_menu = False
                            flask -= 25

                        cursor = 0

                    else:
                        if player_data[0] > 6 and pizza_stand or player_data[1] > 6 and pizza_stand:
                            pizza_data.append([player_data[0],player_data[1]])
                            pizza_stand = False
                            
                        else:
                            for count, terd in enumerate(poop_data):
                                if terd[0] == player_data[0] and terd[1] == player_data[1] and terd[2]:
                                    poop_data.pop(count)
                                    flask += 100
                                    break

                                elif terd[0] == player_data[0] and terd[1] == player_data[1] and not terd[2]:
                                    poop_data.pop(count)
                                    flask += 1
                                    break
                                
                if event.key == K_UP or event.key == K_w:
                    if main_menu or pause_menu or market_menu:
                        cursor_up = True
                        
                    else:
                        player_up = True
                        player_down = False
                        player_left = False
                        player_right = False
                        
                if event.key == K_DOWN or event.key == K_s:
                    if main_menu or pause_menu or market_menu:
                        cursor_down = True

                    else:
                        player_up = False
                        player_down = True
                        player_left = False
                        player_right = False

                if event.key == K_LEFT or event.key == K_a:
                    player_up = False
                    player_down = False
                    player_left = True
                    player_right = False

                if event.key == K_RIGHT or event.key == K_d:
                    player_up = False
                    player_down = False
                    player_left = False
                    player_right = True

            if event.type == KEYUP:
                if event.key == K_UP or event.key == K_w or market_menu:
                    if main_menu or pause_menu:
                        cursor_up = False
    
                if event.key == K_DOWN or event.key == K_s:
                    if main_menu or pause_menu or market_menu:
                        cursor_down = False

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

            screen.blit(triceratops_text, (225, 0))
            screen.blit(trex_text, (275, 75))
            screen.blit(exit_text, (225, 150))
            pygame.display.flip()
        
        elif pause_menu:
            if cursor_down and cursor < 3:
                cursor += 1
                cursor_down = False

            if cursor_up and cursor > 0:
                cursor -= 1
                cursor_up = False

            if cursor == 0:
                resume_text = my_font.render("resume", True, "red")
                keeper_text = my_font.render("hire dino keeper", True, "blue")
                market_text = my_font.render("goto market", True, "blue")
                exit_text = my_font.render("exit game", True, "blue")

            elif cursor == 1:
                resume_text = my_font.render("resume", True, "blue")
                keeper_text = my_font.render("hire dino keeper", True, "red")
                market_text = my_font.render("goto market", True, "blue")
                exit_text = my_font.render("exit game", True, "blue")

            elif cursor == 2:
                resume_text = my_font.render("resume", True, "blue")
                keeper_text = my_font.render("hire dino keeper", True, "blue")
                market_text = my_font.render("goto market", True, "red")
                exit_text = my_font.render("exit game", True, "blue")

            elif cursor == 3:
                resume_text = my_font.render("resume", True, "blue")
                keeper_text = my_font.render("hire dino keeper", True, "blue")
                market_text = my_font.render("goto market", True, "blue")
                exit_text = my_font.render("exit game", True, "red")

            research_text = my_small_font.render(f"research points: {flask}", True, "yellow")

            screen.blit(resume_text, (250, 0))
            screen.blit(keeper_text, (150, 75))
            screen.blit(market_text, (200, 150))
            screen.blit(exit_text, (225, 225))
            screen.blit(research_text, (75, 400))
            pygame.display.flip()

        elif market_menu:
            if cursor_down and cursor < 2:
                cursor += 1
                cursor_down = False

            if cursor_up and cursor > 0:
                cursor -= 1
                cursor_up = False

            if cursor == 0:
                resume_text = my_font.render("resume", True, "red")
                pizza_text = my_font.render("pizza stand | 25 research", True, "blue")
                soda_text = my_font.render("soda stand | 25 research", True, "blue")

            elif cursor == 1:
                resume_text = my_font.render("resume", True, "blue")
                pizza_text = my_font.render("pizza stand | 25 research", True, "red")
                soda_text = my_font.render("soda stand | 25 research", True, "blue")

            elif cursor == 2:
                resume_text = my_font.render("resume", True, "blue")
                pizza_text = my_font.render("pizza stand | 25 research", True, "blue")
                soda_text = my_font.render("soda stand | 25 research", True, "red")

            research_text = my_small_font.render(f"research points: {flask}", True, "yellow")

            screen.blit(resume_text, (250, 0))
            screen.blit(pizza_text, (100, 75))
            screen.blit(soda_text, (100, 150))
            screen.blit(research_text, (75, 400))
            pygame.display.flip()
            
            
        else:
            # player
            if player_up and player_data[1] > 0:
                player_data[1] -= 1
                player_up = False

            if player_down and player_data[1] < 11:
                player_data[1] += 1
                player_down = False

            if player_left and player_data[0] > 0:
                player_data[0] -= 1
                player_left = False

            if player_right and player_data[0] < 11:
                player_data[0] += 1
                player_right = False

            if move_ai:
                # dino ai
                direction = random.randint(1,4)
                for dino in dino_data:
                    if dino[0] == 0 and dino[1] == 5:
                        dino[1] -= 1

                    if dino[1] == 0 and dino[0] == 5:
                        dino[0] -= 1

                    if direction == 1 and dino[0] > 0 and dino[1] > 0:
                        dino[0] -= 1

                    if direction == 2 and dino[0] < 5 and dino[1] < 5:
                        dino[0] += 1

                    if direction == 3 and dino[0] > 0 and dino[1] > 0:
                        dino[1] -= 1

                    if direction == 4 and dino[0] < 5 and dino[1] < 5:
                        dino[1] += 1

                if dino_keeper:
                    # dino keeper ai
                    if len(poop_data) > 0:
                        if poop_data[0][0] < keeper_data[0]:
                            keeper_data[0] -= 1

                        elif poop_data[0][1] < keeper_data[1]:
                            keeper_data[1] -= 1

                        elif poop_data[0][0] > keeper_data[0]:
                            keeper_data[0] += 1

                        elif poop_data[0][1] > keeper_data[1]:
                            keeper_data[1] += 1

                        elif poop_data[0][0] == keeper_data[0] and poop_data[0][1] == keeper_data[1] and len(poop_data) > 0:
                            if poop_data[0][2]:
                                flask += 100

                            else:
                                flask += 1
                            poop_data.pop(0)
                            

                    elif len(poop_data) == 0:
                        direction = random.randint(1,4)

                        if keeper_data[0] == 0 and keeper_data[1] == 5:
                            keeper_data[1] -= 1

                        if keeper_data[1] == 0 and keeper_data[0] == 5:
                            keeper_data[0] -= 1

                        if direction == 1 and keeper_data[0] > 0 and keeper_data[1] > 0:
                            keeper_data[0] -= 1

                        if direction == 2 and keeper_data[0] < 5 and keeper_data[1] < 5:
                            keeper_data[0] += 1

                        if direction == 3 and keeper_data[0] > 0 and keeper_data[1] > 0:
                            keeper_data[1] -= 1

                        if direction == 4 and keeper_data[0] < 5 and keeper_data[1] < 5:
                            keeper_data[1] += 1

                # poop
                for dino in dino_data:
                    poop = random.randint(1,15)
                    if poop == 1:
                        special_poop = random.randint(1,1000)
                        already_pooped = False
                        for terd in poop_data:
                            if terd == dino:
                                already_pooped = True
                                break

                        if not already_pooped:
                            if special_poop == 1:
                                poop_data.append([dino[0], dino[1], True])

                            else:
                                poop_data.append([dino[0], dino[1], False])
                                
            # draw terrain
            for y, row in enumerate(map_data):
                for x, tile in enumerate(row):
                    if tile:
                        display.blit(grass_img, (150 + x * 10 - y * 10, 100 + x * 5 + y * 5))

            # draw fences
            for y, row in enumerate(fence_data):
                for x, tile in enumerate(row):
                    if tile:
                        display.blit(fence_img, (150 + x * 10 - y * 10, 100 + x * 5 + y * 5))
                        
            # draw research points
            research_text = my_small_font.render(f"research points: {flask}", True, "yellow")
            display.blit(research_text, (25, 25))

            # draw poop B)
            for y, row in enumerate(map_data):
                for x, tile in enumerate(row):
                    for terd in poop_data:
                        if x == terd[0] and y == terd[1] and terd[2] == True:
                            display.blit(rainbow_poop_img, (150 + x * 10 - y * 10  + (grass_img.get_width() - poop_img.get_width()) // 2, 100 + x * 5 + y * 5 - poop_img.get_height() + 15))

                        elif  x == terd[0] and y == terd[1] and terd[2] == False:
                            display.blit(poop_img, (150 + x * 10 - y * 10  + (grass_img.get_width() - poop_img.get_width()) // 2, 100 + x * 5 + y * 5 - poop_img.get_height() + 15))

            # draw dino keeper
            if dino_keeper:
                for y, row in enumerate(map_data):
                    for x, tile in enumerate(row):
                        if [x, y] == keeper_data:
                            display.blit(keeper_img, (150 + x * 10 - y * 10  + (grass_img.get_width() - keeper_img.get_width()) // 2, 100 + x * 5 + y * 5 - keeper_img.get_height() + 15))
            
            # draw dinosaurs
            for y, row in enumerate(map_data):
                for x, tile in enumerate(row):
                    for dino in dino_data:
                        if [x, y, "triceratops"] == dino:
                            display.blit(triceratops_img, (150 + x * 10 - y * 10  + (grass_img.get_width() - triceratops_img.get_width()) // 2, 100 + x * 5 + y * 5 - triceratops_img.get_height() + 15))
                        
                        if [x, y, "trex"] == dino:
                            display.blit(trex_img, (150 + x * 10 - y * 10  + (grass_img.get_width() - trex_img.get_width()) // 2, 100 + x * 5 + y * 5 - trex_img.get_height() + 15))

            # draw pizza stands
            for y, row in enumerate(map_data):
                for x, tile in enumerate(row):
                    for food in pizza_data:
                        if food[0] == x and food[1] == y:
                            display.blit(pizza_img, (150 + x * 10 - y * 10  + (grass_img.get_width() - pizza_img.get_width()) // 2, 100 + x * 5 + y * 5 - pizza_img.get_height() + 15))
                            break

            # draw cursor
            for y, row in enumerate(map_data):
                for x, tile in enumerate(row):
                    if [x, y] == player_data:
                        display.blit(cursor_img, (150 + x * 10 - y * 10  + (grass_img.get_width() - cursor_img.get_width()) // 2, 100 + x * 5 + y * 5 - cursor_img.get_height() + 15))
                        if pizza_stand:
                            display.blit(pizza_img, (150 + x * 10 - y * 10  + (grass_img.get_width() - pizza_img.get_width()) // 2, 100 + x * 5 + y * 5 - pizza_img.get_height() + 15))
                            
                        if soda_stand:
                            display.blit(soda_img, (150 + x * 10 - y * 10  + (grass_img.get_width() - soda_img.get_width()) // 2, 100 + x * 5 + y * 5 - soda_img.get_height() + 15))

            time.sleep(0.1)
            screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
            pygame.display.flip()

    pygame.quit()
    sys.exit()

main()
