    
import random
from collections import Counter
import getpass
import sys

class compare_code:

    # To compare the guess made by a player and the solution code 
    # and returning the number of blacks and whites accordingly
    feedbackReturn='jj'
    def __init__(self, code, guess):
        if guess == code:
            self.feedbackReturn= "Match"
        else:
            blacks_count = 0
            whites_count = 0
            self_not_black = []
            other_not_black = []

            #matching and finding the correct positions and colour
            try:
                    
                for i, peg in enumerate(code):
                    try:
                        if peg == guess[i]:
                            blacks_count += 1
                        else:
                            self_not_black.append(peg)
                            other_not_black.append(guess[i])
                    except:
                        self_not_black.append(peg)
                        other_not_black.append(guess[i])



                self_not_black_counter = Counter(self_not_black)
                other_not_black_counter = Counter(other_not_black)

                for color, count in self_not_black_counter.items():
                    whites_count += min(count, other_not_black_counter[color])

                # making the list of blacks and whites    
                out = []
                while blacks_count>0:
                    out.append('B')
                    blacks_count -=1
                while whites_count>0:
                    out.append('W')
                    whites_count -=1
                if(len(out) >= 1):
                    self.feedbackReturn=out
                else:
                    self.feedbackReturn="Nothing"
            except:
                self.feedbackReturn ='Nothingg'
        

        
# to get the players
class Player:
    '''Contains the player info'''
    
    Playerlist = [None]*4
    def __init__(self, n):
        for index in range(n):
            temp = index+1
            Player.Playerlist[index]= input("Player " +temp+": What is your name?  >")

