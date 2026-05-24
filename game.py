import random
import pygame
from sys import exit
from pathlib import Path

"""class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_fall_l = pygame.image.load("images/BlueFist/fall_left.png").convert_alpha()
        self.player_fall_r = pygame.image.load("images/BlueFist/fall_right.png").convert_alpha()
        self.player_ko_r = pygame.image.load("images/BlueFist/ko_right.png").convert_alpha()
        self.player_ko_l = pygame.image.load("images/BlueFist/ko_left.png").convert_alpha()
        self.player_frontkick_r = pygame.image.load("images/BlueFist/front_kick_right.png").convert_alpha()
        self.player_frontkick_l = pygame.image.load("images/BlueFist/front_kick_left.png").convert_alpha()
        self.player_jump_fr = pygame.image.load("images/BlueFist/front_knee_right.png").convert_alpha()
        self.player_jump_fl = pygame.image.load("images/BlueFist/front_knee_left.png").convert_alpha()
        self.player_pas_wide_r = pygame.image.load("images/BlueFist/passive_wide_right.png").convert_alpha()
        self.player_pas_wide_l = pygame.image.load("images/BlueFist/passive_wide_left.png").convert_alpha()
        player_walk_r_2 = pygame.image.load("images/BlueFist/walk_r2.png").convert_alpha()
        player_walk_r_1 = pygame.image.load("images/BlueFist/walk_r1.png").convert_alpha()
        player_walk_r_3 = pygame.image.load("images/BlueFist/walk_r3.png").convert_alpha()
        player_walk_r_4 = pygame.image.load("images/BlueFist/walk_r4.png").convert_alpha()
        player_walk_l_2 = pygame.image.load("images/BlueFist/walk_l2.png").convert_alpha()
        player_walk_l_1 = pygame.image.load("images/BlueFist/walk_l1.png").convert_alpha()
        player_walk_l_3 = pygame.image.load("images/BlueFist/walk_l3.png").convert_alpha()
        player_walk_l_4 = pygame.image.load("images/BlueFist/walk_l4.png").convert_alpha()
        self.player_walk_l = [player_walk_l_1, player_walk_l_2, player_walk_l_3, player_walk_l_4]
        self.player_walk_r = [player_walk_r_1, player_walk_r_2, player_walk_r_3, player_walk_r_4]
        self.player_fail_l = [player_pas_wide_l, player_fall_l, player_fall_l, player_ko_l, player_ko_l, player_ko_l]
        self.player_fail_r = [player_pas_wide_r, player_fall_r, player_fall_r, player_ko_r, player_ko_r, player_ko_r]
        self.player_index = 0
        self.direction = 0
        self.image = self.player_walk_r[self.player_index]
        self.rect = self.image.get_rect(midbottom = (200, 530))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.bottom >= 530:
            self.rect.x -= 5
        if keys[pygame.K_d] and self.rect.bottom >= 530:
            self.rect.x += 5

    def apply_gravity(self):
        keys = pygame.key.get_pressed()

        # jump
        if self.rect.bottom < 530:
            if self.direction == 0:
                self.image = self.player_jump_fl
            else:
                self.image = self.player_jump_fr

        # idle left
        elif self.direction == 0 and not keys[pygame.K_a]:
            self.image = self.player_pas_wide_l

        # idle right
        elif self.direction == 1 and not keys[pygame.K_d]:
            self.image = self.player_pas_wide_r

        # walk left
        elif keys[pygame.K_a]:
            self.direction = 0

            self.player_index += 0.075

            if self.player_index >= len(self.player_walk_l):
                self.player_index = 0

            self.image = self.player_walk_l[int(self.player_index)]

        # walk right
        elif keys[pygame.K_d]:
            self.direction = 1

            self.player_index += 0.075

            if self.player_index >= len(self.player_walk_r):
                self.player_index = 0

            self.image = self.player_walk_r[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()"""

