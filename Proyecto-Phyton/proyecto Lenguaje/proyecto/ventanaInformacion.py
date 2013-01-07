import pygame
import sys
import ventanaInicial
from pygame.locals import *

SCREEN_WIDTH =510
SCREEN_HEIGHT = 555

#510 555
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("informacion")
    fuente = pygame.font.Font(None, 25)
    imagen=pygame.image.load("botones/InstruccionI.png")
    screen.blit(imagen,(0,0))
    
    pygame.display.flip()
    
    while True:
        
        for event in pygame.event.get():
            keys=pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                sys.exit()
            if keys[K_ESCAPE]:
                ext=ventanaInicial.ventanaIni()
                ext.main()
                pygame.display.quit()
            


if __name__ == "__main__":
    main()
