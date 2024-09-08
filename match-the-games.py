import pygame


pygame.init()

HEIGHT=800
WIDTH=800
TITLE="MATCH-THE-GAMES"

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

p1=pygame.image.load("candy_crush.jpg")
p2=pygame.image.load("ludo.png")
p3=pygame.image.load("subway_surfer.jpg")
p4=pygame.image.load("temple_run.jpg")
screen.fill("lightblue")
   

run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            point1=pygame.mouse.get_pos()
            pygame.draw.circle(screen,"white",point1,5,0)

        if event.type==pygame.MOUSEBUTTONUP:
            point2=pygame.mouse.get_pos()
            pygame.draw.circle(screen,"white",point2,5,0)
            pygame.draw.line(screen,"white",point1,point2,5)



    screen.blit(p1,(600,700))
    screen.blit(p2,(600,500))
    screen.blit(p3,(600,300))
    screen.blit(p4,(600,100))
   
    font=pygame.font.SysFont("Arial",40)
    message1=font.render("ludo", True,"black")
    screen.blit(message1,(50,700))
   
        

    message2=font.render("candy crush", True,"black")
    screen.blit(message2,(50,500))
  
  
    message3=font.render("temple run", True,"black")
    screen.blit(message3,(50,300))
  
    
   
    message3=font.render("subway surfer", True,"black")
    screen.blit(message3,(50,100))
   


   
    pygame.display.update()






