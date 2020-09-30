from random import randint

def rand():
    return randint(1,10)
rep = True
while rep:
    x=input("enter a random number between 1 and 10: ")
    print("came out the number",rand())
    if x==rand():
        print("the numbers are equal")
    else:
        print("the numbers are not equal")
        break