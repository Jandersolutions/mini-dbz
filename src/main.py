#!/usr/bin/python
import pygame, sys, glob
from pygame import *
from spriteanimation import SpriteAnimation
from player import Player
import time
import ntpath

#resolution = 640, 480
pygame.init()
scenery1 = "../resources/imagens/scenarios/namek-3d-2.jpg"
scenery2 = "../resources/imagens/scenarios/Wasteland-2.jpg"
scenery3 = "../resources/imagens/scenarios/trunks-future-2.png"
scenery4 = "../resources/imagens/scenarios/arena-2-2.gif"
scenery = [pygame.image.load(scenery1),pygame.image.load(scenery2),pygame.image.load(scenery3),pygame.image.load(scenery4)]
menu_image = "../resources/imagens/Openning/goku-vs-vegeta-2.jpg"
background = pygame.image.load(scenery4)
resolution = background.get_size()
width, height = resolution
screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN, 32)
#screen = pygame.display.set_mode(resolution)
background.convert()
background_openning = pygame.image.load(menu_image).convert()
#background_openning = pygame.transform.flip(background_openning, 1,0)
player1Win = pygame.image.load("../resources/imagens/player/goku/ss4/gokuWin.png")
player2Win = pygame.image.load("../resources/imagens/player/vegeta/vegetaWin.jpeg")
player2Profile = pygame.image.load("../resources/imagens/player/vegeta/vegeta-2.png")
player1Profile = pygame.image.load("../resources/imagens/player/goku/ss4/gokuPhoto.png")
scene1 = pygame.transform.scale(scenery[0], (500,300))
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)
gameState = 0 #Menu
previousGameState = 0
s0Option = range(4) 
is0 = 0
s1Option = range(5)
is1 = 0
s3Option = range(4)
is3 = 0
sc = 0
sg = 0
volume = 0.9
vsPC = False
cronometrar = True
inicio = 0
song1 = '../resources/sounds/sparking.mp3'
song2 = '../resources/sounds/temos-a-forca-1.wav'
song3 = '../resources/sounds/cha-la.mp3'
song = [song1,song2,song3]

#Goku
player1 = Player(acaoInicial="down")
player1.loadSprites("../resources/imagens/player/goku/ss4/goku-ss4.png")
player1.createAnimation(0,0,48,70,4,"down")
player1.createAnimation(6,200,51,70,4,"up")
player1.erasePositions("up", [0,2])
player1.repeatPosition("up",1, [1])
player1.createAnimation(0,72,65,70,4,"right")   
player1.createAnimation(164,2272,56,70,4,"defend") 
player1.erasePositions("defend",[0,1,3])
player1.createAnimation(164,1500,57,80,10,"kameham-1",hold=True, speed = 1) 
player1.erasePositions("kameham-1",[6,7,8,9])

#Goku-Punch
player1.insertFrame(120,367,58,60)
player1.insertFrame(180,367,58,60)
#player1.insertFrame(211,1674,65,60)
player1.insertFrame(211,1674,65,60)
player1.insertFrame(249,367,65,60)
#hold to maintain last frame
player1.buildAnimation("punch",hold=True, speed = 5)

#Goku-Kick
player1.insertFrame(113,443,57,60)
player1.insertFrame(166,443,60,60)
player1.insertFrame(235,443,66,60)
player1.insertFrame(303,443,66,60)
player1.insertFrame(375,443,68,60)
player1.insertFrame(448,443,68,60)
player1.insertFrame(375,443,58,60)
player1.buildAnimation("kick",hold=True, speed = 5)
#Goku-Lose
player1.insertFrame(855,3354,40,60)
player1.buildAnimation("lose",hold=False, speed = 10)
#Goku-Loading
player1.insertFrame(115,1400,83,90)
player1.insertFrame(195,1400,83,90)
#player1.insertFrame(60,1419,60,65)
player1.buildAnimation("load",hold=True, speed = 15)

