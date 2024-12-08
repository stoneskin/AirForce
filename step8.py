#step 8 Load sound

import pygame
#from pygame.locals import *
#3 import math
import math
import random

# 1.2 - Initialize the game 
pygame.init()
pygame.mixer.init()  # for audio 

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
enemyImg = pygame.image.load("images/enemy1.png")
enemyImg=pygame.transform.scale(enemyImg, (75, 75)).convert_alpha()  #use the convert_alpha() method after loading so that the image has per pixel transparency.
enemys=[[640,100]]
enemySpeed=-0.3
enemyMaxnumber=5


#7 initial load explosion animaton images
explosions=[] # store explosion location and img index [(x,y),i,t] 
explosion_anim=[] #store img for animation
BLACK = (0, 0, 0)
explosion_time=60
for i in range(9):
    filename = 'Explosion0{}.png'.format(i)
    img = pygame.image.load("images/"+ filename).convert()  # convert will create a copy that will draw more quickly on the screen.
    img.set_colorkey(BLACK)
    img= pygame.transform.scale(img, (75, 75))
    explosion_anim.append(img)
    
#8 initial load sound
shooting_sound = pygame.mixer.Sound('sounds/pew.wav')
pygame.mixer.music.load('sounds/BG.ogg')
pygame.mixer.music.play(-1) ## makes the gameplay sound in an endless loop

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
    enemy_index=0
    for bulletPos in bullets:
        
        bulletPos[0]=bulletPos[0]+2
        screen.blit(bullet,bulletPos)

        #remove bullet if out the screen
        if bulletPos[0]<-64 or bulletPos[0]>width or bulletPos[1]<-64 or bulletPos[1]>height:
            bullets.pop(enemy_index)  #remove from list
        enemy_index+=1
  
 #5 Draw enemy
 
    if(random.randint(1,100)<3 and len(enemys)<enemyMaxnumber):
        #screen.blit(enemy, badguy)
        enemys.append([640, random.randint(50,430)])
        print("enemys length"+str(len(enemys)))
    
    enemy_index=0
    for enemyPos in enemys:               
        enemyPos[0]+=enemySpeed
        if enemyPos[0]<50:
            enemys.pop(enemy_index)
        screen.blit(enemyImg, enemyPos)
        
    # 6 Check for collistions
        enemyRect=pygame.Rect(enemyImg.get_rect())
        enemyRect.left=enemyPos[0]
        enemyRect.top=enemyPos[1]
        bullet_index=0
        for bulletPos in bullets:
            bulletRect=pygame.Rect(bullet.get_rect()) # get rect of bullet image size
            bulletRect.left=bulletPos[0]
            bulletRect.top=bulletPos[1]            
            if bulletRect.colliderect(enemyRect):
                enemys.pop(enemy_index)
                bullets.pop(bullet_index)
                # step7 play explosion in the location of enemy
                explosions.append([enemyPos,0,explosion_time])
                                
            bullet_index+=1
        enemy_index+=1       
    # end step 6

    #step 7 plan explosion animation
    
    for explosion in explosions:
        if(explosion[1]<9):
            screen.blit(explosion_anim[explosion[1]],explosion[0])
            explosion[2]=explosion[2]-1
            if(explosion[2]<0):     
                explosion[1]=explosion[1]+1
                explosion[2]=explosion_time
                
        else:
            explosions.pop(0) # the first one is always first completed 
        
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
            shooting_sound.play()      # step 8 play the sound when shooting
                
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