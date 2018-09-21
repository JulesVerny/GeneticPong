#
#  Play the Flappy Bird
#
from __future__ import print_function
import sys

import FlappyBirdGame as game
import random
# 

MAXFRAMES = 1000
# ==================================================================================

def PlayGame():
    
    GameQuit = False
	
	# Initialise the Flappy Bird Game
    TheGameState = game.GameState()

    print("Game Environment Complete")
    print(" ============================================ ")		
	
	
    TotalGameStep = 0
    CurrentDistanceScore = 0
	
	# ==============================================
    while ((TotalGameStep< MAXFRAMES) and (not GameQuit)):

	    # Choose the best Action
        AppliedAction = 'N'
        if (TotalGameStep % 5 == 0):
            AppliedAction = 'N'
		
        MaxDistanceScore = 	CurrentDistanceScore	
        #Run the selected action and Capture the Bird Distance and Height 
        CurrentDistanceScore, FuzzyDistance,FuzzyHeight,FuzzyRising, BirdCrashed,GameQuit = TheGameState.Frame_Step(AppliedAction)

        print(" FuzzyD: ", FuzzyDistance, "  FuzzyH: ", FuzzyHeight, "  FuzzyR: ", FuzzyRising) 
		
        if(BirdCrashed):
           print("**Bird Crashed **: ", MaxDistanceScore)	   

        print()		   

		# Display Step
        TotalGameStep = TotalGameStep + 1
        if (TotalGameStep % 100 == 0):
            print("Step:", TotalGameStep)  


    print("Game Run Finished!")
    print("************************")
# =====================================================================================
def main():
    PlayGame()

if __name__ == "__main__":
    main()
# =======================================================================================