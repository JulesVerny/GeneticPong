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
MAXFRAMES = 1252
MAXEPOCHS = 101

# ==================================================================================
def EvaluateGenome(TheGenome,MaxFrames):
    
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
    while ((TotalGameStep< MaxFrames) and (not BirdCrashed) and (not GameQuit)):
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
# =====================================================================================
def CopyGenome(OriginalGenome): 
   NewGenome =  FlappyGenome()
   NewGenome.DistanceValues = OriginalGenome.DistanceValues
   NewGenome.HeightValues = OriginalGenome.HeightValues
   NewGenome.RisingValues = OriginalGenome.RisingValues
   NewGenome.LengthGenome = OriginalGenome.LengthGenome  
   NewGenome.score = -1  
   NewGenome.FlappyBirdGN = list(OriginalGenome.FlappyBirdGN)
   return NewGenome
# =========================================================================================
def CreateGreatGenome():
   GreatGenome = FlappyGenome()
   GreatGenome.Clear()
   #
   print()
   print("Creating a Great Bird Genome: ") 
   
   # Explicitly set Fall Values, to Flap if below
   GreatGenome.SetValue('JBelow','Far','Fall','F')
   GreatGenome.SetValue('Below','Far','Fall','F')
   GreatGenome.SetValue('VBelow','Far','Fall','F')
   GreatGenome.SetValue('JBelow','Med','Fall','F')
   GreatGenome.SetValue('Below','Med','Fall','F')
   GreatGenome.SetValue('VBelow','Med','Fall','F')   
   GreatGenome.SetValue('JBelow','Near','Fall','F')
   GreatGenome.SetValue('Below','Near','Fall','F')
   GreatGenome.SetValue('VBelow','Near','Fall','F')    
   GreatGenome.SetValue('JBelow','Close','Fall','F')
   GreatGenome.SetValue('Below','Close','Fall','F')
   GreatGenome.SetValue('VBelow','Close','Fall','F')   
   GreatGenome.SetValue('JBelow','VClose','Fall','F')
   GreatGenome.SetValue('Below','VClose','Fall','F')
   GreatGenome.SetValue('VBelow','VClose','Fall','F')    
   GreatGenome.SetValue('VBelow','Between','Fall','F')     
   GreatGenome.SetValue('Below','Between','Fall','F')  
  
   # Don't really need to flap if already rising
   GreatGenome.SetValue('VBelow','Far','Rise','F')
   GreatGenome.SetValue('Below','Far','Rise','F')
 
   return  GreatGenome 
