#!/usr/bin/python
import pygame, sys, glob
from pygame import *
from spriteanimation import SpriteAnimation
import time

class Player(SpriteAnimation):
    def __init__(self, acaoInicial, playerId, speed = 15):
        """Iniciation of the player states"""
        SpriteAnimation.__init__(self,acaoInicial, speed = 15)
        self.pos = 1
        self.pos2 = 1
        self.movex, self.movey = 0,0
        self.facingRight = True
        self.x = 250
        self.y = 350
        self.Rect = Rect(self.x, self.y, 35, 70)
        self.HP = 150
        self.XP =30
        self.Defending = False
        self.Attacking = False
        self.punchDamage = 0
        self.kickDamage = 0
        self.hitDefended = 0
        self.powerDamage = 0
        self.powerDamageDefended = 0
        self.inicio = 0
        self.cronometrar2 = True
        self.punchDamage = 2
        self.kickDamage = 2
        self.hitDefended = 0.4
        self.powerDamage = 10
        self.powerDamageDefended = 2
        self.HP = 140
        self.XP = 30
        self.playerId = playerId
        if self.playerId == 1:
            self.k_down = K_s
            self.k_up = K_w
            self.k_defend = K_p
            self.k_kameham = K_u
            self.k_punch = K_i
            self.k_kick = K_o
            self.k_load = K_j
            self.k_rightArrow = K_d
            self.k_leftArrow = K_a
        elif self.playerId == 2:
            self.k_down = K_DOWN
            self.k_up = K_UP
            self.k_defend = K_KP5
            self.k_kameham = K_KP7
            self.k_punch = K_KP8
            self.k_kick = K_KP9
            self.k_load = K_KP4
            self.k_rightArrow = K_RIGHT
            self.k_leftArrow = K_LEFT
    
    def playPlayer(self,eventArg, player2, power1):
        """
        Activate player movements and skills
        """
        if self.HP>0:
            event = eventArg
            if event.type == KEYDOWN:
                #Goku
                if event.key == self.k_down:
                    self.acao = "down"
                    self.pos = 1
                    self.movey+=1
                if event.key == self.k_up:
                    self.acao = "up"
                    self.pos = 1
                    self.movey-=1
                if event.key == self.k_defend:
                    self.acao = "defend"
                    self.pos = 1
                    self.Defending = True
                if self.facingRight == True:
                    if event.key == self.k_rightArrow:
                        self.acao = "right"
                        self.pos = 1
                        self.movex+=1
                    if event.key == self.k_leftArrow:
                        self.acao = "up"
                        self.pos = 1
                        self.movex-=1
                if self.facingRight == False:
                    if event.key == self.k_rightArrow:
                        self.acao = "up"
                        self.pos = 1
                        self.movex+=1
                    if event.key == self.k_leftArrow:
                        self.acao = "right"
                        self.pos = 1
                        self.movex-=1
                if event.key == self.k_kameham:
                    if self.XP > 0:
                        self.acao = "kameham"
                        power1.acao = "kame"
                        self.pressed = True
                        power1.pressed = True
                        self.pos = 1
                        self.Attacking = True
                        self.Defending = False
                        if self.facingRight == True:
                            selfAttackRect = Rect(self.x+30, self.y+20, 1000, 60)
                            #pygame.draw.rect(screen, (0,255,0), selfAttackRect)
                        else:
                            selfAttackRect = Rect(self.x-1000, self.y+20, 1000, 60)
                            #pygame.draw.rect(screen, (0,255,0), selfAttackRect)
                        if selfAttackRect.colliderect(player2.Rect) == True:
                            if player2.Defending == False:
                                player2.HP -= self.powerDamage
                                player2.acao = "hited"
                                player2.inicio = time.time()
                            if player2.Defending == True and player2.Attacking == False:
                                player2.HP -= player2.powerDamageDefended
                        self.XP-=10
                        self.inicio = time.time()
                if event.key == self.k_punch:
                    self.acao = "punch"
                    self.pressed = True
                    self.pos = 1
                    self.Attacking = True
                    self.Defending = False
                    if self.facingRight == True:
                        selfAttackRect = Rect(self.x+30, self.y, 35, 70)
                        #pygame.draw.rect(screen, (0,0,255), selfAttackRect)
                    if self.facingRight == False:
                        selfAttackRect = Rect(self.x-5, self.y, 35, 70)
                        #pygame.draw.rect(screen, (0,0,255), selfAttackRect)
                    if selfAttackRect.colliderect(player2.Rect) == True:
                        if player2.Defending == False:
                            player2.HP -= self.punchDamage
                            player2.acao = "hited"
                            player2.inicio = time.time()
                        if player2.Defending == True and player2.Attacking == False:
                            player2.HP -= player2.hitDefended
                    self.inicio = time.time()
                if event.key == self.k_kick:
                    self.acao = "kick"
                    self.pressed = True
                    self.pos = 1
                    self.Attacking = True
                    self.Defending = False
                    if self.facingRight == True:
                        selfAttackRect = Rect(self.x+30, self.y, 35, 70)
                        #pygame.draw.rect(screen, (255,0,0), selfAttackRect)
                    if self.facingRight == False:
                        selfAttackRect = Rect(self.x-5, self.y, 35, 70)
                        #pygame.draw.rect(screen, (255,0,0), selfAttackRect)
                    if selfAttackRect.colliderect(player2.Rect) == True:
                        if player2.Defending == False:
                            player2.HP -= self.kickDamage
                            player2.acao = "hited"
                            player2.inicio = time.time()
                        if player2.Defending == True and player2.Attacking == False:
                            player2.HP -= player2.hitDefended
                    self.inicio = time.time()
                if event.key == self.k_load:
                    self.acao = "load"
                    self.pressed = True
                    self.pos = 1
                    self.XP+= 5 
                    self.inicio = time.time()
                    
            if event.type == KEYUP:
                if event.key == self.k_down:
                    self.acao = "down"
                    self.pos = 0
                    self.movey=0
                if event.key == self.k_up:
                    self.acao = "up"
                    self.pos = 0
                    self.movey=0
                if event.key == self.k_defend:
                    self.acao = "defend"
                    self.pos = 0
                    self.Defending = False
                if event.key == self.k_punch:
                    self.Attacking = False
                if self.facingRight  == True:
                    if event.key == self.k_rightArrow:
                        self.acao = "right"
                        self.pos = 0
                        self.movex=0
                    if event.key == self.k_leftArrow:
                        self.acao = "up"
                        self.pos = 0
                        self.movex=0
                if self.facingRight  == False:
                    if event.key == self.k_leftArrow:
                        self.acao = "right"
                        self.pos = 0
                        self.movex=0
                    if event.key == self.k_rightArrow:
                        self.acao = "up"
                        self.pos = 0
                        self.movex=0
                if event.key == self.k_kameham:
                    self.acao = "kameham"
                    power1.acao = "void"
                    self.pos = 0
                    self.movex=0
    
    def TurnAround1(self,player2):
        """
        Turn around automatically for player1 and player2
        """
        if self.x > player2.x:
            self.facingRight = False
            player2.facingRight = True
        if self.x < player2.x:
            self.facingRight = True
            player2.facingRight = False

    def lockInsideScreen(self,width,height,delta):
        """
        Lock the player to the visible screen
        """
        if self.facingRight == True:
            if self.movex == -1 and self.x>0:
                self.x += self.movex * delta
            if self.movex == 1 and self.x<width-50:
                self.x += self.movex * delta
        if self.facingRight == False:
            if self.movex == -1 and self.x>0:
                self.x += self.movex * delta
            if self.movex == 1 and self.x<width-50:
                self.x += self.movex * delta
        if self.movey == 1 and self.y<height-70:
            self.y += self.movey * delta
        if self.movey == -1 and self.y>0:
            self.y += self.movey * delta

    def powerPlacing(self,power,dx1=45,dy1=25,dx2=930,dy2=20):
        """
        Adjusting the power position of player1
        """
        if (self.facingRight == True):
            power.x = self.x+dx1
            power.y = self.y+dy1
        else:
            power.x = self.x-dx2
            power.y = self.y+dy2

    def physicalRect(self):
        """
        Physical Rectangle of player1
        """
        if self.acao != "right":
            self.Rect = Rect(self.x, self.y, 35, 70)
        elif self.acao == "right" and self.facingRight == True:
            self.Rect = Rect(self.x+30, self.y, 35, 70)
        elif self.acao == "right" and self.facingRight == False:
            self.Rect = Rect(self.x, self.y, 35, 70)

    def statusBar(self,screen,width):
        """
        Hp and XP bars of player1
        """
        if self.playerId == 1:
            playerHPRect = Rect(80 , 20, self.HP*2, 20)
            playerXPRect = Rect(80 , 60, self.XP*2, 20)
            screen.blit(self.photo3x4, (0,20))
        if self.playerId == 2:
            playerHPRect = Rect(width-80, 20, -self.HP*2, 20)
            playerXPRect = Rect(width-80, 60, -self.XP*2, 20)
            screen.blit(self.photo3x4Fliped, (width-70,20))
        if self.HP >=0:
            pygame.draw.rect(screen, (255,0,0), playerHPRect)
        pygame.draw.rect(screen, (0,0,255), playerXPRect)

    def standUpPosition(self):
        """
        Standard position of player2
        """
        if self.movex or self.movey !=0:
            self.inicio = time.time()
        if self.Defending== True:
            self.inicio = time.time()
        if time.time()-self.inicio>0.4 and self.HP>0:
            self.acao = "down"
            self.inicio = time.time()+1000

    def defeated(self,screen,otherPlayer):
        """
        Show the won frame of player1
        """
        if self.HP <= 0:
            #import pdb; pdb.set_trace()
            self.acao = "lose"
            if self.cronometrar2 == True:
                self.inicioDead = time.time()
                self.cronometrar2 = False
            if time.time()-self.inicioDead>1:
                screen.blit(otherPlayer.Win, (300,200))

    def loadCharacter(self, character):
        """
        Load all images of the Player
        """
        if character == 'goku':
            self.photo3x4 = pygame.image.load("../resources/imagens/player/goku/ss4/gokuPhoto.png")
            self.photo3x4Fliped  = pygame.transform.flip(self.photo3x4, 1,0)
            self.Win = pygame.image.load("../resources/imagens/player/goku/ss4/gokuWin.png")
            self.loadSprites("../resources/imagens/player/goku/ss4/goku-ss4.png")
            self.createAnimation(0,0,48,70,4,"down",hold = False)
            self.createAnimation(6,200,51,70,4,"up")
            self.erasePositions("up", [0,2])
            self.repeatPosition("up",1, [1])
            self.createAnimation(0,72,65,70,4,"right")   
            self.createAnimation(164,2272,56,70,4,"defend") 
            self.erasePositions("defend",[0,1,3])
            self.createAnimation(164,1500,57,80,10,"kameham",hold=True, speed = 1) 
            self.erasePositions("kameham",[6,7,8,9])
            #Goku-Punch
            self.insertFrame(120,367,58,60)
            self.insertFrame(180,367,58,60)
            #player1.insertFrame(211,1674,65,60)
            self.insertFrame(211,1674,65,60)
            self.insertFrame(249,367,65,60)
            #hold to maintain last frame
            self.buildAnimation("punch",hold=True, speed = 5)
            #Goku-Kick
            self.insertFrame(113,443,57,60)
            self.insertFrame(166,443,60,60)
            self.insertFrame(235,443,66,60)
            self.insertFrame(303,443,66,60)
            self.insertFrame(375,443,68,60)
            self.insertFrame(448,443,68,60)
            self.insertFrame(375,443,58,60)
            self.buildAnimation("kick",hold=True, speed = 5)
            #Goku-Lose
            self.insertFrame(855,3354,40,60)
            self.buildAnimation("lose",hold=False, speed = 10)
            #Goku-Loading
            self.insertFrame(115,1400,83,90)
            self.insertFrame(195,1400,83,90)
            #self.insertFrame(60,1419,60,65)
            self.buildAnimation("load",hold=True, speed = 15)
            #Goku been hit
            self.insertFrame(65,900,52,90)
            self.insertFrame(170,900,80,90)
            self.buildAnimation("hited",hold=True, speed = 5)
        if character == 'vegeta':
            self.photo3x4 = pygame.image.load("../resources/imagens/player/vegeta/vegeta-2.png")
            self.photo3x4Fliped  = pygame.transform.flip(self.photo3x4, 1,0)
            self.Win = pygame.image.load("../resources/imagens/player/vegeta/vegetaWin.jpeg")
            self.loadSprites("../resources/imagens/player/vegeta/vegeta-ss4-2.png")
            self.insertFrame(381,68,40,80)
            self.insertFrame(419,68,36,80)
            self.insertFrame(453,68,40,80)
            self.insertFrame(491,68,40,80)
            self.buildAnimation("down",hold=False, speed = 10)
            #Vegeta-Lose
            self.insertFrame(840,1407,40,80)
            self.buildAnimation("lose",hold=False, speed = 10)
            #Vegeta-Back
            self.insertFrame(49,982,48,80)
            self.buildAnimation("up",hold=False, speed = 10)
            #Vegeta-Left
            self.insertFrame(0,161,55,55)
            self.buildAnimation("right",hold=False, speed = 10)
            #Vegeta-Right
            self.insertFrame(634,84,46,55)
            self.buildAnimation("defend",hold=False, speed = 10)
            #Vegeta-Punch
            self.insertFrame(57,417,55,55)
            self.insertFrame(110,417,70,55)
            self.insertFrame(175,417,65,55)
            self.buildAnimation("punch",hold=True, speed = 5)
            #Vegeta-Kick
            #player2.insertFrame(1,594,55,75)
            self.insertFrame(56,594,41,75)
            self.insertFrame(96,594,55,75)
            self.insertFrame(155,594,65,75)
            self.buildAnimation("kick",hold=True, speed = 4)
            #Vegeta-Kameham
            self.insertFrame(225,2007,55,75)
            self.insertFrame(274,2007,55,75)
            self.insertFrame(325,2007,70,75)
            self.buildAnimation("kameham",hold=True, speed = 5)
            #Vegeta-Loading
            self.insertFrame(112,1274,95,85)
            self.insertFrame(200,1274,95,85)
            self.buildAnimation("load",hold=True, speed = 5)
            #Vegeta-Hited
            self.insertFrame(0,1400,48,75)
            self.insertFrame(48,1400,43,75)
            self.buildAnimation("hited",hold=True, speed = 5)
        if character == 'trunks':
            self.photo3x4 = pygame.image.load("../resources/imagens/player/trunks/trunks3x4.png")
            self.photo3x4Fliped  = pygame.transform.flip(self.photo3x4, 1,0)
            if self.playerId == 2:
                self.Win = pygame.image.load("../resources/imagens/player/trunks/win2.jpg")
                self.Win  = pygame.transform.flip(self.Win, 1,0)
            else:
                self.Win = pygame.image.load("../resources/imagens/player/trunks/win2.jpg")
            self.loadSprites("../resources/imagens/player/trunks/trunks.png")
            self.insertFrame(37,18,50,75)
            self.insertFrame(84,18,50,75)
            self.buildAnimation("down",hold=False, speed = 15)
            self.insertFrame(760,118,50,85)
            self.buildAnimation("up",hold=False, speed = 15)
            self.insertFrame(28,994,60,95)
            self.buildAnimation("right",hold=False, speed = 15)
            self.insertFrame(226,1630,50,85)
            self.insertFrame(272,1630,50,85)
            self.insertFrame(318,1630,50,85)
            self.buildAnimation("kameham",hold=True, speed = 5)
            self.insertFrame(239,2524,50,85)
            self.buildAnimation("hited",hold=True, speed = 5)
            self.insertFrame(814,2772,130,135)
            self.insertFrame(940,2772,130,135)
            self.buildAnimation("load",hold=True, speed = 5)
            self.insertFrame(553,2752,100,75)
            self.buildAnimation("lose",hold=False, speed = 15)
            self.insertFrame(85,2304,48,95)
            self.buildAnimation("defend",hold=False, speed = 15)
            self.insertFrame(155,1124,60,95)
            self.insertFrame(216,1103,90,130)
            self.insertFrame(304,1140,90,130)
            self.insertFrame(401,1122,100,130)
            self.buildAnimation("punch",hold=False, speed = 5)
            self.insertFrame(370,682,50,85)
            self.insertFrame(536,500,70,85)
            #self.insertFrame(370,682,50,85)
            #self.insertFrame(428, 681,70,85)
            self.buildAnimation("kick",hold=True, speed = 5)

    def loadPower(self,power):
        """
        Load power images
        """
        power.loadSprites("../resources/imagens/player/goku/ss4/power-1.png")
        power.createAnimation(1300,1604,146,40,1,"void")
        #power1.insertFrame(1300,1604,146,40) #void
        #power1.insertFrame(1300,1604,146,40) #void
        #power1.insertFrame(644,1197,700,40) 
        power.insertFrame(0,132,1100,50) #Full Power
        power.insertFrame(0,132,1100,50) #Full Power
        power.insertFrame(0,132,1100,50) #Full Power
        #power1.insertFrame(1176,1604,70,40)
        power.insertFrame(1300,1604,146,40) #void
        power.buildAnimation("kame",hold=True, speed = 10)
    
    def playPC(self, player1, power2):
        """
        Pc player
        """
        if self.XP > 20:
            self.acao = "kameham"
            power2.acao = "kame"
            self.pressed = True
            power2.pressed = True
            self.pos = 1
            self.Attacking = True
            self.Defending = False
            if self.facingRight == False:
                player2AttackRect = Rect(self.x-950, self.y+10, 1000, 60)
                #pygame.draw.rect(screen, (0,255,0), player2AttackRect)
            elif self.facingRight == True:
                player2AttackRect = Rect(self.x+45, self.y+10, 1000, 60)
                #pygame.draw.rect(screen, (0,255,0), player2AttackRect)
            if player2AttackRect.colliderect(player1.Rect) == True:
                if player1.Defending == False:
                    player1.HP -= 10
                if player1.Defending == True and player1.Attacking == False:
                    player1.HP -= 2
            self.acao = "down"
            self.XP-=10
        if self.XP <0 or self.XP < 30:
            self.acao = "load"
            self.pressed = True
            self.pos = 1
            self.XP+= 5 

