import pygame
from sys import exit
from pathlib import Path

from pygame.examples.music_drop_fade import play_file


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

"""def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 530 and player_direction == 0:
        player_surf = player_jump_fl

    elif player_rect.bottom < 530 and player_direction == 1:
        player_surf = player_jump_fr

    elif player_rect.bottom >= 530 and player_direction == 0:
        player_index += 0.1
        if player_index >= len(player_walk_l): player_index = 0
        player_surf = player_walk_l_1[int(player_index)]"""

def player_animation():
    global player_surf, player_index

    # jump left
    if player_rect.bottom < 530 and player_direction == 0:
        player_surf = player_jump_fl

    # jump right
    elif player_rect.bottom < 530 and player_direction == 1:
        player_surf = player_jump_fr

    elif player_direction == 0 and not keys[pygame.K_a]:
        player_surf = player_pas_wide_l

    elif player_direction == 1 and not keys[pygame.K_d]:
        player_surf = player_pas_wide_r

    # walk left
    elif player_direction == 0 and keys[pygame.K_a]:

        player_index += 0.075

        if player_index >= len(player_walk_l):
            player_index = 0

        player_surf = player_walk_l[int(player_index)]

    elif player_direction == 1 and keys[pygame.K_d]:

        player_index += 0.075

        if player_index >= len(player_walk_r):
            player_index = 0

        player_surf = player_walk_r[int(player_index)]

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

# All player frames:
player_jump_fr = pygame.image.load("images/BlueFist/front_knee_right.png").convert_alpha()
player_jump_fl = pygame.image.load("images/BlueFist/front_knee_left.png").convert_alpha()
player_pas_wide_r = pygame.image.load("images/BlueFist/passive_wide_right.png").convert_alpha()
player_pas_wide_l = pygame.image.load("images/BlueFist/passive_wide_left.png").convert_alpha()
player_walk_r_2 = pygame.image.load("images/BlueFist/walk_r2.png").convert_alpha()
player_walk_r_1 = pygame.image.load("images/BlueFist/walk_r1.png").convert_alpha()
player_walk_r_3 = pygame.image.load("images/BlueFist/walk_r3.png").convert_alpha()
player_walk_r_4 = pygame.image.load("images/BlueFist/walk_r4.png").convert_alpha()
player_walk_l_2 = pygame.image.load("images/BlueFist/walk_l2.png").convert_alpha()
player_walk_l_1 = pygame.image.load("images/BlueFist/walk_l1.png").convert_alpha()
player_walk_l_3 = pygame.image.load("images/BlueFist/walk_l3.png").convert_alpha()
player_walk_l_4 = pygame.image.load("images/BlueFist/walk_l4.png").convert_alpha()
player_walk_l = [player_walk_l_1, player_walk_l_2, player_walk_l_3, player_walk_l_4]
player_walk_r = [player_walk_r_1, player_walk_r_2, player_walk_r_3, player_walk_r_4]
player_index = 0
player_rect = player_pas_wide_l.get_rect(midbottom = (700, 530))
player_gravity = 0

player_direction = 0 # 0 - left, 1- right
if player_direction == 0:
    player_surf =  player_walk_l[player_index]
elif player_direction == 1: player_surf = player_walk_r[player_index]

# health bar
MAX_PLAYER_HEALTH = 8
HIT_COOLDOWN = 700
DAMAGE_BAR_TIME = 350

player_health = MAX_PLAYER_HEALTH
last_hit_time = -HIT_COOLDOWN
health_bar_mode = "stable"
health_bar_mode_started = 0

health_bar_frames = {
    "stable": {},
    "damage": {}
}

for health_bar_path in Path("images/health_bar").glob("hp_*_*.png"):
    _, health_value, health_mode = health_bar_path.stem.split("_")
    health_bar_frames[health_mode][int(health_value)] = pygame.image.load(health_bar_path).convert_alpha()

def get_health_bar_surf(health, mode):
    if health <= 0:
        return health_bar_frames["stable"][0]

    if health not in health_bar_frames[mode]:
        mode = "stable"

    return health_bar_frames[mode][health]

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
            # actual in-game processes:
            if game_state == 1:
                if event.key == pygame.K_w and player_rect.bottom >= 530 and player_direction == 0:
                    player_gravity = -20
                    player_rect.x -= 30
                elif event.key == pygame.K_w and player_rect.bottom >= 530 and player_direction == 1:
                    player_gravity = -20
                    player_rect.x += 30

            if event.key == pygame.K_SPACE:
                if game_state == 0 and arrow_y == 0:

                    game_state = 1
                    player_health = MAX_PLAYER_HEALTH
                    health_bar_mode = "stable"
                    since_start_time = int(pygame.time.get_ticks() / 1000)
                    skeleton_rect.right = 0

               # elif game_state == 1:


                elif game_state == 2:

                    if pygame.time.get_ticks() - since_over_time > 000:
                        game_state = 0

    if game_state == 0:
        screen.blit(startmenu_surf, (0, 0))

        screen.blit(arrow_surf, (0, arrow_y))

    if game_state == 1:
        screen.blit(bg_surf,(0, 0))

        if health_bar_mode == "damage" and pygame.time.get_ticks() - health_bar_mode_started > DAMAGE_BAR_TIME:
            health_bar_mode = "stable"

        screen.blit(get_health_bar_surf(player_health, health_bar_mode), (0, 0))

        # score/time
        # screen.blit(score_surf, score_rect)
        display_time()
        display_score()

        if player_rect.colliderect(skeleton_rect) and pygame.time.get_ticks() - last_hit_time > HIT_COOLDOWN:
            last_hit_time = pygame.time.get_ticks()

            player_health -= 1

            health_bar_mode = "damage"
            health_bar_mode_started = pygame.time.get_ticks()

            if player_health <= 0:
                game_state = 2
                since_over_time = last_hit_time


        #enemy physics
        skeleton_rect.x += 2
        if skeleton_rect.left > 900: skeleton_rect.right = 0

        if keys[pygame.K_a] and player_rect.bottom >= 530:
            player_direction = 0
            player_rect.x -= 5
        if keys[pygame.K_d] and player_rect.bottom >= 530:
            player_direction = 1
            player_rect.x += 5
        #player_rect.x -= 1
        if player_rect.right < 0: player_rect.left = 901

        screen.blit(skeleton_surf, skeleton_rect)

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 530: player_rect.bottom = 530
        player_animation()
        screen.blit(player_surf, player_rect)

    if game_state == 2:
        screen.blit(gameover_surf, (0, 0))

    pygame.display.update()
    clock.tick(60)