class Skeleton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global HIT_COOLDOWN, crouching
        HIT_COOLDOWN = 1000
        self.health = 3
        self.speed = 2
        self.normal_speed = 2
        self.slow_speed = 1
        self.knockback = 0
        self.friction = 0.85
        self.last_hit_time = -HIT_COOLDOWN
        self.slow_start_time = 0

        self.index = 0
        self.direction = 0

        self.passive_r = pygame.image.load(
            "images/skeleton_enemy/skeleton_passive_right.png"
        ).convert_alpha()

        self.passive_l = pygame.image.load(
            "images/skeleton_enemy/skeleton_passive_left.png"
        ).convert_alpha()

        self.walk_split_l = pygame.image.load(
            "images/skeleton_enemy/skeleton_walk_split_left.png"
        ).convert_alpha()

        self.walk_split_r = pygame.image.load(
            "images/skeleton_enemy/skeleton_walk_split_right.png"
        ).convert_alpha()

        self.walk_cross_l = pygame.image.load(
            "images/skeleton_enemy/skeleton_walk_crossed_left.png"
        ).convert_alpha()

        self.walk_cross_r = pygame.image.load(
            "images/skeleton_enemy/skeleton_walk_crossed_right.png"
        ).convert_alpha()

        self.sword_up_l = pygame.image.load(
            "images/skeleton_enemy/skeleton_sword_up_left.png"
        ).convert_alpha()

        self.sword_down_l = pygame.image.load(
            "images/skeleton_enemy/skeleton_sword_down_left.png"
        ).convert_alpha()

        self.sword_up_r = pygame.image.load(
            "images/skeleton_enemy/skeleton_sword_up_right.png"
        ).convert_alpha()

        self.sword_down_r = pygame.image.load(
            "images/skeleton_enemy/skeleton_sword_down_right.png"
        ).convert_alpha()

        self.walk_l = [
            self.passive_l,
            self.walk_split_l,
            self.walk_cross_l
        ]

        self.walk_r = [
            self.passive_r,
            self.walk_split_r,
            self.walk_cross_r
        ]

        self.attack_l = [
            self.sword_up_l,
            self.sword_down_l,
            self.passive_l
        ]

        self.attack_r = [
            self.sword_up_r,
            self.sword_down_r,
            self.passive_r
        ]

        self.passive_left = [
            self.passive_l
        ]

        self.passive_right = [
            self.passive_r
        ]
        self.image = self.passive_r
        self.rect = self.image.get_rect(midbottom=(40, 530))

        self.mask = pygame.mask.from_surface(self.image)

    def animation(self):

        self.index += 0.045

        if self.direction == 0:
            frames = self.walk_l

        elif self.direction == 1:
            frames = self.walk_r

        elif self.direction == 2 and not player_dead:
            frames = self.attack_l

        elif self.direction == 3 and not player_dead:
            frames = self.attack_r

        elif self.direction == 2 and player_dead:
            frames = self.passive_left

        elif self.direction == 3 and player_dead:
            frames = self.passive_right

        if self.index >= len(frames):
            self.index = 0

        self.image = frames[int(self.index)]

        # update mask every frame
        self.mask = pygame.mask.from_surface(self.image)

    def move(self, player_rect):

        difference = player_rect.centerx - self.rect.centerx

        # attack range
        if abs(difference) <= 130:

            if difference > 0:
                self.direction = 3
            else:
                self.direction = 2

        # move toward player
        else:

            if difference > 0:
                self.direction = 1
                self.rect.x += self.speed

            else:
                self.direction = 0
                self.rect.x -= self.speed

    def knockback_func(self):

        self.rect.x += self.knockback

        self.knockback *= self.friction

        if abs(self.knockback) < 0.05:
            self.knockback = 0

    def collision(self, player_rect, player_mask):

        global score
        global pending_damage
        global health_bar_mode
        global health_bar_mode_started
        global enemy_amount
        #global HIT_COOLDOWN
        self.offset = (
            self.rect.x - player_rect.x,
            self.rect.y - player_rect.y
        )

        self.collided = player_mask.overlap(self.mask, self.offset)

        if not self.collided:
            return

        if pygame.time.get_ticks() - self.last_hit_time < HIT_COOLDOWN:
            return

        self.last_hit_time = pygame.time.get_ticks()
        self.difference = player_rect.centerx - self.rect.centerx

        if player_attacking and ((attack_direction == 0 and self.difference > 100) or (attack_direction == 1 and self.difference < 100)):

            if player_rect.bottom < 530:
                self.health -= 2
                score += 20
            elif player_rect.bottom >= 530:
                self.health -= 1
                score += 10
            if self.health <= 1:
                enemy_amount += 1
            difference = player_rect.centerx - self.rect.centerx

            if player_rect.bottom < 530:
                if difference > 0:
                    self.knockback = -50
                else:
                    self.knockback = 50
            else:
                if difference > 0:
                    self.knockback = -25
                else:
                    self.knockback = 25

            # crouch kick slows enem
            if player_crouching:
                self.speed = self.slow_speed
                self.slow_start_time = pygame.time.get_ticks()

        elif self.direction in [2, 3]:

            pending_damage = True
            health_bar_mode = "damage"
            health_bar_mode_started = pygame.time.get_ticks()

    def slow(self):

        if self.speed == self.slow_speed:

            if pygame.time.get_ticks() - self.slow_start_time > SLOW_DURATION:
                self.speed = self.normal_speed

    def update(self, player_rect, player_mask):
        global score, current_enemies
        self.slow()

        self.knockback_func()

        self.move(player_rect)

        self.animation()

        self.collision(player_rect, player_mask)

        if self.health <= 0:
            score += 20
            self.kill()
            current_enemies -= 1
