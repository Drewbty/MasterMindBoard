from menu import mastermind
from game import game

class Mastermind():
    def ComputeChoices(self):
        obj = mastermind()

        choice = obj.play()
        #initializing various games depending on which one tha player wants to play
        # with their respective players
        obj.clr()
        if(choice == 'A' or choice == 'a'):
            gameobj = game(4,12)
            gameobj.mastermind2()
        elif(choice == 'B' or choice =='b'):
            gameobj = game(4,12)
            gameobj.mastermind1()
        elif(choice == 'C' or choice =='c'):
           gameobj = game(4,12)
           gameobj.mastermind4player()
        elif(choice == 'D' or choice =='d'):
            gameobj = game(4,12)
            gameobj.mastermind4playerComputer()
        elif(choice == 'E' or choice =='e'):
            sys.exit("Good Bye")
        else:
            print("Invalid input!")





# The Main function
if __name__ == '__main__':
    
    while True:
        my_game= Mastermind()
        my_game.ComputeChoices()

    

    