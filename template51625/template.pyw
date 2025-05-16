# imports
import pygame
import random
from pygame import mixer

# vars/pygame settings
#-directories
dir1 = "tempAssets/" #directory with everything in it
dirS = dir1 + "sounds/" #sound directory
dirI = dir1 + "images/" #image directory
#-screen setup
pygame.init()
screenH = 500 #height
screenW = 500 #width
screen = pygame.display.set_mode((screenH, screenW))
#-window and scene system setup
done = False
menu = True
clock = pygame.time.Clock()
icon = pygame.image.load(dir1 + "icon.jpg") #icon
pygame.display.set_icon(icon) #icon application
pygame.display.set_caption("ngine template") #window name

# options
opt_scndCircle = True
opt_circleDisappTime = 2

#groups
itemGr = pygame.sprite.Group()

# colors
backgroundColr = "#404040"
objectsColr = "#FFFFFF"
floorPartColr = "#505050"

#blood setup
#i didnt implemented this tbh
b = False
bx = 0
by = 0

# player setup
testcd = 0
health = 10
inventory = []
plrSZ = 55
plrSpeed = 3
plrX = 10 #this var and \/ this are player position vars. Set them to 0 if you want player starting position in the left top corner
plrY = (screenH/2 - plrSZ/2)
lowsoundPlays = False

# sounds
#--pygame mixer supports every sound format i guess
sound = mixer.Sound(dirS + "valve.wav")
sound2 = mixer.Sound(dirS + "valve2.wav")
sound3 = mixer.Sound(dirS + "valve3.wav")

#weapon ray setup
#(if you dont want weapons rays in your game just delete everything that mentions it)
weapons = ["NaN", "NaN-21"]
curWeapon = weapons[0]
curSound = "NaN" #leave this like that
raycolor = (0,0,0) #leave this like that
NaNAmmo = 12
NaN21Ammo = 35
curAmmo = NaNAmmo

# fonts
font = pygame.font.Font(dir1 + "font.ttf", 30)
fontBig = pygame.font.Font(dir1 + "font.ttf", 60)
font2 = pygame.font.Font(dir1 + "font2.ttf", 60)
fontTime = 0
msg = "NaN" #leave this like that
msgTrig = 0

#ray setup
#(if you dont want weapons in your game just delete everything that mentions it)
enabled = False
raycd = 15
posend = (0, 0)
raysize = 0
rayleftoversize = 0

#enemy setup (SRY THEY DONT WORK!!)
enemyHealth = 0
enemyWeapons = []
enemyDropRnd = []

#defs
#(if you DONT understant how functions work in python, please dont touch anything and ask you parents(jk))
def spawnLightEnemy(gridX, gridY, wpn, canDrop, drop, dropAmt):
    # MB THSI DOESNT WORK RN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    global enemyHealth
    global enemyWeapons
    global enemyDropRnd
    enemyHealth = 5
    enemy = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(gridX * 50, gridY * 50, 55, 55))
    if canDrop:
        print("yes")
        
def dealPlrDmg(dmg, wb):
    #litteraly damages player
    global health
    health -= dmg

def fire(curA, rcolr, curS, rs, rcd, rls):
    global curAmmo
    global curSound
    global raycolor
    global raycd
    global rayleftoversize
    global raysize
    
    curAmmo = curA
    raycolor = rcolr
    curSound = curS
    curSound.play()
    raysize = rs
    raycd = rcd
    rayleftoversize = rls
def msgF(msgtext, msgtime, cd):
    global fontTime
    global msgTrig
    global msg
    msgTrig = msgtime
    msg = msgtext
    fontTime = cd

# \/ - exiting system for scenes
#for event in pygame.event.get():
#   if event.type == pygame.QUIT:
#       pygame.quit()
#           exit()

