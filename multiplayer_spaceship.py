import pygame 
import os

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

BORDER = pygame.Rect(WIDTH // 2 - 5, 0,10, HEIGHT)

BULLET_HIT_SOUND = pygame.mixer.sound(os.path.join('assets', 'Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.sound(os.path.join('assets', 'Gun+Silencer.mp3'))

BULLET_HIT_SOUND.set_volume(0.5)
BULLET_FIRE_SOUND.set_volume(0.5)

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('assets', 'space_yellow.png')
)

YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(
        YELLOW_SPACESHIP_IMAGE,
        (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    ),
    90
)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('assets', 'space_red.png')
)

RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(
        RED_SPACESHIP_IMAGE,
        (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    ),
    -90
)

SPACE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'SpaceRigThumbnail.png')),
    (WIDTH,HEIGHT)
)

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render(
        "Health: " + str(red_health), True, WHITE
    )
    
    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(yellow_health), True, WHITE
    )

    WIN.blit(
        red_health_text,
        (WIDTH - red_health_text.get_width() - 10, 10)
    )

    WIN.blit(yellow_health_text, (10,10))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    
    pygame.display.update()

def yellow_handle_movement(keys_pressed,yellow):
    
    if keys_pressed[pygame.K_a] and yellow.x > 0:
        yellow.x -= VEL

    if keys_pressed[pygame.K_d] and yellow.x > 0:
        yellow.x -+ VEL

    if keys_pressed[pygame.K_w] and yellow.x > 0:
        yellow.y -= VEL

    if keys_pressed[pygame.K_s] and yellow.x > 0:
        yellow.y += VEL

def red_handle_movement(keys_pressed,red):

    if keys_pressed[pygame.K_LEFT] and red.x > 0:
        red.x -= VEL

    if keys_pressed[pygame.K_RIGHT] and red.x > 0:
        red.x -+ VEL

    if keys_pressed[pygame.K_UP] and red.x > 0:
        red.y -= VEL

    if keys_pressed[pygame.K_DOWN] and red.x > 0:
        red.y += VEL

