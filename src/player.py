#!/usr/bin/python
import pygame, sys, glob
from pygame import *
from spriteanimation import SpriteAnimation
import time

class Player(SpriteAnimation):
    def __init__(self, acaoInicial, speed = 15):
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
        self.player1Win = pygame.image.load("../resources/imagens/player/goku/ss4/gokuWin.png")
        self.player2Win = pygame.image.load("../resources/imagens/player/vegeta/vegetaWin.jpeg")
        self.player2Profile = pygame.image.load("../resources/imagens/player/vegeta/vegeta-2.png")
        self.player1Profile = pygame.image.load("../resources/imagens/player/goku/ss4/gokuPhoto.png")

    def playPlayer1(self,eventArg, player2, power1):
        """
        Activate player1 movements and skills
        """
        if self.HP>0:
            event = eventArg
            if event.type == KEYDOWN:
                #Goku
                if event.key == K_s:
                    self.acao = "down"
                    self.pos = 1
                    self.movey+=1
                if event.key == K_w:
                    self.acao = "up"
                    self.pos = 1
                    self.movey-=1
                
                if event.key == K_p:
                    self.acao = "defend"
                    self.pos = 1
                    self.Defending = True
                if self.facingRight == True:
                    if event.key == K_d:
                        self.acao = "right"
                        self.pos = 1
                        self.movex+=1
                    if event.key == K_a:
                        self.acao = "up"
                        self.pos = 1
                        self.movex-=1
                if self.facingRight == False:
                    if event.key == K_d:
                        self.acao = "up"
                        self.pos = 1
                        self.movex+=1
                    if event.key == K_a:
                        self.acao = "right"
                        self.pos = 1
                        self.movex-=1
                if event.key == K_u:
                    if self.XP > 0:
                        self.acao = "kameham-1"
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
                if event.key == K_i:
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
                if event.key == K_o:
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

                if event.key == K_j:
                    self.acao = "load"
                    self.pressed = True
                    self.pos = 1
                    self.XP+= 5 
                    
            if event.type == KEYUP:
                if event.key == K_s:
                    self.acao = "down"
                    self.pos = 0
                    self.movey=0
                if event.key == K_w:
                    self.acao = "up"
                    self.pos = 0
                    self.movey=0
                if event.key == K_p:
                    self.acao = "defend"
                    self.pos = 0
                    self.Defending = False
                if event.key == K_i:
                    self.Attacking = False
                if self.facingRight  == True:
                    if event.key == K_d:
                        self.acao = "right"
                        self.pos = 0
                        self.movex=0
                    if event.key == K_a:
                        self.acao = "up"
                        self.pos = 0
                        self.movex=0
                if self.facingRight  == False:
                    if event.key == K_a:
                        self.acao = "right"
                        self.pos = 0
                        self.movex=0
                    if event.key == K_d:
                        self.acao = "up"
                        self.pos = 0
                        self.movex=0

                if event.key == K_u:
                    self.acao = "kameham-1"
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

    def movementInsideScreen1(self,width,height,delta):
        """
        Lock the player1 to the visible screen
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

    def movementInsideScreen2(self,width,height,delta):
        """
        Lock the player2 to the visible screen
        """
        if self.facingRight == False:
            if self.movex == -1 and self.x>0:
                self.x += self.movex * delta
            if self.movex == 1 and self.x<width-50:
                self.x += self.movex * delta
        if self.facingRight == True:
            if self.movex == -1 and self.x>0:
                self.x += self.movex * delta
            if self.movex == 1 and self.x<width-50:
                self.x += self.movex * delta
        if self.movey == 1 and self.y<height-70:
            self.y += self.movey * delta
        if self.movey == -1 and self.y>0:
            self.y += self.movey * delta

    def powerPlacing1(self,power1):
        """
        Adjusting the power position of player1
        """
        #Posicionamento dos Poderes
        if (self.facingRight == True):
            power1.x = self.x+45
            power1.y = self.y+25
        else:
            power1.x = self.x-930
            power1.y = self.y+20
    def powerPlacing2(self,power2):
        """
        Adjusting the power position of player2
        """
        if (self.facingRight == False):
            power2.x = self.x-910
            power2.y = self.y+5
        elif (self.facingRight == True):
            power2.x = self.x+50
            power2.y = self.y+5

    def rect1(self):
        """
        Physical Rectangle of player1
        """
        if self.acao != "right":
            self.Rect = Rect(self.x, self.y, 35, 70)
        elif self.acao == "right" and self.facingRight == True:
            self.Rect = Rect(self.x+30, self.y, 35, 70)
        elif self.acao == "right" and self.facingRight == False:
            self.Rect = Rect(self.x, self.y, 35, 70)

    def rect2(self):
        """
        Physical Rectangle of player2
        """
        self.Rect = Rect(self.x, self.y, 35, 70)

    def statusBar1(self,screen):
        """
        Hp and XP bars of player1
        """
        player1HPRect = Rect(80 , 20, self.HP*2, 20)
        player1XPRect = Rect(80 , 60, self.XP*2, 20)
        if self.HP >=0:
            pygame.draw.rect(screen, (255,0,0), player1HPRect)
        pygame.draw.rect(screen, (0,0,255), player1XPRect)
        screen.blit(self.player1Profile, (0,20))
    
    def statusBar2(self,screen,width):
        """
        Hp and XP bars of player2
        """
        player2HPRect = Rect(width-80, 20, -self.HP*2, 20)
        player2XPRect = Rect(width-80, 60, -self.XP*2, 20)
        if self.HP >=0:
            pygame.draw.rect(screen, (255,0,0), player2HPRect)
        pygame.draw.rect(screen, (0,0,255), player2XPRect)
        screen.blit(self.player2Profile, (width-70,20))

    def standUpPosition2(self):
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

    def defeated2(self,screen):
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
                screen.blit(self.player1Win, (300,200))

    def playPlayer2(self,eventArg,player1,power2):
        """
        Activate player2 movements and skills
        """
        if self.HP>0:
            event = eventArg
            #Vegeta
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    self.acao = "down"
                    self.pos = 1
                    self.movey+=1
                if event.key == K_UP:
                    self.acao = "up"
                    self.pos = 1
                    self.movey-=1
                if self.facingRight == False:
                    if event.key == K_LEFT:
                        self.acao = "right"
                        self.pos = 1
                        self.movex-=1
                    if event.key == K_RIGHT:
                        self.acao = "up"
                        self.pos = 1
                        self.movex+=1
                if self.facingRight == True:
                    if event.key == K_LEFT:
                        self.acao = "up"
                        self.pos = 1
                        self.movex-=1
                    if event.key == K_RIGHT:
                        self.inicio = time.time()
                        self.acao = "right"
                        self.pos = 1
                        self.movex+=1
                if event.key == K_KP5:
                    self.acao = "defend"
                    self.pos = 1
                    self.Defending = True
                if event.key == K_KP8 or event.key == K_8:
                    self.inicio = time.time()
                    self.acao = "punch"
                    self.pos = 1
                    self.pressed = True
                    self.Attacking = True
                    self.Defending = False
                    if self.facingRight == False:
                        player2AttackRect = Rect(self.x-15, self.y, 35, 70)
                        #pygame.draw.rect(screen, (0,0,255), player2AttackRect)
                    elif self.facingRight == True:
                        player2AttackRect = Rect(self.x+30, self.y, 35, 70)
                        #pygame.draw.rect(screen, (0,0,255), player2AttackRect)
                    if player2AttackRect.colliderect(player1.Rect) == True:
                        if player1.Defending == False:
                            player1.HP -= self.punchDamage
                            player1.acao = "hited"
                        if player1.Defending == True and player1.Attacking == False:
                            player1.HP -= player1.hitDefended
                if event.key == K_KP9:
                    self.inicio = time.time()
                    self.acao = "kick"
                    self.pos = 1
                    self.pressed = True
                    self.Attacking = True
                    self.Defending = False
                    if self.facingRight == False:
                        player2AttackRect = Rect(self.x-5, self.y, 35, 70)
                        #pygame.draw.rect(screen, (0,0,255), player2AttackRect)
                    if self.facingRight == True:
                        player2AttackRect = Rect(self.x+30, self.y, 35, 70)
                        #pygame.draw.rect(screen, (0,0,255), player2AttackRect)
                    if player2AttackRect.colliderect(player1.Rect) == True:
                        if player1.Defending == False:
                            player1.HP -= self.kickDamage
                            player1.acao = "hited"
                        if player1.Defending == True and player1.Attacking == False:
                            player1.HP -= player1.hitDefended
                if event.key == K_KP7 or event.key == K_9:
                    if self.XP > 0:
                        self.inicio = time.time()
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
                                player1.HP -= self.powerDamage
                                player1.acao = "hited"
                            if player1.Defending == True and player1.Attacking == False:
                                player1.HP -= player1.powerDamageDefended
                        self.XP-=10
                if event.key == K_KP4:
                    self.acao = "load"
                    self.pressed = True
                    self.pos = 1
                    self.XP+= 5 
                    self.inicio = time.time()

            if event.type == KEYUP:
                if event.key == K_DOWN:
                    self.acao = "down"
                    self.pos = 0
                    self.movey=0
                if event.key == K_UP:
                    self.acao = "up"
                    self.pos = 0
                    self.movey=0
                if event.key == K_KP5:
                    self.acao = "defend"
                    self.pos = 0
                    self.Defending = False
                if self.facingRight == False:
                    if event.key == K_LEFT:
                        self.acao = "right"
                        self.pos = 0
                        self.movex=0
                    if event.key == K_RIGHT:
                        self.acao = "up"
                        self.pos = 0
                        self.movex=0
                if self.facingRight == True:
                    if event.key == K_LEFT:
                        self.acao = "up"
                        self.pos = 0
                        self.movex=0
                    if event.key == K_RIGHT:
                        self.acao = "right"
                        self.pos = 0
                        self.movex=0
    def loadCharacter(self, character):
        if character == 'goku':
            self.loadSprites("../resources/imagens/player/goku/ss4/goku-ss4.png")
            self.createAnimation(0,0,48,70,4,"down")
            self.createAnimation(6,200,51,70,4,"up")
            self.erasePositions("up", [0,2])
            self.repeatPosition("up",1, [1])
            self.createAnimation(0,72,65,70,4,"right")   
            self.createAnimation(164,2272,56,70,4,"defend") 
            self.erasePositions("defend",[0,1,3])
            self.createAnimation(164,1500,57,80,10,"kameham-1",hold=True, speed = 1) 
            self.erasePositions("kameham-1",[6,7,8,9])
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

    def loadPower1(self,power1):
            power1.loadSprites("../resources/imagens/player/goku/ss4/power-1.png")
            power1.createAnimation(1300,1604,146,40,1,"void")
            #power1.insertFrame(1300,1604,146,40) #void
            #power1.insertFrame(1300,1604,146,40) #void
            #power1.insertFrame(644,1197,700,40) 
            power1.insertFrame(0,132,1100,50) #Full Power
            power1.insertFrame(0,132,1100,50) #Full Power
            power1.insertFrame(0,132,1100,50) #Full Power
            #power1.insertFrame(1176,1604,70,40)
            power1.insertFrame(1300,1604,146,40) #void
            power1.buildAnimation("kame",hold=True, speed = 10)
    def loadPower2(self,power2):
        power2.loadSprites("../resources/imagens/player/goku/ss4/power-1.png")
        power2.createAnimation(1300,1604,146,40,1,"void")
        #power2.insertFrame(1300,1604,146,40) #void
        #power2.insertFrame(1300,1604,146,40) #void
        #power1.insertFrame(644,1197,700,40) 
        power2.insertFrame(0,132,1100,50) #Full Power
        power2.insertFrame(0,132,1100,50) #Full Power
        power2.insertFrame(0,132,1100,50) #Full Power
        #power1.insertFrame(1176,1604,70,40)
        power2.insertFrame(1300,1604,146,40) #void
        power2.buildAnimation("kame",hold=True, speed = 10)


