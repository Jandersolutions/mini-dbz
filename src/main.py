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
s0Option = range(4) 
is0 = 0
s1Option = range(5)
is1 = 0
s3Option = range(7)
is3 = 0
s4Option = range(3)
is4 = 0
s5Option = range(3)
is5 = 0
sc = 0
sc1 = 0
sc2 = 1
sg = 0
df = 2
volume = 0.4
vsPC = False
song1 = '../resources/sounds/sparking.mp3'
song2 = '../resources/sounds/temos-a-forca-1.wav'
song3 = '../resources/sounds/cha-la.mp3'
song = [song1,song2,song3]
level = ['easy','Medium','Hard','Super Sayajin','Multiplayer vs 2','Multiplayer vs 3']
xp1 = 400
yp1 = 400
xp1d = xp1
yp1d = yp1
xp2 = 550
yp2 = 400
xp2d = xp2
yp2d = yp2
pcNumber = 1
multiplayer = False
contador = 0

characters = ['goku','vegeta','trunks']
player1 = Player(acaoInicial="down",playerId=1)
player2 = Player(acaoInicial="down",playerId=2)
playerPC = Player(acaoInicial="down",playerId=0)
playerPC2 = Player(acaoInicial="down",playerId=3)
playerPC3 = Player(acaoInicial="down",playerId=4)
power1 = SpriteAnimation(acaoInicial="void")
power2 = SpriteAnimation(acaoInicial="void")
power3 = SpriteAnimation(acaoInicial="void")
power4 = SpriteAnimation(acaoInicial="void")
power5 = SpriteAnimation(acaoInicial="void")
player1.loadPower(power1)
player2.loadPower(power2)
playerPC.loadPower(power3)
playerPC2.loadPower(power4)
playerPC3.loadPower(power5)
playerPC2.loadCharacter(characters[2])
playerPC3.loadCharacter(characters[1])
player2.loadCharacter(characters[2])
PCPlayers = [playerPC,playerPC2,playerPC3]
humanPlayers = [player1,player2]