#Goku been hit
player1.insertFrame(65,900,52,90)
player1.insertFrame(170,900,80,90)
player1.buildAnimation("hited",hold=True, speed = 5)

#Goku-Power-kameham
power1 = SpriteAnimation(acaoInicial="void")
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

#Vegeta-Power-kameham
power2 = SpriteAnimation(acaoInicial="void")
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
#Vegeta

#Vegeta-Front
player2 = Player(acaoInicial="down")
player2.loadSprites("../resources/imagens/player/vegeta/vegeta-ss4-2.png")
player2.insertFrame(381,68,40,80)
player2.insertFrame(419,68,36,80)
player2.insertFrame(453,68,40,80)
player2.insertFrame(491,68,40,80)
player2.buildAnimation("down",hold=False, speed = 10)

#Vegeta-Lose
player2.insertFrame(840,1407,40,80)
player2.buildAnimation("lose",hold=False, speed = 10)
#Vegeta-Back
player2.insertFrame(49,982,48,80)
player2.buildAnimation("up",hold=False, speed = 10)
#Vegeta-Left
player2.insertFrame(0,161,55,55)
player2.buildAnimation("right",hold=False, speed = 10)
#Vegeta-Right
player2.insertFrame(634,84,46,55)
player2.buildAnimation("defend",hold=False, speed = 10)
#Vegeta-Punch
player2.insertFrame(57,417,55,55)
player2.insertFrame(110,417,70,55)
player2.insertFrame(175,417,65,55)
player2.buildAnimation("punch",hold=True, speed = 5)
#Vegeta-Kick
#player2.insertFrame(1,594,55,75)
player2.insertFrame(56,594,41,75)
player2.insertFrame(96,594,55,75)
player2.insertFrame(155,594,65,75)
player2.buildAnimation("kick",hold=True, speed = 4)

#Vegeta-Kameham
player2.insertFrame(225,2007,55,75)
player2.insertFrame(274,2007,55,75)
player2.insertFrame(325,2007,70,75)
player2.buildAnimation("kameham",hold=True, speed = 5)

#Vegeta-Loading
player2.insertFrame(112,1274,95,85)
player2.insertFrame(200,1274,95,85)
player2.buildAnimation("load",hold=True, speed = 5)

#Vegeta-Hited
player2.insertFrame(0,1400,48,75)
player2.insertFrame(48,1400,43,75)
player2.buildAnimation("hited",hold=True, speed = 5)

delta = 13 #Velocidade do movimento, quanto maior mais rapido
player1.pos = 1
player1.pos2 = 1
player1.movex, player1.movey = 0,0
player2.movex, player2.movey = 0,0
player2.facingRight = False
player1.x = 250
player1.y = 350
player2.x = 850
player2.y = 350
screenWidth = screen.get_width()
punchDamage = 2
kickDamage = 2
hitDefended = 0.4
powerDamage = 10
powerDamageDefended = 2
player1.punchDamage = punchDamage
player2.punchDamage = punchDamage
player1.kickDamage = kickDamage
player2.kickDamage = kickDamage
player1.hitDefended = hitDefended
player2.hitDefended = hitDefended
player1.powerDamage = powerDamage
player2.powerDamage = powerDamage
player1.powerDamageDefended = powerDamageDefended
player2.powerDamageDefended = powerDamageDefended
HP = 140
XP = 30
player1.HP = HP
player2.HP = HP
player1.XP = XP
player2.XP = XP

def restart():
    """Restar the game"""
    global HP
    global XP
    player2.acao = "down"
    player1.acao = "down"
    player1.pos = 1
    player2.pos = 1
    player1.movex, player1.movey = 0,0
    player2.movex, player2.movey = 0,0
    player1.facingRight = True
    player2.facingRight = False
    player1.x = 250
    player1.y = 350
    player2.x = 850
    player2.y = 350
    player1.HP = HP
    player2.HP = HP
    player1.XP = XP
    player2.XP = XP
    global cronometrar
    cronometrar = True

