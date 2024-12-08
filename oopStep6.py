# step 6: Check the collisions 

from typing import Any
import pygame,random

class Bullet:
    bulletImg = pygame.image.load("images/bullet.png")    
    pos=[0.0,0.1]
    speed=0.5
    def __init__(self,pos) -> None:
        self.pos=[pos[0],pos[1]]
        self.rect=pygame.Rect(self.bulletImg.get_rect())
    def update(self,screen):
        self.move()
        screen.blit(self.bulletImg,self.pos)
    def move(self):
        self.pos[0]+=self.speed
    def getRect(self):
        self.rect.left=self.pos[0]
        self.rect.top=self.pos[1]
        return self.rect

class Player:
    img=pygame.image.load("images/player.png")
    key_up=key_down=key_left=key_right = False
    pos:list[int] =[100,100]
    speed:float=0.3
    max_w:int
    max_h:int
    bullets:list[Bullet]=[]
    def __init__(self,pos_x,pos_y,screen_W,screen_H) -> None:
       self.pos=[pos_x,pos_y]
       self.max_w=screen_W-100
       self.max_h=screen_H-40
    def update(self,screen):
       self.move()
       screen.blit(self.img, self.pos)
       index=0
       for bullet in self.bullets:
           bullet.update(screen)
           if(bullet.pos[0]>640):
               self.bullets.pop(index)
           index+=1
                      
     
    def onKeyEvent(self,event:any) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_w:
                self.key_up=True
            elif event.key==pygame.K_a:
                self.key_left=True
            elif event.key==pygame.K_s:
                self.key_down=True
            elif event.key==pygame.K_d:
                self.key_right=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                self.key_up=False
            elif event.key==pygame.K_a:
                self.key_left=False
            elif event.key==pygame.K_s:
                self.key_down=False
            elif event.key==pygame.K_d:
                self.key_right=False
        if event.type==pygame.MOUSEBUTTONDOWN or (event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE):
            self.fire()            
        
    def move(self)->None:
        if self.key_up and self.pos[1]>0:
            self.pos[1]-=self.speed
        elif self.key_down and self.pos[1]<self.max_h:
            self.pos[1]+=self.speed
        if self.key_left and self.pos[0]>0:
            self.pos[0]-=self.speed
        elif self.key_right and self.pos[0]<self.max_w:
            self.pos[0]+=self.speed
    def fire(self)->None:
        #fire bullets 
        bullet=Bullet(self.pos)
        self.bullets.append(bullet)

class Enemy:
    speed=-0.01
    enemyImg= pygame.image.load("images/enemy1.png")

    def __init__(self,x,y) -> None:        
        self.pos=[x,y]
        self.speed=random.randint(5,10)*self.speed
        self.img = pygame.transform.scale(Enemy.enemyImg, (75, 75)).convert_alpha()
        self.rect=pygame.Rect(self.img.get_rect())
    def update(self,screen):
       self.move()
       screen.blit(self.img, self.pos)
    def move(self):
        self.pos[0]+=self.speed
    def getRect(self):
        self.rect.left=self.pos[0]
        self.rect.top=self.pos[1]
        return self.rect
        
        
# main class of the Game
class AirForceGame:
    width, height = 640, 480
    enemies:list[Enemy]=[]
    enemyMaxnumber:int=5
    
    def __init__(self,w,h) -> None:
        bg = pygame.image.load("images/sky.jpg")
        self.background = pygame.transform.scale(bg, (w, h))
        if(w>100):
            self.width=w
        if(h>100):
            self.height=h
        self.player=Player(100,100,self.width,self.height)
        
    def createEnemy(self):
        if(random.randint(0,1000)==1 and len(self.enemies)<self.enemyMaxnumber):
            enemy:Enemy=Enemy(self.width,random.randint(50,self.height-50))
            self.enemies.append(enemy)

    def updateEnemies(self,screen):
        index=0
        for enemy in self.enemies:               
            enemy.update(screen)
            if(self.checkCollistion(enemy)):
                self.enemies.pop(index) 
            elif enemy.pos[0]<0:
                self.enemies.pop(index)                
            index+=1       
    
    def checkCollistion(self,enemy)->bool:
        enemyRect= enemy.getRect()
        bullet_index=0
        for bullet in  self.player.bullets:
            bulletRect= bullet.getRect()
            if bulletRect.colliderect(enemyRect):
                self.player.bullets.pop(bullet_index)
                return True
            bullet_index+=1
        return False 
          
    def startGame(self):
        # 1.2 - Initialize the game 
        pygame.init()       
       
        screen=pygame.display.set_mode((self.width, self.height))
        keep_going = True
        
        
       
        # 1.4 - use loop to keep the game running 
        while keep_going:
            screen.fill(0)
            screen.blit(self.background,(0,0))
            self.player.update(screen)
            
            self.createEnemy()
            self.updateEnemies(screen)
            
            pygame.display.flip() # will update the contents of the entire display, and faster than .update()
            # 1.8 - loop through the events
            for event in pygame.event.get():
                # check if the event is the X button
                if event.type==pygame.QUIT:
                    keep_going = False
                self.player.onKeyEvent(event) #update player for event 

        
        pygame.quit()

my_game=AirForceGame(500,500)

my_game.startGame()

exit(0) 