# scenes (if you want to add new one, add a while cycle with a new variable like: settings, menu, etc. Also add exiting system)
#-menu
while menu:
    screen.fill((0,0,0))
    name = font2.render("NaN", True, (255,255,255)) #message test
    screen.blit(name, (20,50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        menu = False #if player presses space scene changes
        sound2.play()
    pygame.display.flip()
    clock.tick(60)
#-game
while not done:
    # ifs
    #\/ part of the office rooms hp code 🥀🥀
    #if health <= 3 and lowsoundPlays == False:
    #    lowsoundPlays = True
    #    lowsound.play()
    #elif health > 3 and lowsoundPlays == True:
    #    lowsoundPlays = False
    #    lowsound.stop()
    #    regen.play()
    #if health <= 0:
    #    health == 0
    #    lowsoundPlays = False
    #    lowsound.stop()
    #    deathBoom.play()
    #    done = True
    if curWeapon == weapons[1]:
        curAmmo = NaNAmmo
    elif curWeapon == weapons[0]:
        curAmmo = NaN21Ammo
    if curAmmo > 0:
        ammoIndexColr = str(objectsColr)
    else:
        ammoIndexColr = (255,0,0)
    if raysize < 0:
        raysize = 0
    if testcd < 0:
        testcd = 0
    if rayleftoversize < 0:
        rayleftoversize = 0
    if raycd < 0:
        raycd = 0
    if fontTime < 0:
        fontTime = 0
    
    #main draw params
    screen.fill((backgroundColr)) #background color(DONT DELETE THIS LINE PLZ, BC EVERYTHING WILL LOOK LIKE YOU ARE OUTSIDE THE MAP IN SOURCE GAMES!)
    
    pos = (plrX+ plrSZ/2,plrY+ plrSZ/2) #player centre

    ray = pygame.draw.line(screen, raycolor, pos, posend, raysize) #ray for a weapon
    
    pygame.draw.circle(screen, raycolor, posend, rayleftoversize) #circle for a ray
    #drawrect()
    
    if opt_scndCircle == True:
        pygame.draw.circle(screen, floorPartColr, posend, rayleftoversize * 2, 1)
        
    plr = pygame.draw.rect(screen, objectsColr, pygame.Rect(plrX, plrY, plrSZ, plrSZ))
    
    messageCorner = font.render(msg, True, objectsColr)
    ammoRender = font.render(str(curAmmo), False, objectsColr)
    gunNameRender = font.render(curWeapon, False, objectsColr)
    
    screen.blit(ammoRender, (screenW - 75, screenH - 50))
    screen.blit(gunNameRender, (screenW - 75, screenH - 100))
    
    if msgTrig > 0:
       screen.blit(messageCorner, (0,0))
    
    #events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            #1 - left click, #2 - middle click, #3 - right click, #4 - scroll up, #5 - scroll down
            if event.button == 1:
                if raycd == 0 and curAmmo != 0:
                    if curWeapon == weapons[1]:
                        fire(NaNAmmo, (0,0,0), sound, 5, 20, 10)
                        posend = pygame.mouse.get_pos()
                        NaNAmmo -= 1
                    elif curWeapon == weapons[0]:
                        fire(NaN21Ammo, (0,0,0), sound, 10, 10, 15)
                        posend = pygame.mouse.get_pos()
                        NaN21Ammo -= 1
                elif raycd == 0 and curAmmo == 0:
                   sound3.play()
                   raycd = 10
            elif event.button == 3:
                if fontTime == 0:
                    msgF("NaN 10", 120, 20)
                    sound2.play()
                    NaNAmmo += 10
                
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
    
    #controls
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_w]: plrY -= 5
    if pressed[pygame.K_a]: plrX -= 5
    if pressed[pygame.K_s]: plrY += 5
    if pressed[pygame.K_d]: plrX += 5

    if pressed[pygame.K_1]:
        curWeapon = weapons[1]
        curAmmo = NaNAmmo
    if pressed[pygame.K_2]:
        curWeapon = weapons[0]
        curAmmo = NaN21Ammo

    if pressed[pygame.K_o]:
        if testcd == 0:
            dealPlrDmg(1, 1)
            testcd = 10
                
    if pressed[pygame.K_i]:
        health += 1
    
    #game params
    clock.tick(60)
    pygame.display.flip()
    testcd -= 1
    raysize -= 1
    msgTrig -= 1
    fontTime -= 1
    raycd -= 1
    rayleftoversize -= opt_circleDisappTime


