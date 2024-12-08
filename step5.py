#Step5, Add Enemies

import pygame
#from pygame.locals import *
#3 import math
import math
import random

# 1.2 - Initialize the game 
pygame.init()
width, height = 740, 480
screen=pygame.display.set_mode((width, height))
keep_going = True

#3.1 initial the value of Key and position
key_up=key_down=key_left=key_right = False
player_pos=[130,100] #change the position to list

# 1.3 - Load images
player = pygame.image.load("images/player.png")

#2.1 load more images
background = pygame.image.load("images/sky.jpg")
background = pygame.transform.scale(background, (width, height))
cargo = pygame.image.load("images/airballoon.png")

#4 bullets
bullets=[]
bullet = pygame.image.load("images/bullet.png")

#5 enemy
enemyImg = pygame.image.load("images/enemy2.png")
enemys=[[640,100]]
enemySpeed=-0.5
enemyMaxnumber=5

# 1.4 - use loop to keep the game running 
while keep_going:
    # 1.5 - clear the screen before drawing it again
    screen.fill(0)
    
    #2.2 load the background
    screen.blit(background,(0,0))
   
    # if you image is small, you need use double loop to fill the background
    #for x in range( int(width/background.get_width())+1):
    #    for y in range(int(height/background.get_height())+1):
    #        screen.blit(background,(x*100,y*100))
    
    # 2.3 load the cargo
    screen.blit(cargo,(0,30))
    screen.blit(cargo,(0,135))
    screen.blit(cargo,(0,240))
    screen.blit(cargo,(0,345))
    
    #1.6 - draw the screen elements
#3.2 set player position use player_pos

    screen.blit(player, player_pos)
    
#4 - Draw bullet
    index=0
    for bulletPos in bullets:
        
        bulletPos[0]=bulletPos[0]+2
        screen.blit(bullet,bulletPos)

        #remove bullet if out the screen
        if bulletPos[0]<-64 or bulletPos[0]>width or bulletPos[1]<-64 or bulletPos[1]>height:
            bullets.pop(index)  #remove from list
        index+=1
  
 #5 Draw enemy
 
    if(random.randint(1,100)<3 and len(enemys)<enemyMaxnumber):
        #screen.blit(enemy, badguy)
        enemys.append([640, random.randint(50,430)])
        print("enemys length"+str(len(enemys)))
    
    index=0
    for enemyPos in enemys:               
        enemyPos[0]+=enemySpeed
        if enemyPos[0]<50:
            enemys.pop(index)
        screen.blit(enemyImg, enemyPos)
        index+=1   
#end step 5
        
    #1.7 - update the screen
    pygame.display.flip() #faster the .update()
    # 1.8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            keep_going = False
    #3.3 monitor the key down and up
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_w:
                key_up=True
            elif event.key==pygame.K_a:
                key_left=True
            elif event.key==pygame.K_s:
                key_down=True
            elif event.key==pygame.K_d:
                key_right=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                key_up=False
            elif event.key==pygame.K_a:
                key_left=False
            elif event.key==pygame.K_s:
                key_down=False
            elif event.key==pygame.K_d:
                key_right=False
# use mouse down to fire         
        if event.type==pygame.MOUSEBUTTONDOWN or (event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE):
            bullets.append([player_pos[0],player_pos[1]])      
                
    #3.4 - Move player base on the key status
    if key_up and player_pos[1]>0:
        player_pos[1]-=1
    elif key_down and player_pos[1]<height-30:
        player_pos[1]+=1
    if key_left and player_pos[0]>0:
        player_pos[0]-=1
    elif key_right and player_pos[0]<width-100:
        player_pos[0]+=1


#1.9 exit pygame and python
pygame.quit()
exit(0) 