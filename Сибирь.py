# учитывай пробелы
shifr = []
tablichka = []


def do_tablichka_for_people():
    global tablichka, line, zn_perehod, kol_vo, done_perehod, line, stolbik
    for i in range(1, n + 1):
        if len(tablichka) <= line:
            tablichka.append(str(i) + " ")
            perehod()
            continue
        tablichka[line] += str(i) + " "
        perehod()
    print(*tablichka, sep='\n')
    zn_perehod, kol_vo, done_perehod = 1, 1, 0
    line, stolbik = 0, 0


def do_tablichka_ready():
    global tablichka, line, zn_perehod, kol_vo, done_perehod, line, stolbik
    for i in range(1, n + 1):
        if len(tablichka) <= line:
            tablichka.append('1')
            perehod()
            continue
        tablichka[line] += '1'
        perehod()

    zn_perehod, kol_vo, done_perehod = 1, 1, 0
    line, stolbik = 0, 0

    global repair_task, shifr
    repair_task_i = 0
    for i in range(len(tablichka)):
        shifr.append('')
        for j in range(len(tablichka[i])):
            shifr[i] += repair_task[repair_task_i]
            repair_task_i += 1


task = input("Шифр: ")
repair_task = ''
n = -1
for i in task:
    n += 1
    if n % 4 == 0 and n:
        n = -1
        continue
    repair_task += i
#repair_task = task

n = len(repair_task)
# print(repair_task, n)
# input()  # Подтвердите (Enter)


def up():
    global line
    line -= 1


def down():
    global line
    line += 1


def right():
    global stolbik
    stolbik += 1


def left():
    global stolbik
    stolbik -= 1


zn_perehod, kol_vo, done_perehod = 1, 1, 0
line, stolbik = 0, 0


def perehod():
    global zn_perehod, kol_vo, done_perehod, line, stolbik
    if zn_perehod == 1:
        right()
        zn_perehod += 1

    elif zn_perehod == 2:
        down()
        left()
        done_perehod += 1
        if done_perehod == kol_vo:
            done_perehod = 0
            kol_vo += 1
            zn_perehod += 1

    elif zn_perehod == 3:
        down()
        zn_perehod += 1

    elif zn_perehod == 4:
        up()
        right()
        done_perehod += 1
        if done_perehod == kol_vo:
            done_perehod = 0
            kol_vo += 1
            zn_perehod = 1


#do_tablichka_for_people()
#input()
do_tablichka_ready()


for i in range(n):
    # print(tablichka[0][0])
    print(shifr[line][stolbik], end="")
    perehod()

input()