delta = 13 #Velocidade do movimento, quanto maior mais rapido
player2.facingRight = False
player2.x = 850
player2.y = 350
playerPC.x = 850
playerPC.y = 350
playerPC.XP = 0
playerPC2.x = 150
playerPC2.y = 50
playerPC2.XP = 0

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
        playerPC2.HP = 140
        playerPC2.XP = 0
        playerPC3.HP = 140
        playerPC3.XP = 0
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
    playerVsPc = myfont.render("Play", 1, (255,255,255))
    options = myfont.render("Options", 1, (255,255,255))
    credits = myfont.render("Credits", 1, (255,255,255))
    quit = myfont.render("Quit", 1, (255,255,255))

    global is0
    if s0Option[is0] == 0:
        playerVsPc = boldFont.render("Play", 1, (255,255,255))
    if s0Option[is0] == 1:
        options = boldFont.render("Options", 1, (255,255,255))
    if s0Option[is0] == 2:
        credits = boldFont.render("Credits", 1, (255,255,255))
    if s0Option[is0] == 3:
        quit = boldFont.render("Quit", 1, (255,255,255))

    #screen.blit(title, (200,105))
    screen.blit(playerVsPc, (400,255))
    screen.blit(options, (400,305))
    screen.blit(credits, (400,355))
    screen.blit(quit, (400,405))
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
                    gameState = 8
                    restart()
                    vsPC = False
                if s0Option[is0] == 1:
                    previousGameState = 0
                    gameState = 3
                if s0Option[is0] == 2:
                    previousGameState = 0
                    gameState = 6
                if s0Option[is0] == 3:
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
    global df
    global level
    black = 0,0,0
    screen.fill(black)
    screen.blit(background_openning, (-70,0))
    myfont = pygame.font.SysFont("monospace", 45)
    boldFont = pygame.font.SysFont("monospace", 55,bold =True)
    playerVsPlayer = myfont.render("Game Speed "+str(delta), 1, (255,255,255))
    playerVsPc = myfont.render("Music Volume "+str(volume*100), 1, (255,255,255))
    options = myfont.render("Resume", 1, (255,255,255))
    music = myfont.render("Music", 1, (255,255,255))
    back = myfont.render("Back", 1, (255,255,255))
    mode = myfont.render("Mode", 1, (255,255,255))
    dificult = myfont.render(level[df], 1, (255,255,255))
    keyboard = myfont.render("Keyboard", 1, (255,255,255))
    title = myfont.render(ntpath.basename(song[sg]), 1, (255,255,255))

    global is3
    if s3Option[is3] == 0:
        playerVsPlayer = boldFont.render("Game Speed "+str(delta), 1, (255,255,255))
    if s3Option[is3] == 2:
        playerVsPc = boldFont.render("Music Volume "+str(volume*100), 1, (255,255,255))
    if s3Option[is3] == 3:
        mode = boldFont.render("Mode", 1, (255,255,255))
        dificult = boldFont.render(level[df], 1, (255,255,255))
    if s3Option[is3] == 4:
        keyboard = boldFont.render("Keyboard", 1, (255,255,255))
    if s3Option[is3] == 5:
        options = boldFont.render("Resume", 1, (255,255,255))
    if s3Option[is3] == 6:
        back = boldFont.render("Back", 1, (255,255,255))
    if s3Option[is3] == 1:
        music = boldFont.render("Music", 1, (255,255,255))
        title = boldFont.render(ntpath.basename(song[sg]), 1, (255,255,255))
    screen.blit(playerVsPlayer, (340,250))
    screen.blit(playerVsPc, (340,350))
    screen.blit(mode, (340,400))
    screen.blit(dificult, (540,400))
    screen.blit(music, (340,300))
    screen.blit(title, (540,300))
    screen.blit(keyboard, (340,450))
    screen.blit(options, (340,500))
    screen.blit(back, (340,550))
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                gameState = previousGameState
            if event.key==K_RETURN:
                if s3Option[is3] == 5:
                    gameState = 2
                if s3Option[is3] == 6:
                    gameState = previousGameState
                if s3Option[is3] == 4:
                    gameState = 7
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
                if s3Option[is3] == 3:
                    if df < len(level)-1:
                        df += 1
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
                if s3Option[is3] == 3:
                    if df > 0:
                        df -= 1
    if df==0:
        playerPC.kamehamMs = 450
        playerPC.punchMs = 200
    if df==1:
        playerPC.kamehamMs = 200
        playerPC.punchMs = 110
    if df==2:
        playerPC.kamehamMs = 160
        playerPC.punchMs = 90
    if df==3:
        playerPC.kamehamMs = 70
        playerPC.punchMs = 70
    if df==4:
        playerPC.kamehamMs = 300
        playerPC.punchMs = 150
        playerPC2.kamehamMs = 300
        playerPC2.punchMs = 150
    if df==5:
        playerPC.kamehamMs = 3000
        playerPC.punchMs = 350
        playerPC2.kamehamMs = 3000
        playerPC2.punchMs = 350
        playerPC3.kamehamMs = 3000
        playerPC3.punchMs = 350
        
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

def keyboard():
    """
    Option Menu
    """
    global gameState
    global previousGameState
    global sg
    black = 0,0,0
    screen.fill(black)
    screen.blit(background_openning, (-70,0))
    myfont = pygame.font.SysFont("monospace", 45, bold = True)
    boldFont = pygame.font.SysFont("monospace", 55,bold =True)
    player1 = boldFont.render("Player 1", 1, (255,255,255))
    left = myfont.render("a - Left", 1, (255,255,0))
    right = myfont.render("d - Right", 1, (255,255,0))
    up = myfont.render("w - Up", 1, (255,255,0))
    down = myfont.render("s - Down", 1, (255,255,0))
    kameham = myfont.render("u - kameham", 1, (255,255,0))
    punch = myfont.render("i - Punch", 1, (255,255,0))
    kick = myfont.render("o - Kick", 1, (255,255,0))
    defend = myfont.render("p - Defend", 1, (255,255,0))
    load = myfont.render("j - Load", 1, (255,255,0))

    player2 = boldFont.render("Player 2", 1, (255,255,255))
    left2 = myfont.render("left arrow - Left", 1, (255,255,0))
    right2 = myfont.render("right arrow - Right", 1, (255,255,0))
    up2 = myfont.render("up arrow - Up", 1, (255,255,0))
    down2 = myfont.render("down arrow - Down", 1, (255,255,0))
    kameham2 = myfont.render("7 - kameham", 1, (255,255,0))
    punch2 = myfont.render("8 - Punch", 1, (255,255,0))
    kick2 = myfont.render("9 - Kick", 1, (255,255,0))
    defend2 = myfont.render("6 - Defend", 1, (255,255,0))
    load2 = myfont.render("5 - Load", 1, (255,255,0))
    back = boldFont.render("OK", 1, (255,255,255))

    screen.blit(player1, (300,100))
    screen.blit(left, (300,180))
    screen.blit(right, (300,230))
    screen.blit(up, (300,280))
    screen.blit(down, (300,330))
    screen.blit(kameham, (300,380))
    screen.blit(punch, (300,430))
    screen.blit(kick, (300,480))
    screen.blit(defend, (300,530))
    screen.blit(load, (300,580))

    screen.blit(player2, (680,100))
    screen.blit(left2, (680,180))
    screen.blit(right2, (680,230))
    screen.blit(up2, (680,280))
    screen.blit(down2, (680,330))
    screen.blit(kameham2, (680,380))
    screen.blit(punch2, (680,430))
    screen.blit(kick2, (680,480))
    screen.blit(defend2, (680,530))
    screen.blit(load2, (680,580))
    screen.blit(back, (780,680))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                gameState = previousGameState
            if event.key==K_RETURN:
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

