import datetime
import site
from playsound import playsound
from random import randint

print("\n \n-----------------------------")
print("|        SET REMINDER          |")
print("-----------------------------")

print("\n \n-----------------------------")

ahour = int(input("ENTER HOUR:"))
amin = int(input("ENTER MINUTES:"))
am_pm = input("AM/PM :")
print("-----------------------------")

if am_pm == "pm" or "am" or "PM" or "AM":
    if am_pm == "pm":
        ahour+=12
    else:
        ahour=ahour

while True:
    if ahour == datetime.datetime.now().hour and amin == datetime.datetime.now().minute:
        print('\n \nits your game time so go on!!!!!!!!!!!!!!!')
        playsound('alram1.wav')
        break
print("\n \n----------------------------------------")
print("| YOU ARE PLAYING ROCK,PAPER,SCISSORS. |")
print("----------------------------------------")

print("\n \n----------------------------------------")

print("1.Play      2.Exit  ")
x = int(input("Enter your choice: "))
print("----------------------------------------")


moves = ["rock", "paper", "scissors"]

cmove = moves[randint(0, 2)]

win = 0
lose = 0


if x == 2:
    {
        exit()
    }
pmove = False
while pmove == False:
    print("\n\n----------------------------------------")
    print("\nChoose between Rock,Paper & Scissors.")
    pmove = input("\nPLYAER MOVE: ")
    if pmove == cmove:
        print("COMPUTER MOVE: ", cmove)
        win =win
        lose =lose
        print("Tie!")
        print("Win: ",win,"Lose:",lose)
        print("----------------------------------------")
    elif pmove == "rock":
        if cmove == "Paper":

            print("COMPUTER MOVE: ", cmove)
            win=win
            lose+=1
            print("You lose!")
            print("Win: ", win, "Lose:",lose)
            print("----------------------------------------")

        else:
            print("COMPUTER MOVE: ", cmove)
            print("You win!")
            win+=1
            lose=lose
            print("Win: ", win, "Lose:",lose)
            print("----------------------------------------")
    elif pmove ==  "paper":
        if cmove == "Scissors":
            print("COMPUTER MOVE: ", cmove)
            print("You lose!")
            win=win
            lose+=1
            print("Win: ", win, "Lose:",lose)
            print("----------------------------------------")

        else:
            print("COMPUTER MOVE: ", cmove)
            print("You win!")
            win+=1
            lose=lose
            print("Win: ", win, "Lose:",lose)
            print("----------------------------------------")

    elif pmove == "scissors":
        if cmove == "rock":
            print("COMPUTER MOVE: ", cmove)
            print("You lose!")
            win=win
            lose+=1
            print("Win: ", win, "Lose:",lose)
            print("----------------------------------------")

        else:
            print("COMPUTER MOVE: ", cmove)
            print("You win!")
            win+=1
            lose=lose
            print("Win: ", win, "Lose:",lose)
            print("----------------------------------------")
    else:
        print("-----------------------------------------------")
        print("That's not a valid play. Check your spelling!!!")
        print("-----------------------------------------------")


    print("\n \n----------------------------------------")

    print("Please select option from below.")
    print("1.play     2.exit ")
    x = int(input("Enter your choice:"))
    print("----------------------------------------")
    if x == 2:
        break
    else:
        pmove = False
        cmove = moves[randint(0, 2)]