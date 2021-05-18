import random
rNumber = random.randint(1,9)

Lives = 5

if Lives == 5:
    print("Welcome to THE GUESSING GAME")
    print("Rules are very simple:-")
    print("Guess the no. and you win")

Guess = int(input("Guess the no. from 1 to 9 "))



if Guess == rNumber:
    print("Congratulations!! You have won!! :)")
elif Guess != rNumber:
    while Lives > 0:
        Lives = Lives - 1
        print("Oh NO!! Your guess was wrong")
        print("You have ",Lives," chances remaining")

        if Lives== 0:
            print("Oh!! No!! You have lost the Game :(")
            print("You can try again if you like")
            break

        Guess = int(input("Guess the no. from 1 to 9 "))


        if Guess == rNumber:
            print("Congratulations!! You have won!! :)")
            break


       


        


