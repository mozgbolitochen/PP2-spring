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
            if EVEEENT.key == pygame.K_UP:
                y-=20
                if y<25:
                    y = 25
                
            if EVEEENT.key == pygame.K_DOWN:
                y+=20
                if y>375:
                    y = 375
            if EVEEENT.key == pygame.K_LEFT:
                x-=20
                if x<25:
                    x = 25
            if EVEEENT.key == pygame.K_RIGHT:
                x+=20
                if x>375:
                    x = 375
        

    keys = pygame.key.get_pressed()
    if ( keys[pygame.K_d]) and x <375 :
        x+=20
        if x>375:
            x = 375
        # x %=400
    if ( keys[pygame.K_a]) and x>25:
        x-=20
        if x<25:
            x = 25
        # x %=400
    if ( keys[pygame.K_s]) and y<375:
        y+=20
        if y>375:
            y = 375
        # y %=400
    if ( keys[pygame.K_w]) and y>25:
        y-=20
        if y<25:
            y = 25
        # y %=400 
    
    scr.fill((255,255,255))
    
    # pygame.draw.circle(scr,ballbgcolor,(x,y),50)
    pygame.draw.circle(scr,(255,0,0),(x,y),25)
    # x1=10000
    # y1=10000
    # if 350<=x:
    #     x1=x-400
    # elif x<=50:
    #     x1=x+400
    # if 350<=y:
    #     y1=y-400
    # elif y<=50:
    #     y1=y+400
    # pygame.draw.circle(scr,ballcolor,(x1,y),50,5)
    # pygame.draw.circle(scr,ballcolor,(x,y1),50,5)
    # pygame.draw.circle(scr,ballcolor,(x1,y1),50,5)
    
    pygame.display.flip()
    clock.tick(200)