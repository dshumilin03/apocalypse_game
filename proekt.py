import pygame
import random
import sys
from os import path
import time
#var
won = False
about = False
paused = False
dead = False
intro = True
sy = 1
sx = 3
pts = 0
bombs = 0
need = 100
shootlimit = 9
meteors = 8
#fonts
pygame.font.init()
smalltext = pygame.font.SysFont("comicsansms", 25)
mediumtext = pygame.font.SysFont("comicsansms", 50)
largetext = pygame.font.SysFont("comicsansms", 75)
#screen
img_dir = path.join(path.dirname(__file__), 'img')
WIDTH = 480
HEIGHT = 600
FPS = 60
#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
D_RED = (200, 0, 0)
GREEN = (0, 255, 0)
D_GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHT_BLUE = (0, 160, 255)

# initialize pygame and create game window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Apocalypse")
clock = pygame.time.Clock()
#sounds
crash_sound = pygame.mixer.Sound("crash.wav")
crash_sound.set_volume(0.08)
pygame.mixer.music.load("march.mp3")
pygame.mixer.music.set_volume(0.2)
laser_sound = pygame.mixer.Sound("laser2.wav")
laser_sound.set_volume(0.2)
pygame.mixer.music.play(-1)
player_crashed = pygame.mixer.Sound("player_crash.wav")
player_crashed.set_volume(0.3)
bomb_sound = pygame.mixer.Sound("charge.wav")
#menu
def menu():
    global about
    global dead
    global intro
    global pts
    global running
    intro = True
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(menu_background, menu_background_rect)
        menu_text = mediumtext.render("Apocalypse", True, LIGHT_BLUE)
        # pygame.draw.rect(screen, GREEN, (180, 155, 122, 45))
        # pygame.draw.rect(screen, RED, (170, 245, 145, 55))
        #pygame.draw.rect(screen, YELLOW, (155, 500, 183, 55))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #print(mouse)
        if 302 >= mouse[0] >= 180 and 200 >= mouse[1] >= 155:
            Play = mediumtext.render("PLAY", True, BLUE)
            screen.blit(Play, [180, 140])
        else:
            Play = mediumtext.render("PLAY", True, LIGHT_BLUE)
            screen.blit(Play, [180, 140])
        if 315 >= mouse[0] >= 170 and 300 >= mouse[1] >= 245:
            Quit = mediumtext.render("QUIT", True, BLUE)
            screen.blit(Quit, [170, 230])
        else:
            Quit = mediumtext.render("QUIT", True, LIGHT_BLUE)
            screen.blit(Quit, [170, 230])
        if 335 >= mouse[0] >= 155 and 547 >= mouse[1] >= 507:
            About = mediumtext.render("ABOUT", True, BLUE)
            screen.blit(About, [155, 490])
        else:
            About = mediumtext.render("ABOUT", True, LIGHT_BLUE)
            screen.blit(About, [155, 490])
        screen.blit(menu_text, [110, 0])

        if click[0] == 1 and 302 >= mouse[0] >= 180 and 200 >= mouse[1] >= 155:
            for s in mobs.sprites():
                s.kill()
            for s in bullets.sprites():
                s.kill()

            player.rect.centerx = WIDTH / 2
            player.rect.bottom = HEIGHT - 10
            spawn()
            intro = False
            dead = False
            pts = 0
            running = True

        elif click[0] == 1 and 315 >= mouse[0] >= 170 and 300 >= mouse[1] >= 245:
            pygame.quit()
            quit()
        else:
            intro = True
            running = False

        if click[0] == 1 and 335 >= mouse[0] >= 155 and 547 >= mouse[1] >= 507:
            about = True
            description()
        pygame.display.update()
        clock.tick(15)
def died():
    global sx
    global sy
    global dead
    dead = True
    sy = 1
    sx = 3
    while dead:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        screen.blit(game_over_img, game_over_img_rect)
        killed = largetext.render("YOU DIED", True, RED)
        screen.blit(killed, [55, 100])
        pygame.display.update()
        clock.tick(15)
        time.sleep(2.5)
        menu()
def pause():
    global paused
    global running
    running = False
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
                    running = True
        pause_text = mediumtext.render("Game is Paused", True, YELLOW)
        screen.blit(pause_text, [65, 150])
        pygame.display.update()
        clock.tick(15)
def score(pts):
    pts_text = smalltext.render("Score: "+str(pts), True, YELLOW)
    screen.blit(pts_text, [0, 0])
    bomb_text = smalltext.render("Bombs available to use: "+str(bombs), True, LIGHT_BLUE)
    screen.blit(bomb_text, [180, 0])
