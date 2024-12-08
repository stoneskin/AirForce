# step 1, init the game and load image

# 1.1 - Import library
import pygame

# 1.2 - Initialize the game 
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
keep_going = True

# 1.3 - Load images
player = pygame.image.load("images/player.png")

# 1.4 - use loop to keep the game running 
while keep_going:
    # 1.5 - clear the screen before drawing it again
    screen.fill(0)
    #1.6 - draw the screen elements
    screen.blit(player, (100,100))
    #1.7 - update the screen
    pygame.display.flip() # will update the contents of the entire display, and faster than .update()
    # 1.8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            keep_going = False
            

#1.9 exit pygame and python
pygame.quit()
exit(0) 
