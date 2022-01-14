# import random library
import random
#Get the input from the user choice
userChoice=input("Enter your choice{rock,paper,scissors}:")
#Make the list of possible choices
possibleChoices=["rock","paper","scissors"]
#Get the computer choice using random.choice
compChoice=random.choice(possibleChoices)
#print the choices
print("You have chosen:{} and Computer have chosen:{}" .format(userChoice,compChoice))

if userChoice==compChoice:
    print("its a tie")
elif userChoice=="rock":
    if compChoice=="paper":
        print("paper covered the rock, YOU LOST...!")
    else:
        print("rock smashed the scissors,YOU WON...!")
elif userChoice=="paper":
    if compChoice=="scissors":
        print("scissors cut the paper, YOU LOST...!" )
    else:
        print("paper covered the rock, YOU WON") 
elif userChoice=="scissors":
    if compChoice=="rock":
        print("rock smashed the scissors,YOU LOST")
    else:  
        print("scissors cut the paper, YOU WON")
