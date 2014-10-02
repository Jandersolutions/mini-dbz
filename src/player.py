#!/usr/bin/python
import pygame, sys, glob
from pygame import *
from spriteanimation import SpriteAnimation
from characters import Characters
import time
import random
import datetime

class Player(Characters):
    def __init__(self, initialAction, playerId, speed = 15):
        """
        Iniciation of the player states
        """
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
        self.timingDispute = False
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
        self.initialSpark = time.time()*1000
        self.initialExplosion = time.time()*1000
        self.initialTime2 = 0
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
        self.isPC = False
        self.singleKameham = True
        self.disputeKamehamBoolean = True

    def superPunch(self, playerList):
        """
        Activate the super punch
        """
        if self.superPunchState == True:
            if time.time()*1000-self.initialPunch <200:
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
        Activate the super kick
        """
        if self.superKickState == True:
            if time.time()*1000-self.initialPunch <200:
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
        self.action = "punch"
        self.pressed = True
        self.Attacking = True
        self.Defending = False
        if self.facingRight == True:
            selfAttackRect = Rect(self.x+30, self.y, 50, 70)
            #pygame.draw.rect(screen, (0,0,255), selfAttackRect)
        if self.facingRight == False:
            selfAttackRect = Rect(self.x-20, self.y, 50, 70)
            #pygame.draw.rect(screen, (0,0,255), selfAttackRect)
        self.initialPunch = time.time()*1000
        for player in playerList:
            if selfAttackRect.colliderect(player.Rect) == True:
                if player.Defending == False:
                    if self.XP <= self.XPMAX:
                        player.HP -= self.punchDamage
                    if self.XP == self.XPMAX:
                        player.HP -= self.powerDamage*self.factorSuper
                        self.superPunchState = True
                    player.initialTime = time.time()
                    if abs(player.initialPunch-self.initialPunch)<400:
                        self.initialEffects = time.time()*1000
                        #pass
                    else:
                        player.action = "hited"
                if player.Defending == True and player.Attacking == False:
                    player.HP -= player.hitDefended
        self.initialTime = time.time()

    def kick(self, playerList):
        """
        Kick action
        """
        self.action = "kick"
        self.pressed = True
        self.Attacking = True
        self.Defending = False
        if self.facingRight == True:
            selfAttackRect = Rect(self.x+30, self.y, 35, 70)
            #pygame.draw.rect(screen, (255,0,0), selfAttackRect)
        if self.facingRight == False:
            selfAttackRect = Rect(self.x-20, self.y, 35, 70)
            #pygame.draw.rect(screen, (255,0,0), selfAttackRect)
        self.initialPunch = time.time()*1000
        for player in playerList:
            if selfAttackRect.colliderect(player.Rect) == True:
                if player.Defending == False:
                    if self.XP <= self.XPMAX:
                        player.HP -= self.kickDamage
                    if self.XP == self.XPMAX:
                        player.HP -= self.powerDamage*self.factorSuper
                        self.superKickState = True
                    if abs(player.initialPunch-self.initialPunch)<400:
                        self.initialEffects = time.time()*1000
                    else:
                        player.action = "hited"
                    player.initialTime = time.time()
                if player.Defending == True and player.Attacking == False:
                    player.HP -= player.hitDefended
        self.initialTime = time.time()

    def combo(self, playerList, power1):
        """ 
        Attempt to implement combo
        """
        self.action = "combo"
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
                    player.action = "hited"
                    player.initialTime = time.time()
                if player.Defending == True and player.Attacking == False:
                    player.HP -= player.hitDefended

    def kameham(self, playerList, power1):
        """
        Kameham power
        """
        self.initialKame = time.time()*1000
        self.kameCont +=1
        if self.XP > 0:
            for player in playerList:
                if abs(self.y - player.y) <50 and abs(player.initialKame-self.initialKame)<400:
                    if self.disputeKamehamBoolean == True:
                        self.timingDispute = True
                        self.releasePower = True
                        self.voidPower = True
                        self.kameCont =0
                        if player.isPC == False:
                            player.kameCont = 0
                        self.disputeKamehamBoolean = False
            if self.singleKameham == True:
                self.action = "kameham"
                power1.action = "kame"
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
                            player.action = "hited"
                            player.initialTime = time.time()
                        if player.Defending == True and player.Attacking == False:
                            player.HP -= player.powerDamageDefended
                self.XP-=10
                self.initialTime = time.time()

    def load(self):
        """
        Load XP
        """
        self.action = "load"
        self.pressed = True
        self.initialTime = time.time()
        if self.XP < self.XPMAX:
            self.XP+= 5 
    
    def teleport(self):
        """
        Teleport to a random place
        """
        self.action = "teleport"
        self.pressed = True
        self.x = random.randint(0,1170)
        self.y = random.randint(0,738)
        self.initialTime = time.time()
    
    def playPlayer(self,eventArg, playerList, power1):
        """
        Play player actions 
        """
        if self.HP>0:
            event = eventArg
            if event.type == KEYDOWN:
                #Goku
                if event.key == self.k_down:
                    self.action = "down"
                    self.movey+=1
                if event.key == self.k_up:
                    self.action = "up"
                    self.movey-=1
                if event.key == self.k_defend:
                    self.action = "defend"
                    self.Defending = True
                if self.facingRight == True:
                    if event.key == self.k_rightArrow:
                        self.action = "right"
                        self.movex+=1
                    if event.key == self.k_leftArrow:
                        self.action = "up"
                        self.movex-=1
                if self.facingRight == False:
                    if event.key == self.k_rightArrow:
                        self.action = "up"
                        self.movex+=1
                    if event.key == self.k_leftArrow:
                        self.action = "right"
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
                    self.action = "down"
                    self.movey=0
                if event.key == self.k_up:
                    self.action = "up"
                    self.movey=0
                if event.key == self.k_defend:
                    self.action = "defend"
                    self.Defending = False
                if event.key == self.k_punch:
                    self.Attacking = False
                if self.facingRight  == True:
                    if event.key == self.k_rightArrow:
                        self.action = "right"
                        self.movex=0
                    if event.key == self.k_leftArrow:
                        self.action = "up"
                        self.movex=0
                if self.facingRight  == False:
                    if event.key == self.k_leftArrow:
                        self.action = "right"
                        self.movex=0
                    if event.key == self.k_rightArrow:
                        self.action = "up"
                        self.movex=0
                if event.key == self.k_kameham:
                    self.action = "kameham"
                    power1.action = "void"
                    self.movex=0
            self.superPunch(playerList)
            self.superKick(playerList)

    def kamehamDispute(self,localPower,playerList,powers):
        """
        Listener of the kameham dispute
        """
        if self.timingDispute == True:
            self.initialTime2 = time.time()*1000
            self.timingDispute = False
            self.staticy = self.y
        if time.time()*1000-self.initialTime2 < 4000:
            if self.facingRight == True:
                localPower.x = self.x+52
                localPower.y = self.y+10
                self.x = 40
                self.y = self.staticy
            if self.facingRight == False:
                self.x = 1120 
                self.y = self.staticy
            self.action = "dispute"
            self.pressed = True
            localPower.pressed = True
            self.initialTime = time.time()
            self.singleKameham = False
            powers2 = powers[:]
            for power in powers2:
                power.action = 'void'
            for otherPlayer in playerList:
                if self.facingRight == True:
                    if self.kameCont-otherPlayer.kameCont >0:
                        localPower.action = "dispute3"
                    if otherPlayer.kameCont-self.kameCont >0:
                        localPower.action = "dispute2"
                    if self.kameCont-otherPlayer.kameCont == 0:
                        localPower.action = "dispute"
                if self.facingRight == False:
                    if self.kameCont-otherPlayer.kameCont >0:
                        localPower.action = "dispute2"
                    if otherPlayer.kameCont-self.kameCont >0:
                        localPower.action = "dispute3"
                    if self.kameCont-otherPlayer.kameCont == 0:
                        localPower.action = "dispute"
                if self.facingRight == True:
                    otherPlayer.y = self.y+10
                    otherPlayer.x = self.x+1080
                if self.facingRight == False:
                    otherPlayer.x = 40
                    otherPlayer.y = self.staticy
                    localPower.x = otherPlayer.x+42
                    localPower.y = otherPlayer.y+5
                otherPlayer.action = 'dispute'
                otherPlayer.initialTime = time.time()
                otherPlayer.singleKameham = False
        if time.time()*1000 -self.initialTime2 > 4000 and self.releasePower == True:
            for otherPlayer in playerList:
                self.releasePower = False
                self.enemykameCont = otherPlayer.kameCont
                if self.kameCont > otherPlayer.kameCont:
                    otherPlayer.HP -= 50
                    if self.facingRight == True:
                        localPower.action = 'from-right'
                    if self.facingRight == False:
                        localPower.action = 'from-left'
                if self.kameCont < otherPlayer.kameCont:
                    if self.facingRight == True:
                        localPower.action = 'from-left'
                    if self.facingRight == False:
                        localPower.action = 'from-right'
                if self.kameCont == otherPlayer.kameCont:
                    localPower.action = "void"
            if self.kameCont < self.enemykameCont:
                self.HP -= 50
        if time.time()*1000 -self.initialTime2 > 4500 and self.voidPower == True:
            self.voidPower = False
            localPower.action = "void"
            self.singleKameham = True
            for otherPlayer in playerList:
                otherPlayer.singleKameham = True
        if time.time()*1000 -self.initialTime2 > 5000:
            self.disputeKamehamBoolean = True

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
        Adjusting the power position of the player
        """
        if (self.facingRight == True):
            power.x = self.x+dx1
            power.y = self.y+dy1
        else:
            power.x = self.x-dx2
            power.y = self.y+dy2

    def physicalRect(self):
        """
        Physical Rectangle of player
        """
        if self.action != "right":
            self.Rect = Rect(self.x, self.y, 35, 70)
        elif self.action == "right" and self.facingRight == True:
            self.Rect = Rect(self.x+30, self.y, 35, 70)
        elif self.action == "right" and self.facingRight == False:
            self.Rect = Rect(self.x, self.y, 35, 70)

    def statusBar(self,screen,width):
        """
        Hp and XP bars of the player
        """
        if self.playerId == 1:
            playerHPRect = Rect(80 , 20, self.HP, 20)
            playerXPRect = Rect(80 , 60, self.XP*2, 20)
            screen.blit(self.photo3x4, (0,20))
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
        Standard stand up position of the player
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
        Show the win picture of the player
        """
        if self.HP <= 0:
            #import pdb; pdb.set_trace()
            self.action = "lose"
            if self.timing2 == True:
                self.initialDead = time.time()
                self.timing2 = False
            if time.time()-self.initialDead>1:
                screen.blit(otherPlayer.Win, (300,200))