def playOptions():
    """
    Menu during the playing game
    """
    global gameState
    global previousGameState
    global multiplayer
    black = 0,0,0
    screen.fill(black)
    screen.blit(background_openning, (-70,0))
    myfont = pygame.font.SysFont("monospace", 45)
    boldFont = pygame.font.SysFont("monospace", 55,bold =True)
    initialScreen = myfont.render("Player Vs PC", 1, (255,255,255))
    playerVsPlayer = myfont.render("Player Vs Player", 1, (255,255,255))
    playerVsPc = myfont.render("Player 1 & 2 Vs World", 1, (255,255,255))

    global is4
    if s4Option[is4] == 0:
        initialScreen = boldFont.render("Player Vs Pc", 1, (255,255,255))
    if s4Option[is4] == 1:
        playerVsPlayer = boldFont.render("Player Vs Player", 1, (255,255,255))
    if s4Option[is4] == 2:
        playerVsPc = boldFont.render("Player 1 & 2 Vs World", 1, (255,255,255))
    screen.blit(initialScreen, (340,250))
    screen.blit(playerVsPlayer, (340,305))
    screen.blit(playerVsPc, (340,360))
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                gameState = 0
            if event.key==K_RETURN:
                if s4Option[is4] == 0:
                    gameState = 9
                    player2.playerId = 2
                    multiplayer = False
                if s4Option[is4] == 1:
                    gameState = 5
                    restart()
                    vsPC = False
                    player2.playerId = 2
                    multiplayer = False
                if s4Option[is4] == 2:
                    multiplayer = True
                    gameState = 9
                    player2.playerId = 4
                    player2.x = 250
                    player2.y = 150
            if event.key==K_DOWN:
                if s4Option[is4] < s4Option[-1]:
                    is4 += 1
            if event.key==K_UP:
                if s4Option[is4] > s4Option[0]:
                    is4 -= 1