def show_splashscreen():
    """
    Show the splash screen.
    This is called once when the game is first started.
    """
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    pygame.mixer.music.load('../resources/splash.ogg')
    pygame.mixer.music.play()
    white = 250, 250, 250
    screen.fill(white) 
    # Slowly fade the splash screen image from white to opaque. 
    splash = pygame.image.load("../resources/estevaosplash.png").convert()
    for i in range(25):
        splash.set_alpha(i)
        screen.blit(splash, (90,50))
        pygame.display.update()
        pygame.time.wait(100)

    pygame.mixer.fadeout(2000)
    screen.blit(splash,(90,50))
    pygame.display.update()
    pygame.time.wait(1500)
    global gameState
    gameState = 0

def openMenu():
    global gameState
    global previousGameState
    global vsPC
    black = 0,0,0
    screen.fill(black)
    screen.blit(background_openning, (-70,0))
    myfont = pygame.font.SysFont("monospace", 45)
    titlefont = pygame.font.SysFont("monospace", 75,bold = True)
    boldFont = pygame.font.SysFont("monospace", 55,bold =True)
    title = titlefont.render("SS4-Battle", 1, (255,255,255))
    playerVsPlayer = myfont.render("Player Vs Player", 1, (255,255,255))
    playerVsPc = myfont.render("Player Vs Pc", 1, (255,255,255))
    options = myfont.render("Options", 1, (255,255,255))
    quit = myfont.render("Quit", 1, (255,255,255))


    global is0
    if s0Option[is0] == 0:
        playerVsPlayer = boldFont.render("Player Vs Player", 1, (255,255,255))
    if s0Option[is0] == 1:
        playerVsPc = boldFont.render("Player Vs Pc", 1, (255,255,255))
    if s0Option[is0] == 2:
        options = boldFont.render("Options", 1, (255,255,255))
    if s0Option[is0] == 3:
        quit = boldFont.render("Quit", 1, (255,255,255))

    #screen.blit(title, (200,105))
    screen.blit(playerVsPlayer, (300,505))
    screen.blit(playerVsPc, (300,555))
    screen.blit(options, (300,605))
    screen.blit(quit, (300,655))
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                gameState = previousGameState
            if event.key==K_RETURN:
                if s0Option[is0] == 0:
                    #gameState = 2
                    #vsPC = False
                    gameState = 4
                    restart()
                if s0Option[is0] == 1:
                    previousGameState = 0
                    #gameState = 2
                    #vsPC = True
                if s0Option[is0] == 2:
                    previousGameState = 0
                    gameState = 3
                if s0Option[is0] == 3:
                    pygame.quit()
                    sys.exit()

            if event.key==K_DOWN:
                if s0Option[is0] < s0Option[-1]:
                    is0 += 1
                    # to jump player vs PC
                    if is0 == 1:
                        is0 +=1
            if event.key==K_UP:
                if s0Option[is0] > s0Option[0]:
                    is0 -= 1
                    # to jump player vs PC
                    if is0 == 1:
                        is0 -=1
