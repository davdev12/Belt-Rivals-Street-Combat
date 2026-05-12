import pygame
from sys import exit

def display_time():
    current_time = int(pygame.time.get_ticks() / 1000) - since_start_time
    time_surf = pixel_font.render("time: " + f"{current_time}", False, (64, 64, 64))
    time_rect = time_surf.get_rect(center = (450, 15))
    screen.blit(time_surf, time_rect)
    # print(current_time)

def display_score():
    score_surf = pixel_font.render("score: " + f"{score}", False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (700, 15))
    screen.blit(score_surf, score_rect)
    # print(current_time)

pygame.init()
screen = pygame.display.set_mode((901, 557))
pygame.display.set_caption("Belt Rivals: Street Combat")
clock = pygame.time.Clock()
game_state = 0
score = 0
arrow_y = 0
# timer variables
since_start_time = 0
since_over_time = 0
since_menu_time = 0

keys = pygame.key.get_pressed()
pixel_font = pygame.font.Font("fonts/pixeltype.ttf", 50)

# image definitions
startmenu_surf = pygame.image.load("images/Startmenu.png").convert()
bg_surf = pygame.image.load("images/background1.png").convert()
gameover_surf = pygame.image.load("images/gameover.PNG").convert()
arrow_surf = pygame.image.load("images/choosing_arrow.png").convert_alpha()
# score_surf = pixel_font.render("level", False, ("Black"))
# score_rect = score_surf.get_rect(center = (600, 50))

skeleton_surf = pygame.image.load("images/skeleton_enemy/skeleton_passive_right.png").convert_alpha()
skeleton_rect = skeleton_surf.get_rect(midbottom = (40, 530) )

player_surf = pygame.image.load("images/BlueFist/passive_wide_left.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (700, 530))
player_gravity = 0

while True:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if game_state == 0:

                if event.key == pygame.K_DOWN:
                    arrow_y = 70

                if event.key == pygame.K_UP:
                    arrow_y = 0
            if event.key == pygame.K_SPACE:
                if game_state == 0 and arrow_y == 0:

                    game_state = 1
                    since_start_time = int(pygame.time.get_ticks() / 1000)
                    skeleton_rect.right = 0

               # elif game_state == 1:


                elif game_state == 2:

                    if pygame.time.get_ticks() - since_over_time > 3000:
                        game_state = 0

    if game_state == 0:
        screen.blit(startmenu_surf, (0, 0))

        screen.blit(arrow_surf, (0, arrow_y))

    if game_state == 1:
        screen.blit(bg_surf,(0, 0))

        # score/time
        # screen.blit(score_surf, score_rect)
        display_time()
        display_score()

        if player_rect.colliderect(skeleton_rect):
            game_state = 2
            since_over_time = pygame.time.get_ticks()

        if keys[pygame.K_w] and player_rect.bottom >= 530:
            player_gravity = -26

        #enemy physics
        skeleton_rect.x += 2
        if skeleton_rect.left > 900: skeleton_rect.right = 0


        #player_rect.x -= 1
        if player_rect.right < 0: player_rect.left = 901

        screen.blit(skeleton_surf, skeleton_rect)

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 530: player_rect.bottom = 530
        screen.blit(player_surf, player_rect)

    if game_state == 2:
        screen.blit(gameover_surf, (0, 0))

    pygame.display.update()
    clock.tick(60)