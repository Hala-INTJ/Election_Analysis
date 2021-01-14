# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")
print(f"Computer chose {computer_choice}")

# Run Conditionals
if user_choice == computer_choice:
    print("It's a Tie!")
elif user_choice == "r" and computer_choice == "p":
    print("You Lose!") 
elif user_choice == "r" and computer_choice == "s":
    print("You Win!") 
elif user_choice == "p" and computer_choice == "r":
    print("You Win!") 
elif user_choice == "p" and computer_choice == "s":
    print("You Lose!") 
elif user_choice == "s" and computer_choice == "p":
    print("You Win!") 
elif user_choice == "s" and computer_choice == "r":
    print("You Lose!")     