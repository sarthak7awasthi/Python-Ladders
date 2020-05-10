#Sarthak Awasthi
#sa3655@drexel.edu
import random
import math
def random_chance():
#This function acts as a dice. This returns a random number from 1 to 6.
    for i in range(0,3):
        #To calculate the random number
        i = random.randint(1,6)
    return i
def newerPlace(current_place,i):
#This function calculates the new_place by adding the current_places with random number i we get from previous function.
    new_place=current_place+i
    return new_place

def listSTOPS(new_place):
#This function calculates the new_place if your current_place is 25. It calculates random number for index of list x and then gives an advantage or disadvantage accordingly. It also returns new_place after applying that function.
    x = ["Start from beginning.","Advance 2 places forward","New place is 40","Go back two places"]
    for i in range(0,3):
        #Using a for loop to increase randomness
        #random.randint() gives a random number(between the size of the list) which serves as an index for the list.
         s=random.randint(0,len(x)-1)
    if new_place==25:
        print()
        print("You are at a stop. Stops can be advantageous and sometimes...............")
        print()
        print("You will get one of these:", x)
        print()
        if s==0:
            new_place=0
            print("you will have to start from the beginning.")
            print()
        elif s==1:
            new_place=new_place+2
            print()
            print("You moved forward two places")
            print()
        elif s==2:
            print()
            print("You just got to place 40.")
            print()
            new_place=40
        else:
            new_place=new_place-2
            print()
            print("You have to go back two places.")
            print()
    return new_place
def ladders(current_place):
#This function checks whether there is a ladder at new_place.
    if current_place==4:
        #If there is a ladder, then it changes the value of new_place which means that player has advanced.
        new_place=12
        print()
        print("You found the ladder and moved up")
        print()
    elif current_place==11:
        new_place==23
        print()
        print("You found the ladder and moved up")
        print()
    elif current_place==19:
        new_place=31
        print()
        print("You found the ladder and moved up")
        print()
    elif current_place==17:
        new_place=21
        print()
        print("You found the ladder and moved up")
        print()
    elif current_place==29:
        new_place=41
        print()
        print("You found the ladder and moved up")
        print()
    else:
        new_place=current_place
    return new_place
def snakes(current_place):
#This function checks if there is no snake at current_place.
    if current_place==49:
        #If there is a snake at that place. The value of new_place is assigned as 'L' and you lose the game once a snake bites you.
        new_place='L'
        print()
        print("Snake bit you. You lose!!")
        print()
    elif current_place==9:
        new_place='L'
        print()
        print("Snake bit you. You lose!!")
        print()
    elif current_place==24:
        new_place='L'
        print()
        print("Snake bit you. You lose!!")
        print()
    else:
        new_place=current_place
    return new_place

def names():
#This function accepts a user input for name. 
    P1=input("enter your name: ")
    j=0
    while j<len(P1):
    #It checks whether there is any special character in the name.
        if P1[j]=='[' or P1[j]=='@' or P1[j]=='_' or P1[j]=='!' or P1[j]=='#' or P1[j]=='$' or P1[j]=='%' or P1[j]=='^' or P1[j]=='&' or P1[j]=='*' or P1[j]=='(' or P1[j]==')' or P1[j]=='<' or P1[j]=='>' or P1[j]=='?' or P1[j]=='/' or P1[j]=='\\' or P1[j]=='|' or P1[j]=='}' or P1[j]=='{' or P1[j]=='~' or P1[j]==':' or P1[j]==']':
            print("Name cannot contain special characters")
        #If there is a special character in the name then the function calls itself until a name is entered in an appropriate way.
            return names()
        else:
            print()
            print("Hello",P1, "Let's start the game")
            #If the name is entered properly then the loop ends.
            break
        #counter for the loop
        j+=1

    
        
if __name__ == "__main__":
    print("Welcome to the Python and Ladders")
    print()
    print("The ladders are at places: 4,11,19,17,29.")
    print()
    print("The snakes are at places: 9,24,49.")
    print()
    print("The stop is at place 25. It includes the following: [Start from beginning.,Advance 2 places forward,New place is 40,Go back two places]")
    print()
    names()
    current_places=0
    new_places=0
    print("Your current place is", current_places)
    #Loop to ensure game runs until the player wins or loses.
    while current_places<51 or new_places<51:
        
        print("Throw the dice? Y/N")
        j=input("Enter Y for yes: ")
        if j=='Y' or j=='y':
            #Loop to proceed the game until a player loses.
            while new_places!='L':
                i=random_chance()
                print("You got", i)
                new_places=newerPlace(current_places,i)
                new= ladders(new_places)
                new_places=new
                new_places=listSTOPS(new_places)
                new_places=snakes(new_places)
                if new_places=='L':
                #Ends the loop if the new_place is 'L' which means the player has lost.
                    break
                print("Your new place is", new_places)
                current_places=new_places
                break
        if new_places=='L':
            print()
            print("Game Ends")
            break
        if new_places>50:
            #If new_place is greater than 50 then the player wins.
            print()
            print("You won!!")
            #Terminates the loop if the player wins.
            break
            