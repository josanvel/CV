import pygame
from pygame.locals import *
from lib2to3.tests.test_main import PY2_TEST_MODULE
from pygame.examples.mask import Sprite
from audiodev import test
import nivelMedio

screen_mode = (770,500)
color_black = 0,0,0
color_Barra = 229,152,20
color_R=60,32,190

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode(screen_mode)
        pygame.display.set_caption("NIVEL FACIL")
        self.quit = False
        self.sonidoArriba=pygame.mixer.Sound("musica\Arriba.wav")
        self.sonidoAbajo=pygame.mixer.Sound("musica\Abajo.wav")
        self.sonidoDerecha=pygame.mixer.Sound("musica\Derecha.wav")
        self.sonidoIzquierda=pygame.mixer.Sound("musica\Izquierda1.wav")
        self.sonidoAD=pygame.mixer.Sound("musica\UD_A-D.wav")
    
        
        self.sonidoError=pygame.mixer.Sound("musica\punch.wav")
        self.sonido1=pygame.mixer.Sound("musica\punch.wav")
        #self.sonidoFondo=
        self.puerta=pygame.image.load("puertas/puerta2.jpg")
        self.moneda=pygame.image.load("puertas/moneda.jpg")
        self.tex = "imagen_d\d.png"
        self.tux = pygame.image.load(self.tex)
        self.x = 30
        self.y = 450
        self.sprite1 = pygame.sprite.Sprite()
        self.sprite1.imagen = self.tux
        #self.sprite1.puerta1=self.puerta
        self.sprite1.rect = self.tux.get_rect()
        self.sprite1.rect.top = self.y
        self.sprite1.rect.left = self.x
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
        self.bordeIZ=pygame.Rect(0,30,5,400)
        self.bordeD=pygame.Rect(765,100,5,400)
        self.bordeS=pygame.Rect(0,30,770,5)
        self.bordeI=pygame.Rect(0,495,770,5)
        
        
        self.rectangulo1=pygame.Rect(70,100,10, 100)
        self.rectangulo2 = pygame.Rect(70,200,130,10)
        self.rectangulo3 = pygame.Rect(200,200,10,300)
        self.rectangulo4 = pygame.Rect(0,300,130,10)
        self.rectangulo5 = pygame.Rect(70,400,130,10)
        self.rectangulo6 = pygame.Rect(270,200,10,300)
        self.rectangulo7 = pygame.Rect(340,200,10,200)
        self.rectangulo8 = pygame.Rect(140,100,270,10)
        self.rectangulo9 = pygame.Rect(410,100,10,200)
        self.rectangulo10 = pygame.Rect(340,300,80,10)
        self.rectangulo11 = pygame.Rect(340,400,290,10)
        self.rectangulo12 = pygame.Rect(480,300,10,30)
        self.rectangulo13 = pygame.Rect(420,200,140,10)
        self.rectangulo14 = pygame.Rect(480,30,10,70)
        self.rectangulo15 = pygame.Rect(480,300,140,10)
        self.rectangulo16 = pygame.Rect(550,100,10,100)
        self.rectangulo17 = pygame.Rect(620,30,10,280)
        self.rectangulo18 = pygame.Rect(690,100,10,400)
        
        
    def update(self):
        keys=pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.sprite1.rect.left=self.sprite1.rect.left  - 1
            
            if (self.sprite1.rect.left >= 70 and self.sprite1.rect.left <= 110) and (self.sprite1.rect.top >= 210 and self.sprite1.rect.top <= 310):
                self.sonidoIzquierda.play()
            
            if (self.sprite1.rect.left >= 10 and self.sprite1.rect.left <= 70) and (self.sprite1.rect.top >= 210 and self.sprite1.rect.top <= 310):
                self.sonidoArriba.play()
            
            if (self.sprite1.rect.left >= 60 and self.sprite1.rect.left <= 100) and (self.sprite1.rect.top >= 90 and self.sprite1.rect.top <= 150):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 250 and self.sprite1.rect.left <= 620) and (self.sprite1.rect.top >= 410 and self.sprite1.rect.top <= 490):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 680 and self.sprite1.rect.left <= 720) and (self.sprite1.rect.top >= 40 and self.sprite1.rect.top <= 90):
                self.sonidoDerecha.play()
                
            self.tux = pygame.image.load(self.arreglo_izqui[self.j])
            if self.j==7:
                self.j=0
            self.sprite1.imagen = self.tux
            self.j=self.j+1
            
            
        elif keys[K_RIGHT]:
            self.sprite1.rect.left=self.sprite1.rect.left + 1
            self.tux = pygame.image.load(self.arreglo_derecho[self.i])
            if (self.sprite1.rect.left >= 20 and self.sprite1.rect.left <= 60) and (self.sprite1.rect.top >= 420 and self.sprite1.rect.top <= 465):
                self.sonidoArriba.play()
                
            if (self.sprite1.rect.left >= 60 and self.sprite1.rect.left <= 100) and (self.sprite1.rect.top >= 310 and self.sprite1.rect.top <= 370):
                self.sonidoDerecha.play()
             
            if (self.sprite1.rect.left >= 110 and self.sprite1.rect.left <= 150) and (self.sprite1.rect.top >= 310 and self.sprite1.rect.top <= 420):
                self.sonidoArriba.play()
                
            if (self.sprite1.rect.left >= 60 and self.sprite1.rect.left <= 100) and (self.sprite1.rect.top >= 230 and self.sprite1.rect.top <= 310):
                self.sonidoDerecha.play()
            
            
            
            if (self.sprite1.rect.left >= 60 and self.sprite1.rect.left <= 100) and (self.sprite1.rect.top >= 40 and self.sprite1.rect.top <= 90):
                '''self.sonidoAbajo.play()'''
                self.sonidoAD.play()
                
            if (self.sprite1.rect.left >= 60 and self.sprite1.rect.left <= 100) and (self.sprite1.rect.top >= 90 and self.sprite1.rect.top <= 150):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 100 and self.sprite1.rect.left <= 250) and (self.sprite1.rect.top >= 90 and self.sprite1.rect.top <= 150):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 250 and self.sprite1.rect.left <= 320) and (self.sprite1.rect.top >= 90 and self.sprite1.rect.top <= 150):
                self.sonidoAbajo.play()
                
            if (self.sprite1.rect.left >= 250 and self.sprite1.rect.left <= 620) and (self.sprite1.rect.top >= 410 and self.sprite1.rect.top <= 490):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 620 and self.sprite1.rect.left <= 680) and (self.sprite1.rect.top >= 410 and self.sprite1.rect.top <= 490):
                self.sonidoArriba.play()
            
            if (self.sprite1.rect.left >= 680 and self.sprite1.rect.left <= 720) and (self.sprite1.rect.top >= 40 and self.sprite1.rect.top <= 90):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 100 and self.sprite1.rect.left <= 420) and (self.sprite1.rect.top >= 40 and self.sprite1.rect.top <= 90):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 420 and self.sprite1.rect.left <= 480) and (self.sprite1.rect.top >= 40 and self.sprite1.rect.top <= 90):
                self.sonidoAbajo.play()
                
            if (self.sprite1.rect.left >= 735 and self.sprite1.rect.left <= 750) and (self.sprite1.rect.top >= 35 and self.sprite1.rect.top <= 80):
                pygame.display.quit()
                game= nivelMedio.Game()
                game.mainLoop()
            
            if (self.sprite1.rect.left >= 480 and self.sprite1.rect.left <= 510) and (self.sprite1.rect.top >= 110 and self.sprite1.rect.top <= 170):
                self.x = 30
                self.y = 450
                self.sprite1.rect.top = self.y
                self.sprite1.rect.left = self.x
                self.screen.blit(self.sprite1.imagen,self.sprite1.rect)
                
                
            if self.i==7:
                self.i=0
            self.sprite1.imagen = self.tux
            self.i=self.i+1
        
        elif keys[K_UP]:
            self.sprite1.rect.top=self.sprite1.rect.top - 1
            if (self.sprite1.rect.left >= 20 and self.sprite1.rect.left <= 60) and (self.sprite1.rect.top >= 310 and self.sprite1.rect.top <= 370):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 100 and self.sprite1.rect.left <= 140) and (self.sprite1.rect.top >= 240 and self.sprite1.rect.top <= 370):
                self.sonidoArriba.play()
            
            if (self.sprite1.rect.left >= 100 and self.sprite1.rect.left <= 140) and (self.sprite1.rect.top >= 190 and self.sprite1.rect.top <= 250):
                self.sonidoIzquierda.play()
            
            if (self.sprite1.rect.left >= 100 and self.sprite1.rect.left <= 170) and (self.sprite1.rect.top >= 200 and self.sprite1.rect.top <= 300):
                self.sonidoIzquierda.play()
            
            if (self.sprite1.rect.left >= 20 and self.sprite1.rect.left <= 60) and (self.sprite1.rect.top >= 100 and self.sprite1.rect.top <= 310):
                self.sonidoArriba.play()
            
            
            if (self.sprite1.rect.left >= 10 and self.sprite1.rect.left <= 60) and (self.sprite1.rect.top >= 40 and self.sprite1.rect.top <= 80):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 60 and self.sprite1.rect.left <= 100) and (self.sprite1.rect.top >= 90 and self.sprite1.rect.top <= 150):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 250 and self.sprite1.rect.left <= 320) and (self.sprite1.rect.top >= 150 and self.sprite1.rect.top <= 380):
                self.sonidoAbajo.play()
            
            if (self.sprite1.rect.left >= 620 and self.sprite1.rect.left <= 680) and (self.sprite1.rect.top >= 90 and self.sprite1.rect.top <= 490):
                self.sonidoArriba.play()
            
            if (self.sprite1.rect.left >= 620 and self.sprite1.rect.left <= 680) and (self.sprite1.rect.top >= 40 and self.sprite1.rect.top <= 90):
                self.sonidoDerecha.play()
                
            self.tux = pygame.image.load(self.arreglo_arriba[self.k])
            
            
            if self.k==7:
                self.k=0
            self.sprite1.imagen = self.tux
            self.k=self.k+1
            
        elif keys[K_DOWN]:
            self.sprite1.rect.top=self.sprite1.rect.top + 1
            
            if (self.sprite1.rect.left >= 100 and self.sprite1.rect.left <= 200) and (self.sprite1.rect.top >= 230 and self.sprite1.rect.top <= 310):
                self.sonidoArriba.play()
            
            
            if (self.sprite1.rect.left >= 60 and self.sprite1.rect.left <= 90) and (self.sprite1.rect.top >= 90 and self.sprite1.rect.top <= 150):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 250 and self.sprite1.rect.left <= 320) and (self.sprite1.rect.top >= 150 and self.sprite1.rect.top <= 380):
                self.sonidoAbajo.play()
            
            if (self.sprite1.rect.left >= 620 and self.sprite1.rect.left <= 680) and (self.sprite1.rect.top >= 90 and self.sprite1.rect.top <= 490):
                self.sonidoArriba.play()
            
            if (self.sprite1.rect.left >= 420 and self.sprite1.rect.left <= 480) and (self.sprite1.rect.top >=90 and self.sprite1.rect.top <= 140):
                self.sonidoAbajo.play()
            
            if (self.sprite1.rect.left >= 420 and self.sprite1.rect.left <= 480) and (self.sprite1.rect.top >=140 and self.sprite1.rect.top <= 190):
                self.sonidoDerecha.play()
            self.tux = pygame.image.load(self.arreglo_abajo[self.l])
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
        self.screen.blit(self.puerta,(700,35))
        self.screen.blit(self.moneda,(480,130))
    
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
        
        #pygame.draw.rect(self.screen,(color_R), self.rectangulo19)
        
        pygame.display.update()
        
    def colision(self):
        if self.rectangulo1.colliderect(self.sprite1):
            self.sonido1.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo2.colliderect(self.sprite1):
            self.sonido1.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo3.colliderect(self.sprite1):
            self.sonido1.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo4.colliderect(self.sprite1):
            self.sonido1.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo5.colliderect(self.sprite1):
            self.sonido1.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo6.colliderect(self.sprite1):
            self.sonido1.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo7.colliderect(self.sprite1):
            self.sonido1.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo8.colliderect(self.sprite1):
            self.sonido1.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo9.colliderect(self.sprite1):
            self.sonido1.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo10.colliderect(self.sprite1):
            self.sonido1.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo11.colliderect(self.sprite1):
            self.sonido1.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo12.colliderect(self.sprite1):
            self.sonido1.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo13.colliderect(self.sprite1):
            self.sonido1.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo14.colliderect(self.sprite1):
            self.sonido1.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo15.colliderect(self.sprite1):
            self.sonido1.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo16.colliderect(self.sprite1):
            self.sonido1.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo17.colliderect(self.sprite1):
            self.sonido1.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.rectangulo18.colliderect(self.sprite1):
            self.sonido1.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.bordeD.colliderect(self.sprite1):
            self.sonido1.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.bordeI.colliderect(self.sprite1):
            self.sonido1.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx  
        elif self.bordeIZ.colliderect(self.sprite1):
            self.sonido1.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        elif self.bordeS.colliderect(self.sprite1):
            self.sonido1.play()
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

