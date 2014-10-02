#!/usr/bin/python
import pygame, sys, glob
from pygame import *
from spriteanimation import SpriteAnimation
from characters import Characters
import time
import random
import datetime

class NPC(Characters):
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
        self.teleport = True

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

    def lockInsideScreenPC(self,width,height,delta,player1):
        """
        Movement of the pc locking him
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

    def playPC(self, enemyPlayer, power2,resolution):
        """
        Pc player
        """
        width,height = resolution
        if self.HP > 0:
            if self.superPunchState == True:
                if time.time()*1000-self.inicioPunch <200:
                    if self.facingRight == True:
                        enemyPlayer.movex = 3
                    if self.facingRight == False:
                        enemyPlayer.movex = -3
                else:
                    enemyPlayer.movex = 0
                    self.superPunchState = False
            if self.superKickState == True:
                if time.time()*1000-self.inicioPunch <200:
                    enemyPlayer.movey = -3
                else:
                    enemyPlayer.movey= 0
                    self.superKickState = False
            if self.teleport == True:
                if self.x > width-50 and abs(self.x-enemyPlayer.x)<60 or self.x<-5 and abs(self.x-enemyPlayer.x)<60:
                        self.acao = "teleport"
                        self.pressed = True
                        self.x = random.randint(0,1170)
                        self.y = random.randint(0,738)
                        self.inicio = time.time()
                if self.y <0 and abs(self.y -enemyPlayer.y)<40:
                        self.acao = "teleport"
                        self.pressed = True
                        self.x = random.randint(0,1170)
                        self.y = random.randint(0,738)
                        self.inicio = time.time()

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
                        if self.XP <= self.XPMAX:
                            enemyPlayer.HP -= self.punchDamage*self.fatorSuper
                        if self.XP == self.XPMAX:
                            enemyPlayer.HP -= self.powerDamage
                            if random.randint(0,11) > 5:
                                self.superPunchState = True
                                #self.inicioEffects2 = time.time()*1000
                            else:
                                self.superKickState = True
                                #self.inicioEffects2 = time.time()*1000

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
                if self.XP < self.XPMAX:
                    self.XP+= 1 
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
        
           