def display_time():
    current_time = int(pygame.time.get_ticks() / 1000) - since_start_time
    time_surf = pixel_font.render("time: " + f"{current_time}", False, (64, 64, 64))
    time_rect = time_surf.get_rect(center = (550, 15))
    screen.blit(time_surf, time_rect)
    # print(current_time)

def display_score():
    score_surf = pixel_font.render("score: " + f"{score}", False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (750, 15))
    screen.blit(score_surf, score_rect)
    # print(current_time)

def player_ko():
    global player_surf, player_index, game_state, player_rect

    player_index += 0.025

    if player_direction == 0:

        if player_index >= len(player_fail_l):
            player_index = len(player_fail_l) - 1

        player_surf = player_fail_l[int(player_index)]

    else:

        if player_index >= len(player_fail_r):
            player_index = len(player_fail_r) - 1

        player_surf = player_fail_r[int(player_index)]

    # after 2 seconds go to game over
    if pygame.time.get_ticks() - ko_start_time > 2000:
        game_state = 2



def player_animation():
    global player_surf, player_index, player_crouching

    if player_attacking:
        return

    if keys[pygame.K_s]:
        player_rect.bottom = 530
        if player_direction == 0:
            player_crouching = 1
            player_surf = player_crouch_l
        elif player_direction == 1:
            player_crouching = 1
            player_surf = player_crouch_r
        return

    else: player_crouching = 0
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
icon = pygame.image.load("images/redtech.png").convert_alpha()
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
game_state = 0
score = 0
arrow_y = 0
enemy_amount = 1
current_enemies = 0

skeletons = pygame.sprite.Group()






#player = pygame.sprite.GroupSingle()
#player.add(Player())

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

