#Step3, Make the player moving with AWSD keys

import pygame

pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
keep_going = True

#3.1 initial the value of Key and position
key_up=key_down=key_left=key_right = False
player_pos=[130,100] #change the position to list

player = pygame.image.load("images/player.png")

background = pygame.image.load("images/sky.jpg")
cargo = pygame.image.load("images/airballoon.png")

while keep_going:
   
    screen.fill(0)
    screen.blit(background,(0,0))
    # if you image is small, you need use double loop to fill the background
    #for x in range( int(width/background.get_width())+1):
    #    for y in range(int(height/background.get_height())+1):
    #        screen.blit(background,(x*100,y*100))

    screen.blit(cargo,(0,30))
    screen.blit(cargo,(0,135))
    screen.blit(cargo,(0,240))
    screen.blit(cargo,(0,345))

#3.2 set player position use player_pos
    screen.blit(player, player_pos)    
    pygame.display.flip() 
    for event in pygame.event.get():

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
#3.4 - Move player base on the key status
    if key_up:
        player_pos[1]-=1
    elif key_down:
        player_pos[1]+=1
    if key_left:
        player_pos[0]-=1
    elif key_right:
        player_pos[0]+=1



pygame.quit()
exit(0) 