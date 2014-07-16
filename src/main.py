#!/usr/bin/python
import pygame, sys, glob
from pygame import *
from spriteanimation import SpriteAnimation
from player import Player
import time
import ntpath

pygame.init()
scenery2 = "../resources/imagens/scenarios/namek-3d-2.jpg"
scenery1 = "../resources/imagens/scenarios/Wasteland-2.jpg"
scenery3 = "../resources/imagens/scenarios/trunks-future-2.png"
scenery4 = "../resources/imagens/scenarios/arena-2-2.gif"
scenery = [pygame.image.load(scenery1),pygame.image.load(scenery2),pygame.image.load(scenery3),pygame.image.load(scenery4)]
menu_image = "../resources/imagens/openning/background/goku-vs-vegeta-2.jpg"
goku3x4 = "../resources/imagens/player/goku/ss4/goku100x100.png"
vegeta3x4 = "../resources/imagens/player/vegeta/vegeta100x100.png"
trunks3x4 = "../resources/imagens/player/trunks/trunks100x100.png"
photos3x4 = [pygame.image.load(goku3x4),pygame.image.load(vegeta3x4),pygame.image.load(trunks3x4)]
ch = pygame.transform.scale(photos3x4[0], (500,300))
ch = pygame.transform.scale(photos3x4[0], (100,100))
background = pygame.image.load(scenery4)
resolution = background.get_size()
width, height = resolution
screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN, 32)
#screen = pygame.display.set_mode(resolution)
background.convert()
background_openning = pygame.image.load(menu_image).convert()
scene1 = pygame.transform.scale(scenery[0], (500,300))
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)
gameState = 0 #Menu
previousGameState = 0
s0Option = range(5) 
is0 = 0
s1Option = range(5)
is1 = 0
s3Option = range(4)
is3 = 0
sc = 0
sc1 = 0
sc2 = 1
sg = 0
volume = 0.2
vsPC = False
song1 = '../resources/sounds/sparking.mp3'
song2 = '../resources/sounds/temos-a-forca-1.wav'
song3 = '../resources/sounds/cha-la.mp3'
song = [song1,song2,song3]
xp1 = 400
yp1 = 400
xp1d = xp1
yp1d = yp1
xp2 = 550
yp2 = 400
xp2d = xp2
yp2d = yp2

characters = ['goku','vegeta','trunks']
player1 = Player(acaoInicial="down",playerId=1)
player2 = Player(acaoInicial="down",playerId=2)
playerPC = Player(acaoInicial="down",playerId=0)
power1 = SpriteAnimation(acaoInicial="void")
power2 = SpriteAnimation(acaoInicial="void")
player1.loadPower(power1)
player2.loadPower(power2)
playerPC.loadPower(power2)

delta = 13 #Velocidade do movimento, quanto maior mais rapido
player2.facingRight = False
player2.x = 850
player2.y = 350
playerPC.x = 850
playerPC.y = 350
playerPC.XP = 0

def restart():
    """
    Restar the game
    """
    global vsPC
    if vsPC == True:
        playerPC.acao = "down"
        player1.acao = "down"
        player1.pos = 1
        playerPC.pos = 1
        player1.movex, player1.movey = 0,0
        playerPC.movex, playerPC.movey = 0,0
        player1.facingRight = True
        playerPC.facingRight = False
        player1.x = 250
        player1.y = 350
        playerPC.x = 850
        playerPC.y = 350
        player1.HP = 140
        playerPC.HP = 140
        player1.XP = 50
        playerPC.XP = 0
        playerPC.inicio1Pc = time.time()
    else:
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
        player1.HP = 140
        player2.HP = 140
        player1.XP = 50
        player2.XP = 50

