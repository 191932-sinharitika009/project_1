import random

def game_win(comp, your):
    if comp == your:              #if two values are same, declare a tie!
        return None

    if comp == 's':
        if your == 'w':
            return False
        elif your == 'g':
            return True

    elif comp == 'w':
        if your == 'g':
            return False
        elif your == 's':
            return True

    elif comp == 'g':
        if your == 's':
            return False
        elif your == 'w':
            return True

print("computer's turn:snake(s), water(w) or gun(g)?")
rand_no=random.randint(1,3)
if rand_no==1:
    comp='s'
elif rand_no==2:
    comp='w'
elif rand_no==3:
    comp='g'

your= input("Your turn:snake(s), water(w) or gun(g)?")
a = game_win(comp, your)

print(f"computer choose {comp}")
print(f"You choose {your}")

if a == None:
    print("the game is a tie!!")
elif a:
    print("you win!!")
else:
    print("you loose!")