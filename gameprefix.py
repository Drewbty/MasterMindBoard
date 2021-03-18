import random
from collections import Counter
import sys
from compare import compare_code

#(R)ed, (B)lue, (G)reen, (Y)ellow, (M)agenta, or (C)yan.

#This list holds all the available colours
colours = ['R', 'B', 'G', 'Y', 'M', 'C'] 




class GamePrefix:

    def __init__(self):
        pass
    
    # to generate code in the single player game
    def code_generator(self, pegs):
        i = 0
        gen_code = ""
        # code generating algorithm using random
        while i < pegs:
            colour = random.randint(0, 5)
            gen_code += colours[colour]
            i = i+1
        return gen_code

    
    # to get the code from the player according to the kind of game
    def get_code(self, l):

        self.l = l
        # 2 player version
        temp1 = input('Enter your combination:')
        temp2 = input('Enter your combination again:')
        temp1="".join(temp1.split()) 
        temp1= temp1.upper()


        temp2= "".join(temp2.split()) 
        temp2= temp2.upper()
        
        #check length
        if(len(temp1) == self.l):
            if(temp1 == temp2):
                #check if th e input is subset of orignal colors
                if self.check_code(temp1)==1:
                    solution_code = temp1
                    print("sdfsdfsdf     " + solution_code)
                    return(solution_code)
                else:
                    print("Invalid! Expecte inputs (R)ed, (B)lue, (G)reen, (Y)ellow, (M)agenta, or (C)yan")
                    self.get_code(l)
            else:
                print("The code doesn't match the one previously entered.\n Please enter the same code twice!")
                self.get_code(l)
                
        else:
            print("The code entered isn't long enough. Enter again!")
            
            self.get_code(l)
        
            
 

    def check_code(self, code):

        flag = 0
        if(set(code).issubset(set(colours))): 
            flag = 1
        return flag

    
    def compute(self,player_1,i,trylength,cur,max,solution_code,peglen,creator):
        print("Attempt #", i, ":")
        guess = input(player_1+">Enter the Code to Crack:  ")
        guess= "".join(guess.split()) 
        guess= guess.upper()
        if guess.find(' ') != -1:

            print("invalid format: Expected Format is 'RGBY'")
        else:


            if (len(guess) == peglen ):
                if self.check_code(guess):
                        
                    compareobj = compare_code(guess, solution_code)
                    feedback=compareobj.feedbackReturn

                    #when matched the game automatically switches to the main menu
                    if(feedback == "Match"):
                        print("Congratulations! ",player_1," You broke the code in", i, "attempts!\n ",player_1," has won this original matermind game! \n Better luck next time ",creator,"!")
                        return 'discontinue'
                    
                    else:
                        print("Feedback #", i, ":", feedback)
                # in case of an invalid input
                else:
                    print("INVALId! Expecte inputs (R)ed, (B)lue, (G)reen, (Y)ellow, (M)agenta, or (C)yan.")
            else:
                print("length doesnt match. EXPECTED LENGTH IS ",peglen)

            if i==trylength:
                print(player_1," You have failed to Break The Code")
            if max==cur:
                    print("You have failed to Break The Code: \n Correct Code was : " + solution_code )
            return 'continue'



