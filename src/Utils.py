import pygame

class Utils:
    #Class attributes (static)
    init_pos_x = 200
    init_pos_y = 410
    enemy_init_pos_x = 100
    enemy_init_pos_y = 410
    screen_width = 500
    screen_height = 480
    charact_width = 40
    charact_height = 60
    enemy_width = 64
    enemy_height = 64
    initCount = 10
    vel = 5
    enemyVel = 3
    numMaxBullet = 5
    img_list = [x for x in range(10) if x > 0]
    img_list_enemy = [x for x in range(11) if x > 0]
    walkRight = [pygame.image.load('../media/R' + str(x) + '.png') for x in img_list]
    walkLeft = [pygame.image.load('../media/L' + str(x) + '.png') for x in img_list]
    walkRightE = [pygame.image.load('../media/R' + str(x) + 'E.png') for x in img_list_enemy]
    walkLeftE = [pygame.image.load('../media/L' + str(x) + 'E.png') for x in img_list_enemy]
    clockTick = int(len(img_list)) * 3  # higher is factor, higher is speed animation
    clockTickEnemy = int(len(img_list_enemy)) * 3  # higher is factor, higher is speed animation
    bg_image = pygame.image.load('../media/bg.jpg')
    char = pygame.image.load('../media/standing.png')
