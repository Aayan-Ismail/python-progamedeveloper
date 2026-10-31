import pygame
from pygame.locals import *
from time import *

pygame.init()

screen = pygame.display.set_mode((1000,1000))

player = pygame.image.load("images/kenjaku-removebg-preview.png")
background = pygame.image.load("images/amon evil.png")

player_x = 500
player_y = 500

keys = [False, False, False,False]

while player_y < 1000:
    screen.blit(background, (0,0))
    screen.blit(player,(player_x, player_y))

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        
        if event.type == pygame.KEYDOWN:

            if event.key == K_UP:
                keys[0] = True
            
            elif event.key == K_LEFT:
                keys[1] = True

            elif event.key == K_DOWN:
                keys[2] = True
            
            elif event.key == K_RIGHT:
                keys[3] = True

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_UP:
                keys[0] = False
            
            elif event.key == K_LEFT:
                keys[1] = False

            elif event.key == K_DOWN:
                keys[2] = False
            
            elif event.key == K_RIGHT:
                keys[3] = False
    
    if keys[0]:
        if player_y > 0:
            player_y -= 10
    
    elif keys[2]:
        if player_y < 700:
            player_y += 10
    
    if keys[1]:
        if player_x > 0:
            player_x -= 10
    
    elif keys[3]:
        if player_x < 700:
            player_x += 10
    
    player_y += 5
    sleep(0.05)