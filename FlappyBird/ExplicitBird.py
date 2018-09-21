#
#  Train a Set of Flappy Birds
#
# ===============================================================================================
from __future__ import print_function
import sys
#
import FlappyBirdGame as game
from FlappyGenome import FlappyGenome
#
import matplotlib.pyplot as plt
import random
import operator
# 
MAXFRAMES = 2500
MAXEPOCHS = 10

# ==================================================================================
def EvaluateGenome(TheGenome):
    
	# Initialise a Flappy Bird Game
    TheGameState = game.GameState()

    TotalGameStep = 0
    CurrentFrameCountScore = 0
    BirdCrashed = False
	
    FuzzyHeight = 'Same'
    FuzzyDistance = 'Far'
    FuzzyRising = 'Rise'
    GameQuit = False
	# ==============================================
    while ((TotalGameStep< MAXFRAMES) and (not BirdCrashed) and (not GameQuit)):
	    # Choose the best Action
        AppliedAction = 'N'
 
        AppliedAction = TheGenome.RtnAction(FuzzyHeight,FuzzyDistance,FuzzyRising)
		
        MaxFrameCountScore = 	CurrentFrameCountScore	
        #Run the selected action and Capture the Bird Distance and Height 
        CurrentFrameCountScore, FuzzyDistance,FuzzyHeight,FuzzyRising, BirdCrashed,GameQuit = TheGameState.Frame_Step(AppliedAction)

		# Display Step
        TotalGameStep = TotalGameStep + 1
 
    TheGenome.SetScore(MaxFrameCountScore)
    return GameQuit

# =========================================================================================
def RunBird():

   print()
   print("Creating The Explicit Bird ") 

   EpochCount = 0
   HighestScore  = 0
   TrainQuit = False
   
   GameHistory = []   
   
   TheGenome = FlappyGenome()
   TheGenome.Clear()
   #
   print()
   print("Set Explicit Bird: ") 
   
   # Explcitly set Fall Values, to Flap if below
   TheGenome.SetValue('JBelow','Far','Fall','F')
   TheGenome.SetValue('Below','Far','Fall','F')
   TheGenome.SetValue('VBelow','Far','Fall','F')
   TheGenome.SetValue('JBelow','Med','Fall','F')
   TheGenome.SetValue('Below','Med','Fall','F')
   TheGenome.SetValue('VBelow','Med','Fall','F')   
   TheGenome.SetValue('JBelow','Near','Fall','F')
   TheGenome.SetValue('Below','Near','Fall','F')
   TheGenome.SetValue('VBelow','Near','Fall','F')    
   TheGenome.SetValue('JBelow','Close','Fall','F')
   TheGenome.SetValue('Below','Close','Fall','F')
   TheGenome.SetValue('VBelow','Close','Fall','F')   
   TheGenome.SetValue('JBelow','VClose','Fall','F')
   TheGenome.SetValue('Below','VClose','Fall','F')
   TheGenome.SetValue('VBelow','VClose','Fall','F')    
   TheGenome.SetValue('VBelow','Between','Fall','F')     
   TheGenome.SetValue('Below','Between','Fall','F')  
  
   # Don't really need to flap if already rising
   TheGenome.SetValue('VBelow','Far','Rise','F')
   TheGenome.SetValue('Below','Far','Rise','F')
 
   TheGenome.DisplayGenome()
   
   print("*** Running Bird *** ")   
   # Now Train the whole Population through MAXEPOCHS
   while ((EpochCount < MAXEPOCHS) and (not TrainQuit)):
   
      # For Evaluate Each of the Genomes in the Population
      TrainQuit = EvaluateGenome(TheGenome) 

   
      EpochCount = EpochCount +1
	  #
      HighestScore = TheGenome.score
      print("Epoch: ", EpochCount, "  High Score: ", HighestScore)
      GameHistory.append((EpochCount,HighestScore))
   # ======================================	  
   print("*** End of Training Epochs*** ")
   
   # ==================================
   #  Plot the Score vs Epochs  profile
   x_val = [x[0] for x in GameHistory]
   y_val = [x[1] for x in GameHistory]

   plt.plot(x_val,y_val)
   plt.xlabel("Epochs ")
   plt.ylabel("Best Score")
   plt.show()
   # ==========================
   print()
   print("Best Genome: ")
   TheGenome.DisplayFlat()
   print()
   TheGenome.DisplayGenome()   

   print("******** END OF SHOW ********* ")
   print()  
# ============================================================================================
def main():
    RunBird()

if __name__ == "__main__":
    main()
# =======================================================================================