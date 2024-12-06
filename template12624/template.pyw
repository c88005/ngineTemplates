# imports
import pygame
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
#-window and running system setup
done = False
menu = True
clock = pygame.time.Clock()
icon = pygame.image.load(dir1 + "icon.jpg") #icon
pygame.display.set_icon(icon) #icon application
pygame.display.set_caption("ngine template") #window name

# colors
backgroundColr = "#404040"
objectsColr = "#FFFFFF"

# player setup
health= 10
inventory = []
plrSZ = 40
plrSpeed = 1
plrX = (screenW/2 - plrSZ/2) #this var and \/ this are player position vars. Set them to 0 if you want player starting position in the left top corner
plrY = (screenH/2 - plrSZ/2)

# sounds
#--pygame mixer supports every sound format i guess
sound = mixer.Sound(dirS + "valve.wav")
sound2 = mixer.Sound(dirS + "valve2.wav")
sound3 = mixer.Sound(dirS + "valve3.wav")

#weapon setup
#(if you dont want weapons rays in your game just delete everything that mentions it)
weapons = ["NaN"]
curWeapon = weapons[0]
curSound = "NaN" #leave this like that
raycolor = (0,0,0)  #leave this like that
NaNAmmo = 12
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
count = 3
enabled = False
raycd = 15
posend = (0, 0)
raysize = 0
rayleftoversize = 0

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
    #-health setup
    if health <= 0:
        health == 0
        done = True #exits the game if health is 0 or lesser
    if curWeapon == weapons[0]:
        curAmmo = NaNAmmo
    #  \/ Additional slot with weapon
    #elif curWeapon == weapons[0]:
    #   curAmmo = NaNAmmo
    if curAmmo > 0:
        ammoIndexColr = str(objectsColr)
    else:
        ammoIndexColr = (255,0,0)
    if raysize < 0:
        raysize = 0
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
    plr = pygame.draw.rect(screen, objectsColr, pygame.Rect(plrX, plrY, plrSZ, plrSZ)) #player
    messageCorner = font.render(msg, True, objectsColr) #message test
    ammoRender = font.render(str(curAmmo), False, objectsColr) #ammo text in the corner
    AmmoS = font.render(str(raycd), False, objectsColr) #weapon cooldown in  the corner
    screen.blit(ammoRender, (screenW - 50,25)) #blit for ammo text
    screen.blit(AmmoS, (screenW - 50,0)) # blit for cooldown
    if msgTrig > 0:
       screen.blit(messageCorner, (0,0))#screenH/2 + screenH/3))
    
    #events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            #1 - left click, #2 - middle click, #3 - right click, #4 - scroll up, #5 - scroll down
            if event.button == 1:
                if raycd == 0 and curAmmo != 0:
                    if curWeapon == weapons[0]:
                        curAmmo = NaNAmmo
                        raycolor = (0,0,0) #btw you can create variables for this
                        curSound = sound
                        curSound.play()
                        count -= 1
                        raysize = 5
                        posend = pygame.mouse.get_pos()
                        raycd = 20
                        rayleftoversize = 10
                        NaNAmmo -= 1
                    # \/ addition if you have more than one weapon
                    #elif curWeapon == weapons[1]:
                    #    curAmmo = rifleAmmo
                    #   raycolor = (0,0,0)
                    #   curSound = sound2
                    #   curSound.play()
                    #   count -= 1
                    #    raysize = 10
                    #    posend = pygame.mouse.get_pos()
                    #    raycd = 10
                    #    rayleftoversize = 15
                    #    rifleAmmo -= 1
                    
                elif raycd == 0 and curAmmo == 0:
                   sound3.play()
                   raycd = 10
            elif event.button == 3:
                if fontTime == 0:
                    msgTrig = 120 #timer wheres 60 ticks is 1 second
                    msg = "NaN" #text that message is gonna display
                    sound2.play()
                    fontTime = 20
        #exiting mechanic
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            done = True
    
    #controls
    pressed = pygame.key.get_pressed()
    #-walking controls
    if pressed[pygame.K_w]: plrY -= 5
    if pressed[pygame.K_a]: plrX -= 5
    if pressed[pygame.K_s]: plrY += 5
    if pressed[pygame.K_d]: plrX += 5

    #-weapon slots (again, its optional)
    #if pressed[pygame.K_1]:
    #    curWeapon = weapons[1]
    #    curAmmo = pistolAmmo
    #if pressed[pygame.K_2]:
    #    curWeapon = weapons[0]
    #    curAmmo = rifleAmmo

    #game params
    pygame.display.flip()
    clock.tick(60)
    raysize -= 1
    msgTrig -= 1
    fontTime -= 1
    raycd -= 1
    rayleftoversize -= 1
