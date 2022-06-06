a = input("Что-то: ")
print(len(a))
if len(a) % 15 == 0:
    print(15)
if len(a) % 8 == 0:
    print(8)
elif len(a) % 4 == 0:
    print(4)

input()
