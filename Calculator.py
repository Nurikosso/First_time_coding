current = None

while True:
    expr = input('enter your expresssion, example: 12 + 34: ')
    part = expr.split()

    if current is not None:
        expr = f'{current} {expr}'

    part = expr.split()

    if len(part) != 3:
        print('Error: Wrong opertaion')
        continue

    a = float(part[0])
    b = part[1]
    c = float(part[2])

    if b == '+':
        res = a + c
    elif b == '-':
        res = a - c
    elif b == '*':
        res = a * c
    elif b == '/':
        if c != 0:
            res = a / c
        else:
            print('You cannot devide by ZERO')
    else:
        print('Invalid operation, choose: "+", "-", "*" or "/"')

    print(res)

    current = res

    cont = input('Countinue? yes/no: ').strip().lower()
    if cont != 'yes':
        12
        break
