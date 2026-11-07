import pygame
import os
import random
from pygame.locals import *
from time import *

pygame.init()

score = 0
display_surface = pygame.display.set_mode((1800,1000))

alien_destroyer = pygame.image.load("images/imperial_star_destroyer (1).png")
d = alien_destroyer.get_rect()

player = pygame.image.load("images/realer_lusankya.png")

background = pygame.image.load("images/White_Comet.webp")

g1 = pygame.mixer.Sound(os.path.join('images/gun_1.wav'))
g2 = pygame.mixer.Sound(os.path.join('images/gun_2.wav'))
g3 = pygame.mixer.Sound(os.path.join('images/gun_3.wav'))
g4 = pygame.mixer.Sound(os.path.join('images/gun_4.wav'))

g1.set_volume(0.5)
g2.set_volume(0.5)
g3.set_volume(0.5)
g4.set_volume(0.5)

enemy = pygame.image.load("images/Banana_Throne_Tech_Tree-removebg-modified.png")
e = enemy.get_rect()

b1 = pygame.mixer.Sound(os.path.join('images/banana_chargeup.mp3'))
b2 = pygame.mixer.Sound(os.path.join('images/banana.wav'))

b1.set_volume(0.5)

turbolaser = [g1,g2,g3,g4]

def alien_position():
    d.x = random.randint(900,1600)
    d.y = random.randint(100,900)
    
    return d.x, d.y

e.x = 1150
e.y = 470

game_over = False

player_x = 0
player_y = 500

while player_y < 1000:
    display_surface.blit(background, (0,0))
    display_surface.blit(player,(player_x, player_y))
    display_surface.blit(alien_destroyer, d)

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
        
            if d.collidepoint(event.pos):
                sound = random.choice(turbolaser)
                sound.play()
                score += 1
                d.x, d.y = alien_position()
            else:
                player_x += 100
                display_surface.blit(enemy,e)
                b1.play()
                pygame.time.delay(1500)
                b2.play()
                pygame.time.delay(1250)
                pygame.quit()

    sleep(0.05)
