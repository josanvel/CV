import pygame
from pygame.locals import *
from lib2to3.tests.test_main import PY2_TEST_MODULE
from pygame.examples.mask import Sprite
from audiodev import test
import ventanaInicial
import tkMessageBox
from Tkinter  import *
import sys


def hello(event):
    print 'Presione 2 veces para salir'              

def quit(event):                             
    print 'SALIENDO...'        
    import sys; sys.exit() 

screen_mode =(755, 485)
color_black= 0,0,0
color_Barra=229,142,13
color_R=60,32,190

class Game:
    def __init__ (self):
        pygame.init()
        
        pygame.mixer.init()
        self.screen= pygame.display.set_mode(screen_mode)
        pygame.display.set_caption("juego >P >P")
        self.sonido = pygame.mixer.Sound("musica\golpe.mp3")
        self.quit=False
        self.tex="imagen_d\d.png"
        self.sonidoArriba=pygame.mixer.Sound("musica\Arriba.wav")
        self.sonidoAbajo=pygame.mixer.Sound("musica\Abajo.wav")
        self.sonidoDerecha=pygame.mixer.Sound("musica\Derecha.wav")
        self.sonidoIzquierda=pygame.mixer.Sound("musica\Izquierda1.wav")
        
        self.sonidoError=pygame.mixer.Sound("musica\punch.wav")
        #self.sonido=pygame.mixer.Sound("musica\punch.wav")
        self.tux = pygame.image.load(self.tex)
        self.puerta=pygame.image.load("puertas/puerta3.jpg")
        self.moneda=pygame.image.load("puertas/moneda.jpg")
        self.x=30
        self.y=440
        self.sprite1=pygame.sprite.Sprite()
        self.sprite1.puerta1=self.puerta
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
        
   
        
        
    def men(self):
        tkMessageBox.Dialog("hola")
    
    def iniciarCua(self):
        self.bordeIZ=pygame.Rect(0,30,5,380)
        self.bordeD=pygame.Rect(750,100,5,380)
        self.bordeS=pygame.Rect(0,30,755,5)
        self.bordeI=pygame.Rect(0,480,755,5)
        
        
        self.rectangulo1=pygame.Rect(100,30,5,150)
        self.rectangulo2=pygame.Rect(5,80,50,5)
        self.rectangulo3=pygame.Rect(50,80,5,100)
        self.rectangulo17=pygame.Rect(100,175,50,5)
        
        self.rectangulo5=pygame.Rect(50,230,100,5)
        self.rectangulo6=pygame.Rect(50,230,5,200)
        
        self.rectangulo7=pygame.Rect(50,430,50,5)
        
        self.rectangulo8=pygame.Rect(100,280,5,155)
        self.rectangulo9=pygame.Rect(150,230,5,250)
        self.rectangulo16=pygame.Rect(150,80,5,100)
        self.rectangulo18=pygame.Rect(200,30,5,150)
        self.rectangulo14=pygame.Rect(200,230,5,100)
        self.rectangulo15=pygame.Rect(200,380,5,100)
        
        
        self.rectangulo10 = pygame.Rect(250,230,50,5)
        self.rectangulo11 = pygame.Rect(200,280,50,5)
        self.rectangulo12 = pygame.Rect(250,325,50,5)
        self.rectangulo13 = pygame.Rect(300,230,5,100)
        self.rectangulo19 = pygame.Rect(250,80,5,150)
        self.rectangulo20 = pygame.Rect(200,380,100,5)
        
        self.rectangulo21 = pygame.Rect(350,280,5,150)
        self.rectangulo22 = pygame.Rect(250,430,105,5)
        self.rectangulo23 = pygame.Rect(300,30,5,150)
        self.rectangulo24 = pygame.Rect(300,180,50,5)
        
        self.rectangulo25 = pygame.Rect(350,130,50,5)
        self.rectangulo26 = pygame.Rect(400,130,5,150)
        self.rectangulo27 = pygame.Rect(400,380,5,100)
        
        self.rectangulo28 = pygame.Rect(350,80,150,5)
        self.rectangulo29 = pygame.Rect(450,130,100,5)
        self.rectangulo30 = pygame.Rect(550,30,5,150)
        
        self.rectangulo31 = pygame.Rect(350,330,100,5)
        self.rectangulo32 = pygame.Rect(450,330,5,100)
        self.rectangulo33 = pygame.Rect(450,430,50,5)
        
        self.rectangulo34 = pygame.Rect(550,380,5,100)
        self.rectangulo35 = pygame.Rect(450,280,5,50)
        self.rectangulo36 = pygame.Rect(400,230,100,5)
        self.rectangulo37 = pygame.Rect(500,230,5,150)
        
        self.rectangulo38 = pygame.Rect(550,230,5,50)
        self.rectangulo39 = pygame.Rect(550,230,55,5)
        self.rectangulo40 = pygame.Rect(600,130,5,100)
        self.rectangulo41 = pygame.Rect(600,80,100,5)
        
        self.rectangulo42 = pygame.Rect(550,330,50,5)
        self.rectangulo43 = pygame.Rect(600,280,5,100)
        self.rectangulo44 = pygame.Rect(600,430,55,5)
        self.rectangulo45 = pygame.Rect(650,330,5,100)
        
        self.rectangulo46 = pygame.Rect(600,280,100,5)
        self.rectangulo47 = pygame.Rect(650,80,5,100)
        self.rectangulo48 = pygame.Rect(700,380,50,5)
        self.rectangulo49 = pygame.Rect(700,380,5,50)
        
        self.rectangulo50 = pygame.Rect(650,330,50,5)
        self.rectangulo51 = pygame.Rect(650,230,55,5)
        self.rectangulo52 = pygame.Rect(700,130,5,100)
        self.rectangulo53 = pygame.Rect(700,130,50,5)
        
        
    def update(self):
        keys=pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.sprite1.rect.left=self.sprite1.rect.left - 1
            if (self.sprite1.rect.left >= 10 and self.sprite1.rect.left <= 50) and (self.sprite1.rect.top >= 430 and self.sprite1.rect.top <= 480):
                self.sonidoArriba.play()
            
            if (self.sprite1.rect.left >= 50 and self.sprite1.rect.left <= 150) and (self.sprite1.rect.top >= 430 and self.sprite1.rect.top <= 480):
                self.sonidoError.play()
            
            if (self.sprite1.rect.left >= 300 and self.sprite1.rect.left <= 350) and (self.sprite1.rect.top >= 120 and self.sprite1.rect.top <=170):
                self.sonidoArriba.play()
            
            if (self.sprite1.rect.left >= 250 and self.sprite1.rect.left <= 300) and (self.sprite1.rect.top >= 370 and self.sprite1.rect.top <= 420):
                self.sonidoIzquierda.play()
            
            if (self.sprite1.rect.left >= 200 and self.sprite1.rect.left <= 250) and (self.sprite1.rect.top >= 370 and self.sprite1.rect.top <= 420):
                self.sonidoAbajo.play()
            
            #if (self.sprite1.rect.left >= 200 and self.sprite1.rect.left <= 250) and (self.sprite1.rect.top >= 370 and self.sprite1.rect.top <= 420):
            
                
                
            self.tux = pygame.image.load(self.arreglo_izqui[self.j])
            if self.j==7:
                self.j=0
            self.sprite1.imagen = self.tux
            self.j=self.j+1
            
            
        elif keys[K_RIGHT]:
            if (self.sprite1.rect.left >= 10 and self.sprite1.rect.left <= 50) and (self.sprite1.rect.top >= 440 and self.sprite1.rect.top <= 480):
                self.sonidoArriba.play()
                
            if (self.sprite1.rect.left >= 50 and self.sprite1.rect.left <= 150) and (self.sprite1.rect.top >= 180 and self.sprite1.rect.top <= 260):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 150 and self.sprite1.rect.left <= 200) and (self.sprite1.rect.top >= 180 and self.sprite1.rect.top <= 260):
                self.sonidoAbajo.play()
                
            if (self.sprite1.rect.left >= 200 and self.sprite1.rect.left <= 300) and (self.sprite1.rect.top >= 320 and self.sprite1.rect.top <= 370):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 300 and self.sprite1.rect.left <= 350) and (self.sprite1.rect.top >= 320 and self.sprite1.rect.top <= 370):
                self.sonidoArriba.play()
            
            if (self.sprite1.rect.left >= 350 and self.sprite1.rect.left <= 400) and (self.sprite1.rect.top >= 170 and self.sprite1.rect.top <= 270):
                self.sonidoArriba.play()
            
            if (self.sprite1.rect.left >= 350 and self.sprite1.rect.left <= 400) and (self.sprite1.rect.top >= 70 and self.sprite1.rect.top <=120):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 400 and self.sprite1.rect.left <= 450) and (self.sprite1.rect.top >= 70 and self.sprite1.rect.top <=120):
                self.sonidoAbajo.play()    
            
            if (self.sprite1.rect.left >= 450 and self.sprite1.rect.left <= 550) and (self.sprite1.rect.top >= 170 and self.sprite1.rect.top <=220):
                self.sonidoDerecha.play()
                
            if (self.sprite1.rect.left >= 550 and self.sprite1.rect.left <= 600) and (self.sprite1.rect.top >= 170 and self.sprite1.rect.top <=220):
                self.sonidoArriba.play()
            
            if (self.sprite1.rect.left >= 600 and self.sprite1.rect.left <= 750) and (self.sprite1.rect.top >= 20 and self.sprite1.rect.top <=70):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 250 and self.sprite1.rect.left <= 350) and (self.sprite1.rect.top >= 420 and self.sprite1.rect.top <= 470):
                self.sonidoDerecha.play()    
            
            if (self.sprite1.rect.left >= 350 and self.sprite1.rect.left <= 400) and (self.sprite1.rect.top >= 420 and self.sprite1.rect.top <= 470):
                self.sonidoArriba.play()    
            
            if (self.sprite1.rect.left >= 200 and self.sprite1.rect.left <= 250) and (self.sprite1.rect.top >= 180 and self.sprite1.rect.top <= 260):
                self.sonidoArriba.play()
            
            if (self.sprite1.rect.left >= 720 and self.sprite1.rect.left <= 750) and (self.sprite1.rect.top >= 30 and self.sprite1.rect.top <= 80):
                
                widget = Button(None, text='G A N A S T E S')
                widget.pack()
                widget.bind('<Button-1>', hello)             
                widget.bind('<First-1>', quit)              
                widget.mainloop()
                
            if (self.sprite1.rect.left >= 400 and self.sprite1.rect.left <= 440) and (self.sprite1.rect.top >= 330 and self.sprite1.rect.top <= 370):
                pygame.mixer.music.stop()
                ext=ventanaInicial.ventanaIni()
                ext.main()
                pygame.display.quit()
            
            if (self.sprite1.rect.left >= 250 and self.sprite1.rect.left <= 290) and (self.sprite1.rect.top >= 40 and self.sprite1.rect.top <= 90):
                self.x = 30
                self.y = 440
                self.sprite1.rect.top = self.y
                self.sprite1.rect.left = self.x
                self.screen.blit(self.sprite1.imagen,self.sprite1.rect)
                
            if (self.sprite1.rect.left >= 500 and self.sprite1.rect.left <= 540) and (self.sprite1.rect.top >= 86 and self.sprite1.rect.top <= 120):
                pygame.mixer.music.stop()
                ext=ventanaInicial.ventanaIni()
                ext.main()
                pygame.display.quit()
                
            if (self.sprite1.rect.left >= 560 and self.sprite1.rect.left <= 600) and (self.sprite1.rect.top >= 280 and self.sprite1.rect.top <= 320):
                self.x = 30
                self.y = 440
                self.sprite1.rect.top = self.y
                self.sprite1.rect.left = self.x
                self.screen.blit(self.sprite1.imagen,self.sprite1.rect)
             
            
            self.sprite1.rect.left=self.sprite1.rect.left + 1
            self.tux = pygame.image.load(self.arreglo_derecho[self.i])
            if self.i==7:
                self.i=0
            self.sprite1.imagen = self.tux
            self.i=self.i+1
        
        elif keys[K_UP]:
            self.sprite1.rect.top=self.sprite1.rect.top - 1
            self.tux = pygame.image.load(self.arreglo_arriba[self.k])
            if (self.sprite1.rect.left >= 10 and self.sprite1.rect.left <= 50) and (self.sprite1.rect.top >= 260 and self.sprite1.rect.top <= 430):
                self.sonidoArriba.play()
            
            if (self.sprite1.rect.left >= 10 and self.sprite1.rect.left <= 50) and (self.sprite1.rect.top >= 180 and self.sprite1.rect.top <= 260):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 300 and self.sprite1.rect.left <= 350) and (self.sprite1.rect.top >= 270 and self.sprite1.rect.top <= 320):
                self.sonidoArriba.play()
            
            if (self.sprite1.rect.left >= 300 and self.sprite1.rect.left <= 350) and (self.sprite1.rect.top >= 170 and self.sprite1.rect.top <= 270):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 350 and self.sprite1.rect.left <= 400) and (self.sprite1.rect.top >= 120 and self.sprite1.rect.top <=170):
                self.sonidoIzquierda.play()
            
            if (self.sprite1.rect.left >= 300 and self.sprite1.rect.left <= 350) and (self.sprite1.rect.top >= 70 and self.sprite1.rect.top <=120):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 550 and self.sprite1.rect.left <= 600) and (self.sprite1.rect.top >= 70 and self.sprite1.rect.top <=170):
                self.sonidoArriba.play()
            
            if (self.sprite1.rect.left >= 550 and self.sprite1.rect.left <= 600) and (self.sprite1.rect.top >= 20 and self.sprite1.rect.top <=70):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 350 and self.sprite1.rect.left <= 400) and (self.sprite1.rect.top >= 370 and self.sprite1.rect.top <= 420):
                self.sonidoArriba.play()    
            
            if (self.sprite1.rect.left >= 350 and self.sprite1.rect.left <= 400) and (self.sprite1.rect.top >= 320 and self.sprite1.rect.top <= 370):
                self.sonidoDerecha.play()    
            
            if (self.sprite1.rect.left >= 200 and self.sprite1.rect.left <= 250) and (self.sprite1.rect.top >= 70 and self.sprite1.rect.top <= 180):
                self.sonidoArriba.play()
            
            if (self.sprite1.rect.left >= 200 and self.sprite1.rect.left <= 250) and (self.sprite1.rect.top >= 20 and self.sprite1.rect.top <= 70):
                self.sonidoDerecha.play()
                
                
            if self.k==7:
                self.k=0
            self.sprite1.imagen = self.tux
            self.k=self.k+1
            
        elif keys[K_DOWN]:
            self.sprite1.rect.top=self.sprite1.rect.top + 1
            self.tux = pygame.image.load(self.arreglo_abajo[self.l])
            
            if (self.sprite1.rect.left >= 150 and self.sprite1.rect.left <= 200) and (self.sprite1.rect.top >= 260 and self.sprite1.rect.top <= 320):
                self.sonidoAbajo.play()
            
            if (self.sprite1.rect.left >= 150 and self.sprite1.rect.left <= 200) and (self.sprite1.rect.top >= 320 and self.sprite1.rect.top <= 370):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 400 and self.sprite1.rect.left <= 450) and (self.sprite1.rect.top >= 120 and self.sprite1.rect.top <=170):
                self.sonidoAbajo.play() 
            
            if (self.sprite1.rect.left >= 400 and self.sprite1.rect.left <= 450) and (self.sprite1.rect.top >= 170 and self.sprite1.rect.top <=220):
                self.sonidoDerecha.play()
            
            if (self.sprite1.rect.left >= 300 and self.sprite1.rect.left <= 350) and (self.sprite1.rect.top >= 370 and self.sprite1.rect.top <= 420):
                self.sonidoIzquierda.play()
            
            if (self.sprite1.rect.left >= 200 and self.sprite1.rect.left <= 250) and (self.sprite1.rect.top >= 420 and self.sprite1.rect.top <= 470):
                self.sonidoDerecha.play()    
            
            
            if self.l==7:
                self.l=0
            self.sprite1.imagen = self.tux
            self.l=self.l+1
        
        elif keys[K_ESCAPE]:
            pygame.mixer.music.stop()
            ext=ventanaInicial.ventanaIni()
            ext.main()
            pygame.display.quit()
            
        # self.exit()
            
            
         
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
        self.screen.blit(self.puerta,(730,35))
        self.screen.blit(self.moneda,(400,335))
        self.screen.blit(self.moneda,(500,85))
        self.screen.blit(self.moneda,(560,280))
        
    
    def cuadrado(self):
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo1)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo2)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo3)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo5)
        pygame.draw.rect(self.screen,(color_Barra), self.bordeD)
        pygame.draw.rect(self.screen,(color_Barra), self.bordeIZ)
        pygame.draw.rect(self.screen,(color_Barra), self.bordeS)
        pygame.draw.rect(self.screen,(color_Barra), self.bordeI)
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
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo39)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo40)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo41)
        
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo42)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo43)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo44)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo45)
        
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo46)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo47)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo48)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo49)
        
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo50)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo51)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo52)
        pygame.draw.rect(self.screen,(color_Barra), self.rectangulo53)
        
        
        pygame.display.update()
        
    def colision(self):
        if self.rectangulo1.colliderect(self.sprite1):
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
             
        elif self.rectangulo5.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
            
        elif self.bordeD.colliderect(self.sprite1):
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
        
        elif self.bordeI.colliderect(self.sprite1):
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
            
        elif self.rectangulo39.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
            
        elif self.rectangulo40.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        
        elif self.rectangulo41.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
                
        elif self.rectangulo42.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        
        elif self.rectangulo43.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        
        elif self.rectangulo44.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        
        elif self.rectangulo45.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
            
        elif self.rectangulo46.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        
        elif self.rectangulo47.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        
        elif self.rectangulo48.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
            
        elif self.rectangulo49.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
            
        elif self.rectangulo50.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        
        elif self.rectangulo51.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx      
                
        elif self.rectangulo52.colliderect(self.sprite1):
            self.sonido.play()
            self.sprite1.rect.top= self.oldy
            self.sprite1.rect.left= self.oldx
        
        elif self.rectangulo53.colliderect(self.sprite1):
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
