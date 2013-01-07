import pygame
from pygame.locals import *
import nivelDificil
import nivelMedio
import nivelFacil


screen_mode1 =(400, 400)
color_black1= 0,0,0

class ventanaIni:
    def __init__(self):
        pygame.init()
        
        self.screen= pygame.display.set_mode(screen_mode1)
        pygame.display.set_caption("Dificultad")
        self.quit=False
        
    
    def tes(self):
        fuente = pygame.font.Font(None, 25)
        tex="Dicultad del Juego"
        self.mensaje = fuente.render(tex, 1, (140, 150, 155))
        self.screen.blit(self.mensaje,(110,80))#self.x,self.y))
        #pygame.display.update()
    
    def tes1(self):
        fuente = pygame.font.Font(None, 25)
        tex="1.Facil"
        self.mensaje = fuente.render(tex, 1, (140, 150, 155))
        self.screen.blit(self.mensaje,(140,160))
        #self.x,self.y))
        #pygame.display.update()
        
    def tes2(self):
        fuente = pygame.font.Font(None, 25)
        tex="2.Medio"
        self.mensaje = fuente.render(tex, 1, (140, 150, 155))
        self.screen.blit(self.mensaje,(140,220))#self.x,self.y))
        #pygame.display.update()
    
    def tes3(self):
        fuente = pygame.font.Font(None, 25)
        tex="3.Dificil"
        self.mensaje = fuente.render(tex, 1, (140, 150, 155))
        self.screen.blit(self.mensaje,(140,260))#self.x,self.y))
        #pygame.display.update()
        
    
    def tes4(self):
        fuente = pygame.font.Font(None, 25)
        tex="presione la opcion a realizar :P :D"
        self.mensaje = fuente.render(tex, 1, (140, 150, 155))
        self.screen.blit(self.mensaje,(80,320))#self.x,self.y))
        pygame.display.update()
    
    def text(self):
        self.tes()
        self.tes1()
        self.tes2()
        self.tes3()
        self.tes4()
    
    def ingreOpcion(self):
        keys=pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            self.exit()
        if keys[K_1]:
            pygame.display.quit()
            game= nivelFacil.Game()
            game.mainLoop()
        if keys[K_2]:
            pygame.display.quit()
            game= nivelMedio.Game()
            game.mainLoop()
        if keys[K_3]:
            pygame.display.quit()
            game= nivelDificil.Game()
            game.mainLoop()
                
    def main(self):
        while not self.quit:
            keys=pygame.key.get_pressed()
            (self.x,self.y)=pygame.mouse.get_pos()
            (self.posx,self.posy)=(140,160)
            (self.posx1,self.posy1)=(140,220)
            (self.posx2,self.posy2)=(140,260)
            for event in pygame.event.get():
                if event.type==QUIT:
                    self.quit=True
                if keys[K_ESCAPE]:
                    self.exit()
                if keys[K_1]:
                    pygame.display.quit()
                    game= nivelFacil.Game()
                    game.mainLoop()
                if keys[K_2]:
                    pygame.display.quit()
                    game1= nivelMedio.Game()
                    game1.mainLoop()
                if keys[K_3]:
                    pygame.display.quit()
                    game3= nivelDificil.Game()
                    game3.mainLoop()
                if (self.x >= self.posx and self.x <= self.posx + 100) and (self.y >= self.posy and self.y <= self.posy + 50):
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        pygame.display.quit()
                        game4= nivelFacil.Game()
                        game4.mainLoop()
                        
                if (self.x >= self.posx1 and self.x <= self.posx1 + 100) and (self.y >= self.posy1 and self.y <= self.posy1 + 50):
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        pygame.display.quit()
                        game5= nivelMedio.Game()
                        game5.mainLoop()
                       
                if (self.x >= self.posx2 and self.x <= self.posx2 + 100) and (self.y >= self.posy2 and self.y <= self.posy2 + 50):
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        pygame.display.quit()
                        game6= nivelDificil.Game()
                        game6.mainLoop()
            self.text()


            
if __name__ == '__main__':
    venta=ventanaIni()
    venta.main()