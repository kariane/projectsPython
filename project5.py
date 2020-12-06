import string

case = None
try:
    case = int(input('cases: '))
except ValueError:
    print('Invalid')
if case:
    for _ in range(case):
        print('--------------------')
        ms = input('Message: ')

        try:
            p = int(input('Positions: '))
        except ValueError:
            print('Invalid')
            break
        b = list(string.ascii_uppercase)
        ce = []
        for c in ms:
            idx = b.index(c.upper())
            n_idx = idx - p if idx - p >= 0 else len(b) + idx - p
            ce.append(b[n_idx])
        print('Deciphered: {}'.format(''.join(ce)))
    print('--------------------')