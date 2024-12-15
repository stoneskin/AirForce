# AirForce

 This is a simple python game write with pyGame. For educational purpose, I used 3 different way to build the game.

 - [Part 1](https://stoneskin.github.io/AirForce/#part-1-build-game-with-basic-game-loop-and-basic-game-object), Implements with the basic game loop and basic game object.
 - [Part 2](https://stoneskin.github.io/AirForce/Part2_OOO.html#part2-rewrite-the-game-with-oop), Rewrote the code with Object-Oriented Programming (OOP) style.
 - [Part 3](https://stoneskin.github.io/AirForce/CursorExample/#part3-example-of-using-cursor-ai-to-build-a-shotting-game), Use prompts to let the [Cursor AI](https://www.cursor.com/) to build the AirForce game.


## Part2: Rewrite the game with OOP

- [Step1: Create a AirForceGame Class](#step1-create-a-airforcegame-class)

- [Step2: Create a class for Player](#step2-create-a-class-for-player)

- [Step3: Define function for key press and move player](#step3-define-function-for-key-press-and-move-player)    

- [Step4:  Define function for fire bullet and check collision](#step4-define-function-for-fire-bullet-and-check-collision)

- [Step5:  Create a class for Enemy](#step5-create-a-class-for-enemy)         

- [Step6: Define function for enemy move and check collision](#step6-define-function-for-enemy-move-and-check-collision)

- [Step7: Define function for explosion animation](#step7-define-function-for-explosion-animation)

### Step1: Create a AirForceGame Class

  - [source code with step1 OOP](/oopStep1.py)
  - Key changes

    ```python
    # step 1: Create first Class 

    # 1.1 - Import library
    import pygame

    # main class of the Game
    class AirForceGame:
        def __init__(self) -> None:
            pass
        def startGame(self) -> None:
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

    my_game=AirForceGame()

    my_game.startGame()

    exit(0) 
    ```

### Step2: Create a class for Player

  - [source code with step2 OOP](https://github.com/stoneskin/AirForce/blob/main/oopStep2.py)
  - Key changes

    ```python
    class Player:
        img:any=pygame.image.load("images/player.png")

        def __init__(self,x:float,y:float) -> None:
        self.pos:list[float]=[x,y]
        def update(self, screen) ->None:
            screen.blit(self.img, self.pos) 
    ```

### Step3: Define function for key press and move player

  - [source code with step3 OOP](https://github.com/stoneskin/AirForce/blob/main/oopStep3.py) 

    ```python
    class Player:
        img:any=pygame.image.load("images/player.png")
        key_up=key_down=key_left=key_right = False
        speed:float=0.3

        def __init__(self,pos_x,pos_y,screen_W,screen_H) -> None:
        self.pos:list[float]=[pos_x,pos_y]
        self.max_w:int=screen_W-100
        self.max_h:int=screen_H-40
        def update(self,screen):
        self.move()
        screen.blit(self.img, self.pos)       
        
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
            
        def move(self)->None:
            if self.key_up and self.pos[1]>0:
                self.pos[1]-=Player.speed
            elif self.key_down and self.pos[1]<self.max_h:
                self.pos[1]+=Player.speed
            if self.key_left and self.pos[0]>0:
                self.pos[0]-=Player.speed
            elif self.key_right and self.pos[0]<self.max_w:
                self.pos[0]+=Player.speed
                

    ```

### Step4:  Define function for fire bullet and check collision

  - [source code with step4 OOP](https://github.com/stoneskin/AirForce/blob/main/oopStep4py) 
  - Key changes

    ```python
    from typing import Any
    import pygame

    class Bullet:
        bulletImg:Any = pygame.image.load("images/bullet.png")
        pos:list[float]=[0.0,0.1]
        speed:float=0.5
        def __init__(self,pos) -> None:
            self.pos=[pos[0],pos[1]]
        def update(self,screen):
            self.move()
            screen.blit(self.bulletImg,self.pos)
        def move(self):
            self.pos[0]+=self.speed
    ```

    ```python
    # in player class
        def fire(self)->None:
            #fire bullets 
            bullet=Bullet(self.pos)
            self.bullets.append(bullet)

    ```

### Step5:  Create a class for Enemy

  - [source code with step5 OOP](https://github.com/stoneskin/AirForce/blob/main/oopStep5.py)     
  - Key changes

    ```python

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
            
    ```

### Step6:  Define function for enemy move and check collision

  - [source code with step6 OOP](https://github.com/stoneskin/AirForce/blob/mainoopStep6.py)
  - Key changes

    ```python
    # in Bullet and Enemy class
    def getRect(self):
            self.rect.left=self.pos[0]
            self.rect.top=self.pos[1]
            return self.rect
    ```
    ```python
    # in  AirForceGame Class
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
    ```

### Step7:   Define function for explosion animation

  - [source code with step7 OOP](https://github.com/stoneskin/AirForce/blob/main/oopStep7.py) 
  - Key changes
    ```python
    from typing import Any
    import pygame,random

    class ExplosionAnimation:
        __instance = None
        @staticmethod
        def getInstance():
            """ Static access method. """
            if ExplosionAnimation.__instance == None:
                ExplosionAnimation.__instance=ExplosionAnimation()
            return ExplosionAnimation.__instance
        
        def __init__(self) -> None:
            #7 initial load explosion animaton images
            self.explosions=[] # store explosion location and img index [(x,y),i,t] 
            self.explosion_anim=[] #store img for animation
            BLACK = (0, 0, 0)
            #self.explosion_time=60
            for i in range(9):
                filename = 'Explosion0{}.png'.format(i)
                img = pygame.image.load("images/"+ filename).convert()  # convert will create a copy that will draw more quickly on the screen.
                img.set_colorkey(BLACK)
                img= pygame.transform.scale(img, (75, 75))
                self.explosion_anim.append(img)
        def getExplosionImg(self,index:int):
            return self.explosion_anim[index]

    class Explosion:
        Explosion_Time:int=150
        def __init__(self,pos:tuple[int,int]) -> None:
            self.pos:tuple[int,int]=pos
            self.index:int=0
            self.elapse:int=Explosion.Explosion_Time
            self.animation=ExplosionAnimation.getInstance()        
        
        def play(self,screen) -> None:
            if(self.index<9):
                screen.blit(self.animation.getExplosionImg(self.index),self.pos)
                self.elapse-=1
                if(self.elapse<0):
                    self.index+=1
                    self.elapse= Explosion.Explosion_Time           
            

    ```


