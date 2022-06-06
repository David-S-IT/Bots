l, a = map(int,input("Числа до и от: ").split())
answer = l
do = 0
if answer == 0 or l <= a:
    print("Ты чё, куку??")
while answer > a:
    do += 1
    if (answer % 2 == 0):
        answer //= 2
    else:
        answer -= 1
    if answer < a:
        print("ERROR")
        print("Решай сам!")
        
#    if answer <= a:
 #       print("Действий:", do)
print("Действий:", do)