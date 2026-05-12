import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((901, 557))
pygame.display.set_caption("Belt Rivals: Street Combat")
clock = pygame.time.Clock()
game_active = True
keys = pygame.key.get_pressed()

bg_surf = pygame.image.load("images/background1.png").convert_alpha()
gameover_surf = pygame.image.load("images/gameover.PNG").convert_alpha()

skeleton_surf = pygame.image.load("images/skeleton_enemy/skeleton_passive_right.png").convert_alpha()
skeleton_rect = skeleton_surf.get_rect(midbottom = (40, 530) )

player_surf = pygame.image.load("images/BlueFist/passive_wide_left.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (700, 530))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] and player_rect.bottom >= 530:
                player_gravity = -26

            if player_rect.colliderect(skeleton_rect):
                game_active = False
        else:
            screen.blit(gameover_surf, (0, 0))
            skeleton_rect.right = 0
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                game_active = True
    if game_active:
        screen.blit(bg_surf,(0, 0))
        skeleton_rect.x += 2
        if skeleton_rect.left > 900: skeleton_rect.right = 0


        #player_rect.x -= 1
        if player_rect.right < 0: player_rect.left = 901

        screen.blit(skeleton_surf, skeleton_rect)

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 530: player_rect.bottom = 530
        screen.blit(player_surf, player_rect)



    pygame.display.update()
    clock.tick(60)