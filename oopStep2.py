# step 2: Create Player Class

import pygame

class Player:
    img:any=pygame.image.load("images/player.png")

    def __init__(self,x:float,y:float) -> None:
       self.pos:list[float]=[x,y]
    def update(self, screen) ->None:
        screen.blit(self.img, self.pos) 
# main class of the Game
class AirForceGame:
    width, height = 640, 480
    def __init__(self,w,h) -> None:
        bg = pygame.image.load("images/sky.jpg")
        self.background = pygame.transform.scale(bg, (w, h))
        if(w>100):
            self.width=w
        if(h>100):
            self.height=h
        self.player=Player(100,100)

    def startGame(self) -> None:
        # 1.2 - Initialize the game 
        pygame.init()
       
        screen=pygame.display.set_mode((self.width, self.height))
        keep_going = True
        

       
        # 1.4 - use loop to keep the game running 
        while keep_going:
            # 1.5 - clear the screen before drawing it again
            screen.fill(0)
            #1.6 - draw the screen elements
            screen.blit(self.background,(0,0))
            #screen.blit(player, (100,100))
            self.player.update(screen)
            
            #1.7 - update the screen
            pygame.display.flip() # will update the contents of the entire display, and faster than .update()
            # 1.8 - loop through the events
            for event in pygame.event.get():
                # check if the event is the X button
                if event.type==pygame.QUIT:
                    keep_going = False
                    

        #1.9 exit pygame and python
        pygame.quit()

my_game=AirForceGame(500,500)

my_game.startGame()

exit(0) 