def Options():
    global gameState
    global delta
    global previousGameState
    global volume
    global song
    global sg
    black = 0,0,0
    screen.fill(black)
    screen.blit(background_openning, (-70,0))
    myfont = pygame.font.SysFont("monospace", 45)
    boldFont = pygame.font.SysFont("monospace", 55,bold =True)
    playerVsPlayer = myfont.render("Game Speed "+str(delta), 1, (255,255,255))
    playerVsPc = myfont.render("Music Volume "+str(volume*100), 1, (255,255,255))
    options = myfont.render("Resume", 1, (255,255,255))
    music = myfont.render("Music", 1, (255,255,255))
    title = myfont.render(ntpath.basename(song[sg]), 1, (255,255,255))

    global is3
    if s3Option[is3] == 0:
        playerVsPlayer = boldFont.render("Game Speed "+str(delta), 1, (255,255,255))
    if s3Option[is3] == 2:
        playerVsPc = boldFont.render("Music Volume "+str(volume*100), 1, (255,255,255))
    if s3Option[is3] == 3:
        options = boldFont.render("Resume", 1, (255,255,255))
    if s3Option[is3] == 1:
        music = boldFont.render("Music", 1, (255,255,255))
        title = boldFont.render(ntpath.basename(song[sg]), 1, (255,255,255))
    screen.blit(playerVsPlayer, (340,250))
    screen.blit(playerVsPc, (340,350))
    screen.blit(options, (340,395))
    screen.blit(music, (340,305))
    screen.blit(title, (540,305))
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                gameState = previousGameState
            if event.key==K_RETURN:
                if s3Option[is3] == 3:
                    gameState = 2
            if event.key==K_DOWN:
                if s3Option[is3] < s3Option[-1]:
                    is3 += 1
            if event.key==K_UP:
                if s3Option[is3] > s3Option[0]:
                    is3 -= 1
            if event.key==K_RIGHT:
                if s3Option[is3] == 0:
                    delta += 1
                if s3Option[is3] == 2:
                    if volume < 0.9:
                        volume += 0.1
                        pygame.mixer.music.set_volume(volume)
                if s3Option[is3] == 1:
                    if sg == len(song)-1:
                        sg =-1
                    sg +=1
                    loadMusic(song[sg])
            if event.key==K_LEFT:
                if s3Option[is3] == 0:
                    delta -= 1
                if s3Option[is3] == 2:
                    if volume > 0.1:
                        volume -= 0.1
                        pygame.mixer.music.set_volume(volume)
                    if volume < 0.2:
                        volume = 0
                        pygame.mixer.music.set_volume(volume)
                if s3Option[is3] == 1:
                    if sg == 0:
                        sg =len(song)
                    sg -=1
                    loadMusic(song[sg])
def chooseScenery():
    global gameState
    global previousGameState
    global sc
    global background
    global scenery
    global scene1
    black = 0,0,0
    screen.fill(black)
    screen.blit(background_openning, (-70,0))
    myfont = pygame.font.SysFont("monospace", 45)
    boldFont = pygame.font.SysFont("monospace", 55,bold =True)

    playerVsPlayer = boldFont.render(">", 1, (255,255,255))
    playerVsPlayer2 = boldFont.render("<", 1, (255,255,255))
    screen.blit(playerVsPlayer, (865,420))
    screen.blit(playerVsPlayer2, (300,420))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                gameState = previousGameState
            if event.key==K_RETURN:
                    gameState = 2
                    vsPC = False
                    background = scenery[sc]
            if event.key==K_RIGHT:
                if sc == len(scenery)-1:
                    sc =-1
                sc +=1
                scene1 = pygame.transform.scale(scenery[sc], (500,300))
            if event.key==K_LEFT:
                if sc == 0:
                    sc = len(scenery)
                sc -=1
                scene1 = pygame.transform.scale(scenery[sc], (500,300))
    screen.blit(scene1,(350,300))
    pygame.display.update()

