a = input("Число: ")
if a == '10000000':
    print(-128, end='')
    input()
    quit()
if a[:1] == '0':
    print(int(str(a), 2), end='')
    input()
    quit()
a = str("{:07d}".format(int(bin(int(a, 2)-1)[2:])))
an = '1'
for i in a[1:]:
    if i == '1':
        an += '0'
    if i == '0':
        an += '1'
print(int(an[1:], 2) * -1, end='')
input()