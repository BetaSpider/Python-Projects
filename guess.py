import random
import math
Name=input("Enter your name:")
print("Hello",Name)
upperlimit=int(input("Enter the upper limit:"))
lowerlimit=int(input("Enter the lower limit:"))
random_no=random.randint(lowerlimit,upperlimit)
print("\n u have only",round(math.log(upperlimit-lowerlimit+1,2))," chances to guess the no which the machine has generated");
count=0
while count<math.log(upperlimit-lowerlimit+1,2):
    count=count+1
    user_guess=int(input("\n \t Guess the number:"))
    if random_no==user_guess:
        print("Welldone!, You have guessed in", count, "try itself")
        break
    if random_no>user_guess:
        print("You haved guessed too low, Try again")

    if random_no<user_guess:
        print("You haved guessed too high, try again")

if count>math.log(upperlimit-lowerlimit+1,2):
        print("\n \t limit exceeded, Better luck next time")
        print("\n\n\t The no is ", random_no)
