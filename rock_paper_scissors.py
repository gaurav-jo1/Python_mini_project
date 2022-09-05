import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Choose Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print(f"Computer picked {computer_pick}.")

    if user_input == "rock" and computer_pick == "scissors":
        user_wins += 1
        print("You Won!")
        continue
    elif user_input == "scissors" and computer_pick == "paper":
        user_wins += 1
        print("You Won!")
        continue
    elif user_input == "paper" and computer_pick == "rock":
        user_wins += 1
        print("You Won!")
        continue
    elif user_input == computer_pick:
        print("It's a tie!")
        continue
    else:
        computer_wins += 1
        print("You Lost!")


print(f"You won {user_wins} times.")
print(f"Computer won {computer_wins} times.")
print("Goodbye!")
