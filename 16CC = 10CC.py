import pyautogui as pg
from time import sleep

a = input("Что ").split()
words = []
for i in a:
    print(int(i, 16), end=" ")       # 16CC в 10СС
    

input()

























#    if int(i, 2) + 848 < 1040:
#        words.append(f"\\{'u00'}{str(hex(int(i, 2)))[2:]}")
#    else:
#        words.append(f"\\{'u0'}{'{:0<3}'.format(str(hex(int(i, 2) + 848))[2:])}")

# print(*words)

#pg.hotkey("alt", "tab")
#pg.write('"')
#pg.write(words[0])
#pg.write('"')
#for i in words[1:]:
#    pg.write(' + "')
#    pg.write(i)
#    pg.write('"')
#pg.write('\n')