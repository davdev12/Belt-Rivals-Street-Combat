import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((901, 557))
pygame.display.set_caption("Belt Rivals: Street Combat")
clock = pygame.time.Clock()

bg_surface = pygame.image.load("images/background1.png").convert_alpha()

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

    screen.blit(bg_surface,(0, 0))


    skeleton_rect.x += 2
    if skeleton_rect.left > 900: skeleton_rect.right = 0


    #player_rect.x -= 1
    if player_rect.right < 0: player_rect.left = 901

    screen.blit(skeleton_surf, skeleton_rect)

    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 530: player_rect.bottom = 530
    screen.blit(player_surf, player_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_rect.bottom >= 530:
        player_gravity = -26


    pygame.display.update()
    clock.tick(60)