numd=int(input('Enter any number to see your tablet: '))
for x in range(1,numd+1):
    for base in range(1, 11):
        r=base*x
        print(f"{x} x {base}  = {r}")
    print('=====================')