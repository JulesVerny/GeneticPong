#
# Based upon Flappy Game used in Convolutional Learning examples in from 
# https://github.com/yanpanlau/Keras-FlappyBird
#
# ==================================================================================================
import numpy as np
import sys
import random
import pygame
import flappy_bird_utils

from pygame.locals import *
from itertools import cycle
# ===========================================================================================
FPS = 30
SCREENWIDTH  = 288
SCREENHEIGHT = 512

pygame.init()
FPSCLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('Flappy Bird')

IMAGES, SOUNDS, HITMASKS = flappy_bird_utils.load()
PIPEGAPSIZE = 130 # gap between upper and lower part of pipe  * Was100
BASEY = SCREENHEIGHT * 0.79

PLAYER_WIDTH = IMAGES['player'][0].get_width()
PLAYER_HEIGHT = IMAGES['player'][0].get_height()
PIPE_WIDTH = IMAGES['pipe'][0].get_width()
PIPE_HEIGHT = IMAGES['pipe'][0].get_height()
BACKGROUND_WIDTH = IMAGES['background'].get_width()

PLAYER_INDEX_GEN = cycle([0, 1, 2, 1])
# ======================================================================
def GetFuzzyValues(Distance,Height,RBoolean):
    """Returns the Fuzzifed Values for Distance, Heioght and Rising"""
    """ Fuzzy Values Will need some Tuning  to get optimum GA performance"""
	
    DString = 'Null'
    HString = 'Null'
    RString = 'Null'	

    # Enumerate the Distance Values	
    if(Distance >= 150):
        DString = 'Far'	
    if((Distance < 150) and (Distance >= 80)):
        DString = 'Med'	
    if((Distance < 80) and (Distance >= 55)):
        DString = 'Near'				    
    if((Distance < 55) and (Distance >= 35)):
        DString = 'Close'			
    if((Distance < 35) and (Distance >= 20)):
        DString = 'VClose'			
    if(Distance < 20):
        DString = 'Between'	

    # Enumerate the Height Values	
    if(Height >= 60):
        HString = 'VAbove'	
    if((Height < 60) and (Height >= 30)):
        HString = 'Above'	
    if((Height < 30) and (Height >= 15)):
        HString = 'JAbove'		    
    if((Height < 15) and (Height >= -15)):
        HString = 'Same'			
    if((Height < -15) and (Height >= -30)):
        HString = 'JBelow'
    if((Height < -30) and (Height >= -60)):
        HString = 'Below'		
    if(Height < -60):
        HString = 'VBelow'	
	
    # Enumerate the Rising/ Falling Values 
    if(RBoolean):
        RString = 'Rise'
    else:
        RString = 'Fall'
		
    return DString, HString, RString
 # =================================================================
 