# All player frames:
player_lowkick_r = pygame.transform.scale(pygame.image.load("images/BlueFist/back_lowkick_right.png"), (310, 310)).convert_alpha()
player_lowkick_l = pygame.transform.scale(pygame.image.load("images/BlueFist/back_lowkick_left.png"), (310, 310)).convert_alpha()
player_crouch_r = pygame.transform.scale(pygame.image.load("images/BlueFist/crouch_right.png"), (310, 310)).convert_alpha()
player_crouch_l = pygame.transform.scale(pygame.image.load("images/BlueFist/crouch_left.png"), (310, 310)).convert_alpha()
player_jumpkick_r = pygame.image.load("images/BlueFist/front_jumpkick_right.png").convert_alpha()
player_jumpkick_l = pygame.image.load("images/BlueFist/front_jumpkick_left.png").convert_alpha()
player_fall_l = pygame.image.load("images/BlueFist/fall_left.png").convert_alpha()
player_fall_r = pygame.image.load("images/BlueFist/fall_right.png").convert_alpha()
player_ko_r = pygame.image.load("images/BlueFist/ko_right.png").convert_alpha()
player_ko_l = pygame.image.load("images/BlueFist/ko_left.png").convert_alpha()
player_frontkick_r = pygame.image.load("images/BlueFist/front_kick_right.png").convert_alpha()
player_frontkick_l = pygame.image.load("images/BlueFist/front_kick_left.png").convert_alpha()
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
player_fail_l = [player_pas_wide_l, player_fall_l, player_ko_l]
player_fail_r = [player_pas_wide_r, player_fall_r, player_ko_r]

crouching = 0
player_index = 0
player_rect = player_pas_wide_l.get_rect(midbottom = (700, 530))
player_gravity = 0
player_attacking = 0
pos_difference = 0
player_dead = False
ko_start_time = 0




#skeleton_knockback = 0

#skeleton_index = 0
#skeleton_direction = 1
"""skeleton_walk_l = [skeleton_pas_l, skeleton_walk_split_l, skeleton_walk_crossed_l]
skeleton_walk_r = [skeleton_pas_r, skeleton_walk_split_r, skeleton_walk_crossed_r]
skeleton_pas_l = [skeleton_sword_up_l, skeleton_sword_down_l, skeleton_pas_l]
skeleton_pas_r = [skeleton_sword_up_r, skeleton_sword_down_r, skeleton_pas_r]"""

player_direction = 0 # 0 - left, 1- right
if player_direction == 0:
    player_surf =  player_walk_l[player_index]
elif player_direction == 1: player_surf = player_walk_r[player_index]

"""if skeleton_direction == 0:
    skeleton_surf =  skeleton_walk_l[skeleton_index]
elif skeleton_direction == 1: skeleton_surf = skeleton_walk_r[skeleton_index]
elif skeleton_direction == 2: skeleton_surf = skeleton_pas_r"""
player_mask = pygame.mask.from_surface(player_surf)
#skeleton_mask = pygame.mask.from_surface(skeleton_surf)
# health bar
MAX_PLAYER_HEALTH = 8
HIT_COOLDOWN = 1000
DAMAGE_BAR_TIME = 350
DAMAGE_DELAY = 0
ATTACK_TIME = 500
ATTACK_COOLDOWN = 600
#SKELETON_HEALTH = 300
#FRICTION = 0.85
player_health = MAX_PLAYER_HEALTH
max_enemies = 6

NORMAL_SKELETON_SPEED = 2
SLOW_SKELETON_SPEED = 1
SLOW_DURATION = 2500  # milliseconds (2 sec)

skeleton_speed = NORMAL_SKELETON_SPEED
slow_start_time = 0
#player hits
last_attack_time = -ATTACK_COOLDOWN

#skeleton hits
last_hit_time = -HIT_COOLDOWN

