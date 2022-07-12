
import random

def game_func(comp, player):
    
    if comp == player:
        return None

    elif comp == 's':
        if player == 'w':
            return False
        elif player == 'g':
            return True

    elif comp == 'w':
        if player == 'g':
            return False
        elif player == 's':
            return True

    elif comp == 'g':
        if player == 's':
            return False
        if player == 'w':
            return True

print("comp : Snake(s) Water(w) Gun(g) = ")
randnumber = random.randint(1, 3)
if randnumber == 1:
    comp = 's'
elif randnumber == 2:
    comp = 'w'
elif randnumber == 3:
    comp = 'g'

player = input("your turn : Snake(s) Water(w) Gun(g) = ")

game_win = game_func(comp, player)

print(f"computer choose {comp}")
print(f"you choose {player}")

if game_win == None:
    print("match tie!")
elif game_win:
    print("you win")
else:
    print("you loose!")