def show_splashscreen():
    """
    Show the splash screen.
    This is called once when the game is first started.
    """
    global volume
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    pygame.mixer.music.load('../resources/sounds/splash.ogg')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(volume)
    white = 250, 250, 250
    screen.fill(white) 
    # Slowly fade the splash screen image from white to opaque. 
    splash = pygame.image.load("../resources/imagens/openning/splash/estevaosplash.png").convert()
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
def show_video():
    inicio = time.time()
    loadMusic(song[0])
    global screen
    pygame.init()
    #pygame.mixer.quit()
    screen.fill((0,0,0))
    pygame.display.update()
    movie = pygame.movie.Movie("../resources/videos/goku-vs-vegeta.mpg")
    w, h = movie.get_size()
    w = int(w * 1.3 + 0.5)
    h = int(h * 1.3 + 0.5)
    wsize = (w+10, h+10)
    msize = (w+745, h+200)
    movie.set_display(screen, Rect((0, 80), msize))
    pygame.event.set_allowed((QUIT, KEYDOWN))
    pygame.time.set_timer(USEREVENT, 1000)
    movie.play()
    while movie.get_busy():
        if abs(time.time()-inicio)>=30:
            movie.stop()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_RETURN:
                    #break
                    movie.stop()
                if event.key==K_ESCAPE:
                    movie.stop()
                pygame.time.set_timer(USEREVENT, 0)

def openMenu():
    """
    Main Menu
    """
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
    credits = myfont.render("Credits", 1, (255,255,255))
    quit = myfont.render("Quit", 1, (255,255,255))

    global is0
    if s0Option[is0] == 0:
        playerVsPlayer = boldFont.render("Player Vs Player", 1, (255,255,255))
    if s0Option[is0] == 1:
        playerVsPc = boldFont.render("Player Vs Pc", 1, (255,255,255))
    if s0Option[is0] == 2:
        options = boldFont.render("Options", 1, (255,255,255))
    if s0Option[is0] == 3:
        credits = boldFont.render("Credits", 1, (255,255,255))
    if s0Option[is0] == 4:
        quit = boldFont.render("Quit", 1, (255,255,255))

    #screen.blit(title, (200,105))
    screen.blit(playerVsPlayer, (300,505))
    screen.blit(playerVsPc, (300,555))
    screen.blit(options, (300,605))
    screen.blit(credits, (300,655))
    screen.blit(quit, (300,705))
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
                    gameState = 5
                    restart()
                    vsPC = False
                if s0Option[is0] == 1:
                    previousGameState = 0
                    gameState = 5
                    vsPC = True
                    restart()
                if s0Option[is0] == 2:
                    previousGameState = 0
                    gameState = 3
                if s0Option[is0] == 3:
                    previousGameState = 0
                    gameState = 6
                if s0Option[is0] == 4:
                    pygame.quit()
                    sys.exit()
            if event.key==K_DOWN:
                if s0Option[is0] < s0Option[-1]:
                    is0 += 1
            if event.key==K_UP:
                if s0Option[is0] > s0Option[0]:
                    is0 -= 1
def Options():
    """
    Option Menu
    """
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

def Credits():
    """
    Option Menu
    """
    global gameState
    global previousGameState
    global sg
    black = 0,0,0
    screen.fill(black)
    screen.blit(background_openning, (-70,0))
    myfont = pygame.font.SysFont("monospace", 45)
    boldFont = pygame.font.SysFont("monospace", 55,bold =True)
    gameDeveloper = boldFont.render("Game Developer", 1, (255,255,255))
    estevao = myfont.render("Estevao Fonseca", 1, (255,255,255))
    supporters = boldFont.render("Supporters", 1, (255,255,255))
    bru = myfont.render("Bruno Fonseca", 1, (255,255,255))
    hel = myfont.render("Helena A. Lisboa", 1, (255,255,255))
    artWork = boldFont.render("Art Work", 1, (255,255,255))
    akira = myfont.render("Akira Torayama", 1, (255,255,255))

    screen.blit(gameDeveloper, (340,250))
    screen.blit(estevao, (340,310))
    screen.blit(supporters, (340,370))
    screen.blit(bru, (340,430))
    screen.blit(hel, (340,490))
    screen.blit(artWork, (340,550))
    screen.blit(akira, (340,610))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                gameState = previousGameState

