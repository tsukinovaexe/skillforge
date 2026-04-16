import random

# score
player_score = 0
computer_score = 0

while True:
    player = input("Choose rock, paper, or scissors (or type quit): ").lower()

    # stop the game
    if player == "quit":
        print("Game ended.")
        break

    # Check invalid input
    if player not in ["rock", "paper", "scissors"]:
        print("Invalid choice, try again.")
        continue

    # computer choice
    computer = random.choice(["rock", "paper", "scissors"])
    print("Computer chose:", computer)

    # winner logic
    if player == computer:
        print("It's a tie, damn!")

    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("GG, you win, congrats buddy!")
        player_score += 1

    else:
        print("HAHAHA, You lose!")
        computer_score += 1

    print("Score -> You:", player_score, "Computer:", computer_score)