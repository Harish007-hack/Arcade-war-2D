import pygame
pygame.init()


def main():
    run = True
    while run:
        for event in pygame.event:
            if event.type == pygame.QUIT:
                run = False
                
if __name__ == '__main__':
    main()
        