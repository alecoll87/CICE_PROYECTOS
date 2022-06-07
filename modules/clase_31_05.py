import random as rdm
from secrets import choice

choices = ["Piedra", "Papel", "Tijera"]
user = ""

rdm.choice(choices)


while user !="q":
    pc_choice = choices.index(rdm.choice(choices))
    for i, choice in enumerate (choices):
        print(f"{i+1}. {choice}")
    user = input(": ")
    if not user.isdigit():
        break
    else:
        user = int(user) - 1
        print("user: ", choices[user])
        print("pc: ", choices[pc_choice])
    if user != pc_choice:
        if user == len(choices) -1:
            user = -1
        if user +1 == pc_choice:
            print ("PC GANA")
        else:
            print("HAS GANADO")
    else:
        print("Empate!")

