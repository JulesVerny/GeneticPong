## Pong Game Genetic Algorithm Learning ##
Genetic Algorithm Based Learning for simple Pong PyGame.  This python based plays a Py Pong Game (control of Left Hand Yellow Paddle against a programmed RHS Paddle)

![alt text](https://github.com/JulesVerny/PongReinforcementLearning/blob/master/PongGame.PNG "Game Play")

The Objective is simply measured as successfully returning of the Ball by the Yellow RL DQN Agent.  
The programmed opponent player is a pretty hot player. So success as is simply the  ability to return ball served from Serena Williams.
In this Interpration, Success is deemed when the Player continues a Game for 500 Frames


![alt text](https://github.com/JulesVerny/PongReinforcementLearning/blob/master/PongGALearning.png "Score growth")

The Use of Genetic Algorithms and some Fuzzy Logic of the Ball Postions, Paddle Positiosn and Direction.  This was inspiredm due to frustrations with excessive
learning time for Convolutional and Nueral Netwrok solutions.  The Genetic Algorithm, with Fuzzy logic rules, results in an intepretation of the solution. 
As the Fuzzy Rules cxan be interpreted and Questioned by Humans. 

The Genomes are diplayed either in a Flat Structure or Tabular Structure.  The Tabular Strcuture can be interepeted by humans.
   

![alt text](https://github.com/JulesVerny/PongReinforcementLearning/blob/master/Evolution.png "Score growth")
This shows the Console Output part way through evolution, with the Best Genome Displayed, and the Populaiton Genomes. The Populations shows that the Top Most Genmoe is already at Optimum, with other Genomes (Mutated, Children, Random) not perfming so well.
A review of the Best Genmome can be comapred with Inution, that The Paddle should move U (up) when the Paddle is Below the Ball, and Paddle should move D (Down) when above the Ball. Especially when the Ball is moving left twoards the Plye Paddle. The Padle Action when Moving Right, so critical, the AI has enough time to to respond, waiting for the Ball to be returned. When the Paddle is at the 'same' height s the ball, it does not need to do any action 'S' [Same]  
   

### Useage ##
python TrainPongGA.py

This main Training runs through a Population of 14 x PongGenomes, a releselects the Best Genomes at each Epoch.  A Total of only 30 Epochs to Train the Population, and evolve consistent results.
The Genetic Algorithm Choice, after sorting the scores of the Populaiton :
- Keep Top Two Scoring Genomce from Population [0,1]   - With the Bets Ever Genome replaced in [0]   
- The Next 5 [2,3,4,5,6,7 ]Genomes are Created as Mutants from the top two - Just a single Bit is changed at Random
- The next four [8,9,10,11] Are Creted as Childen from the Top two, by crossover splits (Two crossover points) 
- The last two slots [12,13] Are two compltely new Randm Genomes.

This new Population is then reevaluated by playimng the Game, and collecting the Frame Score Count (Number of Frames played, until the Paddle misses the returned Ball) 

The Genome class describes the Genome methods, and Genetic Modifications and CLI Display methods  : 
PongGenome.py

The Pong Game is described in:  
PongGame.py

The ExplicitPong.Py, is  Main executable against a Manually prepared (Simple presumed optimum Genome) to compare Perfomance against the GA evolved Genomes 

### Other Pong Experiments ###
Please see my other repository for a Convolotional DQN game of Pong from Game Screen Imagary
https://github.com/JulesVerny/PongConvolutionalDQN
and  and Explcit Nueral network based upon  Game Paramters Ball Postion, and Player Position
https://github.com/JulesVerny/PongReinforcementLearning

### Acknowledgments: ###
* The  Pong Game Code is based upon Siraj Raval's inspiring vidoes on Machine learning and Reinforcement Learning [ Which does employ full convolutional DQN example]:   https://github.com/llSourcell/pong_neural_network_live
