# Game 1 : Made by Me 

# print("Welcome to my computer quiz!")

# playing = (input("Do you wanna play the game? "))

# if playing.capitalize() == ("Yes"):
#     NameOfTheGame = input("Enter the name of the game you wanna play: ")
#     print(f"Opening {NameOfTheGame} .....")
# else:
#     print("Come sometime else bitch 😝")

# Game 2 :

print("Welcome to my computer quiz!")

playing = (input("Do you wanna play the game? "))

if playing.lower() != "yes":
    quit()

print("OKay! Let's play :)")
score = 0
incorrect = 0

answer = input("What does CPU stand for?: ")

if answer == "central processing unit":
    print("Correct !")
    score += 1
else:
    print("Wrong bitch 🤪")
    incorrect +=1

answer = input("What does GPU stand for?: ")

if answer == "graphics processing unit":
    print("Correct !")
    score += 1
else:
    print("Wrong bitch 🤪")
    incorrect +=1

answer = input("What does RAM stand for?: ")

if answer == "random access memory":
    print("Correct !")
    score += 1
else:
    print("Wrong bitch 🤪")
    incorrect +=1

answer = input("What does SSD stand for?: ")

if answer == "solid state drive":
    print("Correct !")
    score += 1
else:
    print("Wrong bitch 🤪")
    incorrect +=1

print(f"Your score is {score} out of {score + incorrect}")