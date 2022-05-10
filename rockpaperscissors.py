import random
computer_wins = 0
user_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    
    user_pick = input("choose rock, paper or scissors or q to quit the game: ")
    if user_pick == "q":
        print("Goodbye")
        break
    if user_pick not in options:
        continue
    random_no = random.randint(0,2)
    comp_pick = options[random_no]
    print("computer has picked: "+ comp_pick)
    
    if user_pick == "paper" and comp_pick == "rock":
        print("you win\n")
        user_wins += 1
        
    elif user_pick == "scissors" and comp_pick == "paper":
        print("you win\n")
        user_wins += 1
    elif user_pick == "rock" and comp_pick == "scissors":
        print("you win\n")
        user_wins += 1
        
    
    elif user_pick == comp_pick:
        print("it's a draw\n")
    else:
        print("computer wins\n")
        computer_wins += 1

    print("your total score is: " + str(user_wins) + " points\n")
    print("computer score is: " + str(computer_wins) + " points\n")
    

    