#!/usr/bin/python
import pygame, sys, glob
from pygame import *

class SpriteAnimation:
    def __init__(self, acaoInicial, speed = 15):
        self.acao = acaoInicial 
        self.x = 200
        self.y = 0
        self.ani_speed = speed
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
        xo,yo initial points
        lx,ly length of sprites
        n number of sprites
        """
        rect = []
        for i in range (n):
            rect.append(pygame.Rect(xo+lx*i, yo, lx,ly))
        rect.sort()
        return rect

    def insertFrame(self,xo,yo,lx,ly):
        """
        Insert frame by frame manually
        """
        self.manualList.append(pygame.Rect(xo,yo,lx,ly))
    
    def buildAnimation(self,acao,hold=False,speed =15):
        """
        Build Animation from the inserted frames and give the animation a label
        """
        self.animationSpeed[acao] = speed
        self.dicOfRects[acao] = self.manualList
        self.manualList = []
        self.holdState[acao] = hold
        
    def erasePositions(self, acao, indices):
        """
        Erase a rectangle sprite of the self-generated rectangle list
        """
        indices.sort()
        indices.reverse()
        lista = self.dicOfRects[acao]
        for item in indices:
            lista.pop(item)
        self.dicOfRects[acao] = lista

    def repeatPosition(self, acao, nvezes, indices):
        """
        Repeat a rectangle sprite of the self-generated rectangle list
        """
        indices.sort()
        lista = self.dicOfRects[acao]
        #append at the end n times
        while nvezes != 0:
            for item in indices:
                lista.append(lista[item])
            nvezes = nvezes -1

    def loadSprites(self, imagem):
        """
        Load the sprites image
        """
        self.spriteSheet = (pygame.image.load(imagem).convert_alpha())

    def createAnimation(self, xo,yo,lx,ly,n, acao, hold=False, speed = 15):
        """
        Create the self-generated list animation and give the animation a label
        """
        self.animationSpeed[acao] = speed
        #Define Animations
        self.dicOfRects[acao] = self.rectList(xo,yo,lx,ly,n) 
        self.holdState[acao] = hold

    def update(self,screen):
        """
        Run and update the animation
        """
        #new animation starts at 0
        if self.acaoLocal != self.acao:
            self.ani_pos = 0
        self.acaoLocal = self.acao
        rectList = self.dicOfRects[self.acao]
        self.ani_max = len(rectList)-1
        self.ani_speed-=1
        if self.ani_speed == 0:
            self.ani_speed = self.animationSpeed[self.acao]
            #if animation has reached the last position and it is continues
            if self.ani_pos == self.ani_max and self.holdState[self.acao] == False:
                self.ani_pos = 0
            #if its pressed the key and the animation its not continues
            elif self.ani_pos == self.ani_max and self.holdState[self.acao] == True and self.pressed==True:
                self.ani_pos = 0
                self.pressed = False
            #if the animation has reached the last position and its continues
            elif self.holdState[self.acao] == False:
                self.ani_pos+=1
            #if the animation has reached the last position and isnt continues
            elif self.holdState[self.acao] == True and self.ani_pos < self.ani_max:
                self.ani_pos+=1
                self.pressed = False
        if self.facingRight == True:
            cropped = self.spriteSheet.subsurface(rectList[self.ani_pos]).copy()
            screen.blit(cropped, (self.x,self.y))
        if self.facingRight == False:
            cropped = self.spriteSheet.subsurface(rectList[self.ani_pos]).copy()
            new_image = pygame.transform.flip(cropped, True, False)
            screen.blit(new_image, (self.x,self.y))
