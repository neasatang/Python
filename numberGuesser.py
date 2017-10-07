import random

while True:
    print("Welcome to Guessing the number!")
    try:
        answer = int(input ("The number is between 1 - 10. What do you think the number is?"))

    except ValueError:
        print("Sorry but you must enter an integer to play!")

    else:
        break

random = random.randint(1, 10)
print(random)
playing = True;
while playing:
    print("You think the number is " + str(answer))
    if int(answer) > random:
        answer = input("The number is lower than you think. Guess again!")
    elif int(answer) < random:
        answer = input("The number is higher than you think. Guess again!")
    else:
        playing = input( "You got it correct! The number was " + str(answer) + ". Would you like you play again? Type 'y/n'") == 'y' or 'Y'
        if playing == 'n' or 'N':
            playing = False
            print("Thank you for playing!")
