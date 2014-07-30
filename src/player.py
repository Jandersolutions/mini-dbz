#!/usr/bin/python
import pygame, sys, glob
from pygame import *
from spriteanimation import SpriteAnimation
import time
import random
import datetime

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
        self.cronometrarDisputa = False
        self.punchDamage = 2
        self.kickDamage = 2
        self.hitDefended = 0.4
        self.powerDamage = 10
        self.powerDamageDefended = 2
        self.comboDamage = 10
        self.HP = 400
        self.XP = 50
        self.playerId = playerId
        self.loading = False
        self.powerDisputa = True
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
            self.k_combo = K_c
            self.k_teleport = K_k
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
            self.k_combo = K_n
            self.k_teleport = K_KP6
        self.inicio1Pc = time.time()*1000
        self.inicio2Pc = time.time()*1000
        self.inicio3Pc = time.time()*1000
        self.inicio4Pc = time.time()*1000
        self.inicio5Pc = time.time()*1000
        self.inicio6Pc = time.time()*1000
        self.inicio7Pc = time.time()*1000
        self.inicio8Pc = time.time()*1000
        self.inicioFaisca = time.time()*1000
        self.inicioExplosao = time.time()*1000
        self.inicio2 = 0
        self.kamehamMs = 160
        self.punchMs = 90
        self.releasePower = True
        self.voidPower = True
        self.kameCont = 12
        self.enemykameCont = 0
        self.staticy = 0
        self.inicioKame = time.time()*1000
        self.inicioPunch = time.time()*1000
        self.inicioEffects = time.time()*1000
        self.isPC = False
        self.singleKameham = True
    
    def playPlayer(self,eventArg, playerList, power1):
        """
        Activate player movements and skills
        """
        if self.HP>0:
            event = eventArg
            if event.type == KEYDOWN:
                #Goku
                if event.key == self.k_down:
                    self.acao = "down"
                    self.movey+=1
                if event.key == self.k_up:
                    self.acao = "up"
                    self.movey-=1
                if event.key == self.k_defend:
                    self.acao = "defend"
                    self.Defending = True
                if self.facingRight == True:
                    if event.key == self.k_rightArrow:
                        self.acao = "right"
                        self.movex+=1
                    if event.key == self.k_leftArrow:
                        self.acao = "up"
                        self.movex-=1
                if self.facingRight == False:
                    if event.key == self.k_rightArrow:
                        self.acao = "up"
                        self.movex+=1
                    if event.key == self.k_leftArrow:
                        self.acao = "right"
                        self.movex-=1
                if event.key == self.k_kameham:
                    self.inicioKame = time.time()*1000
                    if self.XP > 0:
                        for player in playerList:
                            if abs(self.y - player.y) <50 and abs(player.inicioKame-self.inicioKame)<400:
                                self.cronometrarDisputa = True
                                self.releasePower = True
                                self.voidPower = True
                                self.kameCont =0
                                if player.isPC == False:
                                    player.kameCont = 0
                        if self.singleKameham == True:
                            self.acao = "kameham"
                            power1.acao = "kame"
                            self.pressed = True
                            power1.pressed = True
                            self.Attacking = True
                            self.Defending = False
                            if self.facingRight == True:
                                selfAttackRect = Rect(self.x+30, self.y+20, 1000, 60)
                                #pygame.draw.rect(screen, (0,255,0), selfAttackRect)
                            else:
                                selfAttackRect = Rect(self.x-1000, self.y+20, 1000, 60)
                                #pygame.draw.rect(screen, (0,255,0), selfAttackRect)
                            for player in playerList:
                                if selfAttackRect.colliderect(player.Rect) == True:
                                    if player.Defending == False:
                                        player.HP -= self.powerDamage
                                        player.acao = "hited"
                                        player.inicio = time.time()
                                    if player.Defending == True and player.Attacking == False:
                                        player.HP -= player.powerDamageDefended
                            self.XP-=10
                            self.inicio = time.time()
                if event.key == self.k_punch:
                    self.kameCont +=1
                    self.acao = "punch"
                    self.pressed = True
                    self.Attacking = True
                    self.Defending = False
                    if self.facingRight == True:
                        selfAttackRect = Rect(self.x+30, self.y, 50, 70)
                        #pygame.draw.rect(screen, (0,0,255), selfAttackRect)
                    if self.facingRight == False:
                        selfAttackRect = Rect(self.x-20, self.y, 50, 70)
                        #pygame.draw.rect(screen, (0,0,255), selfAttackRect)
                    self.inicioPunch = time.time()*1000
                    for player in playerList:
                        if selfAttackRect.colliderect(player.Rect) == True:
                            if player.Defending == False:
                                player.HP -= self.punchDamage
                                player.inicio = time.time()
                                if abs(player.inicioPunch-self.inicioPunch)<400:
                                    pass
                                else:
                                    player.acao = "hited"
                            if player.Defending == True and player.Attacking == False:
                                player.HP -= player.hitDefended
                    self.inicio = time.time()

                if event.key == self.k_combo:
                    self.acao = "combo"
                    #self.pressed = True
                    self.pos = 1
                    self.Attacking = True
                    self.Defending = False
                    if self.facingRight == True:
                        selfAttackRect = Rect(self.x+30, self.y, 50, 70)
                        #pygame.draw.rect(screen, (0,0,255), selfAttackRect)
                    if self.facingRight == False:
                        selfAttackRect = Rect(self.x-15, self.y, 50, 70)
                        #pygame.draw.rect(screen, (0,0,255), selfAttackRect)
                    for player in playerList:
                        if selfAttackRect.colliderect(player.Rect) == True:
                            if player.Defending == False:
                                player.HP -= self.comboDamage
                                player.acao = "hited"
                                player.inicio = time.time()
                            if player.Defending == True and player.Attacking == False:
                                player.HP -= player.hitDefended
                    #self.inicio = time.time()
                if event.key == self.k_kick:
                    self.acao = "kick"
                    self.pressed = True
                    self.Attacking = True
                    self.Defending = False
                    if self.facingRight == True:
                        selfAttackRect = Rect(self.x+30, self.y, 35, 70)
                        #pygame.draw.rect(screen, (255,0,0), selfAttackRect)
                    if self.facingRight == False:
                        selfAttackRect = Rect(self.x-20, self.y, 35, 70)
                        #pygame.draw.rect(screen, (255,0,0), selfAttackRect)
                    self.inicioPunch = time.time()*1000
                    for player in playerList:
                        if selfAttackRect.colliderect(player.Rect) == True:
                            if player.Defending == False:
                                player.HP -= self.kickDamage
                                if abs(player.inicioPunch-self.inicioPunch)<400:
                                    self.inicioEffects = time.time()*1000
                                else:
                                    player.acao = "hited"
                                player.inicio = time.time()
                            if player.Defending == True and player.Attacking == False:
                                player.HP -= player.hitDefended
                    self.inicio = time.time()
                if event.key == self.k_load:
                    self.acao = "load"
                    self.pressed = True
                    self.XP+= 5 
                    self.inicio = time.time()
                if event.key == self.k_teleport:
                    self.acao = "teleport"
                    self.pressed = True
                    self.x = random.randint(0,1170)
                    self.y = random.randint(0,738)
                    self.inicio = time.time()
            if event.type == KEYUP:
                if event.key == self.k_down:
                    self.acao = "down"
                    self.movey=0
                if event.key == self.k_up:
                    self.acao = "up"
                    self.movey=0
                if event.key == self.k_defend:
                    self.acao = "defend"
                    self.Defending = False
                if event.key == self.k_punch:
                    self.Attacking = False
                if self.facingRight  == True:
                    if event.key == self.k_rightArrow:
                        self.acao = "right"
                        self.movex=0
                    if event.key == self.k_leftArrow:
                        self.acao = "up"
                        self.movex=0
                if self.facingRight  == False:
                    if event.key == self.k_leftArrow:
                        self.acao = "right"
                        self.movex=0
                    if event.key == self.k_rightArrow:
                        self.acao = "up"
                        self.movex=0
                if event.key == self.k_kameham:
                    self.acao = "kameham"
                    power1.acao = "void"
                    self.movex=0
    
    def kameham(self,localPower,playerList,powers):
        if self.cronometrarDisputa == True:
            self.inicio2 = time.time()*1000
            self.cronometrarDisputa = False
            self.staticy = self.y
        if time.time()*1000-self.inicio2 < 4000:
            #powerDisputa responsabilidade de um player pela Disputa
            #if self.powerDisputa == True:
                #localPower.acao = "disputa"
            if self.facingRight == True:
                localPower.x = self.x+52
                localPower.y = self.y+10
                self.x = 40
                self.y = self.staticy
            if self.facingRight == False:
                self.x = 1120 
                self.y = self.staticy
            self.acao = "disputa"
            self.pressed = True
            localPower.pressed = True
            self.inicio = time.time()
            self.singleKameham = False
            powers2 = powers[:]
            #powers2.remove(power1)
            for power in powers2:
                power.acao = 'void'
            for otherPlayer in playerList:
                if self.facingRight == True:
                    if self.kameCont-otherPlayer.kameCont >3:
                        localPower.acao = "disputa3"
                    if otherPlayer.kameCont-self.kameCont >3:
                        localPower.acao = "disputa2"
                    if self.kameCont-otherPlayer.kameCont <2 and self.kameCont-otherPlayer.kameCont>=0:
                        localPower.acao = "disputa"
                if self.facingRight == False:
                    if self.kameCont-otherPlayer.kameCont >3:
                        localPower.acao = "disputa2"
                    if otherPlayer.kameCont-self.kameCont >3:
                        localPower.acao = "disputa3"
                    if self.kameCont-otherPlayer.kameCont <2 and self.kameCont-otherPlayer.kameCont>=0:
                        localPower.acao = "disputa"
                if self.facingRight == True:
                    otherPlayer.y = self.y+10
                    otherPlayer.x = self.x+1080
                if self.facingRight == False:
                    otherPlayer.x = 40
                    otherPlayer.y = self.staticy
                    localPower.x = otherPlayer.x+42
                    localPower.y = otherPlayer.y+5
                otherPlayer.acao = 'disputa'
                otherPlayer.inicio = time.time()
                otherPlayer.singleKameham = False
        if time.time()*1000 -self.inicio2 > 4000 and self.releasePower == True:
            for otherPlayer in playerList:
                self.releasePower = False
                self.enemykameCont = otherPlayer.kameCont
                if self.kameCont > otherPlayer.kameCont:
                    otherPlayer.HP -= 50
                    if self.facingRight == True:
                        localPower.acao = 'from-right'
                    if self.facingRight == False:
                        localPower.acao = 'from-left'
                if self.kameCont < otherPlayer.kameCont:
                    if self.facingRight == True:
                        localPower.acao = 'from-left'
                    if self.facingRight == False:
                        localPower.acao = 'from-right'
                if self.kameCont == otherPlayer.kameCont:
                    localPower.acao = "void"
            if self.kameCont < self.enemykameCont:
                self.HP -= 50
        if time.time()*1000 -self.inicio2 > 4500 and self.voidPower == True:
            self.voidPower = False
            localPower.acao = "void"
            self.singleKameham = True
            for otherPlayer in playerList:
                otherPlayer.singleKameham = True
    def playEffects(self, effects):
        if abs(time.time()*1000-self.inicioEffects) < 200:
            if random.random()>0.5 and abs(time.time()*1000-self.inicioFaisca)>1500:
                effects.acao = "faiscas"
                if abs(time.time()*1000 - self.inicioFaisca) > 2500:
                    effects.acao = "void"
                    self.inicioFaisca = time.time()*1000
            if random.random()<0.5 and abs(time.time()*1000-self.inicioExplosao)>3500:
                effects.acao = "explosao"
                if abs(time.time()*1000 - self.inicioExplosao) > 3700:
                    effects.acao = "void"
                    self.inicioExplosao = time.time()*1000
        else:
            effects.acao = "void"
        if self.facingRight == True:
            if effects.acao == "faiscas":
                effects.x = self.x+20
                effects.y = self.y+15
            if effects.acao == "explosao":
                effects.x = self.x
                effects.y = self.y-20
        else:
            if effects.acao == "faiscas":
                effects.x = self.x-5
                effects.y = self.y+15
            if effects.acao == "explosao":
                effects.x = self.x-25
                effects.y = self.y-25

    def TurnAround(self,otherPlayer):
        """
        Turn around automatically for player1 and player2
        """
        if self.x > otherPlayer.x:
            self.facingRight = False
            #player2.facingRight = True
        if self.x < otherPlayer.x:
            self.facingRight = True
            #player2.facingRight = False

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
    def lockInsideScreenPC(self,width,height,delta,player1):
        """
        Lock the PC to the visible screen
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
        if self.y < player1.y:
            if self.movey == 1 and self.y<height-70:
                self.y += self.movey * delta
        if self.y > player1.y:
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
        if self.playerId == 4:
            playerHPRect = Rect(80 , 100, self.HP*2, 20)
            playerXPRect = Rect(80 , 140, self.XP*2, 20)
            screen.blit(self.photo3x4, (0,100))
        if self.playerId == 2 or self.playerId ==0:
            playerHPRect = Rect(width-80, 20, -self.HP*2, 20)
            playerXPRect = Rect(width-80, 60, -self.XP*2, 20)
            screen.blit(self.photo3x4Fliped, (width-70,20))
        if self.playerId == 3:
            playerHPRect = Rect(width-80, 100, -self.HP*2, 20)
            playerXPRect = Rect(width-80, 140, -self.XP*2, 20)
            screen.blit(self.photo3x4Fliped, (width-70,100))
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

    def teamDefeated(self,screen,otherPlayer,teamList):
        """
        Show the won frame of otherPlayer
        """
        mortos = 0
        totalOfPlayer=len(teamList)
        for player in teamList:
            if player.HP <= 0:
                mortos+=1
                
        if mortos == totalOfPlayer:
            #import pdb; pdb.set_trace()
            self.acao = "lose"
            if self.cronometrar2 == True:
                self.inicioDead = time.time()
                self.cronometrar2 = False
            if time.time()-self.inicioDead>1:
                screen.blit(otherPlayer.Win, (300,200))
    
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
            self.buildAnimation("hited",hold=False, speed = 15)
            #Goku-Combo
            self.insertFrame(119,1653,50,80)
            self.insertFrame(167,1653,47,80)
            self.insertFrame(114,1728,50,80)
            self.insertFrame(168,1730,50,80)
            self.insertFrame(217,1730,70,80)
            self.insertFrame(284,1730,70,80)
            self.insertFrame(349,1730,50,80)
            self.insertFrame(402,1730,50,80)
            #puch-combo
            self.insertFrame(120,367,58,60)
            self.insertFrame(180,367,58,60)
            #player1.insertFrame(211,1674,65,60)
            self.insertFrame(211,1674,65,60)
            self.insertFrame(249,367,65,60)
            #kick-combo
            self.insertFrame(113,443,57,60)
            self.insertFrame(166,443,60,60)
            self.insertFrame(235,443,66,60)
            self.insertFrame(303,443,66,60)
            self.insertFrame(375,443,68,60)
            self.insertFrame(448,443,68,60)
            self.insertFrame(375,443,58,60)
            self.insertFrame(454,1730,50,80)
            self.buildAnimation("combo",hold=True, speed = 5)
            #Goku-Teleport
            self.insertFrame(119,1653,50,80)
            self.insertFrame(167,1653,47,80)
            self.buildAnimation("teleport",hold=True, speed = 5)
            #Goku-Disputa
            self.insertFrame(498,1815,55,60)
            self.insertFrame(560,1815,55,60)
            self.buildAnimation("disputa",hold=True, speed = 5)
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
            self.buildAnimation("hited",hold=False, speed = 15)
            #Vegeta-Teleport
            self.insertFrame(642,289,50,80)
            self.buildAnimation("teleport",hold=True, speed = 5)
            #Vegeta-Disputa
            self.insertFrame(333,2012,55,60)
            self.insertFrame(390,2012,55,60)
            self.buildAnimation("disputa",hold=False, speed = 10)
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
            self.insertFrame(272,1630,50,85)
            self.insertFrame(318,1630,50,85)
            self.buildAnimation("disputa",hold=False, speed = 5)
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
            self.insertFrame(597,1115,70,90)
            self.buildAnimation("teleport",hold=True, speed = 5)
        if character == 'frieza':
            self.photo3x4 = pygame.image.load("../resources/imagens/player/frieza/frieza3x4.png")
            self.photo3x4Fliped  = pygame.transform.flip(self.photo3x4, 1,0)
            self.Win = pygame.image.load("../resources/imagens/player/frieza/win.png")
            self.loadSprites("../resources/imagens/player/frieza/frieza-3.png")
            self.insertFrame(29,98,40,65)
            self.insertFrame(73,98,40,65)
            self.buildAnimation("down",hold=False, speed = 10)
            self.insertFrame(110,1170,55,85)
            self.insertFrame(163,1170,55,85)
            self.buildAnimation("up",hold=False, speed = 10)
            self.insertFrame(23,200,65,75)
            self.insertFrame(91,200,65,75)
            self.buildAnimation("right",hold=False, speed = 10)
            self.insertFrame(75,2490,65,75)
            self.buildAnimation("hited",hold=False, speed = 10)
            self.insertFrame(256,2500,80,90)
            self.buildAnimation("lose",hold=False, speed = 10)
            self.insertFrame(289,1742,120,90)
            self.insertFrame(408,1742,120,90)
            self.buildAnimation("load",hold=False, speed = 10)
            self.insertFrame(23,522,50,80)
            self.insertFrame(80,522,50,80)
            self.insertFrame(143,522,78,80)
            self.insertFrame(234,522,78,80)
            self.insertFrame(306,522,50,80)
            self.insertFrame(358,522,50,80)
            self.buildAnimation("kick",hold=False, speed = 5)
            #self.insertFrame(378,1870,60,70)
            self.insertFrame(148,1888,100,60)
            self.insertFrame(262,1888,100,60)
            self.insertFrame(456,2598,60,60)
            self.insertFrame(522,2598,60,60)
            self.insertFrame(580,2598,60,60)
            self.insertFrame(640,2598,60,60)
            self.buildAnimation("punch",hold=True, speed = 4)
            self.insertFrame(405,100,55,65)
            self.buildAnimation("defend",hold=False, speed = 15)
            self.insertFrame(318,193,70,80)
            self.buildAnimation("teleport",hold=True, speed = 5)
            #self.insertFrame(294,2080,60,85)
            #self.insertFrame(363,2080,70,85)
            #self.insertFrame(443,2080,80,85)
            #self.insertFrame(544,2080,80,85)
            self.insertFrame(331,2165,70,100)
            self.insertFrame(395,2147,65,120)
            self.insertFrame(458,2180,65,90)
            self.insertFrame(609,2180,75,80)
            self.buildAnimation("kameham",hold=False, speed = 5)
            self.insertFrame(443,2080,90,75)
            self.insertFrame(544,2080,80,85)
            self.buildAnimation("disputa",hold=True, speed = 5)
        if character == 'gohan':
            self.photo3x4 = pygame.image.load("../resources/imagens/player/gohan/gohan3x4.png")
            self.photo3x4Fliped  = pygame.transform.flip(self.photo3x4, 1,0)
            self.Win = pygame.image.load("../resources/imagens/player/gohan/win.png")
            self.loadSprites("../resources/imagens/player/gohan/gohan.png")
            self.insertFrame(10,53,50,80)
            self.insertFrame(57,53,50,80)
            self.buildAnimation("down",hold=False, speed = 10)
            self.insertFrame(167,330,50,85)
            self.insertFrame(65,330,50,85)
            self.buildAnimation("up",hold=False, speed = 10)
            self.insertFrame(12,150,70,85)
            self.insertFrame(83,150,70,85)
            self.buildAnimation("right",hold=False, speed = 10)
            self.insertFrame(83,947,57,85)
            self.insertFrame(190,947,57,85)
            self.buildAnimation("hited",hold=False, speed = 10)
            self.insertFrame(28,1105,90,105)
            self.insertFrame(118,1105,90,105)
            self.buildAnimation("load",hold=False, speed = 10)
            self.insertFrame(74,442,57,80)
            self.buildAnimation("defend",hold=False, speed = 10)
            self.insertFrame(15,1412,57,80)
            self.buildAnimation("teleport",hold=True, speed = 10)
            self.insertFrame(70,564,60,80)
            self.insertFrame(127,564,60,80)
            self.insertFrame(182,564,75,80)
            self.buildAnimation("punch",hold=True, speed = 2)
            self.insertFrame(122,656,60,80)
            self.insertFrame(180,656,64,80)
            self.insertFrame(255,656,64,80)
            self.insertFrame(326,656,69,80)
            self.insertFrame(406,656,69,80)
            self.insertFrame(479,656,69,80)
            self.buildAnimation("kick",hold=True, speed = 5)
            self.insertFrame(495,1740,69,80)
            self.insertFrame(160,1740,69,80)
            self.insertFrame(292,1740,69,80)
            self.buildAnimation("kameham",hold=False, speed = 5)
            self.insertFrame(216,1420,72,80)
            self.insertFrame(346,1420,72,80)
            self.buildAnimation("disputa",hold=False, speed = 10)
            self.insertFrame(460,1065,80,80)
            self.buildAnimation("lose",hold=False, speed = 10)

    def loadPower(self,power):
        """
        Load power images
        """
        power.loadSprites("../resources/imagens/player/goku/ss4/power-1.png")
        power.createAnimation(1300,1604,146,40,1,"void")
        power.insertFrame(0,132,1100,50) #Full Power
        power.insertFrame(0,132,1100,50) #Full Power
        power.insertFrame(0,132,1100,50) #Full Power
        power.insertFrame(1300,1604,146,40) #void
        power.buildAnimation("kame",hold=True, speed = 10)
        power.insertFrame(10,370,1200,50) 
        power.insertFrame(10,480,1200,50) 
        power.insertFrame(10,370,1200,50) 
        power.insertFrame(10,540,1200,50) 
        power.buildAnimation("disputa",hold=False, speed = 10)
        power.insertFrame(10,851,1200,50) 
        power.insertFrame(10,914,1200,50) 
        power.buildAnimation("disputa2",hold=False, speed = 10)
        power.insertFrame(10,972,1200,50) 
        power.insertFrame(10,1037,1200,50) 
        power.buildAnimation("disputa3",hold=False, speed = 10)
        power.insertFrame(10,600,1200,50) #void
        power.insertFrame(10,660,1200,50) #void
        #power.insertFrame(1300,1604,146,40) #void
        power.buildAnimation("from-right",hold=True, speed = 10)
        power.insertFrame(3,720,1200,50) #void
        power.buildAnimation("from-left",hold=True, speed = 10)
        power.insertFrame(266,1580,50,50)
        power.insertFrame(108,1486,40,40)
        power.insertFrame(72,1486,40,40)
        power.insertFrame(295,1486,40,40)
        power.buildAnimation("faiscas",hold=False, speed = 10)
        power.insertFrame(506,2850,100,110)
        power.insertFrame(506,2850,100,110)
        power.insertFrame(358,2883,77,90)
        #power.insertFrame(274,2883,47,80)
        power.insertFrame(1300,1604,146,40) #void
        power.buildAnimation("explosao",hold=False, speed = 20)
    
    def playPC(self, enemyPlayer, power2,screen):
        """
        Pc player
        """
        if self.HP > 0:
            if time.time()*1000-self.inicio1Pc>self.kamehamMs and abs(self.y-enemyPlayer.y)< 50 and self.loading == False and abs(self.x-enemyPlayer.x)>65:
                if self.XP >= 10:
                    if self.singleKameham == True:
                        self.inicioKame = time.time()*1000
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
                        if player2AttackRect.colliderect(enemyPlayer.Rect) == True:
                            if enemyPlayer.Defending == False:
                                enemyPlayer.HP -= 10
                                enemyPlayer.acao = 'hited'
                                enemyPlayer.inicio = time.time()
                            if enemyPlayer.Defending == True and enemyPlayer.Attacking == False:
                                enemyPlayer.HP -= 2
                        self.XP-=10
                        self.inicio = time.time()
                        self.inicio1Pc = time.time()*1000
            if abs(self.x-enemyPlayer.x)<55 and abs(self.y-enemyPlayer.y)< 30 and abs(time.time()*1000-self.inicio2Pc) > self.punchMs:
                if random.randint(0,11) > 5:
                    self.acao = "punch"
                else:
                    self.acao = "kick"
                self.pressed = True
                self.pos = 1
                self.Attacking = True
                self.Defending = False
                if self.facingRight == True:
                    selfAttackRect = Rect(self.x+15, self.y, 70, 70)
                    #pygame.draw.rect(screen, (0,0,255), selfAttackRect)
                if self.facingRight == False:
                    selfAttackRect = Rect(self.x-15, self.y, 70, 70)
                    #pygame.draw.rect(screen, (0,0,255), selfAttackRect)
                self.inicioPunch = time.time()*1000
                if selfAttackRect.colliderect(enemyPlayer.Rect) == True:
                    if enemyPlayer.Defending == False:
                        enemyPlayer.HP -= self.punchDamage
                        if abs(self.x - enemyPlayer.x) <30 and abs(enemyPlayer.inicioPunch-self.inicioPunch)<400:
                            pass
                        else:
                            enemyPlayer.acao = "hited"
                        enemyPlayer.inicio = time.time()
                    if enemyPlayer.Defending == True and enemyPlayer.Attacking == False:
                        enemyPlayer.HP -= enemyPlayer.hitDefended
                self.inicio = time.time()
                self.inicio2Pc = time.time()*1000
            if abs(time.time()*1000-self.inicio3Pc) > 2000 and abs(self.x-enemyPlayer.x)>100:
                self.acao = "load"
                self.pressed = True
                self.pos = 1
                self.XP+= 2 
                self.inicio = time.time()
                self.loading = True
                if abs(time.time()*1000-self.inicio4Pc) >3000:
                    self.inicio3Pc = time.time()*1000
                    self.inicio4Pc = time.time()*1000
                    self.loading = False

            if abs(time.time()*1000-self.inicio5Pc) >2000:
                if enemyPlayer.y-self.y <0:
                    self.acao = "up"
                    self.pos = 1
                    self.movey=-1
                    if abs(time.time()*1000-self.inicio5Pc) >2350:
                        self.inicio5Pc = time.time()*1000
                        self.movey=0
                        self.pos = 0
                if enemyPlayer.y-self.y >0:
                    self.acao = "down"
                    self.pos = 1
                    self.movey=1
                    if abs(time.time()*1000-self.inicio5Pc) >2350:
                        self.inicio5Pc = time.time()*1000
                        self.movey=0
                        self.pos = 0
            if abs(enemyPlayer.x-self.x) >15 and abs(time.time()*1000-self.inicio6Pc) >2000:
                if self.facingRight == False:
                    self.acao = "right"
                    self.pos = 1
                    self.movex=-1
                    if abs(time.time()*1000-self.inicio6Pc) >2350:
                        self.inicio6Pc = time.time()*1000
                        self.movex=0
                        self.pos = 0
                if self.facingRight == True:
                    self.acao = "down"
                    self.pos = 1
                    self.movex=1
                    if abs(time.time()*1000-self.inicio6Pc) >2350:
                        self.inicio6Pc = time.time()*1000
                        self.movex=0
                        self.pos = 0
        
           
