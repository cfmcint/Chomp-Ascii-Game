# Chomp-Ascii-Game

NOTE: The formatting of the exmaple AI moves do not format correctly in the file preview provided by GitHub. To see these examples properly please
open the actual file in Blame or Raw view.

How to play: The game I am created is CHOMP. The game consists of a gameboard that is made up of 6 x 7 squares. To play the game, each turn the 
player chooses a square ex. square column 4 row 3. Then the all of the squares up and to the right of that square go dark / turn off
those squares can no longer be chosen during the gameplay. The goal of the game is to not be the person to choose the bottom most left
square ("▣"). Whoever does so loses.

How my AI plays: My AI generally plays randomly except in a certain case where it uses game theory to ensure a computer win. For the random aspect 
I have two conditions where a random move is made. One is a general one and the other is when the remaining on squares form less than a 3x3 square.
The reason I made this second random condition is to increase the speed which the computer can find an allowed move to make. When developing my game
I found that about when there was 9 squuares or fewer left on the computer began to take a noticeable amount of time to figure out a move. Another 
feature of my AI is that when the player plays a move that makes the remaining on squares form a square then the computer will always chose the square
one northeast from the losing square. By doing this the computer sets itself up for my symmetry AI sequence which will always ensure a computer win.
This symmetry sequence, in short, keeps the board symmetrical about the line y = x. Whatever move the player makes will be coppied by the AI on the
other side of the y = x line. For example, if the player choses a square that is 4 horizontally from the losing square the AI will chose a square that
is 4 vertical from the losing square. It is important to remember that this symmetry sequence only occurs if the AI has done its square move. Bellow are
examples of the AI moves.

In this player move the player makes the board a square by choosing the square (6,5).

PLAYER'S MOVE

Choose a column: 6
Choose a row: 5
Player's CHOICE: ( 6 , 5 )
0| □ □ □ □ □ □ ■
1| □ □ □ □ □ □ ■
2| □ □ □ □ □ □ ■
3| □ □ □ □ □ □ ■
4| □ □ □ □ □ □ ■
5| ▣ □ □ □ □ □ ■
  ---------------
   0 1 2 3 4 5 6

Because the on squares form a square shape, the AI does its square move and choses the square (1,4). The AI will always choose the square (1,4) no mater the
dimensions of the square created by the player. Note how the number of remaining on squares along the x-axis is the same of the number of remaining squares
along the y-axis.

COMPUTER'S Move
COMPUTER'S CHOICE: ( 1 , 4 )
0| □ ■ ■ ■ ■ ■ ■ 
1| □ ■ ■ ■ ■ ■ ■
2| □ ■ ■ ■ ■ ■ ■
3| □ ■ ■ ■ ■ ■ ■
4| □ ■ ■ ■ ■ ■ ■
5| ▣ □ □ □ □ □ ■
  ---------------
   0 1 2 3 4 5 6

Next, let's say the player choses the square (4,5).

Player's CHOICE: ( 4 , 5 )
0| □ ■ ■ ■ ■ ■ ■
1| □ ■ ■ ■ ■ ■ ■
2| □ ■ ■ ■ ■ ■ ■
3| □ ■ ■ ■ ■ ■ ■
4| □ ■ ■ ■ ■ ■ ■
5| ▣ □ □ □ ■ ■ ■
  ---------------
   0 1 2 3 4 5 6

The computer will chose the square (0,1) to keep the number of squares on on the x-axis the same as those on on the y-axis. By continuing to do this an AI win will
be guaranteed.

COMPUTER'S Move
COMPUTER'S CHOICE: ( 0 , 1 )
0| ■ ■ ■ ■ ■ ■ ■
1| ■ ■ ■ ■ ■ ■ ■
2| □ ■ ■ ■ ■ ■ ■
3| □ ■ ■ ■ ■ ■ ■
4| □ ■ ■ ■ ■ ■ ■
5| ▣ □ □ □ ■ ■ ■
  ---------------
   0 1 2 3 4 5 6
