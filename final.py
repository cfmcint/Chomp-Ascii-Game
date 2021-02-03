#
# final.py
# Chomp Finale game
#

import random
import webbrowser
import time

class Board(object):
    """A data type representing a Chomp board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """ Constructs an object type Board with the given width and height"""
        self.width = width
        self.height = height
        self.data = [['□']*width for row in range(height)]
        self.data[height-1][0] = "▣" # Makes the losing sqaure this unique character to distinguish it
        self.off = [[False]*width for row in range(height)]
        self.AIprevMove = 'rand' # Keeps track of the previous move(s) for use by the AI. 
                                 # Used in AI move for the AI to know whether to do the symmetry moves or any of the other options.
        self.score = [0,0] #keeps track of the score. [user wins, user losses]

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # the string to return
        for row in range(0, self.height):
            s += str(row % 10) + '| '
            for col in range(0, self.width):
                s += self.data[row][col] + ' '
        
            s += '\n'

        s+= '  '
        s += (2*self.width + 1) * '-'   # bottom of the board

        # and the numbers underneath here
        s += '\n  '
        for col in range(0, self.width):
            s += ' ' + str(col % 10) 

        return s       # the board is complete, return it


    def addMove(self, row, col):
        """ Adds a move to the board removing all squares up and right of the chosen one
            Arguments: col the index of the column of the chose square and row the index of the row of the chosen square
        """
        W = self.width

        for r in range(0, row + 1):
            for c in range(col, W):
                self.data[r][c] = '■'
                self.off[r][c] = True
        
        return

    def clear(self):
        """ Clears the Board """
        W = self.width
        H = self.height

        self.data = [['□']*W for row in range(H)]
        self.data[H-1][0] = "▣"
        self.off = [[False]*W for row in range(H)]

    def allowsMove(self, r, c):
        """ Return: True if the calling object allows a move into column and row c. False if c is not a legal column/ row 
            or if it has already been Chomped, or it is the losing square.
            Arguments: c a column number, r a row number
        """
        loseMove = False

        if r == self.height - 1 and c == 0: # Checks to see if the move chosen would cause the computer or player to automatically lose
            loseMove = True

        if c in range(self.width) and r in range(self.height) and not self.off[r][c] and not loseMove:  
            return True
        else:
            return False

    def loses(self):
        """ Return: True if the only square left is the bottom left one. False otherwise
        """
        W = self.width
        H = self.height

        for r in range(H-1):  # Checks the whole board except for the bottom row
            for c in range(W):
                if not self.off[r][c]:
                    return False
        for c in range(1, W): # Checks the bottom row
            if not self.off[H-1][c]:
                return False

        return True

    def aiMove(self):
        """ Returns: the col and row where the ai will move
        """
        W = self.width
        H = self.height
        smallBoard = 3

        if self.AIprevMove == 'sqr': # If the AI played its special move when the gameboard is a square then this will have it match -
            L = symmetry(self)       # the symmetry of the player's moves ensuring an AI win.

            if L[0] == 'e':
                col = 0
                row = (H-1) - L[0]

            elif L[1] == 'c':
                col = 0
                row = (H-2) - L[0]
            else:
                row = H - 1
                col = H - L[0]

        elif onSquare(self): # If the on squares make the shape of a square chose the square one northeast from the bottom left
            col = 1
            row = H - 2
            self.AIprevMove = 'sqr'

        elif countOn(self) <= smallBoard: # The larger randomizer tends to not work efficently where there are 3ish on squares left so this will fix that
            col = random.choice(range(smallBoard))
            row = random.choice(range(H-smallBoard, H))
            self.AIprevMove = 'rand'

        else: # Randomizer to chose a move if none of the other conditions are met
            col = random.choice(range(W))
            row = random.choice(range(H))
            self.AIprevMove = 'rand'

        return col, row

    def playOneRound(self):
        """ plays one round of a CHOMP game
        """

        print("WELCOME TO CHOMP")
        print
        print(self)

        while True:
            users_col = -1
            users_row = -1
            print("PLAYER'S MOVE")

            while not self.allowsMove(users_row, users_col):  # Player coming up with a valid move
                print()
                users_col = int(input("Choose a column: "))
                users_row = int(input("Choose a row: "))

            print("Player's CHOICE: (", users_col, ",", users_row, ")")
            self.addMove(users_row, users_col)  # Adding player move
            print(self)

            if self.loses():
                print()
                print("PLAYER WINS! CONGRATS")
                self.score[0] += 1
                break
        
            ai_col = -1
            ai_row = -1
            print()
            print("COMPUTER'S Move")

            while not self.allowsMove(ai_row, ai_col):  # Computer trying to come up with a valid move
                ai_col, ai_row = self.aiMove()

            time.sleep(1)   # Delay to make the game play smoother
            print("COMPUTER'S CHOICE: (", ai_col, ",", ai_row, ")")  
            self.addMove(ai_row, ai_col)  # Computer adding its move
            print(self)

            if self.loses():
                print()
                print("COMPUTER WINS... better luck next time")
                self.score[1] += 1
                break
        
        self.clear()

    def menu(self):
        """ prints the menu"""
        print()
        print("-------score-------")
        print("Player wins:", self.score[0])
        print("Computer wins:", self.score[1])
        print()
        print("-------menu-------")
        print("     (1) Play Chomp")
        print("     (2) Load Save")
        print("     (3) Save Game")
        print("     (4) How to Play")
        print("     (5) Quit")
        print()

        uc = input("Your choice:")
        
        try:
            uc = int(uc)
            if uc not in [1,2,3,4,5]:
                 print("Not a valid input\n")  # Not an int in the list of possiible inputs
            else:
                return uc
        except: 
            print("Not a valid input\n")  # Not an integer input

        return self.menu()

    def play(self):
        """ Hosts a series of CHOMP games"""
        while True:
            userchoice = self.menu()

            if userchoice == 1:
                self.clear()
                self.playOneRound()

            if userchoice == 2:
                self.loadGame("CHOMPgameFile.txt")

            if userchoice == 3:
                self.saveGame("CHOMPgameFile.txt")
            
            if userchoice == 4:
                webbrowser.open_new_tab("http://pi.math.cornell.edu/~mec/2003-2004/graphtheory/chomp/howtoplaychomp.html")

            if userchoice == 5:
                print("GOODBYE")
                break
    
    def loadGame(self, filename):
        """ Load game from a file"""
        f = open(filename,"r")  # open file for reading
        data = eval(f.read())   # evaluate the results as a Python object
        f.close()
        self.score[0] = data[0]
        self.score[1] = data[1]
        print(filename, " loaded.")

    def saveGame(self, filename):
        """ save to a file """
        f = open(filename,"w")  # open file for writing
        data = self.score
        print(data,file=f)
        f.close()
        print(filename, " saved.")


def onSquare(b):
    """ Return: True if the remiaining on squares form a square shape.
        Arugument: Chomp game board b
    """
    H = b.height
    W = b.width
    topR = H
    rightC = -1

    for r in range(H):   # Finding the right most and top most on sqaures
        for c in range(W):
            if not b.off[r][c] and r < topR:
                topR = r
            
            if not b.off[r][c] and c > rightC:
                rightC = c

    if (H-1) - topR == rightC and not b.off[topR][rightC]: #Checking to see if those square indecies mean that that the on squares form a sqaure board shape
        return True
    else:
        return False

def symmetry(b):
    """ Return: a list containg the index of column or row where there are fewer on squares and whether that integer correcpond to
        a row or column coordinate.
        Argument: Chomp game board b
    """
    H = b.height
    W = b.width
    col = 0
    row = 0

    for c in range(W):   # Finding the highest column index that is on
        if not b.off[H-1][c] and c > col :
            col = c

    for r in range(H):   # Finding the lowest row index that is on
        if not b.off[r][0] and (H-1) - r > row:
            row = (H-1) - r   # Instead of row being the index of the row it is the number of squares that row is from the losing square

    if col < row:
        return [col, 'c']
    elif row < col:
        return [(H-1) - row, 'r']
    else:
        return [col, 'e']

def countOn(b):
    """ Return: The number of squares still left on
        Argument: Chomp game board b
    """
    H = b.height
    W = b.width
    count = 0

    for r in range(H):
        for c in range(W):
            if not b.off[r][c]:
                count += 1

    return count

#create a Board object, b
b = Board(7,6)

# play when run
b.play()
