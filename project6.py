
from random import randint
rand= randint(0,100)
print('guessing game')
rep = False
guess=0
while not rep:
    x=int(input("enter a random number between 0 and 100: "))
    guess+=1
    if x==rand:
        rep = True
    else:
        print("the numbers are not equal")
        if x<rand:
            print('The number entered is smaller')
        elif x>rand:
            print('The number entered is higher')
print("Amazing!!\nwith {} attempts you won".format(guess))