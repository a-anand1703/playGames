import random

def game(comp,you):
    if(comp==you):
        return None
    if(comp=='r'):
        if(you=='p'):
            return True
        elif(you=='s'):
            return False
    if(comp=='p'):
        if(you=='s'):
            return True
        elif(you=='r'):
            return False
    if(comp=='s'):
        if(you=='r'):
            return True
        elif(you=='p'):
            return False
print('comp\'s turn: rock(r) paper(p) scissor(s)')
random=random.randint(1,3)
if(random==1):
    comp='r'
elif(random==2):
    comp='p'
elif(random==3):
    comp='s'
you=input('yours\'s turn: rock(r) paper(p) scissor(s)\n')
points=0
a=game(comp,you)
if a==None:
    print('Tie')
elif a==True:
    print('You Won')
    points+=1
else:
    print('You Lose')
print(f'You chose {you}')
print(f'Comp chose {comp}')
print(f'Your points: {points}')