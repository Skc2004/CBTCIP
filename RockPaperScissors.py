import random

def choice():
    print("Choose from the following:- \n")
    print("1. Rock\n")
    print("2. Paper\n")
    print("3. Scissors\n")
    guess  = int(input("Enter choice: "))
    choice1=[1,2,3]
    if guess in choice1:
        return guess
    else:
        print("Invalid choice!!!")
        choice()
    
def computer():
    print("Computer Choosing...........\n\n")
    comp = random.randint(1, 3)
    print("Computer Choice: ",comp,"\n")
    return comp

def RockPaperScissors():
    print("WELCOME TO THE ROCK PAPER SCISSORS GAME!!!\n")
    ch=choice();
    comp=computer();
    
    if((ch==1 and comp==2) or (ch==2 and comp==1) or (ch==3 and comp==2) or (ch==1 and comp==3)):
        print("You Win!!!")
    elif(ch==comp):
        print("It is a Tie")
    else:
        print("Computer Win!!!") 
        
if __name__ == "__main__":
    RockPaperScissors()