def loadMenu():
    global gameState
    global previousGameState
    black = 0,0,0
    screen.fill(black)
    screen.blit(background_openning, (-70,0))
    myfont = pygame.font.SysFont("monospace", 45)
    boldFont = pygame.font.SysFont("monospace", 55,bold =True)
    initialScreen = myfont.render("Initial Screen", 1, (255,255,255))
    playerVsPlayer = myfont.render("Resume", 1, (255,255,255))
    playerVsPc = myfont.render("Options", 1, (255,255,255))
    options = myfont.render("Restart", 1, (255,255,255))
    quit = myfont.render("Quit", 1, (255,255,255))

    global is1
    if s1Option[is1] == 0:
        initialScreen = boldFont.render("Initial Screen", 1, (255,255,255))
    if s1Option[is1] == 1:
        playerVsPlayer = boldFont.render("Resume", 1, (255,255,255))
    if s1Option[is1] == 2:
        playerVsPc = boldFont.render("Options", 1, (255,255,255))
    if s1Option[is1] == 3:
        options = boldFont.render("Restart", 1, (255,255,255))
    if s1Option[is1] == 4:
        quit = boldFont.render("Quit", 1, (255,255,255))
    screen.blit(initialScreen, (340,250))
    screen.blit(playerVsPlayer, (340,305))
    screen.blit(playerVsPc, (340,360))
    screen.blit(options, (340,415))
    screen.blit(quit, (340,470))
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                gameState = 2
                previousGameState = 1
            if event.key==K_RETURN:
                if s1Option[is1] == 0:
                    gameState = 0
                if s1Option[is1] == 1:
                    gameState = 2
                if s1Option[is1] == 2:
                    gameState = 3
                    previousGameState = 1
                if s1Option[is1] == 3:
                    restart()
                    gameState = 2
                if s1Option[is1] == 4:
                    pygame.quit()
                    sys.exit()
            if event.key==K_DOWN:
                if s1Option[is1] < s1Option[-1]:
                    is1 += 1
            if event.key==K_UP:
                if s1Option[is1] > s1Option[0]:
                    is1 -= 1
def loadMusic (music):
    #pygame.mixer.music.load('resources/sounds/sparking.mp3')
    pygame.mixer.music.load(music)
    #pygame.mixer.music.play(-1,9)
    pygame.mixer.music.play(-1)

def playPC():
    if player2.XP > 20:
        player2.acao = "kameham"
        power2.acao = "kame"
        player2.pressed = True
        power2.pressed = True
        player2.pos = 1
        player2.Attacking = True
        player2.Defending = False
        if player2.facingRight == False:
            player2AttackRect = Rect(player2.x-950, player2.y+10, 1000, 60)
            #pygame.draw.rect(screen, (0,255,0), player2AttackRect)
        elif player2.facingRight == True:
            player2AttackRect = Rect(player2.x+45, player2.y+10, 1000, 60)
            #pygame.draw.rect(screen, (0,255,0), player2AttackRect)
        if player2AttackRect.colliderect(player1.Rect) == True:
            if player1.Defending == False:
                player1.HP -= 10
            if player1.Defending == True and player1.Attacking == False:
                player1.HP -= 2
        player2.acao = "down"
        player2.XP-=10
    if player2.XP <0 or player2.XP < 30:
        player2.acao = "load"
        player2.pressed = True
        player2.pos = 1
        player2.XP+= 5 

