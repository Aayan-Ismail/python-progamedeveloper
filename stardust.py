import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 1000

screen = pygame.display.set_mode((WIDTH,HEIGHT))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0,0,0))
    
    pygame.draw.line(screen, (255,255,255),(500,100),(675,600), 10)
    pygame.draw.line(screen, (255,255,255),(500,100),(325,600), 10)
  
    pygame.draw.line(screen, (255,255,255),(675,600),(550,550), 10)
    pygame.draw.line(screen, (255,255,255),(325,600),(450,550), 10)

    pygame.draw.line(screen, (255,255,255),(550,550),(500,500), 10)
    pygame.draw.line(screen, (255,255,255),(450,550),(500,500), 10)
    
    pygame.draw.polygon(screen, (255,255,255), [(250,300), (426.5,300), (395,401)])
    pygame.draw.polygon(screen, (255,255,255), [(570,300), (740.5,300), (605,401)])

    pygame.draw.circle(screen, (220, 230, 255), (500,350), 50)
    pygame.draw.circle(screen, (255,255,255), (500,350), 40)
    pygame.display.update()


pygame.quit()

