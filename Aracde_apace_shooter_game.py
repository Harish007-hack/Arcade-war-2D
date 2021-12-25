import pygame
import os
from pygame import rect
from pygame.constants import USEREVENT
pygame.font.init()
from pygame.key import key_code

White = (255,255,255)
RED = (255,0,0)
YELLOW = (255,255,0)
WIDTH,HEIGHT = 1000,720
s_width,s_height = 55,40
Border_display = pygame.Rect(WIDTH//2-5,0,10,HEIGHT)
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Arcade-space-shooter-2D')

HEALTH_FONT = pygame.font.SysFont('comicsans',40)
FPS= 60
vel = 5
BULLET_VEL = 7
MAX_BULLETS = 3

YELLOW_HIT = pygame.USEREVENT + 1 
RED_HIT =pygame.USEREVENT + 2

Yellow_spaceship_image = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
yellow_resized= pygame.transform.rotate(pygame.transform.scale(Yellow_spaceship_image,(s_width,s_height)),90)
red_spaceship_image = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
red_resized = pygame.transform.rotate(pygame.transform.scale(red_spaceship_image,(s_width,s_height)),270)

SPACE = pygame.transform.scale( pygame.image.load(os.path.join('Assets','space.png')), (WIDTH,HEIGHT))

def draw(red,yellow,red_bullets,yellow_bullets,red_heath,yellow_heath):
    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN,(0,0,0),Border_display)
    
    red_heath_text = HEALTH_FONT.render("Heath: "+str(red_heath),1, White)
    yellow_heath_text = HEALTH_FONT.render("Heath: "+str(yellow_heath),1, White)
    WIN.blit(red_heath_text,(WIDTH-red_heath_text.get_width()-10,10))
    WIN.blit(yellow_heath_text,(10,10))
    
    WIN.blit(yellow_resized,(yellow.x,yellow.y))
    WIN.blit(red_resized,(red.x,red.y))
    
    
    
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED,bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW,bullet)
    
    pygame.display.update()
    
def  yellow_handles(keys_pressed,yellow):
        if keys_pressed[pygame.K_a] and yellow.x - vel > 0:
            yellow.x -= vel
        if keys_pressed[pygame.K_d] and yellow.x + vel + yellow.width < Border_display.x:
            yellow.x += vel
        if keys_pressed[pygame.K_w] and yellow.y - vel > 0:
            yellow.y -= vel 
        if keys_pressed[pygame.K_s] and yellow.y + vel + yellow.height < HEIGHT - 15:
            yellow.y += vel
    
def red_handles(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x - vel  > Border_display.x+Border_display.width :
            red.x -= vel
    if keys_pressed[pygame.K_RIGHT] and red.x + vel + red.width < WIDTH:
            red.x += vel
    if keys_pressed[pygame.K_UP]  and red.y - vel > 0:
        red.y -= vel
    if keys_pressed[pygame.K_DOWN]and red.y + vel + red.height < HEIGHT - 15:
        red.y += vel
        
        
def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)
            

def main():
    red = pygame.Rect(900,300,s_width,s_height)
    yellow = pygame.Rect(100,300,s_width,s_height)
    
    red_bullets = []
    yellow_bullet = []
    
    red_heath =10
    yellow_heath = 10
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LCTRL and len(yellow_bullet)<MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height//2-2,10,5)
                    yellow_bullet.append(bullet)
                    
                if event.key == pygame.K_RCTRL and len(red_bullets)< MAX_BULLETS:
                    bullet = pygame.Rect(red.x,red.y+red.height//2-2,10,5)
                    red_bullets.append(bullet)
                    
                if event.type == RED_HIT:
                    red_heath -=1
                    
                if event.type == YELLOW_HIT:
                    yellow_heath -= 1
        
        winner_text = ''
                    
        if red_heath <= 0 :
            winner_text = 'Yellow Wins!'
        if yellow_heath <= 0:
            winner_text = 'Red WIns!'
        if winner_text != '':
            pass
        
            
        print(red_bullets,yellow_bullet)            
        keys_pressed = pygame.key.get_pressed()
        yellow_handles(keys_pressed,yellow)
        red_handles(keys_pressed,red)        
        
        handle_bullets(yellow_bullet,red_bullets,yellow,red)
        
        draw(red,yellow,red_bullets,yellow_bullet,red_heath,yellow_heath)
        
        
    pygame.quit()
                
if __name__ == '__main__':
    main()
        