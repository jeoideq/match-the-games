import pygame

HEIGHT=600
WIDTH=600
TITLE="MATCH-THE-GAMES"

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill("orange")
    pygame.display.update()






