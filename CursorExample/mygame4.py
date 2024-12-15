import pygame
import random
import os

# Initialize Pygame and Pygame sound mixer
pygame.init()
pygame.mixer.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shooting Game")
clock = pygame.time.Clock()

# Load all images
# Load and scale background
background = pygame.image.load('sky.jpg').convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load game images
player_img = pygame.image.load('player.png').convert_alpha()
bullet_img = pygame.image.load('bullet.png').convert_alpha()
enemy_img = pygame.image.load('enemy1.png').convert_alpha()

# Scale images
player_img = pygame.transform.scale(player_img, (50, 50))
bullet_img = pygame.transform.scale(bullet_img, (50, 10))  # Horizontal bullet
enemy_img = pygame.transform.scale(enemy_img, (40, 40))

# Load explosion animation images
explosion_anim = []
for i in range(9):
    filename = f'Explosion0{i}.png'
    img = pygame.image.load(filename).convert_alpha()
    img = pygame.transform.scale(img, (50, 50))
    explosion_anim.append(img)

# Load sounds
shoot_sound = pygame.mixer.Sound('pew.wav')
explosion_sound = pygame.mixer.Sound('expl.wav')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.left = 10
        self.rect.centery = SCREEN_HEIGHT // 2
        self.speed_y = 0

    def update(self):
        self.speed_y = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.speed_y = -5
        if keys[pygame.K_DOWN]:
            self.speed_y = 5
        
        self.rect.y += self.speed_y
        
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.centery = y
        self.speed_x = 10

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left > SCREEN_WIDTH:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + 10
        self.rect.y = random.randrange(SCREEN_HEIGHT - self.rect.height)
        self.speed_x = random.randrange(-6, -1)

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.right < 0:
            self.rect.x = SCREEN_WIDTH + 10
            self.rect.y = random.randrange(SCREEN_HEIGHT - self.rect.height)
            self.speed_x = random.randrange(-6, -1)

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.frame = 0
        self.image = explosion_anim[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50  # Speed of the animation

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

# Create sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
explosions = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Create initial enemies
for i in range(8):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.right, player.rect.centery)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()

    # Update
    all_sprites.update()

    # Check for bullet/enemy collisions
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits:
        explosion_sound.play()
        # Create explosion animation
        expl = Explosion(hit.rect.center)
        all_sprites.add(expl)
        explosions.add(expl)
        # Create new enemy
        score += 10
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # Check for player/enemy collisions
    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        running = False

    # Draw / render
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    
    # Draw score
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()

# Game over screen
screen.blit(background, (0, 0))
game_over_text = font.render(f'Game Over! Final Score: {score}', True, WHITE)
text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
screen.blit(game_over_text, text_rect)
pygame.display.flip()

# Wait a few seconds before closing
pygame.time.wait(3000)

pygame.quit()
