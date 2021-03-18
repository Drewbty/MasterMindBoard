from menu import Menu
from game import MasterMind4PlayerComputer,MasterMind4Player,MasterMind1,MasterMind2
import sys

#               multiple Inheritence

class Mastermind(Menu):
    def __init__(self):
        #Dispaly menu and Get User Choice 
        Menu.__init__(self)
        choice=self.returnchoice


        
        #various games depending on which one tha player wants to play
        # with their respective players
        # constructer parameters are passed Peglength and Number of turs and num of players for each game respectivily  
        if(choice == 'A' or choice == 'a'):
            obj = MasterMind2(4,12,2)
            obj.ply()
            
        elif(choice == 'B' or choice =='b'):
            obj=MasterMind1(4,12,1)
            obj.ply()
        elif(choice == 'C' or choice =='c'):
            obj= MasterMind4Player(4,8,4)
            obj.ply()
        elif(choice == 'D' or choice =='d'):
            # super(mastermind4playerComputer,self).__init__(3,7)
            obj=MasterMind4PlayerComputer(4,10,4)
            obj.ply()

        elif(choice == 'E' or choice =='e'):
            sys.exit("Good Bye")
        else:
            print("Invalid input!")





# The Main function
if __name__ == '__main__':
    
    while True:
        my_game= Mastermind()
       
    

    