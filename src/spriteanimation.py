#!/usr/bin/python
import pygame, sys, glob
from pygame import *

class SpriteAnimation:
    def __init__(self, acaoInicial, speed = 15):
        self.acao = acaoInicial 
        self.x = 200
        self.y = 0
        self.ani_speed_init= speed
        self.ani_speed = self.ani_speed_init
        self.ani_pos = 0
        self.spriteSheet = None 
        self.animation = []
        self.dicOfRects = {}
        self.animationSpeed = {}
        self.acaoLocal = ""
        self.manualList = []
        self.holdState = {} #Dicionario para registrar a continuidade ou descontinuidade da animacao
        self.pressed = False
        self.facingRight = True

    def rectList(self,xo,yo, lx, ly, n):
        """
        Build a list of rectangles sprites

        xo,yo pontos iniciais
        lx,ly comprimentos das sprites
        numeros de sprites
        """

        rect = []
        for i in range (n):
            rect.append(pygame.Rect(xo+lx*i, yo, lx,ly))
        
        rect.sort()
        return rect

    def insertFrame(self,xo,yo,lx,ly):
        """Insert frame by frame manually"""
        self.manualList.append(pygame.Rect(xo,yo,lx,ly))
    
    def buildAnimation(self,acao,hold=False,speed =15):
        """Build Animation from the inserted frames and give the animation a label"""
        self.animationSpeed[acao] = speed
        self.dicOfRects[acao] = self.manualList
        self.manualList = []
        self.holdState[acao] = hold
        
    def erasePositions(self, acao, indices):
        """Erase a rectangle sprite of the self-generated rectangle list"""
        indices.sort()
        indices.reverse()
        lista = self.dicOfRects[acao]
        for i in range(len(indices)):
            lista.pop(indices[i])
        self.dicOfRects[acao] = lista

    def repeatPosition(self, acao, nvezes, indices):
        """Repeat a rectangle sprite of the self-generated rectangle list"""
        indices.sort()
        lista = self.dicOfRects[acao]
        #adiciona no final n vezes
        while nvezes != 0:
            for i in range(len(indices)):
                lista.append(lista[indices[i]])
            nvezes = nvezes -1

    def loadSprites(self, imagem):
        """Load the image containing the sprites"""
        self.spriteSheet = (pygame.image.load(imagem).convert_alpha())

    def createAnimation(self, xo,yo,lx,ly,n, acao, hold=False, speed = 15):
        """Create the self-generated list animation and give the animation a label"""
        self.animationSpeed[acao] = speed
        #Define Animations
        self.dicOfRects[acao] = self.rectList(xo,yo,lx,ly,n) 
        self.holdState[acao] = hold

    def update(self, pos,screen):
        """Run and update the animation"""
        #import pdb; pdb.set_trace()
        
        #Nova animacao comeca no indice 0
        if self.acaoLocal != self.acao:
            self.ani_pos = 0
        self.acaoLocal = self.acao
        
        rectList = self.dicOfRects[self.acao]
        self.ani_max = len(rectList) - 1

        if pos !=0:
            self.ani_speed-=1
 
            if self.ani_speed == 0:

                self.ani_speed = self.animationSpeed[self.acao]
                #Caso a animacao tenha atingido o ultimo indice e eh continua
                if self.ani_pos == self.ani_max and self.holdState[self.acao] == False:
                    self.ani_pos = 0
                #Caso seja apertada a tecla novamente numa animacao desconitnua
                elif self.ani_pos == self.ani_max and self.holdState[self.acao] == True and self.pressed==True:
                    self.ani_pos = 0
                    self.pressed = False
                #Caso a animacao nao tenha atingido o ultimo indice e eh continua
                elif self.holdState[self.acao] == False:
                    self.ani_pos+=1
                #Caso a animacao nao tenha atingido o ultimo indice e eh descontinua
                elif self.holdState[self.acao] == True and self.ani_pos < self.ani_max:
                    self.ani_pos+=1
                    self.pressed = False
        #screen.blit(self.spriteSheet[0], (self.x,self.y), rectList[self.ani_pos])
        if self.facingRight == True:
            cropped = self.spriteSheet.subsurface(rectList[self.ani_pos]).copy()
            screen.blit(cropped, (self.x,self.y))
        
        if self.facingRight == False:
            cropped = self.spriteSheet.subsurface(rectList[self.ani_pos]).copy()
            new_image = pygame.transform.flip(cropped, True, False)
            screen.blit(new_image, (self.x,self.y))
