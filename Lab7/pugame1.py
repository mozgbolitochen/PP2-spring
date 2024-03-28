import pygame
import random

pygame.init()

scr = pygame.display.set_mode((600,400))
work = True
right = True
up = False
height = scr.get_height()
width = scr.get_width()
ballcolor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
bg_color  = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
ballbgcolor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
projectiles =[]
x = width//2
y = height//2
bulletspeed = 3
bulletradius = 10
ballradius = 50
ballspeed = 1
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
            if EVEEENT.key == pygame.K_j:
                projectiles.append({'x':x-ballradius,'y':y,'up':False,'right':False,'down':False,'left':True})
            if EVEEENT.key == pygame.K_i:
                projectiles.append({'x':x,'y':y-ballradius,'up':True,'right':False,'down':False,'left':False})
            if EVEEENT.key == pygame.K_k:
                projectiles.append({'x':x,'y':y+ballradius,'up':False,'right':False,'down':True,'left':False})
            if EVEEENT.key == pygame.K_l:
                projectiles.append({'x':x+ballradius,'y':y,'up':False,'right':True,'down':False,'left':False})
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x+=1
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x-=1
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y+=1
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y-=1

    # if up:
    #     y-=ballspeed
    # else:
    #     y+=ballspeed
    # if right:
    #     x+=ballspeed
    # else:
    #     x-=ballspeed
    # if width-ballradius<x or x<ballradius :
    #     right = not right
    # if height-ballradius<y or y<ballradius:
    #     up = not up
    
    
    y %=height
    x %=width
    scr.fill(bg_color)
    x1=10000
    y1=10000
    if width-ballradius<=x:
        x1=x-width
    elif x<=ballradius:
        x1=x+width
    if height-ballradius<=y:
        y1=y-height
    elif y<=ballradius:
        y1=y+height
    #           projectiles.append({'x':x,'y':y,'up':False,'right':True,'down':False,'left':False})

    for i in projectiles:
        if i['up']:
            i['y']-=bulletspeed
            if i['y']<-bulletradius:
                projectiles.remove(i)
        if i['down']:
            i['y']+=bulletspeed
            if i['y']>height+bulletradius:
                projectiles.remove(i)
        if i['left']:
            i['x']-=bulletspeed
            if i['x']<-bulletradius:
                projectiles.remove(i)
        if i['right']:
            i['x']+=bulletspeed
            if i['x']>width+bulletradius:
                projectiles.remove(i)
        

        pygame.draw.circle(scr,ballcolor,(i['x'],i['y']),bulletradius)
        
    pygame.draw.circle(scr,ballbgcolor,(x,y),ballradius,ballradius)
    pygame.draw.circle(scr,ballbgcolor,(x1,y),ballradius)
    pygame.draw.circle(scr,ballbgcolor,(x,y1),ballradius)
    pygame.draw.circle(scr,ballbgcolor,(x1,y1),ballradius)
    pygame.draw.circle(scr,ballcolor,(x,y),ballradius,5)
    pygame.draw.circle(scr,ballcolor,(x1,y),ballradius,5)
    pygame.draw.circle(scr,ballcolor,(x,y1),ballradius,5)
    pygame.draw.circle(scr,ballcolor,(x1,y1),ballradius,5)
    
    pygame.display.flip()
    clock.tick(100)