def PCOptions():
    """
    Menu during the playing game
    """
    global gameState
    global previousGameState
    global vsPC
    global pcNumber
    global df
    black = 0,0,0
    screen.fill(black)
    screen.blit(background_openning, (-70,0))
    myfont = pygame.font.SysFont("monospace", 45)
    boldFont = pygame.font.SysFont("monospace", 55,bold =True)
    initialScreen = myfont.render("Vs 1 PC", 1, (255,255,255))
    playerVsPlayer = myfont.render("Vs 2 PC", 1, (255,255,255))
    playerVsPc = myfont.render("Vs 3 PC", 1, (255,255,255))

    global is5
    if s5Option[is5] == 0:
        initialScreen = boldFont.render("Vs 1 PC", 1, (255,255,255))
    if s5Option[is5] == 1:
        playerVsPlayer = boldFont.render("Vs 2 PC", 1, (255,255,255))
    if s5Option[is5] == 2:
        playerVsPc = boldFont.render("Vs 3 PC", 1, (255,255,255))
    screen.blit(initialScreen, (340,250))
    screen.blit(playerVsPlayer, (340,305))
    screen.blit(playerVsPc, (340,360))
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                gameState = 0
            if event.key==K_RETURN:
                if s5Option[is5] == 0:
                    gameState = 5
                    vsPC = True
                    restart()
                    pcNumber = 1
                if s5Option[is5] == 1:
                    gameState = 5
                    vsPC = True
                    restart()
                    pcNumber = 2
                    df = 4
                    playerPC.kamehamMs = 300
                    playerPC.punchMs = 150
                    playerPC2.kamehamMs = 300
                    playerPC2.punchMs = 150
                if s5Option[is5] == 2:
                    gameState = 5
                    vsPC = True
                    restart()
                    pcNumber = 3
                    df = 5
                    playerPC.kamehamMs = 3000
                    playerPC.punchMs = 350
                    playerPC2.kamehamMs = 3000
                    playerPC2.punchMs = 350
                    playerPC3.kamehamMs = 3000
                    playerPC3.punchMs = 350
            if event.key==K_DOWN:
                if s5Option[is5] < s5Option[-1]:
                    is5 += 1
            if event.key==K_UP:
                if s5Option[is5] > s5Option[0]:
                    is5 -= 1

def loadMusic (music):
    """Load the musics of a list"""
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)
def distance(xo,yo,x,y):
    dx = x - xo
    dy = y - yo
    d = ((dx**2)+(dy**2))**0.5
    return d


