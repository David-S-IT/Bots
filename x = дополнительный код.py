a = int(input("Число: "))
if a == -128:
    print(10000000, end='')
    input()
    quit()
if a >= 0:
    print("{:08d}".format(int(bin(a)[2:])), end='')
    input()
    quit()
a = abs(a)
a = "1" + str("{:07d}".format(int(bin(a)[2:])))
an = '1'
for i in a[1:]:
    if i == '1':
        an += '0'
    if i == '0':
        an += '1'
print(bin(int(an, 2)+1)[2:], end='')
input()