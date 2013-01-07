import pygame
from pygame.locals import *
from lib2to3.tests.test_main import PY2_TEST_MODULE
from pygame.examples.mask import Sprite
from audiodev import test
import nivelDificil
import ventanaInicial

screen_mode =(770, 520)
color_black= 0,0,0
color_Barra=229,142,13
color_R=60,32,190

class Game:
    def __init__ (self):
        pygame.init()
        
        pygame.mixer.init()
        self.screen= pygame.display.set_mode(screen_mode)
        pygame.display.set_caption("juego >P >P")
        self.quit=False
        self.tex="imagen_d\d.png"
        self.sonidoArriba=pygame.mixer.Sound("musica\Arriba.wav")
        self.sonidoAbajo=pygame.mixer.Sound("musica\Abajo.wav")
        self.sonidoDerecha=pygame.mixer.Sound("musica\Derecha.wav")
        self.sonidoIzquierda=pygame.mixer.Sound("musica\Izquierda1.wav")
        self.sonidoError=pygame.mixer.Sound("musica\punch.wav")
        self.sonido=pygame.mixer.Sound("musica\punch.wav")
        self.tux = pygame.image.load(self.tex)
        self.x=30
        self.y=35
        self.puerta=pygame.image.load("puertas/puerta1.jpg")
        self.moneda=pygame.image.load("puertas/moneda.jpg")
        self.sprite1=pygame.sprite.Sprite()
        self.sprite1.imagen = self.tux
        self.sprite1.rect = self.tux.get_rect()
        self.sprite1.rect.top= self.y
        self.sprite1.rect.left= self.x
        self.arreglo_abajo=["imagen\p_1.png","imagen\p_2.png","imagen\p_3.png","imagen\p_4.png","imagen\p_5.png","imagen\p_6.png","imagen\p_7.png","imagen\p_8.png"]
        self.arreglo_derecho=["imagen_d\d.png","imagen_d\d_2.png","imagen_d\d_3.png","imagen_d\d_4.png","imagen_d\d_5.png","imagen_d\d_6.png","imagen_d\d_7.png","imagen_d\d_8.png"]
        self.arreglo_izqui=["imagen_i\i_1.png","imagen_i\i_2.png","imagen_i\i_3.png","imagen_i\i_4.png","imagen_i\i_5.png","imagen_i\i_6.png","imagen_i\i_7.png","imagen_i\i_8.png"]
        self.arreglo_arriba=["imagen_a\u_1.png","imagen_a\u_2.png","imagen_a\u_3.png","imagen_a\u_4.png","imagen_a\u_5.png","imagen_a\u_6.png","imagen_a\u_7.png","imagen_a\u_8.png"]
        self.i=0
        self.j=0
        self.k=0
        self.l=0
        self.oldx=0
        self.oldy=0
         
        
    def iniciarCua(self):
        self.bordeIZ=pygame.Rect(0,90,5,430)
        
        self.bordeD=pygame.Rect(765,30,5,430)
        
        self.bordeS=pygame.Rect(0,30,770,5)
        self.bordeI=pygame.Rect(0,515,770,5)
        
        self.rectangulo1 = pygame.Rect(0,90,120, 10)
        self.rectangulo2 = pygame.Rect(180,30,10,120)
        self.rectangulo3 = pygame.Rect(60,150,130,10)
        
        self.rectangulo4 = pygame.Rect(0,210,250, 10)
        self.rectangulo5 = pygame.Rect(240,90,10, 120)
        
        self.rectangulo6 = pygame.Rect(300,30,10,180)
        self.rectangulo7 = pygame.Rect(300,210,60,10)
        self.rectangulo8 = pygame.Rect(480,270,90,10)
        
        self.rectangulo9 = pygame.Rect(60,270,120,10)
        self.rectangulo10 = pygame.Rect(240,270,180,10)
        self.rectangulo11 = pygame.Rect(120,270,10,60)
        self.rectangulo12 = pygame.Rect(240,270,10,180)
        self.rectangulo13 = pygame.Rect(120,330,120,10)
        
        self.rectangulo14 = pygame.Rect(60,330,10,120)
        self.rectangulo15 = pygame.Rect(60,450,60,10)
        
        self.rectangulo16 = pygame.Rect(60,390,120,10)
        self.rectangulo17 = pygame.Rect(180,390,10,120)
        
        self.rectangulo18 = pygame.Rect(300,330,180,10)
        self.rectangulo19 =  pygame.Rect(300,330,10,120)
        self.rectangulo20 = pygame.Rect(300,450,60,10)
        self.rectangulo21 = pygame.Rect(360,390,60,10)
        self.rectangulo22 = pygame.Rect(410,390,10,120)
        
        self.rectangulo23 = pygame.Rect(360,90,10,60)
        self.rectangulo24 = pygame.Rect(360,150,150,10)
        self.rectangulo25 = pygame.Rect(420,150,10,130)
        self.rectangulo26 = pygame.Rect(420,90,60,10)
        
        self.rectangulo27 = pygame.Rect(570,30,10,120)
        self.rectangulo28 = pygame.Rect(630,90,60,10)
        self.rectangulo29 = pygame.Rect(570,150,60,10)
        self.rectangulo30 = pygame.Rect(480,210,220,10)
        self.rectangulo31 = pygame.Rect(690,90,10,120)
        
        self.rectangulo32 = pygame.Rect(570,270,10,180)
        self.rectangulo33 = pygame.Rect(480,450,150,10)
        
        self.rectangulo34 = pygame.Rect(630,270,10,120)
        self.rectangulo35 = pygame.Rect(630,390,60,10)
        self.rectangulo36 = pygame.Rect(690,390,10,60)
        self.rectangulo37 = pygame.Rect(690,330,70,10)
        self.rectangulo38 = pygame.Rect(690,450,70,10)
        
        
        
    def update(self):
        keys=pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.sprite1.rect.left=self.sprite1.rect.left - 1
            self.tux = pygame.image.load(self.arreglo_izqui[self.j])
            if (self.sprite1.rect.left >=70 and self.sprite1.rect.left <= 110) and (self.sprite1.rect.top >= 80 and self.sprite1.rect.top <= 130):
                self.sonidoIzquierda.play()
            
            if (self.sprite1.rect.left >= 10 and self.sprite1.rect.left <=70) and (self.sprite1.rect.top >= 80 and self.sprite1.rect.top <= 130):
                self.sonidoAbajo.play()
            
            if (self.sprite1.rect.left >= 320 and self.sprite1.rect.left <= 380) and (self.sprite1.rect.top >= 150 and self.sprite1.rect.top <= 200):
                self.sonidoArriba.play()
                
            if (self.sprite1.rect.left >= 475 and self.sprite1.rect.left <= 500) and (self.sprite1.rect.top >= 140 and self.sprite1.rect.top <= 200):
                self.sonidoIzquierda.play()
            
            if (self.sprite1.rect.left >= 440 and self.sprite1.rect.left <= 475) and (self.sprite1.rect.top >= 140 and self.sprite1.rect.top <= 200):
                self.sonidoAbajo.play()
                
            if (self.sprite1.rect.left >= 60 and self.sprite1.rect.left <= 230) and (self.sprite1.rect.top >= 200 and self.sprite1.rect.top <= 250):
                self.sonidoIzquierda.play()
            
            if (self.sprite1.rect.left >= 5 and self.sprite1.rect.left <= 60) and (self.sprite1.rect.top >= 200 and self.sprite1.rect.top <= 250):
                self.sonidoAbajo.play()
            
            if (self.sprite1.rect.left >= 300 and self.sprite1.rect.left <= 440) and (self.sprite1.rect.top >= 250 and self.sprite1.rect.top <= 300):
                self.sonidoIzquierda.play()
            
            if (self.sprite1.rect.left >= 250 and self.sprite1.rect.left <= 300) and (self.sprite1.rect.top >= 250 and self.sprite1.rect.top <= 300):
                self.sonidoAbajo.play()
            
            if self.j==7:
                self.j=0
            self.sprite1.imagen = self.tux
            self.j=self.j+1
            
            
        elif keys[K_RIGHT]:
            self.sprite1.rect.left=self.sprite1.rect.left + 1
            self.tux = pygame.image.load(self.arreglo_derecho[self.i])
            
            if (self.sprite1.rect.left >= 20 and self.sprite1.rect.left <= 110) and (self.sprite1.rect.top >= 35 and self.sprite1.rect.top <= 80):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 110 and self.sprite1.rect.left <= 140) and (self.sprite1.rect.top >= 35 and self.sprite1.rect.top <= 80):
                self.sonidoAbajo.play()
            
            if (self.sprite1.rect.left >= 50 and self.sprite1.rect.left <= 160) and (self.sprite1.rect.top >= 120 and self.sprite1.rect.top <= 180):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 160 and self.sprite1.rect.left <= 210) and (self.sprite1.rect.top >= 120 and self.sprite1.rect.top <= 180):
                self.sonidoArriba.play()
                
            if (self.sprite1.rect.left >= 250 and self.sprite1.rect.left <= 290) and (self.sprite1.rect.top >= 35 and self.sprite1.rect.top <= 80):
                self.sonidoAbajo.play()
                
            if (self.sprite1.rect.left >= 290 and self.sprite1.rect.left <= 340) and (self.sprite1.rect.top >= 200 and self.sprite1.rect.top <= 250):
                self.sonidoDerecha.play()
                
            if (self.sprite1.rect.left >= 340 and self.sprite1.rect.left <=420) and (self.sprite1.rect.top >= 200 and self.sprite1.rect.top <= 250):
                self.sonidoArriba.play()
                
            if (self.sprite1.rect.left >= 430 and self.sprite1.rect.left <= 500) and (self.sprite1.rect.top >= 100 and self.sprite1.rect.top <= 160):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 320 and self.sprite1.rect.left <= 380) and (self.sprite1.rect.top >= 40 and self.sprite1.rect.top <= 100):
                self.sonidoAbajo.play()
            
            if (self.sprite1.rect.left >= 500 and self.sprite1.rect.left <= 550) and (self.sprite1.rect.top >= 100 and self.sprite1.rect.top <= 160):
                self.sonidoAbajo.play()
            
            if (self.sprite1.rect.left >= 475 and self.sprite1.rect.left <= 560) and (self.sprite1.rect.top >= 200 and self.sprite1.rect.top <= 250):
                self.sonidoDerecha.play()
                
            if (self.sprite1.rect.left >= 560 and self.sprite1.rect.left <= 610) and (self.sprite1.rect.top >= 200 and self.sprite1.rect.top <= 250):
                self.sonidoAbajo.play()
            
            if (self.sprite1.rect.left >= 600 and self.sprite1.rect.left <= 660) and (self.sprite1.rect.top >= 390 and self.sprite1.rect.top <= 430):
                self.sonidoAbajo.play()
                
            if (self.sprite1.rect.left >= 60 and self.sprite1.rect.left <= 80) and (self.sprite1.rect.top >= 460 and self.sprite1.rect.top <= 515):
                self.sonidoDerecha.play()
                
            if (self.sprite1.rect.left >= 300 and self.sprite1.rect.left <= 360) and (self.sprite1.rect.top >= 430 and self.sprite1.rect.top <= 500):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 730 and self.sprite1.rect.left <= 750) and (self.sprite1.rect.top >= 460 and self.sprite1.rect.top <= 500):
                pygame.display.quit()
                game= nivelDificil.Game()
                game.mainLoop()
            
            if (self.sprite1.rect.left >= 650 and self.sprite1.rect.left <=700) and (self.sprite1.rect.top >= 165 and self.sprite1.rect.top <= 210):
                pygame.mixer.music.stop()
                ext=ventanaInicial.ventanaIni()
                ext.main()
                pygame.display.quit()
            
            if (self.sprite1.rect.left >=360 and self.sprite1.rect.left <= 390) and (self.sprite1.rect.top >= 470 and self.sprite1.rect.top <= 510):
                self.x = 30
                self.y = 35
                self.sprite1.rect.top = self.y
                self.sprite1.rect.left = self.x
                self.screen.blit(self.sprite1.imagen,self.sprite1.rect)
            
            if self.i==7:
                self.i=0
            self.sprite1.imagen = self.tux
            self.i=self.i+1
            
        elif keys[K_UP]:
            self.sprite1.rect.top=self.sprite1.rect.top - 1
            self.tux = pygame.image.load(self.arreglo_arriba[self.k])
            if (self.sprite1.rect.left >= 160 and self.sprite1.rect.left <= 240) and (self.sprite1.rect.top >= 80 and self.sprite1.rect.top <= 140):
                self.sonidoArriba.play()
                
            if (self.sprite1.rect.left >= 160 and self.sprite1.rect.left <= 240) and (self.sprite1.rect.top >= 35 and self.sprite1.rect.top <= 80):
                self.sonidoDerecha.play()
             
            if (self.sprite1.rect.left >= 320 and self.sprite1.rect.left <= 480) and (self.sprite1.rect.top >= 150 and self.sprite1.rect.top <= 200):
                self.sonidoIzquierda.play()
                
            if (self.sprite1.rect.left >= 320 and self.sprite1.rect.left <= 380) and (self.sprite1.rect.top >= 100 and self.sprite1.rect.top <= 150):
                self.sonidoArriba.play()
            
            if (self.sprite1.rect.left >= 240 and self.sprite1.rect.left <= 290) and (self.sprite1.rect.top >= 200 and self.sprite1.rect.top <= 250):
                self.sonidoIzquierda.play()
            
            if (self.sprite1.rect.left >= 320 and self.sprite1.rect.left <= 380) and (self.sprite1.rect.top >= 40 and self.sprite1.rect.top <= 100):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 130 and self.sprite1.rect.left <= 170) and (self.sprite1.rect.top >= 470 and self.sprite1.rect.top <= 500):
                self.sonidoArriba.play()
            
            if self.k==7:
                self.k=0
            self.sprite1.imagen = self.tux
            self.k=self.k+1
            
            
        elif keys[K_DOWN]:
            self.sprite1.rect.top=self.sprite1.rect.top + 1
            self.tux = pygame.image.load(self.arreglo_abajo[self.l])
            
            if (self.sprite1.rect.left >= 110 and self.sprite1.rect.left <= 160) and (self.sprite1.rect.top >= 80 and self.sprite1.rect.top <= 110):
                self.sonidoIzquierda.play()
            
            if (self.sprite1.rect.left >= 10 and self.sprite1.rect.left <= 70) and (self.sprite1.rect.top >= 150 and self.sprite1.rect.top <= 200):
                self.sonidoDerecha.play()
                
            if (self.sprite1.rect.left >= 240 and self.sprite1.rect.left <= 290) and (self.sprite1.rect.top >= 80 and self.sprite1.rect.top <= 200):
                self.sonidoAbajo.play()
            
            if (self.sprite1.rect.left >= 240 and self.sprite1.rect.left <= 290) and (self.sprite1.rect.top >= 200 and self.sprite1.rect.top <= 250):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 320 and self.sprite1.rect.left <= 380) and (self.sprite1.rect.top >= 40 and self.sprite1.rect.top <= 100):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 380 and self.sprite1.rect.left <= 430) and (self.sprite1.rect.top >= 110 and self.sprite1.rect.top <= 170):
                self.sonidoDerecha.play()
                
            if (self.sprite1.rect.left >= 500 and self.sprite1.rect.left <= 550) and (self.sprite1.rect.top >= 140 and self.sprite1.rect.top <= 200):
                self.sonidoIzquierda.play()
            
            if (self.sprite1.rect.left >= 440 and self.sprite1.rect.left <= 475) and (self.sprite1.rect.top >= 200 and self.sprite1.rect.top <= 250):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 560 and self.sprite1.rect.left <= 610) and (self.sprite1.rect.top >= 250 and self.sprite1.rect.top <= 390):
                self.sonidoAbajo.play()
            
            if (self.sprite1.rect.left >= 560 and self.sprite1.rect.left <= 610) and (self.sprite1.rect.top >= 390 and self.sprite1.rect.top <= 430):
                self.sonidoDerecha.play()
                
            if (self.sprite1.rect.left >= 600 and self.sprite1.rect.left <= 660) and (self.sprite1.rect.top >= 430 and self.sprite1.rect.top <= 510):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 5 and self.sprite1.rect.left <= 60) and (self.sprite1.rect.top >= 250 and self.sprite1.rect.top <= 460):
                self.sonidoAbajo.play()
            
            if (self.sprite1.rect.left >= 5 and self.sprite1.rect.left <= 60) and (self.sprite1.rect.top >= 460 and self.sprite1.rect.top <= 515):
                self.sonidoDerecha.play()
                
            if (self.sprite1.rect.left >= 440 and self.sprite1.rect.left <= 475) and (self.sprite1.rect.top >= 250 and self.sprite1.rect.top <= 300):
                self.sonidoIzquierda.play()
            
            if (self.sprite1.rect.left >= 250 and self.sprite1.rect.left <= 300) and (self.sprite1.rect.top >= 300 and self.sprite1.rect.top <= 440):
                self.sonidoAbajo.play()
            
            if (self.sprite1.rect.left >= 250 and self.sprite1.rect.left <= 300) and (self.sprite1.rect.top >= 440 and self.sprite1.rect.top <= 510):
                self.sonidoDerecha.play()
            
            
            if self.l==7:
                self.l=0
            
            self.sprite1.imagen = self.tux
            self.l=self.l+1
        
        elif keys[K_ESCAPE]:
            self.exit()
            
        elif keys[K_SPACE]:
            pygame.mixer.music.load("musica\musi.mp3")
            pygame.mixer.music.play(1)
            
        elif keys[K_END]:
            pygame.mixer.music.stop()
        elif keys[K_PAGEUP]:
            pygame.mixer.music.pause()
        elif keys[K_PAGEDOWN]:
            pygame.mixer.music.unpause()
        
        return 
    
    def draw(self):
        self.screen.fill(color_black)
        self.screen.blit(self.sprite1.imagen,self.sprite1.rect)
        self.screen.blit(self.puerta,(720,460))
        self.screen.blit(self.moneda,(650,165))
        self.screen.blit(self.moneda,(360,470))
    
    def cuadrado(self):
        
        pygame.draw.rect(self.screen,(color_Barra), self.bordeD)
        pygame.draw.rect(self.screen,(color_Barra), self.bordeIZ)
        pygame.draw.rect(self.screen,(color_Barra), self.bordeS)
        pygame.draw.rect(self.screen,(color_Barra), self.bordeI)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo1)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo2)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo3)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo4)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo5)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo6)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo7)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo8)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo9)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo10)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo11)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo12)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo13)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo14)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo15)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo16)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo17)
        
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo18)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo19)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo20)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo21)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo22)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo23)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo24)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo25)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo26)
       
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo27)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo28)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo29)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo30)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo31)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo32)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo33)
        
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo34)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo35)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo36)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo37)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo38)
        
        pygame.display.update()
        
    def colision(self):
        if self.rectangulo1.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
            
        elif self.bordeD.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.bordeI.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.bordeIZ.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.bordeS.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
            
        elif self.rectangulo2.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo3.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo4.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo5.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo6.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo7.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo8.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo9.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo10.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo11.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo12.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo13.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo14.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo15.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo16.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo17.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo18.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo19.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo20.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo21.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo22.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo23.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo24.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo25.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo26.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo27.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo28.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo29.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo30.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo31.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo32.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo33.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo34.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo35.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo36.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo37.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo38.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        
        
       
        self.oldx=self.sprite1.rect.left
        self.oldy=self.sprite1.rect.top
            

    def mainLoop(self):
        pygame.mixer.music.load("musica\Secret.wav")
        pygame.mixer.music.play(1000)
        while not self.quit:
            for event in pygame.event.get():
                if event.type==QUIT:
                    self.quit=True
            
            self.iniciarCua()
            self.update()
            self.colision()
            self.draw()
            self.cuadrado()