#
#  Base Genome Class
#   
#  Constrcutor creates a random Genome
#  Set Value of an indexed Chromosphone
#  Mutate Single Chromosphone
#  Random Flip - Split Point Part Way through
#  Inherit from parents (At two split points) 
#  Display Genome in a Tabular format
# ===================================================
import random
# =================================================
class FlappyGenome:
   def __init__(self):
       self.HeightValues = ('VAbove','Above','JAbove', 'Same', 'JBelow','Below','VBelow')   # tuple
       self.DistanceValues = ('Far','Med','Near','Close', 'VClose', 'Between')  # tuple
       self.RisingValues = ('Rise','Fall') 
	   
       self.LengthGenome = len(self.HeightValues) * len(self.DistanceValues)* len(self.RisingValues)
       self.score = -11
       # Genome really needs to be one flattened list, only restructure for display purposes
       self.FlappyBirdGN = ['N' for ix in range(self.LengthGenome)]

	   # Now Randomise the Initial Values
       for ix in range(self.LengthGenome):
           if(random.randrange(100)>75):
              self.FlappyBirdGN[ix] = 'F'
	
# ========================================
   def SetValue(self,Height,Distance,Rising, NewValue):
      GIndex =   self.RisingValues.index(Rising)*len(self.DistanceValues)*len(self.HeightValues) + self.HeightValues.index(Height)*len(self.DistanceValues) + self.DistanceValues.index(Distance)
      self.FlappyBirdGN[GIndex] = NewValue
# ========================================
   def Clear(self):
      for ix in range(self.LengthGenome):
         self.FlappyBirdGN[ix] = 'N'
	  
# ========================================
   def RtnAction(self,Height,Distance,Rising):
      GIndex =   self.RisingValues.index(Rising)*len(self.DistanceValues)*len(self.HeightValues) + self.HeightValues.index(Height)*len(self.DistanceValues) + self.DistanceValues.index(Distance)
      return self.FlappyBirdGN[GIndex]	  
	  
# ======================================================
   def RtnAction(self,Height,Distance,Rising):
      GIndex =   self.RisingValues.index(Rising)*len(self.DistanceValues)*len(self.HeightValues) + self.HeightValues.index(Height)*len(self.DistanceValues) + self.DistanceValues.index(Distance)
      return self.FlappyBirdGN[GIndex]	  	  
	  
# ========================================
   def SetScore(self,NewScore):
      self.score = NewScore
# ========================================	  
   def Mutate(self):
      index_mutate = int(random.random() * len(self.FlappyBirdGN))
   
      if(self.FlappyBirdGN[index_mutate] == 'N'):
         self.FlappyBirdGN[index_mutate] = 'F'
      else:
         self.FlappyBirdGN[index_mutate] = 'N'  
# =========================================
   def RandomFlip(self):
      index_FlipPoint = int(random.random() * len(self.FlappyBirdGN))
      #print("Flipoint:",  index_FlipPoint)
	  
      flipchoice = (random.randrange(100)>50)
      # Up To Flip Point
      for ix in range(0,index_FlipPoint):
         if(flipchoice):	  
            if(self.FlappyBirdGN[ix] == 'N'):
               self.FlappyBirdGN[ix] = 'F'
            else:
               self.FlappyBirdGN[ix] = 'N' 
      # beyond Flip Point
      for ix in range(index_FlipPoint,len(self.FlappyBirdGN)):
         if( not flipchoice):	  
            if(self.FlappyBirdGN[ix] == 'N'):
               self.FlappyBirdGN[ix] = 'F'
            else:
               self.FlappyBirdGN[ix] = 'N'	
# =========================================
   def InheritFromParents(self,Parent1,Parent2):
    
      SplitPoint1 = int(random.randrange(0,len(self.FlappyBirdGN)//2))     # // is an integer division
      SplitPoint2 = int(random.randrange(SplitPoint1,len(self.FlappyBirdGN)))	  	  
      # print("SPoint1: ",  SplitPoint1,"  SPoint2: ",  SplitPoint2)
	  
      Parentchoice = (random.randrange(100)>50)   # Binary random Choice
	  
      # Up To Split Point1
      for ix in range(0,SplitPoint1):
         if(Parentchoice):	  
            self.FlappyBirdGN[ix] = Parent1.FlappyBirdGN[ix]
         else:
             self.FlappyBirdGN[ix] = Parent2.FlappyBirdGN[ix] 
      # Between Split Points
      for ix in range(SplitPoint1,SplitPoint2):
         if(Parentchoice):	  
            self.FlappyBirdGN[ix] = Parent2.FlappyBirdGN[ix]
         else:
             self.FlappyBirdGN[ix] = Parent1.FlappyBirdGN[ix] 
     # Beyond second Split Point
      for ix in range(SplitPoint2,len(self.FlappyBirdGN)):
         if(Parentchoice):	  
            self.FlappyBirdGN[ix] = Parent1.FlappyBirdGN[ix]
         else:
             self.FlappyBirdGN[ix] = Parent2.FlappyBirdGN[ix] 
   
# ========================================
   def DisplayGenome(self):
      print("\t\t   Rising Values: \t\t\t\t\t     Falling Values: ") 
      header = str(self.score) + "\t"
      for hdri in range(len(self.DistanceValues)):
          header = header + self.DistanceValues[hdri] + "\t" 
      # And Repeat Again 
      header = header + "\t"
      for hdri in range(len(self.DistanceValues)):
         header = header + self.DistanceValues[hdri] + "\t"   
      print(header)
      # Now print row content
      for rowi in range(len(self.HeightValues)):
         rowstring = self.HeightValues[rowi] + "\t"
 
         # First Half  of Genome [Rising] 
         for hdri in range(len(self.DistanceValues)): 
            rowstring = rowstring + self.FlappyBirdGN[rowi*len(self.DistanceValues)+ hdri] + "\t"
 
         rowstring = rowstring + "\t"
         # Second Half  of Genome [Falling]  - These are at Additional len(self.HeightValues)*len(self.DistanceValues)  Index
         for hdri in range(len(self.DistanceValues)): 
             rowstring = rowstring + self.FlappyBirdGN[len(self.HeightValues)*len(self.DistanceValues) + rowi*len(self.DistanceValues)+ hdri] + "\t"
 
         print(rowstring)
# ======================================== 
   def DisplayFlat(self):
      GString = str(self.score) + "\t"  
      # Now create Lower Part of Genome [Rising] 
      for rowi in range(len(self.HeightValues)):
         for hdri in range(len(self.DistanceValues)): 
            GString = GString + self.FlappyBirdGN[rowi*len(self.HeightValues)+ hdri]
      
      GString = GString + "\t"
      # Now create Second Part of Genome [Falling] - These are at Additional len(self.HeightValues)*len(self.DistanceValues)  Index
      for rowi in range(len(self.HeightValues)):
         for hdri in range(len(self.DistanceValues)): 
            GString = GString + self.FlappyBirdGN[len(self.HeightValues)*len(self.DistanceValues) + rowi*len(self.DistanceValues)+ hdri]

      print(GString)
# ======================================== 


