import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 1000

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lights On/Off")

font = pygame.font.SysFont(None,30)

lightblub = pygame.image.load("images/lightbulbs.jpg")

button = "On"

no_light = (0,0,0)
light = (255,255,255)

running = True

while running:    

    off_button = pygame.Rect(225,250,50,50)

    on_button = pygame.Rect(275,750,50,50)

    if on_button:
        pygame.draw.rect(screen, light, on_button)
        text = font.render("TURN ON", True, no_light)

    else:
        pygame.draw.rect(screen, no_light, off_button)
        text = font.render("TURN OFF", True, light)
    screen.blit(text, (275,750))
    screen.blit(text, (225,250))

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
             running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
        
            if off_button.collidepoint(event.pos):
                button = "Off"
        
            elif on_button.collidepoint(event.pos):
                button = "On"
    

        
    pygame.display.update()
    clock.tick(60)

pygame.quit()