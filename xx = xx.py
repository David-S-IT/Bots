x = input('Уравнение: (Число) ')
print(x + 'x = ', end='')
a, CC = map(str, input().split())
CC = int(CC)
if len(x) == 2:
    print(x, abs((int(x[1]) - int(a, CC)) // int(x[0])), '=', a, CC)
elif len(x) == 3:
    import math

    aa = int(a, CC)
    a, b, c = int(x[0]), int(x[1]), int(x[2]) - int(aa)
    if b ** 2 - 4 * a * c > 0:
        print(x, int(abs((int('-' + str(b)) + math.sqrt(b ** 2 - 4 * a * c)) // (2*a))), '=', aa, CC)
    else:
        print(b // 2 * a, 'это может быть не правильно!!')
input()
