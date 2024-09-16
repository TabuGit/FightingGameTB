import numpy as np
import random as rd
def Menu():
    print ('The Fighting Game \nSelect the configuration\ntype:\n1 - Human VS Human\n2 - Human VS Robot(random mode)\n3 - Human VS Robot(smart mode)')
    a = int(input())
    if a == 1:
        HvH()
    elif a == 2:
        HvR_rndm()
    elif a == 3:
        HvR_smrt()
    else:
        print('There is no such configuration !')
        Menu()
def Hit(x):
    if x == 1:
        return 1
    elif x == 2:
        return np.random.choice([1, 0], size=1, p=[0.9, 0.1])
    elif x == 3:
        return np.random.choice([1, 0], size=1, p=[0.7, 0.3])
    elif x == 4:
        return np.random.choice([1, 0], size=1, p=[0.6, 0.4])
    elif x == 5:
        return np.random.choice([1, 0], size=1, p=[0.4, 0.6])
    elif x == 6:
        return np.random.choice([1, 0], size=1, p=[0.3, 0.7])
    elif x == 7:
        return np.random.choice([1, 0], size=1, p=[0.25, 0.75])
    elif x == 8:
        return np.random.choice([1, 0], size=1, p=[0.20, 0.8])
    elif x == 9:
        return np.random.choice([1,0], size=1, p = [0.1, 0.9])
def HvH():
    print('Type your name player 1')
    name1 = input()
    print('Type your name player 2')
    name2 = input()
    names = [name1, name2]
    first = rd.choice(names)
    names.remove(first)
    second = names.pop()
    print('Game has started')
    a = 50
    b = 50
    firstturn = 0
    secondturn = 0
    while a or b > 0:
        print(f'{first} hp is {a}\n{second} hp is {b}\n {first}, make your move!')
        print('Choose the damage of the hit:\n 1--100%\n 2--90%\n 3--70%\n 4--60%\n 5--40%\n 6==30%\n 7--25%\n 8--20%\n 9--10%')
        x = int(input())
        while firstturn == 0:
            if Hit(x) == 1:
                b -= x 
                print(f'You managed to hit enemy for {x} damage!')
                secondturn = 0
                firstturn = 1
            elif Hit(x) == 0:
                print('You missed :(')
                secondturn = 0
                firstturn = 1
        if b > 0:
            print(f'{first} hp is {a}\n{second} hp is {b}\n {second}, make your move!')
            print('Choose the damage of the hit:\n 1--100%\n 2--90%\n 3--70%\n 4--60%\n 5--40%\n 6==30%\n 7--25%\n 8--20%\n 9--10%')
            x = int(input())
            while secondturn == 0:
                if Hit(x) == 1:
                    a -= x
                    print(f'You managed to hit enemy for {x} damage!')
                    firstturn = 0
                    secondturn = 1
                elif Hit(x) == 0:
                    print('You missed :(')
                    firstturn = 0
                    secondturn = 1
        elif b <= 0:
            print(f'{first} wins!')
            Menu()
        elif a <= 0:
            print(f'{second} wins!')
            Menu()

def HvR_rndm():
    print('Print your name!')
    player = input() 
    P_hp = 50
    R_hp = 50
    playerturn = 0
    robotturn = 0
    while R_hp or P_hp > 0:
        print(f'{player} hp is {P_hp}\n Robot hp is {R_hp}\n {player}, make your move!')
        print('Choose the damage of the hit:\n 1--100%\n 2--90%\n 3--70%\n 4--60%\n 5--40%\n 6==30%\n 7--25%\n 8--20%\n 9--10%')
        x = int(input())
        while playerturn == 0:
            if Hit(x) == 1:
                R_hp -= x 
                print(f'You managed to hit enemy for {x} damage!')
                robotturn = 0
                playerturn = 1
            elif Hit(x) == 0:
                print('You missed :(')
                robotturn = 0
                playerturn = 1
        if R_hp > 0:
            print(f'{player} hp is {P_hp}\n Robot hp is {R_hp}\n Robot makes his move')
            x = rd.randint(1,9)
            while robotturn == 0:
                if Hit(x) == 1:
                    P_hp -= x
                    print(f'Robot managed to hit you for {x} damage!')
                    playerturn = 0
                    robotturn = 1
                elif Hit(x) == 0:
                    print(f'Robot missed his {x} damage hit')
                    playerturn = 0
                    robotturn = 1
        elif R_hp <= 0:
            print(f'{player} wins!')
            Menu()
        if P_hp <= 0:
            print('Robot wins!')
            Menu()

def HvR_smrt():
    print('Print your name!')
    player = input() 
    P_hp = 50
    R_hp = 50 
    playerturn = 0
    robotturn = 0
    while R_hp or P_hp > 0:
       
        print(f'{player} hp is {P_hp}\n Robot hp is {R_hp}\n {player}, make your move!')
        print('Choose the damage of the hit:\n 1--100%\n 2--90%\n 3--70%\n 4--60%\n 5--40%\n 6==30%\n 7--25%\n 8--20%\n 9--10%')
        x = int(input())
        while playerturn == 0:
            if Hit(x) == 1:
                R_hp -= x 
                print(f'You managed to hit enemy for {x} damage!')
                robotturn = 0
                playerturn = 1
            elif Hit(x) == 0:
                print('You missed :(')
                robotturn = 0
                playerturn = 1
        if R_hp > 0:
            print(f'{player} hp is {P_hp}\n Robot hp is {R_hp}\n Robot makes his move')
            if P_hp == 2:
                x = 2
            elif P_hp == 1:
                x = 1
            elif P_hp >= 3:
                x = 3
            while robotturn == 0:
                if Hit(x) == 1:
                    P_hp -= x
                    print(f'Robot managed to hit you for {x} damage!')
                    playerturn = 0
                    robotturn = 1
                elif Hit(x) == 0:
                    print(f'Robot missed his {x} damage hit')
                    playerturn = 0
                    robotturn = 1
        elif R_hp <= 0:
            print(f'{player} wins!')
            Menu()
        if P_hp <= 0:
            print('Robot wins!')
            Menu()

Menu()