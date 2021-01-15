# Initial variable to track game play
user_play = "y"
last_number = 0

# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    user_number = input("What is the number?")
    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for x in range(last_number,int(user_number)):
        print(x)
    
    last_number = int(user_number)

    # Once complete...
    user_play = input("Continue: (y)es or (n)o? ")

# Rather than just displaying numbers constantly starting at 0, have the numbers begin at the end of the previous chain.