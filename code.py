import random
from collections import Counter
import getpass
import os
import sys
from compare import compare_code

#(R)ed, (B)lue, (G)reen, (Y)ellow, (M)agenta, or (C)yan.

#This list holds all the available colours
colours = ['R', 'B', 'G', 'Y', 'M', 'C'] 




class code:
    
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
        colour_code = []
        position_code = []
        self.l = l
        # 2 player version
        temp1 = getpass.getpass('Enter your combination:')
        temp2 = getpass.getpass('Enter your combination again:')
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

    
    def compute(self,player_1,i,trylength,cur,max,solution_code,peglen):
        print("Attempt #", i, ":")
        guess = input(player_1+">Enter the Code to Crack:  ")
        guess= "".join(guess.split()) 
        guess= guess.upper()
        code1=code()
        if guess.find(' ') != -1:

            print("invalid format: Expected Format is 'RGBY'")
        else:


            if (len(guess) == peglen ):
                if code1.check_code(guess):
                        
                    compareobj = compare_code(guess, solution_code)
                    feedback=compareobj.feedbackReturn

                    #when matched the game automatically switches to the main menu
                    if(feedback == "Match"):
                        os.system("clear")
                        print("Congratulations! ",player_1," You broke the code in", i, "attempts!")
                        return 'discontinue'
                    
                    else:
                        print("Feedback on attempt #", i, ":", feedback)
                # in case of an invalid input
                else:
                    print("INVALId! Expecte inputs (R)ed, (B)lue, (G)reen, (Y)ellow, (M)agenta, or (C)yan.")
            else:
                print("length doesnt match. EXPECTED LENGTH IS ",peglen)

            if i==trylength:
                os.system("clear")
                print(player_1," You have failed to Break The Code")
            if max==cur and i==trylength:
                    print("You have failed to Break The Code: \n Correct Code was : " + solution_code )
            return 'continue'