def description():
    global about
    while about:
         mouse = pygame.mouse.get_pos()
         click = pygame.mouse.get_pressed()
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
         screen.blit(about_img, about_img_rect)
         #print(mouse)
         #pygame.draw.rect(screen, YELLOW, (157, 413, 150, 49))

         #one line is about 42 symbols
         about_text = smalltext.render("This game is about space ship that came", True, LIGHT_BLUE)
         screen.blit(about_text, [4, 5])

         about_text1 = smalltext.render("to the meteor rain.", True, LIGHT_BLUE)
         screen.blit(about_text1, [4, 35])

         about_text2 = smalltext.render("To shoot, you must press Space.", True, LIGHT_BLUE)
         screen.blit(about_text2, [4, 85])

         about_text3 = smalltext.render("To shoot the bomb, you must press G", True, LIGHT_BLUE)
         screen.blit(about_text3, [4, 125])

         about_text4 = smalltext.render("Arrows to move left/right.", True, LIGHT_BLUE)
         screen.blit(about_text4, [4, 185])

         about_text5 = smalltext.render("You can pause the game by clicking Esc", True, LIGHT_BLUE)
         screen.blit(about_text5, [4, 225])
         #
         if 307 >= mouse[0] >= 157 and 457 >= mouse[1] >= 417:
            About = mediumtext.render("MENU", True, BLUE)
            screen.blit(About, [155, 400])
         else:
            About = mediumtext.render("MENU", True, LIGHT_BLUE)
            screen.blit(About, [155, 400])

         if click[0] == 1 and 335 >= mouse[0] >= 155 and 457 >= mouse[1] >= 417:
            about = False
            menu()
         #
         pygame.display.update()
         clock.tick(15)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        click = pygame.mouse.get_pressed()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 35))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.radius = 21
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        #hitboxes CBEPXY
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    def shoot(self):
          bullet = Bullet(self.rect.centerx, self.rect.top)
          all_sprites.add(bullet)
          bullets.add(bullet)
    def shoot1(self):
          bomb = seismic(self.rect.centerx, self.rect.top)
          all_sprites.add(bomb)
          bomb5.add(bomb)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = meteor_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width*.85 / 2)
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        #hitboxes CBEPXY
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(sx, sy+7)
        self.speedx = random.randrange(sx-6, sy+2)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(sx, sy+7)

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
class seismic(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bomb_image
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
    def update(self):
        self.rect.y += self.speedy
        #bomb is killing all
        if self.rect.bottom < 0:
            self.kill()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
    def update(self):
        self.rect.y += self.speedy
        # kill if it moves out from screen
        if self.rect.bottom < 0:
            self.kill()
# Load all game graphics
bomb_image = pygame.image.load(path.join(img_dir, "bomb.png")).convert()
background = pygame.image.load(path.join(img_dir, "starfield.png")).convert()
menu_background = pygame.image.load(path.join(img_dir, "71.jpg")).convert()
player_img = pygame.image.load(path.join(img_dir, "playerShip1_orange.png")).convert()
meteor_img = pygame.image.load(path.join(img_dir, "meteorBrown_med1.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "laserRed16.png")).convert()
game_over_img = pygame.image.load(path.join(img_dir, "68.jpg")).convert()
about_img = pygame.image.load(path.join(img_dir, "about.png")).convert()
about_img_rect = about_img.get_rect()
game_over_img_rect = game_over_img.get_rect()
menu_background_rect = menu_background.get_rect()
background_rect = background.get_rect()
bomb_image_rect = bomb_image.get_rect()
explosion_anim = {}
explosion_anim["lg"] = []
explosion_anim["sm"] = []
for i in range(9):
    filename = "regularExplosion0{}.png".format(i)
    img = pygame.image.load(filename).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim["lg"].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim["sm"].append(img_sm)
#
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
def spawn():
    for i in range(meteors):
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
spawn()
def congrats():
    won = True
    while won:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        screen.blit(game_over_img, game_over_img_rect)
        congr = smalltext.render("CONGRATULATIONS", True, RED)
        congr1 = smalltext.render("YOU ARE WINNER", True, RED)
        screen.blit(congr, [130, 50])
        screen.blit(congr1, [145, 100])
        pygame.display.update()
        clock.tick(15)
        time.sleep(5)
        won = False
        menu()
bullets = pygame.sprite.Group()
bomb5 = pygame.sprite.Group()
# Game loop
menu()
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for game over
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and len(bullets) < shootlimit:
                player.shoot()
                pygame.mixer.Sound.play(laser_sound)
            if event.key == pygame.K_g and bombs > 0:
                player.shoot1()
                pygame.mixer.Sound.play(bomb_sound)
                bombs -= 1

            if event.key == pygame.K_ESCAPE:
                pause()
    if need == 0:
        bombs += 1
        need = 100
    if 100 > pts >= 50:
        shootlimit = 8
        if sy + sx == 2:
            sy += 2
    if 150 > pts >= 100:
        shootlimit = 7
        if sy + sx == 4:
            sy += 2
    if 200 > pts >= 150:
        shootlimit = 6
        if sy + sx == 6:
            sy += 1
    if 250 > pts >= 200:
        shootlimit = 5
        if sy + sx == 7:
            sy += 1
    if 300 > pts >= 250:
        shootlimit = 4
        if sy + sx == 9:
            sy += 1
    if pts >= 300:
        shootlimit = 3
        if sy + sx == 11:
            sy += 2
    # Update
    pygame.display.update()
    all_sprites.update()
    # check to see if a bullet hit a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    bomb_hits = pygame.sprite.groupcollide(mobs, bomb5, True, True)
    for hit in bomb_hits:
        for s in mobs.sprites():
                s.kill()

        spawn()
        pts += meteors
        expl = Explosion(hit.rect.center, "lg")
        all_sprites.add(expl)

    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
        pygame.mixer.Sound.play(crash_sound)
        pts += 1
        need -= 1
        expl = Explosion(hit.rect.center, "lg")
        all_sprites.add(expl)
    # check to see if a mob hit the player
    hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
    if hits:
        pygame.mixer.Sound.play(player_crashed)
        running = False
        time.sleep(1)
        died()
        #menu()
    if pts >= 2034:
        running = False
        congrats()

    # Draw and render
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    score(pts)
    # helpful thing
    pygame.display.flip()
pygame.quit()
