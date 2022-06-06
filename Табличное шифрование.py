task = input("Шифр: ")
key = input("Ключ: ")
if len(task) % len(key) != 0:
    line, stolbik = int(input("Линий: ")), int(input("Столбцов: "))
else:
    line = len(task) // len(key)
    stolbik = len(task) // line

tablichka = ['' for i in range(len(key))]

zn_perehod, kol_vo, done_perehod = 1, 1, 0

# miny_stolbik = []
# miny_line = []
# max_kol_vo_min = int(input("Количество мин: "))
# for i in range(max_kol_vo_min):
#     if i == 0:
#         print("x, y, отсчет с нуля:")
#     x, y = map(int, input(f'Мина {i + 1}: ').split())
#     miny_stolbik.append(y)
#     miny_line.append(x)
# print(miny_stolbik, miny_line)


def do_tablichka_for_people(line):
    global task, key, tablichka, miny_stolbik, miny_line, max_kol_vo_min
    kol_vo_min = 0
    task_i = 0
    for i in range(len(key)):
        stolbik = key.find(str(i + 1))
        for j in range(line):
            # if kol_vo_min != max_kol_vo_min:
            #     if miny_stolbik[kol_vo_min] == i and miny_line[kol_vo_min] == j:
            #         kol_vo_min += 1
            #         tablichka[stolbik] += "ъ"
            #         print(23323422343)
            #         continue

            tablichka[stolbik] += task[task_i]
            task_i += 1
    # print(task_i)

do_tablichka_for_people(line)
for i in range(line):
    for j in range(stolbik):
        # print(i, j)
        print(tablichka[j][i], end='')
    #print(end=" ")
# print(*tablichka, sep='\n')

input()




# 00010111001010111101011100100110
# 214365
# 6
# 6
# 4
# 0 0
# 0 5
# 5 0
# 5 5