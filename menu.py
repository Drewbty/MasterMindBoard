class Menu( ):
    
    returnchoice=""

    def __init__(self):
        print("*********************************************************")

        
        print("\n\n\n\nSelect which game you want to play:")
        print("(A)  Mastermind for 2 players")
        print("(B)  Mastermind for 1 player with Computer Support")
        print("(C)  Mastermind44 for 4 players")
        print("(D)  Mastermind44 for 4 players  with Computer Support")
        print("(E) to Exit")
        print("*********************************************************")

        choice = input("\n\n****Enter A, B, C, D or E **** >")

        self.returnchoice= choice


   

