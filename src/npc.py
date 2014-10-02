#!/usr/bin/python
import pygame, sys, glob
from pygame import *
from spriteanimation import SpriteAnimation
from characters import Characters
import time
import random
import datetime

class NPC(Characters):
    def __init__(self, initialAction, playerId, speed = 15):
        """Iniciation of the player states"""
        Characters.__init__(self,initialAction, speed = 15)
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
        self.initialTime = 0
        self.timing2 = True
        self.punchDamage = 2
        self.kickDamage = 2
        self.hitDefended = 0.4
        self.powerDamage = 10
        self.powerDamageDefended = 2
        self.comboDamage = 10
        self.playerId = playerId
        self.loading = False
        self.superPunchState = False
        self.superKickState = False
        self.factorSuper = 1.4
        #self.inicialTime
        self.initialTime1 = time.time()*1000
        self.initialTime2 = time.time()*1000
        self.initialTime3 = time.time()*1000
        self.initialTime4 = time.time()*1000
        self.initialTime5 = time.time()*1000
        self.initialTime6 = time.time()*1000
        self.initialSpark = time.time()*1000
        self.initialExplosion = time.time()*1000
        self.kamehamMs = 160
        self.punchMs = 90
        self.releasePower = True
        self.voidPower = True
        self.kameCont = 22
        self.enemykameCont = 0
        self.staticy = 0
        self.initialKame = time.time()*1000
        self.initialPunch = time.time()*1000
        self.initialEffects = time.time()*1000
        self.isPC = True
        self.singleKameham = True
        self.disputeKamehamBoolean = True
        self.teleportBoolean = True

    def playEffects(self, effects):
        """
        Animation effects of the fight
        """
        if abs(time.time()*1000-self.initialEffects) < 200:
            if random.random()>0.5 and abs(time.time()*1000-self.initialSpark)>1500:
                effects.action = "spark"
                if abs(time.time()*1000 - self.initialSpark) > 2500:
                    effects.action = "void"
                    self.initialSpark = time.time()*1000
            if random.random()<0.5 and abs(time.time()*1000-self.initialExplosion)>3500:
                effects.action = "explosion"
                if abs(time.time()*1000 - self.initialExplosion) > 3700:
                    effects.action = "void"
                    self.initialExplosion = time.time()*1000
        else:
            effects.action = "void"

        if self.XP == self.XPMAX:
            effects.action = "ki"
            if self.facingRight == True:
                effects.x = self.x-22
                effects.y = self.y-20
            else:
                effects.x = self.x-30
                effects.y = self.y-20
        if self.facingRight == True:
            if effects.action == "spark":
                effects.x = self.x+20
                effects.y = self.y+15
            if effects.action == "explosion":
                effects.x = self.x
                effects.y = self.y-20
        else:
            if effects.action == "spark":
                effects.x = self.x-5
                effects.y = self.y+15
            if effects.action == "explosion":
                effects.x = self.x-25
                effects.y = self.y-25

    def TurnAround(self,otherPlayer):
        """
        Turn around automatically
        """
        if self.x > otherPlayer.x:
            self.facingRight = False
        if self.x < otherPlayer.x:
            self.facingRight = True

    def lockInsideScreen(self,width,height,delta,player1):
        """
        Movement of the pc, locking it
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
        Adjusting the power position of npc
        """
        if (self.facingRight == True):
            power.x = self.x+dx1
            power.y = self.y+dy1
        else:
            power.x = self.x-dx2
            power.y = self.y+dy2

    def physicalRect(self):
        """
        Physical Rectangle of the npc
        """
        if self.action != "right":
            self.Rect = Rect(self.x, self.y, 35, 70)
        elif self.action == "right" and self.facingRight == True:
            self.Rect = Rect(self.x+30, self.y, 35, 70)
        elif self.action == "right" and self.facingRight == False:
            self.Rect = Rect(self.x, self.y, 35, 70)

    def statusBar(self,screen,width):
        """
        Hp and XP bars of the npc
        """
        if self.playerId == 2 or self.playerId ==0:
            playerHPRect = Rect(width-80, 20, -self.HP, 20)
            playerXPRect = Rect(width-80, 60, -self.XP*2, 20)
            screen.blit(self.photo3x4Fliped, (width-70,20))
        if self.HP >=0:
            pygame.draw.rect(screen, (255,0,0), playerHPRect)
        pygame.draw.rect(screen, (0,0,255), playerXPRect)
        if self.XP == self.XPMAX:
            pygame.draw.rect(screen, (0,255,0), playerXPRect)

    def standUpPosition(self):
        """
        Standard stand up position of the npc
        """
        if self.movex or self.movey !=0:
            self.initialTime = time.time()
        if self.Defending== True:
            self.initialTime = time.time()
        if time.time()-self.initialTime>0.4 and self.HP>0:
            self.action = "down"
            self.initialTime = time.time()+1000

    def defeated(self,screen,otherPlayer):
        """
        Show the win picture of the npc
        """
        if self.HP <= 0:
            #import pdb; pdb.set_trace()
            self.action = "lose"
            if self.timing2 == True:
                self.initialDead = time.time()
                self.timing2 = False
            if time.time()-self.initialDead>1:
                screen.blit(otherPlayer.Win, (300,200))

    def superPunch(self, enemyPlayer):
        """
        Activate the super punch
        """
        if self.superPunchState == True:
            if time.time()*1000-self.initialPunch <200:
                if self.facingRight == True:
                    enemyPlayer.movex = 3
                if self.facingRight == False:
                    enemyPlayer.movex = -3
            else:
                enemyPlayer.movex = 0
                self.superPunchState = False
        if self.superKickState == True:
            if time.time()*1000-self.initialPunch <200:
                enemyPlayer.movey = -3
            else:
                enemyPlayer.movey= 0
                self.superKickState = False

    def teleport(self, enemyPlayer,width):
        """
        Teleport to a randon place
        """
        if self.teleportBoolean == True:
            if self.x > width-50 and abs(self.x-enemyPlayer.x)<60 or self.x<-5 and abs(self.x-enemyPlayer.x)<60:
                self.action = "teleport"
                self.pressed = True
                self.x = random.randint(0,1170)
                self.y = random.randint(0,738)
                self.initialTime = time.time()
            if self.y <0 and abs(self.y -enemyPlayer.y)<40:
                self.action = "teleport"
                self.pressed = True
                self.x = random.randint(0,1170)
                self.y = random.randint(0,738)
                self.initialTime = time.time()

    def kameham(self,enemyPlayer,power2):
        """
        Kameham power
        """
        if time.time()*1000-self.initialTime1>self.kamehamMs and abs(self.y-enemyPlayer.y)< 50 and self.loading == False and abs(self.x-enemyPlayer.x)>65:
            if self.XP >= 10:
                if self.singleKameham == True:
                    self.initialKame = time.time()*1000
                    self.action = "kameham"
                    power2.action = "kame"
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
                            enemyPlayer.action = 'hited'
                            enemyPlayer.initialTime = time.time()
                        if enemyPlayer.Defending == True and enemyPlayer.Attacking == False:
                            enemyPlayer.HP -= 2
                    self.XP-=10
                    self.initialTime = time.time()
                    self.initialTime1 = time.time()*1000

    def punchKick(self, enemyPlayer):
        """
        It punchs or kicks
        """
        if abs(self.x-enemyPlayer.x)<55 and abs(self.y-enemyPlayer.y)< 30 and abs(time.time()*1000-self.initialTime2) > self.punchMs:
            if random.randint(0,11) > 5:
                self.action = "punch"
            else:
                self.action = "kick"
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
            self.initialPunch = time.time()*1000
            if selfAttackRect.colliderect(enemyPlayer.Rect) == True:
                if enemyPlayer.Defending == False:
                    if self.XP <= self.XPMAX:
                        enemyPlayer.HP -= self.punchDamage*self.factorSuper
                    if self.XP == self.XPMAX:
                        enemyPlayer.HP -= self.powerDamage
                        if random.randint(0,11) > 5:
                            self.superPunchState = True
                        else:
                            self.superKickState = True

                    if abs(self.x - enemyPlayer.x) <30 and abs(enemyPlayer.initialPunch-self.initialPunch)<400:
                        pass
                    else:
                        enemyPlayer.action = "hited"
                    enemyPlayer.initialTime = time.time()
                if enemyPlayer.Defending == True and enemyPlayer.Attacking == False:
                    enemyPlayer.HP -= enemyPlayer.hitDefended
            self.initialTime = time.time()
            self.initialTime2 = time.time()*1000
    
    def load(self, enemyPlayer):
        """
        Load XP
        """
        if abs(time.time()*1000-self.initialTime3) > 2000 and abs(self.x-enemyPlayer.x)>100:
            self.action = "load"
            self.pressed = True
            self.pos = 1
            if self.XP < self.XPMAX:
                self.XP+= 1 
            self.initialTime = time.time()
            self.loading = True
            if abs(time.time()*1000-self.initialTime4) >3000:
                self.initialTime3 = time.time()*1000
                self.initialTime4 = time.time()*1000
                self.loading = False

    def playPC(self, enemyPlayer, power2,resolution):
        """
        Play npc actions
        """
        width,height = resolution
        if self.HP > 0:
            self.superPunch(enemyPlayer)
            self.teleport(enemyPlayer,width)
            self.kameham(enemyPlayer,power2)
            self.punchKick(enemyPlayer)
            self.load(enemyPlayer)

            if abs(time.time()*1000-self.initialTime5) >2000:
                if enemyPlayer.y-self.y <0:
                    self.action = "up"
                    self.pos = 1
                    self.movey=-1
                    if abs(time.time()*1000-self.initialTime5) >2350:
                        self.initialTime5 = time.time()*1000
                        self.movey=0
                        self.pos = 0
                if enemyPlayer.y-self.y >0:
                    self.action = "down"
                    self.pos = 1
                    self.movey=1
                    if abs(time.time()*1000-self.initialTime5) >2350:
                        self.initialTime5 = time.time()*1000
                        self.movey=0
                        self.pos = 0
            if abs(enemyPlayer.x-self.x) >15 and abs(time.time()*1000-self.initialTime6) >2000:
                if self.facingRight == False:
                    self.action = "right"
                    self.pos = 1
                    self.movex=-1
                    if abs(time.time()*1000-self.initialTime6) >2350:
                        self.initialTime6 = time.time()*1000
                        self.movex=0
                        self.pos = 0
                if self.facingRight == True:
                    self.action = "down"
                    self.pos = 1
                    self.movex=1
                    if abs(time.time()*1000-self.initialTime6) >2350:
                        self.initialTime6 = time.time()*1000
                        self.movex=0
                        self.pos = 0
        