def chooseCharacter():
    """
    Choose Scenery Screen
    """
    global gameState
    global previousGameState
    global sc1
    global sc2
    global background
    global photo3x4
    global characters
    global ch
    global xp1
    global yp1
    global xp1d
    global yp1d
    global xp2
    global yp2
    global xp2d
    global yp2d
    black = 0,0,0
    screen.fill(black)
    screen.blit(background_openning, (-70,0))
    myfont = pygame.font.SysFont("monospace", 45)
    boldFont = pygame.font.SysFont("monospace", 65,bold =True)

    playerVsPlayer = boldFont.render("P1", 1, (255,0,0))
    if vsPC == True: 
        playerVsPlayer2 = boldFont.render("PC", 1, (0,0,255))
    else:
        playerVsPlayer2 = boldFont.render("P2", 1, (0,0,255))

    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                gameState = previousGameState
            if event.key==K_RETURN:
                    gameState = 4
                    if vsPC == True:
                        player1.loadCharacter(characters[sc1])
                        playerPC.loadCharacter(characters[sc2])
                    else:
                        player1.loadCharacter(characters[sc1])
                        player2.loadCharacter(characters[sc2])
            if event.key==K_d:
                if sc1 >= len(photos3x4)-1:
                    sc1 = 0
                    xp1 = xp1d
                elif sc1>=0 and sc1 <len(photos3x4):
                    xp1 +=150
                    sc1 +=1
            if event.key== K_RIGHT:
                if sc2 >= len(photos3x4)-1:
                    sc2 = 0
                    xp2 = xp1d
                elif sc2>=0 and sc2 <len(photos3x4):
                    xp2 +=150
                    sc2 +=1

            if event.key==K_a:
                if sc1 <= 0:
                    sc1 = len(photos3x4)-1
                    xp1 = xp1d+300
                elif sc1>=0 and sc1 <len(photos3x4):
                    xp1 -=150
                    sc1 -=1

            if event.key==K_LEFT:
                if sc2 <= 0:
                    sc2 = len(photos3x4)-1
                    xp2 = xp1d+300
                elif sc2>=0 and sc2 <len(photos3x4):
                    xp2 -=150
                    sc2 -=1

    x=350
    y=350
    dx=0
    for picture in photos3x4:
        ch = pygame.transform.scale(picture, (150,150))
        screen.blit(ch, (x+dx,y))
        dx+=150
    screen.blit(playerVsPlayer, (xp1,yp1))
    screen.blit(playerVsPlayer2, (xp2,yp2))
    #sc2String = str(sc2)
    #debug = boldFont.render(sc2String, 1, (0,0,255))
    #screen.blit(debug, (0,0))
    pygame.display.update()

def chooseScenery():
    """
    Choose Scenery Screen
    """
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
    debug = boldFont.render("<", 1, (255,255,255))
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
    """
    Menu during the playing game
    """
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
    """Load the musics of a list"""
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)

def playLoop():
    """
    Game Loop
    """
    global vsPC
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if vsPC == False:
            player1.playPlayer(event,player2,power1)
            player2.playPlayer(event,player1,power2)
        elif vsPC == True:
            player1.playPlayer(event,playerPC,power1)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                global gameState
                global previousGameState
                gameState = 1
                previousGameState = 2

    global width
    global height
    player1.lockInsideScreen(width,height,delta)
    player1.physicalRect()
    player1.powerPlacing(power1)
    player1.statusBar(screen,width)
    player1.standUpPosition()
    
    if vsPC == True:
        player1.defeated(screen,playerPC)
        player1.TurnAround1(playerPC)
        playerPC.playPC(player1,power2,screen)
        playerPC.lockInsideScreenPC(width, height, delta, player1)
        playerPC.physicalRect()
        playerPC.powerPlacing(power2)
        playerPC.statusBar(screen,width)
        playerPC.standUpPosition()
        playerPC.defeated(screen,player1)
        playerPC.update(playerPC.pos,screen)
    else:
        player1.defeated(screen,player2)
        player1.TurnAround1(player2)
        player2.lockInsideScreen(width,height,delta)
        player2.powerPlacing(power2,dx2=920,dy2=0)
        player2.physicalRect()
        player2.statusBar(screen,width)
        player2.standUpPosition()
        player2.defeated(screen,player1)
        player2.update(player2.pos,screen)
    player1.update(player1.pos,screen)
    power1.update(player1.pos,screen)
    if vsPC == True:
        power2.update(playerPC.pos,screen)
    else:
        power2.update(player2.pos,screen)

    clock.tick(60)
    pygame.display.update()

show_splashscreen()
show_video()
#loadMusic(song[0])
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
    elif gameState == 5:
        chooseCharacter()
    elif gameState == 6:
        Credits()

