a, b = map(int, input("НОД, введите 2 числа: ").split())
while b != 0:
    a, b = b, a % b
print(a)
input()






#while (b != 0) {
#    int tempa = a;
#    a = b;
#    b = tempa % b;
#}
#return a;
