from random import randint

def rand():
    return randint(1,6)
    
rep = True
while rep:
    print("came out the value:",rand())
    print("would you like to roll the dice again?")
    rep = ("yes") in input().lower()
print("Game Over")