import pygame
import random

pygame.init()

scr = pygame.display.set_mode((400,400))
work = True

ballcolor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
bg_color  = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
ballbgcolor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

x = 200
y = 200

clock = pygame.time.Clock()
while work:
    for EVEEENT in pygame.event.get():
        if EVEEENT.type == pygame.QUIT:
            work = False
        if EVEEENT.type == pygame.KEYDOWN:
            if EVEEENT.key == pygame.K_ESCAPE:
                work = False
            if EVEEENT.key == pygame.K_SPACE:
                bg_color  = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                ballcolor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                ballbgcolor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                while ballcolor ==bg_color:
                    ballcolor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                while ballbgcolor ==ballcolor:
                    ballbgcolor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))


    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x+=1
        x %=400
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x-=1
        x %=400

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y+=1
        y %=400

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y-=1
        y %=400 
    
    scr.fill(bg_color)
    
    # pygame.draw.circle(scr,ballbgcolor,(x,y),50)
    pygame.draw.circle(scr,ballcolor,(x,y),50,5)
    x1=10000
    y1=10000
    if 350<=x:
        x1=x-400
    elif x<=50:
        x1=x+400
    if 350<=y:
        y1=y-400
    elif y<=50:
        y1=y+400
    pygame.draw.circle(scr,ballcolor,(x1,y),50,5)
    pygame.draw.circle(scr,ballcolor,(x,y1),50,5)
    pygame.draw.circle(scr,ballcolor,(x1,y1),50,5)
    
    pygame.display.flip()
    clock.tick(100)