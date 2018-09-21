## Flappy Bird  Genetic Algorithm Learning ##
Genetic Algorithm Based Learning for simple Flappy Bird PyGame.  This python based Flappy Bird  Game 
![alt text](https://github.com/JulesVerny/GeneticPong/blob/master/FlappyBird/GamePic.PNG "Game Play")

The Objective is simply measured as staying alive, and getting through as many pipes as possible. This is also evolved from Genetic Algorithm.  
 
In this Interpration, Success is deemed when the Player is able to continues to return Fly the Bird fpor a max of 1250 Game Frames.
The following diagram demonstrates the evolution of the Score, through 100 Evolution Epochs. Tyhe Initial Population performs poorly by hitting the first pipe around 52 Frames.  The final Population achieves near optimum perforance, but is rather erratic.  
![alt text](https://github.com/JulesVerny/GeneticPong/blob/master/FlappyBird/EvolvedScore100.png "Score growth")

The use of Genetic Algorithms and some Fuzzy Logic has been inspired from frustrations with Nueral Net Reinforcement processing being so slow, lack of robustness and lack of interpretation.  As with the other Pong Experiment below, this relies upon a capture of Ball and player positions. So it DOES NOT generalise as Convolutional Reinforcement learning methods have the advantage of.  
The Paddle, Ball positions and Direction are passded into a Fuzzy Logic Interetation (Or basic Binning) so as to map into Genome Based Rules Table. The advantage of Fuzzy Logic (and Genetic Algorith Development) is that it allows the developed Genomes rules to be Human Readable, Interpreted and Reviewable. This is  major advantage over Nueral network based solutions which are effectively Black Box. 

The Genomes can either be displayed either in a Flat Genome String Sequence Structure or laid out in a Tabular Structure.  The Tabular Strcuture ie easily interepeted by humans.  See the example below, halfway through the Training. 
![alt text](https://github.com/JulesVerny/GeneticPong/blob/master/FlappyBird/FinalGenome100.PNG "CLI Output")
This shows the Console Output part way through evolution, with the Best Genome Displayed in a Tabular Format and the Population of Genomes displayed as a set of Genome sequences with their scores. The Populations shows the Top most Genome is already achieved Optimum perfomance (1250), with the other Genomes (Mutated, Children, Random) not perfoming quite so well.

A review of the Best Genome in Tabular format (at the conclusion of the Training Epochs) can be compared against an intuitive understanding of the optimum Pong Player perfomance. 
Basically we would expect the Bird to only Flap, if it is Falling, and getting close to the pipes.  Otherwise would not wish to See Flap 
The Fuzzy Logic input (controls) are based upon distance to middle of next pipe gap (Farm Med, Near, Close, Very Close and Between)  and whther the bird is above or below the next Pipe Gap point( Very Above, Above, Just Above, Same. Just below, Below and very Below)
The Output controls are to Flap [F] or Not to Flap [N] 

### Useage ###
python TrainFlappyBirds.py

This main Training runs through a Population of 14 x FlappyGenomes, and resorts and releselects the best Genomes at each Epoch, based upon the scores acehievd for each Genome in the population.  A Total of only 100 Epochs appears to be needed to train the Population, and evolve reasonable perfomance growth.

The Genetic Algorithm choice selections (following a sorted population) are as follows :
- Keep Top Two Scoring Genomes in the Population [0,1]   - Also noting to potentially replace the top [0] entry with the Best Ever Genome    
- The Next 5 [2,3,4,5,6 ] Genomes are Created as Mutants from the top two [0] and [1] - Just a single Bit is changed at random
- The Next 5 [8,8] Genomes are Created as randome cross over Flips between the  the top two [0] and [1] - Just flip the bits N to F and F to N at a random point through the Genome
- The next three [9,10,11] Are Created as Childen from the Top two, through crossover splits (Two crossover points) of [0] and [1] 
- The last two slots [12,13] Are two compltely new Random Genomes.

This new Population is then reevaluated by playing through the game for Genome of the Population and capturing the Frame Score Count (Number of Frames played, until the Bird Strikes a Pipe) for each.  

### Supporting Classes ###
The Genome class describes the Genome methods:  Genetic Modifications and CLI Display methods  : 
FlappyGenome.py

The Py Game based Pong Game is:  
FlappyBirdGame.py
This is Based upon Flappy Game used in Convolutional Learning examples in from 
https://github.com/yanpanlau/Keras-FlappyBird

ExplicitBird.Py is a Main Executable, which is used to set up an intuitive optimum Genome, so as to compare performance and the evolved  Genomes against.  