# =================================================================================================   
# 
def TrainPopulation():

   print()
   print("Creating Initial Population") 

   EpochCount = 0
   HighestScore  = 0
   TrainQuit = False
   
   GameHistory = []

   # Create a Best Ever Genome to Keep   
   BestEverScore = 0
   BestEverGenome = FlappyGenome()
   
   # Create an Initial Population of 14 Genomes 
   FlappyBirdPopulation = []   
   for ix in range(14):
     FlappyBirdPopulation.append(FlappyGenome())    

   #  ***  Cheat Create a Great Genome and insert into Population[7]  **   
   # AGreatGenome = CreateGreatGenome()
   # FlappyBirdPopulation[7] = CopyGenome(AGreatGenome)       # COMMENT OUT !
   # *****  End of Cheat  **** 
   
   print("Initial Random Population ")
   for AGenome in FlappyBirdPopulation:
      AGenome.DisplayFlat()    
   
   print()
   print("*** Starting Epoch Generations *** ")   
   # Now Train the whole Population through MAXEPOCHS
   while ((EpochCount < MAXEPOCHS) and (not TrainQuit)):
   
      # For Evaluate Each of the Genomes in the Population
      #TrainQuit = EvaluateGenome(FlappyBirdPopulation[0])
      for AGenome in FlappyBirdPopulation:
         TrainQuit = EvaluateGenome(AGenome,MAXFRAMES)
         if(TrainQuit):
            break
			
	  # Now Sort the Population into Highest Scores
      FlappyBirdPopulation.sort(key=operator.attrgetter('score'), reverse = True)	  
      HighestScore = FlappyBirdPopulation[0].score	  	  
		  
      print("Epoch: ", EpochCount, "  High Score: ", HighestScore)
	  #  Periodically Display Best Genome and Population
      if EpochCount % 5 == 0:
	  # Display Current Best Genome
         print()
         FlappyBirdPopulation[0].DisplayGenome()
         for AGenome in FlappyBirdPopulation:
            AGenome.DisplayFlat() 
			
      GameHistory.append((EpochCount,HighestScore))		  	  

	  # Check the Best Ever Genome and Capture it
      if(HighestScore > BestEverScore):
         BestEverScore = HighestScore
         BestEverGenome = CopyGenome(FlappyBirdPopulation[0])
         BestEverGenome.SetScore(BestEverScore)

      # Pick and Retain Two (As Parents) into New Population
	  # Best Parents  Exists as Top Two sorted entries [0] and [1]

      # But Ensure that Best Ever Genome Stays at [0]
      FlappyBirdPopulation[0] = CopyGenome(BestEverGenome)
      FlappyBirdPopulation[0].SetScore(HighestScore)	  
	  
	  # Mutate Five (Three from Best, and Two from second) Genomes
      FlappyBirdPopulation[2] = CopyGenome(FlappyBirdPopulation[0]) 						# ensure copy by value 
      FlappyBirdPopulation[2].Mutate()	
      FlappyBirdPopulation[3] = CopyGenome(FlappyBirdPopulation[0]) 						# ensure copy by value 
      FlappyBirdPopulation[3].Mutate()
      FlappyBirdPopulation[4] = CopyGenome(FlappyBirdPopulation[0]) 						# ensure copy by value 
      FlappyBirdPopulation[4].Mutate()
	  
      FlappyBirdPopulation[5] = CopyGenome(FlappyBirdPopulation[1])
      FlappyBirdPopulation[5].Mutate()	
      FlappyBirdPopulation[6] = CopyGenome(FlappyBirdPopulation[1])
      FlappyBirdPopulation[6].Mutate()		  
	 
	  # Flip Top Two Genomes
      FlappyBirdPopulation[7] = CopyGenome(FlappyBirdPopulation[0])
      FlappyBirdPopulation[7].RandomFlip()	  
      FlappyBirdPopulation[8] = CopyGenome(FlappyBirdPopulation[1])
      FlappyBirdPopulation[8].RandomFlip()	
	  
	  # Create Three Children  
      FlappyBirdPopulation[9] = FlappyGenome()
      FlappyBirdPopulation[9].InheritFromParents(FlappyBirdPopulation[0], FlappyBirdPopulation[1])
      FlappyBirdPopulation[10] = FlappyGenome()
      FlappyBirdPopulation[10].InheritFromParents(FlappyBirdPopulation[0], FlappyBirdPopulation[1])
      FlappyBirdPopulation[11] = FlappyGenome()
      FlappyBirdPopulation[11].InheritFromParents(FlappyBirdPopulation[0], FlappyBirdPopulation[1])
	  
	  # Create Two  New Completely Random Genomes
      FlappyBirdPopulation[12] = FlappyGenome()
      FlappyBirdPopulation[13] = FlappyGenome()	  
   
      EpochCount = EpochCount +1
	  #	      
   # ======================================	
   print(" ==================================================")   
   print("*** End of Training Epochs*** ")
   print()
   print("Final Population: ")
   for AGenome in FlappyBirdPopulation:
      AGenome.DisplayFlat()  
   print()
   print(" Best in Population: ")
   FlappyBirdPopulation[0].DisplayFlat()
   print()
   FlappyBirdPopulation[0].DisplayGenome()  
   # ==================================
   #  Plot the Score vs Epochs  profile
   x_val = [x[0] for x in GameHistory]
   y_val = [x[1] for x in GameHistory]
   #
   plt.plot(x_val,y_val)
   plt.xlabel("Epochs ")
   plt.ylabel("Best Score")
   plt.show()
   # ==========================
   print(" ==================================================")
   print()
   print("Best Ever Score: ", BestEverScore)
   print()
   print("Best Ever Genome: ")
   BestEverGenome.DisplayFlat()
   print()
   BestEverGenome.DisplayGenome()  
   #  Really should think about saving it
   print(" *** Demo Play of the Best Discovered Genome  *** ")
   # Now Demo the Best Genome:
   TrainQuit = EvaluateGenome(BestEverGenome,5000)
   # If did not perform attempt to demo again   
   if(BestEverGenome.score <500):
      TrainQuit = EvaluateGenome(BestEverGenome,5000)
      
   print("******** END OF SHOW ********* ")
   print()  
# ============================================================================================
def main():
    TrainPopulation()

if __name__ == "__main__":
    main()
# =======================================================================================