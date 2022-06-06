a, l = map(int,input("Числа от и до: ").split())
do, p, u = 0, 0, 0
while a < l:
    if (l % 2 == 0) and (l // 2 > a):
        l //= 2
        print('*')
        u += 1
    else:
        l -= 1
        print('+')
        p += 1
    do += 1
    print(do)
print("+{}, *{}, всего {}".format(p, u, do))
#print(l)