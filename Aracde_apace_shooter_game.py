import pygame
import os
from pygame import rect

from pygame.key import key_code

White = (255,255,255)
WIDTH,HEIGHT = 1000,720
s_width,s_height = 55,40
Border_display = pygame.Rect(WIDTH/2-5,0,10,HEIGHT)
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Arcade-space-shooter-2D')

FPS= 60
vel = 5

Yellow_spaceship_image = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
yellow_resized= pygame.transform.rotate(pygame.transform.scale(Yellow_spaceship_image,(s_width,s_height)),90)
red_spaceship_image = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
red_resized = pygame.transform.rotate(pygame.transform.scale(red_spaceship_image,(s_width,s_height)),270)

def draw(red,yellow):
    WIN.fill(White)
    pygame.draw.rect(WIN,(0,0,0),Border_display)
    WIN.blit(yellow_resized,(yellow.x,yellow.y))
    WIN.blit(red_resized,(red.x,red.y))
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

def main():
    red = pygame.Rect(900,300,s_width,s_height)
    yellow = pygame.Rect(100,300,s_width,s_height)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        yellow_handles(keys_pressed,yellow)
        red_handles(keys_pressed,red)        
        draw(red,yellow)
        
        
    pygame.quit()
                
if __name__ == '__main__':
    main()
        