def playLoop():
    global vsPC
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if vsPC == False:
            player1.playPlayer1(event,player2,power1)
            player2.playPlayer2(event,player1,power2)
        #playPlayer2(event)
        elif vsPC == True:
            player1.playPlayer1(event,player2,power1)
            #playPC() 
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                global gameState
                global previousGameState
                gameState = 1
                previousGameState = 2
    #Virar automaticamente
    if player1.x > player2.x:
        player1.facingRight = False
        player2.facingRight = True
    if player1.x < player2.x:
        player1.facingRight = True
        player2.facingRight = False

    if player2.movex or player2.movey !=0:
        player2.inicio = time.time()
    
    #Movimento dos Jogadores
    global width
    global height
    if player1.facingRight == True:
        if player1.movex == -1 and player1.x>0:
            player1.x += player1.movex * delta
        if player1.movex == 1 and player1.x<width-50:
            player1.x += player1.movex * delta
    if player1.facingRight == False:
        if player1.movex == -1 and player1.x>0:
            player1.x += player1.movex * delta
        if player1.movex == 1 and player1.x<width-50:
            player1.x += player1.movex * delta
    if player2.facingRight == False:
        if player2.movex == -1 and player2.x>0:
            player2.x += player2.movex * delta
        if player2.movex == 1 and player2.x<width-50:
            player2.x += player2.movex * delta
    if player2.facingRight == True:
        if player2.movex == -1 and player2.x>0:
            player2.x += player2.movex * delta
        if player2.movex == 1 and player2.x<width-50:
            player2.x += player2.movex * delta
    if player1.movey == 1 and player1.y<height-70:
        player1.y += player1.movey * delta
    if player1.movey == -1 and player1.y>0:
        player1.y += player1.movey * delta
    if player2.movey == 1 and player2.y<height-70:
        player2.y += player2.movey * delta
    if player2.movey == -1 and player2.y>0:
        player2.y += player2.movey * delta
    
    #Adaptacao do Retangulo do player 1 para quando ele vai para frente
    if player1.acao != "right":
        player1.Rect = Rect(player1.x, player1.y, 35, 70)
    elif player1.acao == "right" and player1.facingRight == True:
        player1.Rect = Rect(player1.x+30, player1.y, 35, 70)
    elif player1.acao == "right" and player1.facingRight == False:
        player1.Rect = Rect(player1.x, player1.y, 35, 70)
    player2.Rect = Rect(player2.x, player2.y, 35, 70)

    #Posicionamento dos Poderes
    if (player1.facingRight == True):
        power1.x = player1.x+45
        power1.y = player1.y+25
    else:
        power1.x = player1.x-930
        power1.y = player1.y+20
    
    if (player2.facingRight == False):
        power2.x = player2.x-910
        power2.y = player2.y+5
    elif (player2.facingRight == True):
        power2.x = player2.x+50
        power2.y = player2.y+5

    #Barras de Hp e XP
    player1HPRect = Rect(80 , 20, player1.HP*2, 20)
    player1.XPRect = Rect(80 , 60, player1.XP*2, 20)
    player2HPRect = Rect(screenWidth-80, 20, -player2.HP*2, 20)
    player2.XPRect = Rect(screenWidth-80, 60, -player2.XP*2, 20)
    global player2Profile
    global player1Profile
    screen.blit(player2Profile, (screenWidth-70,20))
    screen.blit(player1Profile, (0,20))
    if player1.HP >=0:
        pygame.draw.rect(screen, (255,0,0), player1HPRect)
    if player2.HP >=0:
        pygame.draw.rect(screen, (255,0,0), player2HPRect)
    pygame.draw.rect(screen, (0,0,255), player1.XPRect)
    pygame.draw.rect(screen, (0,0,255), player2.XPRect)
    
    clock.tick(60)
    player2.update(player2.pos,screen)
    player1.update(player1.pos,screen)
    #pygame.draw.rect(screen, (255,255,255), player1.Rect)
    #pygame.draw.rect(screen, (255,255,255), player2.Rect)

    #Animacao de derrota
    global cronometrar
    if player2.HP <= 0:
        player2.acao = "lose"
        if cronometrar == True:
            player2.inicio = time.time()
            cronometrar = False
        if time.time()-player2.inicio>1:
            screen.blit(player1Win, (300,150))
    if player1.HP <= 0:
        player1.acao = "lose"
        if cronometrar == True:
            player2.inicio = time.time()
            cronometrar = False
        if time.time()-player2.inicio>1:
            screen.blit(player2Win, (320,200))
    
    if player2.Defending== True:
        player2.inicio = time.time()
    if time.time()-player2.inicio>0.4 and player2.HP>0:
        player2.acao = "down"
        player2.inicio = time.time()+1000
    
    power1.update(player1.pos,screen)
    power2.update(player2.pos,screen)
    pygame.display.update()

show_splashscreen()
loadMusic(song[0])
while 1:
    if gameState == 0:
        openMenu()
    elif gameState == 1:
        loadMenu()
    elif gameState == 2:
        playLoop()
    elif gameState == 3:
        Options()
    elif gameState == 4:
        chooseScenery()

