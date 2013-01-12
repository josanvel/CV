import pygame
from pygame.locals import *
import sys
from pygame.examples.midi import key_class
color_black1=0,0,0
screen_mode1=10,10

class Audio:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen= pygame.display.set_mode(screen_mode1)
        pygame.display.set_caption("Proyecto Laberintos")
        self.screen.fill(color_black1)
        self.quit=False
        self.contador=0
        
        self.sonidoInstruc=pygame.mixer.Sound("sonidos/instrcucciones.ogg")
        self.sonido2=pygame.mixer.Sound("sonidos/empezarjugar.ogg")            
        self.sonido20=pygame.mixer.Sound("sonidos/a.ogg")
        self.sonido3=pygame.mixer.Sound("sonidos/b.ogg")
        self.sonido4=pygame.mixer.Sound("sonidos/dce.ogg")
        self.sonido5=pygame.mixer.Sound("sonidos/f.ogg")
        self.sonido6=pygame.mixer.Sound("sonidos/q.ogg")
        self.sonido7=pygame.mixer.Sound("sonidos/nop.ogg")
        self.sonidoH=pygame.mixer.Sound("sonidos/k.ogg")
        self.sonido10=pygame.mixer.Sound("sonidos/sut.ogg")
        self.sonidoJ=pygame.mixer.Sound("sonidos/l.ogg")
        self.sonidoM=pygame.mixer.Sound("sonidos/M.ogg")
        self.sonidoN=pygame.mixer.Sound("sonidos/N.ogg")
        self.regresarInicio=pygame.mixer.Sound("sonidos/reI.ogg")
        
        self.regreso=pygame.mixer.Sound("sonidos/inicio.ogg")
        self.perdio=pygame.mixer.Sound("sonidos/perdido.ogg")
        
        self.ganaste=pygame.mixer.Sound("sonidos/felicidades.ogg")
        
        self.inicial=pygame.mixer.Sound("sonidos/menu.ogg")
        
            
         
    
        
    def main(self):
        
        pygame.mixer.music.load("sonidos/primerNivel.mid")
        pygame.mixer.music.play(100)
        
        self.inicial.play(100)
        while not self.quit:
            keys=pygame.key.get_pressed()
            for event in pygame.event.get():
                (self.x,self.y)=pygame.mouse.get_pos()
                
                    
                if event.type==QUIT:
                    self.quit=True
                elif keys[K_1]:
                    self.sonido3.stop()
                    self.sonido10.stop()
                    self.sonido20.stop()
                    self.sonido4.stop()
                    self.sonido5.stop()
                    self.sonido6.stop()
                    self.sonido7.stop()
                    self.sonidoInstruc.stop()
                    self.sonidoH.stop()
                    self.sonidoJ.stop()
                    self.sonidoM.stop()
                    self.sonidoN.stop()
                    self.ganaste.stop()
                    self.perdio.stop()
                    self.regresarInicio.stop()
                    self.regreso.stop()
                    
                    self.inicial.stop()
                    self.sonido2.play(100)
                    
                elif keys[K_2]:
                    self.sonido10.stop()
                    self.sonido20.stop()
                    self.sonido2.stop()
                    self.sonido3.stop()
                    self.sonido4.stop()
                    self.sonido5.stop()
                    self.sonido6.stop()
                    self.sonido7.stop()
                    self.sonidoH.stop()
                    self.sonidoJ.stop()
                    self.sonidoM.stop()
                    self.sonidoN.stop()
                    self.ganaste.stop()
                    self.perdio.stop()
                    self.regresarInicio.stop()
                    self.regreso.stop()
                    self.inicial.stop()
                    
                    self.sonidoInstruc.play(100)
                    
                elif keys[K_3]:
                    self.inicial.stop()
                    pygame.display.quit()
                
                
                elif keys[K_RETURN]:
                    self.inicial.stop()
                    self.sonido2.stop()
                    self.sonido3.stop()
                    self.sonido4.stop()
                    self.sonido5.stop()
                    self.sonido6.stop()
                    self.sonido7.stop()
                    self.sonidoInstruc.stop()
                    self.sonidoH.stop()
                    self.sonidoJ.stop()
                    self.sonidoM.stop()
                    self.sonidoN.stop()
                    self.ganaste.stop()
                    self.perdio.stop()
                    self.regresarInicio.stop()
                    self.regreso.stop()
                    self.sonido10.stop()
                    
                    self.sonido20.play(100)
                
                elif keys[K_a]:
                    self.inicial.stop()
                    self.sonido2.stop()
                    self.sonido4.stop()
                    self.sonido5.stop()
                    self.sonido6.stop()
                    self.sonido7.stop()
                    self.sonidoInstruc.stop()
                    self.sonidoH.stop()
                    self.sonidoJ.stop()
                    self.sonidoM.stop()
                    self.sonidoN.stop()
                    self.ganaste.stop()
                    self.perdio.stop()
                    self.regresarInicio.stop()
                    self.regreso.stop()
                    self.sonido10.stop()
                    
                    self.sonido20.stop()
                    self.sonido3.play(100)
                    
                elif keys[K_b]:
                    self.inicial.stop()
                    self.sonido2.stop()
                    self.sonido5.stop()
                    self.sonido6.stop()
                    self.sonido7.stop()
                    self.sonidoInstruc.stop()
                    self.sonidoH.stop()
                    self.sonidoJ.stop()
                    self.sonidoM.stop()
                    self.sonidoN.stop()
                    self.ganaste.stop()
                    self.perdio.stop()
                    self.regresarInicio.stop()
                    self.regreso.stop()
                    self.sonido10.stop()
                    self.sonido20.stop()
                    
                    self.sonido3.stop()
                    self.sonido4.play(100)
                
                
                elif keys[K_c]:
                    self.inicial.stop()
                    self.sonido2.stop()
                    self.sonido3.stop()
                    self.sonido5.stop()
                    self.sonido6.stop()
                    self.sonido7.stop()
                    self.sonidoInstruc.stop()
                    self.sonidoH.stop()
                    self.sonidoJ.stop()
                    self.sonidoM.stop()
                    self.sonidoN.stop()
                    self.ganaste.stop()
                    self.perdio.stop()
                    self.regresarInicio.stop()
                    self.sonido10.stop()
                    
                    self.sonido4.stop()
                    self.regreso.play()
                    self.sonido20.play(100)
                    
                
                elif keys[K_d]:
                    
                    self.sonido2.stop()
                    self.sonido3.stop()
                    self.sonido4.stop()
                    self.sonido5.stop()
                    self.sonido6.stop()
                    self.sonido7.stop()
                    self.sonidoInstruc.stop()
                    self.sonidoH.stop()
                    self.sonidoJ.stop()
                    self.sonidoM.stop()
                    self.sonidoN.stop()
                    self.ganaste.stop()
                    self.regresarInicio.stop()
                    self.regreso.stop()
                    self.sonido10.stop()
                    self.sonido20.stop()
                    
                    
                    self.perdio.play()
                    self.inicial.play(100)
                    
                    
                    
                    
                elif keys[K_e]:
                    self.inicial.stop()
                    self.sonido2.stop()
                    self.sonido3.stop()
                    self.sonido6.stop()
                    self.sonido7.stop()
                    self.sonidoInstruc.stop()
                    self.sonidoH.stop()
                    self.sonidoJ.stop()
                    self.sonidoM.stop()
                    self.sonidoN.stop()
                    self.ganaste.stop()
                    self.perdio.stop()
                    self.regresarInicio.stop()
                    self.regreso.stop()
                    self.sonido10.stop()
                    self.sonido20.stop()
                    self.sonido4.stop()
                    
                    self.sonido5.play(100)
                    
                
                elif keys[K_f]:
                    self.inicial.stop()
                    self.sonido2.stop()
                    self.sonido3.stop()
                    self.sonido4.stop()
                    self.sonido5.stop()
                    self.sonido7.stop()
                    self.sonidoInstruc.stop()
                    self.sonidoH.stop()
                    self.sonidoJ.stop()
                    self.sonidoM.stop()
                    self.sonidoN.stop()
                    self.ganaste.stop()
                    self.perdio.stop()
                    self.regresarInicio.stop()
                    self.regreso.stop()
                    self.sonido10.stop()
                    
                    self.sonido20.stop()
                    
                    self.sonido6.play(100)
                    
                elif keys[K_q]:
                    self.sonido2.stop()
                    self.sonido3.stop()
                    self.sonido4.stop()
                    self.sonido5.stop()
                    self.sonido6.stop()
                    self.sonidoInstruc.stop()
                    self.sonidoH.stop()
                    self.sonidoJ.stop()
                    self.sonidoM.stop()
                    self.sonidoN.stop()
                    self.ganaste.stop()
                    self.perdio.stop()
                    self.regresarInicio.stop()
                    self.regreso.stop()
                    self.sonido10.stop()
                    self.sonido20.stop()
                    self.inicial.stop()
                    
                    self.sonido7.play(100)
                    
                    
                
                elif keys[K_o]:
                    self.sonido2.stop()
                    self.sonido3.stop()
                    self.sonido4.stop()
                    self.sonido5.stop()
                    self.sonido6.stop()
                    self.sonido7.stop()
                    self.sonidoInstruc.stop()
                    self.sonidoH.stop()
                    self.sonidoJ.stop()
                    self.sonidoM.stop()
                    self.sonidoN.stop()
                    self.ganaste.stop()
                    self.regresarInicio.stop()
                    self.regreso.stop()
                    self.sonido10.stop()
                    self.sonido20.stop()
                    
                    self.perdio.play()
                    self.inicial.play(100)
                    
                    
                    
                elif keys[K_p]:
                    self.inicial.stop()
                    self.sonido2.stop()
                    self.sonido3.stop()
                    self.sonido4.stop()
                    self.sonido5.stop()
                    self.sonido6.stop()
                    self.sonido7.stop()
                    self.sonidoInstruc.stop()
                    self.sonidoH.stop()
                    self.sonidoJ.stop()
                    self.sonidoM.stop()
                    self.sonidoN.stop()
                    self.ganaste.stop()
                    self.perdio.stop()
                    self.regresarInicio.stop()
                    self.regreso.stop()
                    self.sonido10.stop()
                    self.sonido20.stop()
                    
                    self.sonidoH.play(100)   
                
                elif keys[K_k]:
                    self.inicial.stop()
                    self.sonido2.stop()
                    self.sonido3.stop()
                    self.sonido4.stop()
                    self.sonido5.stop()
                    self.sonido6.stop()
                    self.sonido7.stop()
                    self.sonidoInstruc.stop()
                    self.sonidoH.stop()
                    self.sonidoM.stop()
                    self.sonidoN.stop()
                    self.ganaste.stop()
                    self.perdio.stop()
                    self.regresarInicio.stop()
                    self.regreso.stop()
                    self.sonido10.stop()
                    self.sonido20.stop()
                    
                    self.sonidoJ.play(100)  
                    
                elif keys[K_l]:
                    self.sonido2.stop()
                    self.sonido3.stop()
                    self.sonido4.stop()
                    self.sonido5.stop()
                    self.sonido6.stop()
                    self.sonido7.stop()
                    self.sonidoInstruc.stop()
                    self.sonidoH.stop()
                    self.sonidoJ.stop()
                    self.sonidoM.stop()
                    self.sonidoN.stop()
                    self.ganaste.stop()
                    self.perdio.stop()
                    self.regresarInicio.stop()
                    self.regreso.stop()
                    self.sonido20.stop()
                    self.inicial.stop()
                    
                    self.sonido10.play(100)
                    
                elif keys[K_u]:
                    self.sonido2.stop()
                    self.sonido3.stop()
                    self.sonido4.stop()
                    self.sonido5.stop()
                    self.sonido6.stop()
                    self.sonido7.stop()
                    self.sonidoInstruc.stop()
                    self.sonidoH.stop()
                    self.sonidoJ.stop()
                    self.sonidoM.stop()
                    self.sonidoN.stop()
                    self.ganaste.stop()
                    self.perdio.stop()
                    self.regresarInicio.stop()
                    self.regreso.stop()
                    self.sonido10.stop()
                    self.inicial.stop()
                    
                    self.regreso.play()
                    self.sonido20.play(100)
                    
                elif keys[K_s]:
                    self.sonido2.stop()
                    self.sonido3.stop()
                    self.sonido4.stop()
                    self.sonido5.stop()
                    self.sonido6.stop()
                    self.sonido7.stop()
                    self.sonidoInstruc.stop()
                    self.sonidoH.stop()
                    self.sonidoJ.stop()
                    self.sonidoM.stop()
                    self.sonidoN.stop()
                    self.ganaste.stop()
                    self.regresarInicio.stop()
                    self.regreso.stop()
                    self.sonido10.stop()
                    self.sonido20.stop()
                    self.perdio.play()
                     
                    self.inicial.play(100)
                
                elif keys[K_t]:
                    self.sonido2.stop()
                    self.sonido3.stop()
                    self.sonido4.stop()
                    self.sonido5.stop()
                    self.sonido6.stop()
                    self.sonido7.stop()
                    self.sonidoInstruc.stop()
                    self.sonidoH.stop()
                    self.sonidoJ.stop()
                    self.sonidoN.stop()
                    self.ganaste.stop()
                    self.perdio.stop()
                    self.regresarInicio.stop()
                    self.regreso.stop()
                    self.sonido10.stop()
                    self.sonido20.stop()
                    
                    self.sonidoM.play(100) 
                
                elif keys[K_m]:
                    self.sonido2.stop()
                    self.sonido3.stop()
                    self.sonido4.stop()
                    self.sonido5.stop()
                    self.sonido6.stop()
                    self.sonido7.stop()
                    self.sonidoInstruc.stop()
                    self.sonidoH.stop()
                    self.sonidoJ.stop()
                    self.sonidoM.stop()
                    self.ganaste.stop()
                    self.perdio.stop()
                    self.regresarInicio.stop()
                    self.regreso.stop()
                    self.sonido10.stop()
                    self.inicial.stop()
                    self.sonido20.stop()
                    
                    self.ganaste.play()
                    self.contador=1
                    
                elif keys[K_n]:
                    self.sonido2.stop()
                    self.sonido3.stop()
                    self.sonido4.stop()
                    self.sonido5.stop()
                    self.sonido6.stop()
                    self.sonido7.stop()
                    self.sonidoInstruc.stop()
                    self.sonidoH.stop()
                    self.sonidoJ.stop()
                    self.sonidoM.stop()
                    self.sonidoN.stop()
                    self.perdio.stop()
                    self.regreso.stop()
                    self.sonido10.stop()
                    self.sonido20.stop()
                    self.inicial.stop()
                    
                    self.regreso.play()
                    self.sonido20.play(100)
                    
                    
                    
                elif keys[K_ESCAPE]:
                    self.inicial.stop()
                    self.sonido2.stop()
                    self.sonido3.stop()
                    self.sonido4.stop()
                    self.sonido5.stop()
                    self.sonido6.stop()
                    self.sonido7.stop()
                    self.sonidoInstruc.stop()
                    self.sonidoH.stop()
                    self.sonidoJ.stop()
                    self.sonidoM.stop()
                    self.sonidoN.stop()
                    self.ganaste.stop()
                    self.perdio.stop()
                    self.regresarInicio.stop()
                    self.regreso.stop()
                    self.sonido10.stop()
                    self.sonido20.stop()
                    self.inicial.play(100)
                    
                if self.contador==1:
                    self.regresarInicio.play(2) #graba un sonido q diga "presion esc para regresar o 1 para jugar de nuevo"
                    self.contador=0

if __name__ == '__main__':
    venta=Audio()
    venta.main()