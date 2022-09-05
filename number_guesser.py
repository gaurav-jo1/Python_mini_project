import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("PLease type a number larger than 0 next time.")
        quit()
else:
    print("PLease type a number next time.")
    quit()


random_number = random.randrange(top_of_range)
gusses = 0

while True:
    gusses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("PLease type a number larger than 0 next time.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    else:
        if user_guess == random_number:
            print("You got the number")
            break
        elif user_guess > random_number:
            print("You are above the number!")
        else:
            print("You are below the number!")


print(f"You got it in ,{gusses} gusses")