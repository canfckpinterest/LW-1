a, b, c = map(float, input().split())

if a != 0:                        # является ли уравнение квадратным
    if c != 0 and b != 0:          # для полного квадартного уравнения
        d = b ** 2 - 4 * a * c
        if d < 0:
            print('Корней нет')
        elif d == 0:
            print(f'x = {-b / (2 * a)}')
        else:
            print(f'x1 = {(-b + d ** 0.5) / (2 * a)}')
            print(f'x2 = {(-b - d ** 0.5) / (2 * a)}')
    else:                                                # для неполного квадратного уравнения, т.е. вида
        if c == 0 and b == 0:                            # a * x^2 + 0 * x + 0 = 0
            print('x = 0')
        elif c == 0:                                     # a * x^2 + b*x + 0 = 0
           print(f'x1 = 0')
           print(f'x2 = {-b / a}')
        else:                                            # a * x^2 + 0 * x + c = 0
            x2 = -c / a
            if x2 < 0:
                print('Корней нет')
            else:
                print(f'x1 = {x2 ** 0.5}')
                print(f'x2 = {-1 * (x2 ** 0.5)}')
else:
    print('Уравнение не квадратное')