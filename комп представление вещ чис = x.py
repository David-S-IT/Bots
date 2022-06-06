x = input("Машинное представление вещественного числа ")
poriadok = int(x[1:6], 2)-15
print('НФЗ:  -1,', x[6:], ' * 2^', poriadok, sep='') if x[0] == '1' else print('НФЗ:  1,', x[6:], ' * 2^', poriadok, sep='')
nfz = '1.' + x[6:].replace('0', '')
ch = float('1.' + str(x[6:]))
if poriadok > 0:
    for i in range(poriadok):
        ch *= 10
else:
    for i in range(abs(poriadok)):
        ch /= 10
        print(ch)
print('10СС: -', int(str(int(ch)), 2), ",", sep='', end='') if x[0] == '1' else print('10СС: ', int(str(int(ch)), 2), ",", sep='', end='')
sum = 0
j = 0
for i in str(ch)[1+len(str(int(ch))):]:
    j += 1
    i = int(i)
    sum += i*(2**-j)
print(str(sum)[2:].replace('0', ''), end='')
input()