kod = list(map(int, input("Числа ").split(", ")))
for i in range(len(kod)):
    kod[i] = bin(kod[i])[2:]
for i in kod:
    print("0" * (len(i) - 1), i, sep='', end='')
input()
