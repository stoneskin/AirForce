#Step2, Load background and cargo

# 1.1 - Import library
import pygame

pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
keep_going = True


player = pygame.image.load("images/player.png")

#2.1 load more images
background = pygame.image.load("images/sky.jpg")
cargo = pygame.image.load("images/airballoon.png")


while keep_going:

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
    

    screen.blit(player, (130,100))
    
    pygame.display.flip() 
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            keep_going = False

pygame.quit()
exit(0) 