health_bar_mode = "stable"
health_bar_mode_started = 0
pending_damage = False
attack_start_time = 0


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

                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    arrow_y = 70

                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    arrow_y = 0
            # actual in-game processes:
            if game_state == 1:

                # JUMP left
                if (event.key == pygame.K_w and player_rect.bottom >= 530) and not player_dead and not player_attacking:
                    if player_direction == 0:
                        player_gravity = -20
                        player_rect.x -= 30
                    else:
                        player_gravity = -20
                        player_rect.x += 30
                # KICK
                elif event.key == pygame.K_j and player_rect.bottom >= 530  and player_crouching == 0 and not player_dead:
                    if pygame.time.get_ticks() - last_attack_time >= ATTACK_COOLDOWN:

                        last_attack_time = pygame.time.get_ticks()

                        player_attacking = 1
                        attack_start_time = pygame.time.get_ticks()

                        # LOCK direction during attack
                        attack_direction = player_direction

                        if attack_direction == 0:
                            player_surf = player_frontkick_l
                        else:
                            player_surf = player_frontkick_r

                elif event.key == pygame.K_j and player_rect.bottom < 530  and player_crouching == 0  and not player_dead:
                    if pygame.time.get_ticks() - last_attack_time >= ATTACK_COOLDOWN:

                        last_attack_time = pygame.time.get_ticks()

                        player_attacking = 1
                        attack_start_time = pygame.time.get_ticks()

                        # LOCK direction during attack
                        attack_direction = player_direction

                        if attack_direction == 0:
                            player_surf = player_jumpkick_l
                        else:
                            player_surf = player_jumpkick_r

                            ############### LOW KICK
                elif event.key == pygame.K_j and player_crouching == 1 and not player_dead:
                    if pygame.time.get_ticks() - last_attack_time >= ATTACK_COOLDOWN:

                        last_attack_time = pygame.time.get_ticks()

                        player_attacking = 1
                        attack_start_time = pygame.time.get_ticks()

                        # LOCK direction during attack
                        attack_direction = player_direction

                        if attack_direction == 0:
                            player_surf = player_lowkick_l
                        else:
                            player_surf = player_lowkick_r

            if event.key == pygame.K_SPACE:
                if game_state == 0 and arrow_y == 0:

                    game_state = 1
                    player_health = MAX_PLAYER_HEALTH
                    player_dead = False
                    player_index = 0
                    health_bar_mode = "stable"
                    pending_damage = False
                    since_start_time = int(pygame.time.get_ticks() / 1000)
                    #skeleton_rect.right = 0

               # elif game_state == 1:


                elif game_state == 2:

                    if pygame.time.get_ticks() - since_over_time > 000:
                        game_state = 0

    if game_state == 0:
        screen.blit(startmenu_surf, (0, 0))

        screen.blit(arrow_surf, (0, arrow_y))
    player_mask = pygame.mask.from_surface(player_surf)
    #skeleton_mask = pygame.mask.from_surface(skeleton_surf)

    if game_state == 1:
        screen.blit(bg_surf,(0, 0))
        if enemy_amount > current_enemies and current_enemies < max_enemies:
            current_enemies += 1
            enemy = Skeleton()

            # spread them out
            enemy.rect.centerx = random.randint(-300, -100) or random.randint(1000, 1300)
            skeletons.add(enemy)
        # restore speed after slow expires
        if skeleton_speed == SLOW_SKELETON_SPEED:
            if pygame.time.get_ticks() - slow_start_time > SLOW_DURATION:
                skeleton_speed = NORMAL_SKELETON_SPEED

        if health_bar_mode == "damage" and pygame.time.get_ticks() - health_bar_mode_started > DAMAGE_BAR_TIME:
            health_bar_mode = "stable"
            if pending_damage:
                player_health -= 1
                pending_damage = False
                if player_health <= 0 and not player_dead:
                    player_dead = True
                    ko_start_time = pygame.time.get_ticks()
                    player_index = 0

        screen.blit(get_health_bar_surf(player_health, health_bar_mode), (0, 0))

        # score/time
        # screen.blit(score_surf, score_rect)
        display_time()
        display_score()
        if player_attacking:
            if pygame.time.get_ticks() - attack_start_time > ATTACK_TIME:
                player_attacking = 0

        #offset = (skeleton_rect.x - player_rect.x,
                  #skeleton_rect.y - player_rect.y)

        """if player_mask.overlap(self.mask, self.offset) and pygame.time.get_ticks() - last_hit_time > HIT_COOLDOWN and SKELETON_HEALTH >  0:
            last_hit_time = pygame.time.get_ticks()
            # PLAYER IS ATTACKING

            if player_attacking and SKELETON_HEALTH > 0 and player_rect.bottom >= 530 and player_crouching == 0:
                SKELETON_HEALTH -= 1
                score += 10
                if attack_direction == 0 and pos_difference > 100:
                    skeleton_knockback = -25

                elif attack_direction == 1 and pos_difference < 100:
                    skeleton_knockback = 25
            elif player_attacking and SKELETON_HEALTH > 0 and player_rect.bottom < 535 and player_crouching == 0:
                SKELETON_HEALTH -= 2
                score += 20
                if attack_direction == 0 and pos_difference > 100:
                    skeleton_knockback = -40

                elif attack_direction == 1 and pos_difference < 100:
                    skeleton_knockback = 40
            elif player_attacking and SKELETON_HEALTH > 0 and player_rect.bottom >= 530 and player_crouching == 1:
                SKELETON_HEALTH -= 1
                skeleton_speed = SLOW_SKELETON_SPEED
                slow_start_time = pygame.time.get_ticks()
                score += 10
                if attack_direction == 0 and pos_difference > 100:
                    skeleton_knockback = -15

                elif attack_direction == 1 and pos_difference < 100:
                    skeleton_knockback = 15
            # PLAYER IS NOT ATTACKING
            elif skeleton_direction >= 2:
                if pygame.time.get_ticks() - DAMAGE_DELAY >= 600:
                    pending_damage = True
                    health_bar_mode = "damage"
                    health_bar_mode_started = pygame.time.get_ticks()"""

        """pos_difference = player_rect.centerx - skeleton_rect.centerx"""

        """skeleton_rect.x += skeleton_knockback
        skeleton_knockback *= FRICTION

        if abs(skeleton_knockback) < 0.05:
            skeleton_knockback = 0

        if abs(pos_difference) <= 130:

            if pos_difference > 0:
                skeleton_direction = 2
            else:
                skeleton_direction = 3
        else:
            if pos_difference > 0:
                skeleton_direction = 1
                skeleton_rect.x += skeleton_speed
            else:
                skeleton_direction = 0
                skeleton_rect.x -=  skeleton_speed"""
        #enemy physics
        #

        #if skeleton_rect.left > 900: skeleton_rect.right = 0

        if not player_dead and keys[pygame.K_a] and player_rect.bottom >= 530 and player_attacking == 0 and player_crouching == 0 and not player_rect.left < -600:
            player_direction = 0
            player_rect.x -= 5

        if not player_dead and keys[pygame.K_d] and player_rect.bottom >= 530 and player_attacking == 0 and player_crouching == 0 and not player_rect.right > 1500:
            player_direction = 1
            player_rect.x += 5

        #if not player_dead:
            #skeleton_animation()
        skeletons.update(player_rect, player_mask)
        skeletons.draw(screen)

        # player_rect.x -= 1
        #if player_rect.right < 0: player_rect.left = 901
        #if SKELETON_HEALTH > 0:
            #screen.blit(skeleton_surf, skeleton_rect)


############################################################################
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 530: player_rect.bottom = 530
#################################################################################
        if player_dead:
            player_ko()
        else:
            player_animation()

        if not player_crouching:
            screen.blit(player_surf, player_rect)
        else: screen.blit(player_surf, player_rect.move(0, 50))
        #player.draw(screen)
        #player.update()

    if game_state == 2:
        screen.blit(gameover_surf, (0, 0))

    pygame.display.update()
    clock.tick(60)