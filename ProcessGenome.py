#
#  Flappy Bird Genome Processing
#
from PongGenome import PongGenome
import random
#
# ===========================================================
print(" ======================================")
print()
print("\n Create a Genome")
#
# HeightValues = ('Above', 'Same','Below')   # tuple
# DistanceValues = ('Far','Med','Near')  # tuple
# BallDirection = ('Right','Left') 
# Action Values, ("U", "S", "D")

#
FirstGenome = PongGenome()
#
FirstGenome.DisplayGenome()
#
# Set a few values
FirstGenome.SetValue('Below','Near','Right','U')
FirstGenome.SetValue('Above','Far','Left','U')
FirstGenome.SetValue('Same','Med','Right','S')
FirstGenome.SetValue('Below','Near','Left','D')
FirstGenome.SetValue('Above','Far','Right','D')
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
# ===================================
print(" ==================")
print("\n Now Create a Family")
print("")
#
Parent1 = PongGenome()
print("\n Parent 1")
Parent1.DisplayGenome()
#
Parent2 = PongGenome()
print("\n Parent 2")
Parent2.DisplayGenome()
#
# Create a Child
Child1 = PongGenome()
# Now Inherit from Parents
Child1.InheritFromParents(Parent1, Parent2)
print("\n Display Child")
Child1.DisplayGenome()
print()
Parent1.DisplayFlat()
Parent2.DisplayFlat()
Child1.DisplayFlat()
# =============================================================

# =================================================================
def CopyGenome(OriginalGenome): 
   NewGenome =  PongGenome()
   NewGenome.DistanceValues = OriginalGenome.DistanceValues
   NewGenome.HeightValues = OriginalGenome.HeightValues
   NewGenome.DirectionValues = OriginalGenome.DirectionValues
   NewGenome.LengthGenome = OriginalGenome.LengthGenome  
   NewGenome.score = -1  
   NewGenome.PongGN = list(OriginalGenome.PongGN)
   return NewGenome
# =====================================================================
 
 
 