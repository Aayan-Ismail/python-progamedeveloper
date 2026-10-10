import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 1000

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("on and off switch")

lightblub = pygame.load.image("lighbulbs")