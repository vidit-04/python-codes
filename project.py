import random

choices = ["rock","paper","scissors"]


player=None

while True:
    player=input("rock,paper,or scissors?: ")
    computer=random.choice(choices)

    if player==computer:
        print('computer: ',computer)
        print("player: ",player)
        print("tie")
    elif player=="rock":
        if computer=="paper":
            print('computer: ',computer)
            print("player: ",player)
            print("you lose")
        if computer=="scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("You win")

    elif player=="paper":
        if computer=="scissors":
            print('computer: ',computer)
            print("player: ",player)
            print("you lose")
        if computer=="rock":
            print("computer: ",computer)
            print("player: ",player)
            print("You win")

    elif player=="scissors":
        if computer=="rock":
            print('computer: ',computer)
            print("player: ",player)
            print("you lose")
        if computer=="paper":
            print("computer: ",computer)
            print("player: ",player)
            print("You win")
    elif player=="exit":
        break
    else:
        print('invalid')

