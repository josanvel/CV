import pygame
import ventanaDifi
import ventanaInformacion
from pygame.locals import *
from lib2to3.tests.test_main import PY2_TEST_MODULE
from pygame.examples.mask import Sprite
from audiodev import test
from sched import Event
from compiler.ast import Mul
import nivelFacil


screen_mode1 =(300, 350)
color_black1= 0,0,0
class ventanaIni:
    def __init__(self):
        pygame.init()
        self.x=0
        self.y=0
        self.posx=0
        self.posy=0
        self.posx1=0
        self.posy1=0
        self.posx2=0
        self.posy2=0
        
        
        self.screen= pygame.display.set_mode(screen_mode1)
        pygame.display.set_caption("Ventana Inicial")
        self.screen.fill(color_black1)
        self.quit=False
            
    def tes(self):
        fuente = pygame.font.Font(None, 25)
        '''tex="Tutulo del juego"
        self.mensaje = fuente.render(tex, 1, (140, 150, 155))
        '''
        self.tux = pygame.image.load("botones\Titulo.jpg")
        self.screen.blit(self.tux,(60,50))#self.x,self.y))
        #pygame.display.update()
    
    def tes1(self):
        self.tux = pygame.image.load("botones\JuegoNuevoS.jpg")
        self.screen.blit(self.tux,(70,130))
        
        
    def tes2(self):
        self.tux = pygame.image.load("botones\InstruccionesS.jpg")
        self.screen.blit(self.tux,(70,210))
    
    def tes3(self):
        self.tux = pygame.image.load("botones\SalirS.jpg")
        self.screen.blit(self.tux,(70,290))
        pygame.display.update()
        
       
    def tes4(self):
        fuente = pygame.font.Font(None, 25)
        tex="presione la opcion a realizar :P :D"
        self.mensaje = fuente.render(tex, 1, (140, 150, 155))
        self.screen.blit(self.mensaje,(80,320))#self.x,self.y))
        pygame.display.update()
    
    def tes5(self):
        self.tux = pygame.image.load("botones\JuegoNuevo.jpg")
        self.screen.blit(self.tux,(120,130))
        
        
    def tes6(self):
        self.tux = pygame.image.load("botones\Instruccion.jpg")
        self.screen.blit(self.tux,(120,190))
    
    def tes7(self):
        self.tux = pygame.image.load("botones\Salir.jpg")
        self.screen.blit(self.tux,(120,270))
        pygame.display.update()
        
    
    def text(self):
        self.tes()
        self.tes1()
        self.tes2()
        self.tes3()
    
    def ingreOpcion(self):
        keys=pygame.key.get_pressed()
        mouse=pygame.mouse.get_pressed()
        if keys[K_ESCAPE]:
            self.exit()
        if keys[K_1]:
            pygame.display.quit()
            game= ventanaDifi.ventanaIni()
            game.main()
        if keys[K_2]:
            pygame.display.quit()
            game= ventanaInformacion.main()
            
        if keys[K_3]:
            pygame.display.quit()
        if mouse.pygame.event.get():
            pygame.display.quit()
            game= ventanaDifi.ventanaIni()
            game.main()
                
    def main(self):
        while not self.quit:
            keys=pygame.key.get_pressed()
            for event in pygame.event.get():
                (self.x,self.y)=pygame.mouse.get_pos()
                (self.posx,self.posy)=(70,130)
                (self.posx1,self.posy1)=(70,210)
                (self.posx2,self.posy2)=(70,290)
                if event.type==QUIT:
                    self.quit=True
                if keys[K_ESCAPE]:
                    self.exit()
                if keys[K_1]:
                    pygame.display.quit()
                    game= ventanaDifi.ventanaIni()
                    game.main()
                if keys[K_2]:
                    pygame.display.quit()
                    game= ventanaInformacion.main()
                    
                if keys[K_3]:
                    pygame.display.quit()
                if (self.x >= self.posx and self.x <= self.posx + 125) and (self.y >= self.posy and self.y <= self.posy + 45):
                    
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        self.tes5()
                        pygame.display.quit()
                        game4= nivelFacil.Game()
                        game4.mainLoop()
                        
                        
                if (self.x >= self.posx1 and self.x <= self.posx1 + 125) and (self.y >= self.posy1 and self.y <= self.posy1 + 45):
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        self.tes6()
                        pygame.display.quit()
                        game= ventanaInformacion.main()
                       
                if (self.x >= self.posx2 and self.x <= self.posx2 + 125) and (self.y >= self.posy2 and self.y <= self.posy2 + 45):
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        self.tes7()
                        pygame.display.quit()
                
                
            self.text()

            
if __name__ == '__main__':
    venta=ventanaIni()
    venta.main()