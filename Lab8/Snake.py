import pygame
import random
import time
import colors as clr 
c = 20
pygame.init()

colors = [(240,240,240),(255,255,255)]
food_stash = []
fps = 2
#class for defining position of objects
class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'({self.x},{self.y})'
    def __eq__(self,pt):
        return (self.x ==pt.x) and (self.y == pt.y)
    def Out_range(self):# for finding is point out of screen
            return not (self.x>=0 and self.x<=31 and self.y>=0 and self.y<=21)
#main class which will make actions
class snake:
    def __init__(self):
        self.body = [point(16,11),point(17,11),point(18,11)]
        self.dx = -1
        self.dy = 0
        self.score = 0
        self.lvl = 1
    def move(self):
        global fps
        head = point(self.body[0].x+self.dx,self.body[0].y+self.dy)
        #finding collision for snake
        if head.Out_range() or self.check_in(head,1):
            return False    

        self.body.insert(0,head)
        #if food is not eaten snake moves, else it grows
        if self.body[0] != food_stash[0].pos:
            self.body.pop()
        else:
            self.score+=1
            self.lvl = 1+ self.score//3.4
            food_stash[0].reincarnate(self)
            #increasing speed
            fps = 1+self.lvl
        return True

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(scr,clr.colorRED,(head.x*c,head.y*c,c,c))
        for seg in self.body[1:]:
            pygame.draw.rect(scr,clr.colorGRAY,(seg.x*c,seg.y*c,c,c))
    def check_in(self,pos,posit = 0):
        #cheking is point in some range of the snake
        if pos in self.body[posit:]:
            return True
        else:
            return False
#helpfull class for growing
class food:
    def __init__(self,color,snk):
        self.color = color
        x = random.randint(0,31)
        y = random.randint(0,21)
        self.pos = point(x,y)
        # if food is summoned on snake or other food recreate it
        while snk.check_in(self.pos):
            x = random.randint(0,31)
            y = random.randint(0,21)
            self.pos = point(x,y)
    def draw(self):
        pygame.draw.rect(scr,self.color,(self.pos.x*c,self.pos.y*c,c,c))        

    def reincarnate(self,snk):
        #changing position for food
        self.__init__(self.color,snk)


scr = pygame.display.set_mode((640,540))

work = True

height = scr.get_height()
width = scr.get_width()

clock = pygame.time.Clock()
snakc = snake()
food_stash.append(food(clr.colorRED,snakc))
while work:
    for EVEEENT in pygame.event.get():
        if EVEEENT.type == pygame.QUIT:
            work = False
        if EVEEENT.type == pygame.KEYDOWN:
            if EVEEENT.key == pygame.K_ESCAPE:
                pygame.quit()
                work = False
                break
            if EVEEENT.key == pygame.K_SPACE:
                pass
            if EVEEENT.key == pygame.K_a:
                if snakc.dy:
                    snakc.dy,snakc.dx = 0,-1                                       
            if EVEEENT.key == pygame.K_w:
                if snakc.dx:
                    snakc.dy,snakc.dx = -1,0                                       
            if EVEEENT.key == pygame.K_s:
                if snakc.dx:
                    snakc.dy,snakc.dx = 1,0                                       
            if EVEEENT.key == pygame.K_d:
                if snakc.dy:
                    snakc.dy,snakc.dx = 0,1                                       
    # for myself, so i will work faster
    if not work:
        break
    #drawing field of game
    pygame.draw.rect(scr,clr.colorWHITE,pygame.Rect(0,0,640,480))
    pygame.draw.rect(scr,clr.colorBLACK,pygame.Rect(0,480,640,60))
    #returns false if snake is dead
    if not snakc.move():
        work = 0
    #drawing food
    food_stash[0].draw()
    snakc.draw()
    # drawing info of game irl
    font  = pygame.font.SysFont('Verdana',20)
    score = font.render('Score:'+str(snakc.score),True,clr.colorRED)
    lvl = font.render('Level:'+str(snakc.lvl),True,clr.colorRED)
    scr.blit(score,(20,490))
    scr.blit(lvl,(20,510))
    pygame.display.flip()
    clock.tick(fps)
else:
    #gently stopping the game
    font = pygame.font.SysFont('Verdana',60)
    GO_text = font.render("GAME OVER",True,clr.colorRED)
    scr.blit(GO_text,(125,225))
    pygame.display.flip()
    time.sleep(3)