class GameState:
   # =================================================================
    def __init__(self):
        self.score = self.playerIndex = self.loopIter = 0
        self.playerx = int(SCREENWIDTH * 0.2)
        self.playery = int((SCREENHEIGHT - PLAYER_HEIGHT) / 2)
        self.basex = 0
        self.baseShift = IMAGES['base'].get_width() - BACKGROUND_WIDTH

        newPipe1 = getRandomPipe()
        newPipe2 = getRandomPipe()
		
		# Make Start Earsier with One set of Pipes (To Avoid Interfernces
        self.upperPipes = [
            {'x': (8*SCREENWIDTH//10), 'y': newPipe1[0]['y']},          
#            {'x': SCREENWIDTH + (8*SCREENWIDTH//10), 'y': newPipe2[0]['y']},
        ]
        self.lowerPipes = [
            {'x': (8*SCREENWIDTH//10), 'y': newPipe1[1]['y']},
#            {'x': SCREENWIDTH + (8*SCREENWIDTH // 10), 'y': newPipe2[1]['y']},
        ]

        # player velocity, max velocity, downward accleration, accleration on flap
        self.pipeVelX = -4
        self.playerVelY    =  0    # player's velocity along Y, default same as playerFlapped
        self.playerMaxVelY =  10   # max vel along Y, max descend speed
        self.playerMinVelY =  -8   # min vel along Y, max ascend speed
        self.playerAccY    =   1   # players downward accleration
        self.playerFlapAcc =  -9   # players speed on flapping
        self.playerFlapped = False # True when player flaps
		
        self.FrameCount = 0 
		
# ======================================================================================================
    def Frame_Step(self, Action):
	
        Quit = False	

		# ====================================
		#  Process Keyboard Entry
        KeyPressed = pygame.key.get_pressed()
        if (KeyPressed[pygame.K_ESCAPE]):
            print("Esc pressed")
            Quit = True
        if (KeyPressed[pygame.K_q]):
            print("Esc pressed")
            Quit = True		
        if(KeyPressed[pygame.K_UP]):
            Action = 'F'		
			
        pygame.event.pump() # process event queue
		# ===================================
        Crashed = False
        Rising = False
		
        if Action == 'F':
		# Flap the Bird
            if self.playery > -2 * PLAYER_HEIGHT:
                self.playerVelY = self.playerFlapAcc
                self.playerFlapped = True

        # check for score
        playerMidPos = self.playerx + PLAYER_WIDTH / 2
        for pipe in self.upperPipes:
            pipeMidPos = pipe['x'] + PIPE_WIDTH / 2
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                self.score += 1
                # print("** Through Pipe: ** ")				
 
        # playerIndex basex change
        if (self.loopIter + 1) % 3 == 0:
            self.playerIndex = next(PLAYER_INDEX_GEN)
        self.loopIter = (self.loopIter + 1) % 30
        self.basex = -((-self.basex + 100) % self.baseShift)

        # Player's Y movement
        if self.playerVelY < self.playerMaxVelY and not self.playerFlapped:
            self.playerVelY += self.playerAccY
        if self.playerFlapped:
            self.playerFlapped = False

        DeltaY = 	min(self.playerVelY, BASEY - self.playery - PLAYER_HEIGHT)		
        self.playery = self.playery + DeltaY

        if(DeltaY < 0):
            Rising = True       		
		
        if self.playery < 0:
            self.playery = 0
		
        # move pipes to left
        for uPipe, lPipe in zip(self.upperPipes, self.lowerPipes):
            uPipe['x'] += self.pipeVelX
            lPipe['x'] += self.pipeVelX

        # add new pipe when first pipe is about to touch left of screen
        if 0 < self.upperPipes[0]['x'] < 5:
            newPipe = getRandomPipe()
            self.upperPipes.append(newPipe[0])
            self.lowerPipes.append(newPipe[1])

        # remove first pipe if its out of the screen
        if self.upperPipes[0]['x'] < -PIPE_WIDTH:
            self.upperPipes.pop(0)
            self.lowerPipes.pop(0)

        self.FrameCount =  self.FrameCount +1
		
		# Determine Player to Nearest PipeDistances
        BDistance, BHeight = GetPlayerToPipePositions(self.playerx,self.playery, self.upperPipes, self.lowerPipes)

        #print("Delta X, Y: [ ", BDistance, " , ", BHeight, " ]")
		
        # Fuzzyfy the Return Values
        FDistance,FHeight,FRising = GetFuzzyValues(BDistance, BHeight,Rising)		
        #print("Fuzzy Values: [ ", FDistance, " , ", FHeight, ", ",FRising, " ]")
		
		# check if crash here
        isCrash= checkCrash({'x': self.playerx, 'y': self.playery,
                             'index': self.playerIndex},
                            self.upperPipes, self.lowerPipes)
        if isCrash:
            Crashed = True
            self.__init__()

        # draw sprites
        SCREEN.blit(IMAGES['background'], (0,0))

        for uPipe, lPipe in zip(self.upperPipes, self.lowerPipes):
            SCREEN.blit(IMAGES['pipe'][0], (uPipe['x'], uPipe['y']))
            SCREEN.blit(IMAGES['pipe'][1], (lPipe['x'], lPipe['y']))

        SCREEN.blit(IMAGES['base'], (self.basex, BASEY))
        # print score so player overlaps the score
        showScore(self.score)
        SCREEN.blit(IMAGES['player'][self.playerIndex],
                    (self.playerx, self.playery))

		
        pygame.display.update()
        #print ("FPS" , FPSCLOCK.get_fps())
        FPSCLOCK.tick(FPS)
        #print self.upperPipes[0]['y'] + PIPE_HEIGHT - int(BASEY * 0.2)
		
		
        return self.FrameCount, FDistance,FHeight,FRising, Crashed, Quit
# ======================================================================================================

def getRandomPipe():
    """returns a randomly generated pipe"""
    # y of gap between upper and lower pipe
    gapYs = [20,30, 40, 50, 60, 70, 80, 90]
    index = random.randint(0, len(gapYs)-1)
    gapY = gapYs[index]

    gapY += int(BASEY * 0.2)
    pipeX = 8*SCREENWIDTH/10    # Was +10

    return [
        {'x': pipeX, 'y': gapY - PIPE_HEIGHT},  # upper pipe
        {'x': pipeX, 'y': gapY + PIPEGAPSIZE},  # lower pipe
    ]
# ======================================================================================================
def showScore(score):
    """displays score in center of screen"""
    scoreDigits = [int(x) for x in list(str(score))]
    totalWidth = 0 # total width of all numbers to be printed

    for digit in scoreDigits:
        totalWidth += IMAGES['numbers'][digit].get_width()

    Xoffset = (SCREENWIDTH - totalWidth) / 2

    for digit in scoreDigits:
        SCREEN.blit(IMAGES['numbers'][digit], (Xoffset, SCREENHEIGHT * 0.1))
        Xoffset += IMAGES['numbers'][digit].get_width()

# ======================================================================================================
def checkCrash(player, upperPipes, lowerPipes):
    """returns True if player collders with base or pipes."""
    pi = player['index']
    player['w'] = IMAGES['player'][0].get_width()
    player['h'] = IMAGES['player'][0].get_height()

    # if player crashes into ground
    if player['y'] + player['h'] >= BASEY - 1:
        return True
    else:

        playerRect = pygame.Rect(player['x'], player['y'],
                      player['w'], player['h'])

        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            # upper and lower pipe rects
            uPipeRect = pygame.Rect(uPipe['x'], uPipe['y'], PIPE_WIDTH, PIPE_HEIGHT)
            lPipeRect = pygame.Rect(lPipe['x'], lPipe['y'], PIPE_WIDTH, PIPE_HEIGHT)

            # player and upper/lower pipe hitmasks
            pHitMask = HITMASKS['player'][pi]
            uHitmask = HITMASKS['pipe'][0]
            lHitmask = HITMASKS['pipe'][1]

            # if bird collided with upipe or lpipe
            uCollide = pixelCollision(playerRect, uPipeRect, pHitMask, uHitmask)
            lCollide = pixelCollision(playerRect, lPipeRect, pHitMask, lHitmask)

            if uCollide or lCollide:
                return True

    return False
# ======================================================================================================

def GetPlayerToPipePositions(PBaseX,PBaseY, upperPipes, lowerPipes):
    """returns Player Horizontal and Vertical Distance to the next nearest Pipe"""
    """ Note Baswd upon above  Collsion Code which uses Rect to understand height and Width of Image Sprites """

    HDistance = 1000
    VDistance = 0
	
    playerwidth = IMAGES['player'][0].get_width()
    playerheight = IMAGES['player'][0].get_height()
   
	# Player Centre 
    PlayerCX = PBaseX + playerwidth//2
    PlayerCY = PBaseY + playerheight//2		
    # print("Player: [", PlayerCX, " , ", PlayerCY, "]")
	
	#  Need to review each Pipe   - would think x centre of upper and lower is the same
    for uPipe, lPipe in zip(upperPipes, lowerPipes):
        # upper and lower pipe rects

        uPipeCX = uPipe['x'] + PIPE_WIDTH//2
        uPipeCY = uPipe['y'] + PIPE_HEIGHT		
        lPipeCX = lPipe['x'] + PIPE_WIDTH//2
        lPipeCY = lPipe['y'] 
        # print("Pipe: [", uPipeCX, " , ", uPipeCY, " , ", lPipeCX," , ", lPipeCY, "]")  
        dx = uPipeCX - PlayerCX
        dy = (lPipeCY + uPipeCY)//2 - PlayerCY
        if((dx > 0) and (dx <HDistance)):
            HDistance = dx
            VDistance = dy
			
#    print("Delta X, Y: [ ", HDistance, " , ", VDistance, " ]")
#    print(" ------------------- ")

    return HDistance, VDistance
# ======================================================================================================
def pixelCollision(rect1, rect2, hitmask1, hitmask2):
    """Checks if two objects collide and not just their rects"""
    rect = rect1.clip(rect2)

    if rect.width == 0 or rect.height == 0:
        return False

    x1, y1 = rect.x - rect1.x, rect.y - rect1.y
    x2, y2 = rect.x - rect2.x, rect.y - rect2.y

    for x in range(rect.width):
        for y in range(rect.height):
            if hitmask1[x1+x][y1+y] and hitmask2[x2+x][y2+y]:
                return True
    return False
# ======================================================================================================