def playLoop():
    """
    Game Loop
    """
    global vsPC
    global pcNumber
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if vsPC == False:
            p1 = [humanPlayers[0]]
            p2 = [humanPlayers[1]]
            player1.playPlayer(event,p2,power1)
            player2.playPlayer(event,p1,power2)
        if multiplayer == True:
            player2.playPlayer(event,PCPlayers,power2)
            player1.playPlayer(event,PCPlayers,power1)
        if vsPC == True and multiplayer ==False:
            player1.playPlayer(event,PCPlayers,power1)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                global gameState
                global previousGameState
                gameState = 1
                previousGameState = 2
    global width
    global height
    #playerVsplayer
    if vsPC == False and multiplayer == False:
        player1.lockInsideScreen(width,height,delta)
        player1.physicalRect()
        player1.powerPlacing(power1)
        player1.statusBar(screen,width)
        player1.standUpPosition()
        player1.defeated(screen,player2)
        player1.TurnAround(player2)
        player2.lockInsideScreen(width,height,delta)
        player2.physicalRect()
        player2.powerPlacing(power2,dx2=920,dy2=0)
        player2.statusBar(screen,width)
        player2.standUpPosition()
        player2.defeated(screen,player1)
        player2.TurnAround(player1)
        player1.update(player1.pos,screen)
        player2.update(player2.pos,screen)
        power1.update(player1.pos,screen)
        power2.update(player2.pos,screen)
    if vsPC == True and multiplayer == False:
        player1.lockInsideScreen(width,height,delta)
        player1.physicalRect()
        player1.powerPlacing(power1)
        player1.statusBar(screen,width)
        player1.standUpPosition()
        player1.defeated(screen,playerPC)
        #player1.TurnAround(playerPC)
        player1.update(player1.pos,screen)
        #power1.update(player1.pos,screen)
        
        #playerPC.playPC(player1,power3,screen)
        playerPC.lockInsideScreenPC(width, height, delta, player1)
        playerPC.physicalRect()
        playerPC.powerPlacing(power3)
        playerPC.statusBar(screen,width)
        playerPC.standUpPosition()
        playerPC.defeated(screen,player1)
        #playerPC.TurnAround(player1)
        playerPC.update(playerPC.pos,screen)
        power3.update(playerPC.pos,screen)
        if pcNumber == 1:
            player1.TurnAround(playerPC)
            playerPC.TurnAround(player1)
            playerPC.playPC(player1,power3,screen)
            power1.update(player1.pos,screen)
        if pcNumber >= 2:
            playerPC.TurnAround(player1)
            playerPC.playPC(player1,power3,screen)
            power1.update(player1.pos,screen)
            
            playerPC2.playPC(player1,power4,screen)
            playerPC2.lockInsideScreenPC(width, height, delta, player1)
            playerPC2.physicalRect()
            playerPC2.powerPlacing(power4)
            playerPC2.statusBar(screen,width)
            playerPC2.standUpPosition()
            #playerPC2.defeated(screen,player1)
            playerPC2.TurnAround(player1)
            playerPC2.teamDefeated(screen,player1,PCPlayers)
            playerPC2.update(playerPC2.pos,screen)
            
            if pcNumber == 2:
                d1=distance(player1.x,player1.y,playerPC.x,playerPC.y)
                d2=distance(player1.x,player1.y,playerPC2.x,playerPC2.y)
                if d1 < d2 and playerPC.HP>0:
                    player1.TurnAround(playerPC)
                if d1 > d2 and playerPC2.HP>0:
                    player1.TurnAround(playerPC2)
            power4.update(playerPC2.pos,screen)
        if pcNumber >= 3:
            playerPC3.playPC(player1,power5,screen)
            playerPC3.lockInsideScreenPC(width, height, delta, player1)
            playerPC3.physicalRect()
            playerPC3.powerPlacing(power5)
            playerPC3.statusBar(screen,width)
            playerPC3.standUpPosition()
            #playerPC2.defeated(screen,player1)
            playerPC3.TurnAround(player1)
            playerPC3.teamDefeated(screen,player1,PCPlayers)
            playerPC3.update(playerPC3.pos,screen)
            power5.update(playerPC3.pos,screen)
            if pcNumber == 3:
                d1=distance(player1.x,player1.y,playerPC.x,playerPC.y)
                d2=distance(player1.x,player1.y,playerPC2.x,playerPC2.y)
                d3=distance(player1.x,player1.y,playerPC3.x,playerPC3.y)
                if d1 < d2 and d1<d3 and playerPC.HP>0:
                    player1.TurnAround(playerPC)
                if d2 < d1 and d1<d3 and playerPC2.HP>0:
                    player1.TurnAround(playerPC2)
                if d3 < d1 and d3<d2 and playerPC2.HP>0:
                    player1.TurnAround(playerPC3)

    if multiplayer == True:
        player1.lockInsideScreen(width,height,delta)
        player1.physicalRect()
        player1.powerPlacing(power1)
        player1.statusBar(screen,width)
        player1.standUpPosition()
        player1.defeated(screen,playerPC)
        player1.TurnAround(playerPC)
        player2.lockInsideScreen(width,height,delta)
        player2.physicalRect()
        player2.powerPlacing(power2,dx2=920,dy2=0)
        player2.statusBar(screen,width)
        player2.standUpPosition()
        player2.defeated(screen,playerPC)
        player2.TurnAround(playerPC)
        player1.update(player1.pos,screen)
        player2.update(player2.pos,screen)
        power1.update(player1.pos,screen)
        power2.update(player2.pos,screen)

        #playerPC.playPC(player1,power3,screen)
        playerPC.physicalRect()
        playerPC.powerPlacing(power3)
        playerPC.statusBar(screen,width)
        playerPC.standUpPosition()
        playerPC.defeated(screen,player1)
        #playerPC.TurnAround(player1)
        playerPC.update(playerPC.pos,screen)
        power3.update(playerPC.pos,screen)

        d3=distance(player1.x,player1.y,playerPC.x,playerPC.y)
        d5=distance(player2.x,player2.y,playerPC.x,playerPC.y)
        global contador
        contador +=1
        if player1.HP> 0 and player2.HP >0:
            if d3<d5:
                playerPC.playPC(player1,power3,screen)
                playerPC.TurnAround(player1)
                playerPC.lockInsideScreenPC(width, height, delta, player1)
            if d5<d3:
                playerPC.playPC(player2,power3,screen)
                playerPC.TurnAround(player2)
                playerPC.lockInsideScreenPC(width, height, delta, player2)
        if player1.HP <=0:
            playerPC.playPC(player2,power3,screen)
            playerPC.TurnAround(player2)
            playerPC.lockInsideScreenPC(width, height, delta, player2)
        if player2.HP <=0:
            playerPC.playPC(player1,power3,screen)
            playerPC.TurnAround(player1)
            playerPC.lockInsideScreenPC(width, height, delta, player1)

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
    elif gameState == 7:
        keyboard()
    elif gameState == 8:
        playOptions()
    elif gameState == 9:
        PCOptions()
