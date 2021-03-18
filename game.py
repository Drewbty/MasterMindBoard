import random
from collections import Counter
import sys
from gameprefix import GamePrefix
from compare import Player


class Game(GamePrefix):
    def __init__(self,PegLength,trylength,playernum):
        self._PegLength= PegLength
        self._trylength = trylength
        self._playernum= playernum
        

    def ply(self):
        print("player/s =  ",self._playernum)
        print("Mode  =  vs Computer ")
        
        solution_code = GamePrefix.code_generator(self,self._PegLength)
        playerobj = Player(self._playernum)
        

        
        for x in range(0,len(playerobj.Playerlist)):
            
            print("Welcome to MasterMind", playerobj.Playerlist[x])
            
            for i in range(1, self._trylength+1):
                if (GamePrefix.compute(self,playerobj.Playerlist[x],i, self._trylength,x,3,solution_code,self._PegLength))=='discontinue':
                    break


        



###################################################
#####      Game#1                           #####
###################################################

class MasterMind4PlayerComputer(Game):
    def __init__(self,PegLength,trylength,playernum):
        super().__init__(PegLength,trylength,playernum)
    
        
    

###################################################
#####      Game#2                           #####
###################################################

class MasterMind4Player(Game):
    def __init__(self,PegLength,trylength,playernum):
        super().__init__(PegLength,trylength,playernum)

    def ply(self):
          
        


        playerobj = Player(self._playernum)
        print("\n\n Welcome  ", playerobj.Playerlist[0] )
        print("\nYou are the codemaker for this game./nYou need to make a Code that consists of "+self._PegLength+ "  pegs.\nEach peg can be of the colour (R)ed, (B)lue, (G)reen, (Y)ellow, (M)agenta or (C)yan \nMake the Code by specifying four characters where each character indicates a colour as above.\n For example, BYRG represents the code Blue Yellow Red Green.\nYou need to enter the Code twice.") 
        solution_code='X'
        while solution_code =='X':
            solution_code = GamePrefix.get_code(self,self._PegLength)
        for x in range(1,self._playernum):
            print("\n\nWelcome ", playerobj.Playerlist[x])
            print("\nYou are the codebreaker for this game.\n",playerobj.Playerlist[0]," has made a Code for you.\nYou need to break the Code that consists of ",self._PegLength," pegs.\nEach peg can be of the colour (R)ed, (B)lue, (G)reen, (Y)ellow, (M)agenta or (C)yan.\nBreak the Code by specifying four characters where each character indicates a colour as above.\nFor example, BYRG represents the code Blue Yellow Red Green.\nFeedback will be provided on your attempted Code.\nBlack peg means there is a peg in your Code with correct colour and correct order.\nWhite peg means there is a peg in your Code with correct colour but incorrect order.\nBlank space in the feedback denotes a peg in your Code with incorrect colour and incorrect order.\nYou will get "+self._trylength+" attempts to break the code. Good luck!\n\n ")
            
            for i in range(1, self._trylength+1):
                if (GamePrefix.compute(self,playerobj.Playerlist[x],i, self._trylength,x,3,solution_code,self._PegLength))=='discontinue':
                    break
                

        



###################################################
#####      Game#3                           #####
###################################################

class MasterMind2(MasterMind4Player):
    def __init__(self,PegLength,trylength,playernum):
        super().__init__(PegLength,trylength,playernum)

    
            
###################################################
#####      Game#4                           #####
###################################################
 

class MasterMind1(Game):
    def __init__(self,PegLength,trylength,playernum):
        super().__init__(PegLength,trylength,playernum)

