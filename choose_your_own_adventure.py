name = input("What is your name? ")
print(f"Welcome {name} to the adventure!")

answer = input("You are on a dirt road. Do you want to go left or right? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross. Do you wanna walk or swim?  ").lower()

    if answer == "swim":
        print("You swim accross the river and you are eaten by an alligator!")
    elif answer == "walk":
        print("You walked for miles , ran down a hill and you are eaten by a bear!")
    else:
        print("Not a valid option, You are lost!")
    
elif answer == "right":
    print("You come to a bridge, you can walk across it or jump over it. Do you wanna cross or back? ")
    if answer == "cross":
        print("You crossed the bridge and you are eaten by a shark!")
    elif answer == "back":
        print("You back up and you are eaten by a shark!")
    else:
        print("Not a valid option, You are lost!")
else:
    print("Not a valid option, You are lost!")


print(f"Thanks for playing! {name}")