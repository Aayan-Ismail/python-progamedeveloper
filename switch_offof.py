import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 1000

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lights On/Off")

font = pygame.font.SysFont(None,30)

#lightblub = pygame.image.load("images/lightbulbs.jpg")

button = "On"

no_light = (0,0,0)
light = (255,255,255)

running = True

while running:

    if button == "On":
        screen.fill(light)
    else:
        screen.fill(no_light)

    on_button = pygame.Rect(250,500,60,60)
    off_button = pygame.Rect(750,500,60,60)

    screen.blit(font.render("TURN ON", True, light), (250,500))
    screen.blit(font.render("TURN OFF", True, no_light), (750,500))

    #if on_button:
        #pygame.draw.rect(screen, light, on_button)
        #text = font.render("TURN ON", True, no_light)

    #else:
        #pygame.draw.rect(screen, no_light, off_button)
       # text2 = font.render("TURN OFF", True, light)

#screen.blit(font.render("Sunny", True, BLACK), (82, 540))

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