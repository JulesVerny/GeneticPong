#
#  Flappy Bird Genome Processing
#
from FlappyGenome import FlappyGenome
import random
#
# ===========================================================
print("\n Create a Genome")
#

FirstGenome = FlappyGenome()
#
FirstGenome.DisplayGenome()
#
# Set a few values
FirstGenome.SetValue('Below','Close','Rise','F')
FirstGenome.SetValue('Above','VClose','Fall','F')
FirstGenome.SetValue('Same','Between','Fall','F')
FirstGenome.SetValue('Below','Between','Rise','F')
#
print("\nUpdated Genome")
FirstGenome.DisplayGenome()
#
#  Mutate
FirstGenome.Mutate()
print("\nMutated Genome")
FirstGenome.DisplayGenome()
#
#
print("\nFirst Flip")
FirstGenome.RandomFlip()
FirstGenome.DisplayGenome()
#
print("\nSecond Flip")
FirstGenome.RandomFlip()
FirstGenome.DisplayGenome()
#
# ===================================
print(" ==================")
print("\n Now Create a Family")
print("")
#
Parent1 = FlappyGenome()
print("\n Parent 1")
Parent1.DisplayGenome()
#
Parent2 = FlappyGenome()
print("\n Parent 2")
Parent2.DisplayGenome()
#
# Create a Child
Child1 = FlappyGenome()
# Now Inherit from Parents
Child1.InheritFromParents(Parent1, Parent2)
print("\n Display Child")
Child1.DisplayGenome()
print()
Parent1.DisplayFlat()
Parent2.DisplayFlat()
Child1.DisplayFlat()
# =============================================================
print(" ==================")
print("Check Flip Operations")
FirstGenome = FlappyGenome()
FirstGenome.DisplayFlat()
print("Now Create Copy and Flip It")
SecondGenome = FirstGenome      # Believs copy by Reference NOT Value
SecondGenome.RandomFlip()
FirstGenome.DisplayFlat()
SecondGenome.DisplayFlat()
# =================================================================
def CopyGenome(OriginalGenome): 
   NewGenome =  FlappyGenome()
   NewGenome.DistanceValues = OriginalGenome.DistanceValues
   NewGenome.HeightValues = OriginalGenome.HeightValues
   NewGenome.RisingValues = OriginalGenome.RisingValues
   NewGenome.LengthGenome = OriginalGenome.LengthGenome  
   NewGenome.score = -1  
   NewGenome.FlappyBirdGN = list(OriginalGenome.FlappyBirdGN)
   return NewGenome
# =====================================================================
print(" ==================")
print("Check Flip Operations using CopyGenome ")
FirstGenome = FlappyGenome()
FirstGenome.DisplayFlat()
print("Now Create CopyGenome() and Flip It")
SecondGenome = CopyGenome(FirstGenome)      # Believs copy by Reference NOT Value
SecondGenome.RandomFlip()
FirstGenome.DisplayFlat()
SecondGenome.DisplayFlat()
 
 
 