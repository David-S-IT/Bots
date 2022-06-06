a, b = map(int, input("НОК, введите 2 числа: ").split())
c = a*b
while b != 0:
    a, b = b, a % b
print(c // a)
input()




#int c = a*b;
#while (b != 0) {
#    int tempa = a;
#    a = b;
#    b = tempa % b;
#}
#return c / a;