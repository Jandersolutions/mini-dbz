#!/usr/bin/python
import pygame, sys, glob
from pygame import *
from spriteanimation import SpriteAnimation
from characters import Characters
import time
import random
import datetime

class Player(Characters):
    def __init__(self, acaoInicial, playerId, speed = 15):
        """Iniciation of the player states"""
        Characters.__init__(self,acaoInicial, speed = 15)
        self.pos = 1
        self.pos2 = 1
        self.movex, self.movey = 0,0
        self.facingRight = True
        self.x = 250
        self.y = 350
        self.Rect = Rect(self.x, self.y, 35, 70)
        self.HP = 400
        self.XP = 50
        self.XPMAX = 150
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
        self.playerId = playerId
        self.loading = False
        self.powerDisputa = True
        self.superPunchState = False
        self.superKickState = False
        self.fatorSuper = 1.4
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
        #self.inicialTime
        self.inicio1Pc = time.time()*1000
        self.inicio2Pc = time.time()*1000
        self.inicio3Pc = time.time()*1000
        self.inicio4Pc = time.time()*1000
        self.inicio5Pc = time.time()*1000
        self.inicio6Pc = time.time()*1000
        self.inicio7Pc = time.time()*1000
        self.inicio8Pc = time.time()*1000
        self.startTimer = time.time()*1000
        self.inicioFaisca = time.time()*1000
        self.inicioExplosao = time.time()*1000
        self.inicioExplosao2 = time.time()*1000
        self.inicio2 = 0
        self.kamehamMs = 160
        self.punchMs = 90
        self.releasePower = True
        self.voidPower = True
        self.kameCont = 22
        self.enemykameCont = 0
        self.staticy = 0
        self.inicioKame = time.time()*1000
        self.inicioPunch = time.time()*1000
        self.inicioEffects = time.time()*1000
        self.inicioEffects2 = time.time()*1000
        self.isPC = False
        self.singleKameham = True
        self.disputeKamehamBoolean = True

    def superPunch(self, playerList):
        """
        Activates the super punch
        """
        if self.superPunchState == True:
            if time.time()*1000-self.inicioPunch <200:
                for player in playerList:
                    if self.facingRight == True:
                        player.movex = 3
                    if self.facingRight == False:
                        player.movex = -3
            else:
                for player in playerList:
                    player.movex = 0
                self.superPunchState = False

    def superKick(self, playerList):
        """
        Activates the super kick
        """
        if self.superKickState == True:
            if time.time()*1000-self.inicioPunch <200:
                for player in playerList:
                    player.movey = -3
            else:
                for player in playerList:
                    player.movey= 0
                self.superKickState = False

    def punch(self, playerList):
        """
        Punch action
        """
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
                    if self.XP <= self.XPMAX:
                        player.HP -= self.punchDamage
                    if self.XP == self.XPMAX:
                        player.HP -= self.powerDamage*self.fatorSuper
                        self.superPunchState = True
                        #self.inicioEffects2 = time.time()*1000
                    player.inicio = time.time()
                    if abs(player.inicioPunch-self.inicioPunch)<400:
                        self.inicioEffects = time.time()*1000
                        #pass
                    else:
                        player.acao = "hited"
                if player.Defending == True and player.Attacking == False:
                    player.HP -= player.hitDefended
        self.inicio = time.time()

    def kick(self, playerList):
        """
        Kick action
        """
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
                    if self.XP <= self.XPMAX:
                        player.HP -= self.kickDamage
                    if self.XP == self.XPMAX:
                        player.HP -= self.powerDamage*self.fatorSuper
                        self.superKickState = True
                        #self.inicioEffects2 = time.time()*1000
                    if abs(player.inicioPunch-self.inicioPunch)<400:
                        self.inicioEffects = time.time()*1000
                    else:
                        player.acao = "hited"
                    player.inicio = time.time()
                if player.Defending == True and player.Attacking == False:
                    player.HP -= player.hitDefended
        self.inicio = time.time()

    def combo(self, playerList, power1):
        """ 
        Attempt to implement combo
        """
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

    def kameham(self, playerList, power1):
        """
        Kameham power
        """
        self.inicioKame = time.time()*1000
        self.kameCont +=1
        if self.XP > 0:
            for player in playerList:
                if abs(self.y - player.y) <50 and abs(player.inicioKame-self.inicioKame)<400:
                    if self.disputeKamehamBoolean == True:
                        self.cronometrarDisputa = True
                        self.releasePower = True
                        self.voidPower = True
                        self.kameCont =0
                        if player.isPC == False:
                            player.kameCont = 0
                        self.disputeKamehamBoolean = False
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

    def load(self):
        """
        Loads XP
        """
        self.acao = "load"
        self.pressed = True
        self.inicio = time.time()
        if self.XP < self.XPMAX:
            self.XP+= 5 
    
    def teleport(self):
        """
        Teleports to a random place
        """
        self.acao = "teleport"
        self.pressed = True
        self.x = random.randint(0,1170)
        self.y = random.randint(0,738)
        self.inicio = time.time()
    
    def playPlayer(self,eventArg, playerList, power1):
        """
        Play movements and skills
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
                    self.kameham(playerList, power1)
                if event.key == self.k_punch:
                    self.punch(playerList)
                if event.key == self.k_combo:
                    self.kameham(playerList, power1)
                if event.key == self.k_kick:
                    self.kick(playerList)
                if event.key == self.k_load:
                    self.load()
                if event.key == self.k_teleport:
                    self.teleport()
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
            self.superPunch(playerList)
            self.superKick(playerList)

    def kamehamDispute(self,localPower,playerList,powers):
        """
        Listener of the kameham dispute
        """
        if self.cronometrarDisputa == True:
            self.inicio2 = time.time()*1000
            self.cronometrarDisputa = False
            self.staticy = self.y
        if time.time()*1000-self.inicio2 < 4000:
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
            for power in powers2:
                power.acao = 'void'
            for otherPlayer in playerList:
                if self.facingRight == True:
                    if self.kameCont-otherPlayer.kameCont >0:
                        localPower.acao = "disputa3"
                    if otherPlayer.kameCont-self.kameCont >0:
                        localPower.acao = "disputa2"
                    if self.kameCont-otherPlayer.kameCont == 0:
                        localPower.acao = "disputa"
                if self.facingRight == False:
                    if self.kameCont-otherPlayer.kameCont >0:
                        localPower.acao = "disputa2"
                    if otherPlayer.kameCont-self.kameCont >0:
                        localPower.acao = "disputa3"
                    if self.kameCont-otherPlayer.kameCont == 0:
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
        if time.time()*1000 -self.inicio2 > 5000:
            self.disputeKamehamBoolean = True

    def playEffects(self, effects):
        """
        Animation effects of the fight
        """
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

        if self.XP == self.XPMAX:
            effects.acao = "ki"
            if self.facingRight == True:
                effects.x = self.x-22
                effects.y = self.y-20
            else:
                effects.x = self.x-30
                effects.y = self.y-20
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
        if self.x < otherPlayer.x:
            self.facingRight = True

    def lockInsideScreen(self,width,height,delta):
        """
        Movement of the player, locking him 
        on the visible screen
        """
        if self.facingRight == True:
            if self.movex <= -1 and self.x>0:
                self.x += self.movex * delta
            if self.movex >= 1 and self.x<width-50:
                self.x += self.movex * delta
        if self.facingRight == False:
            if self.movex <= -1 and self.x>0:
                self.x += self.movex * delta
            if self.movex >= 1 and self.x<width-50:
                self.x += self.movex * delta
        if self.movey >= 1 and self.y<height-70:
            self.y += self.movey * delta
        if self.movey <= -1 and self.y>0:
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
        Hp and XP bars of the player
        """
        if self.playerId == 1:
            playerHPRect = Rect(80 , 20, self.HP, 20)
            playerXPRect = Rect(80 , 60, self.XP*2, 20)
            screen.blit(self.photo3x4, (0,20))
        if self.playerId == 4:
            playerHPRect = Rect(80 , 100, self.HP, 20)
            playerXPRect = Rect(80 , 140, self.XP*2, 20)
            screen.blit(self.photo3x4, (0,100))
        if self.playerId == 2 or self.playerId ==0:
            playerHPRect = Rect(width-80, 20, -self.HP, 20)
            playerXPRect = Rect(width-80, 60, -self.XP*2, 20)
            screen.blit(self.photo3x4Fliped, (width-70,20))
        if self.playerId == 3:
            playerHPRect = Rect(width-80, 100, -self.HP, 20)
            playerXPRect = Rect(width-80, 140, -self.XP*2, 20)
            screen.blit(self.photo3x4Fliped, (width-70,100))
        if self.HP >=0:
            pygame.draw.rect(screen, (255,0,0), playerHPRect)
        pygame.draw.rect(screen, (0,0,255), playerXPRect)
        if self.XP == self.XPMAX:
            pygame.draw.rect(screen, (0,255,0), playerXPRect)

    def standUpPosition(self):
        """
        Standard stand up position of player
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
        Show the win picture of the otherPlayer
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
        Show the win picture of player1
        """
        if self.HP <= 0:
            #import pdb; pdb.set_trace()
            self.acao = "lose"
            if self.cronometrar2 == True:
                self.inicioDead = time.time()
                self.cronometrar2 = False
            if time.time()-self.inicioDead>1:
                screen.blit(otherPlayer.Win, (300,200))
