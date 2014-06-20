#!/usr/bin/python
import pygame, sys, glob
from pygame import *

from SpriteAnimation import SpriteAnimation
class Player(SpriteAnimation):
    def __init__(self, acaoInicial, speed = 15):
        """Iniciation of the player states"""
        SpriteAnimation.__init__(self,acaoInicial, speed = 15)
        self.pos = 1
        self.movex, self.movey = 0,0
        self.facingRight = True
        self.x = 200
        self.y = 300
        self.Rect = Rect(self.x, self.y, 35, 70)
        self.HP = 150
        self.XP =30
        self.Defending = False
        self.Attacking = False
