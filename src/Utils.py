import pygame

class Utils:
    init_pos_x = 50
    init_pos_y = 50
    screen_width = 500
    screen_height = 480
    charact_width = 40
    charact_height = 60
    vel = 5
    run = True
    initCount = 10
    img_list = [x for x in range(10) if x > 0]
    walkRight = [pygame.image.load('../media/R' + str(x) + '.png') for x in img_list]
    walkLeft = [pygame.image.load('../media/L' + str(x) + '.png') for x in img_list]
    clockTick = int(len(img_list)) * 3  # higher is factor, higher is speed animation
    bg_image = pygame.image.load('../media/bg.jpg')
    char = pygame.image.load('../media/standing.png')