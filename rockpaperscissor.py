import random
option = ("rock","paper","scissor")
player = None
computer = random.choice(option)
running = True
while running:
    while player not in option:
        player = input("Enter choice (rock, paper, scissor) : ")
    print(f"player:{player}")
    print(f"computer:{computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissor":
        print ("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissor" and computer == "paper":
        print ("You win!")
    else:
        print("You Loss!")
    if not input("play again? (y/n): ").lower() == "y":
        running = False
print("Thanks for playing!")