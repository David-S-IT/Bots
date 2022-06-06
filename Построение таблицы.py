import pyautogui as pg
from time import sleep
kod = int(input("Сколько "))
pg.hotkey("alt", "tab")
#for i in range(len(kod)):
#    if kod[i] == "":
#        kod[i] = " "

#rus = "йцукенгшщзхъфывапролджэячсмитьбю?1234567890"
eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,.?1234567890"
up_rus = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ?1234567890"
up_eng = "QWERTYUIOP[]ASDFGHJKL;'ZXCVBNM,.1234567890"
zn_perehod, kol_vo, done_perehod = 1, 1, 0
was_space = 0


def perehod():
    global zn_perehod, done_perehod, kol_vo
    if zn_perehod == 1:
        pg.hotkey("right")
        zn_perehod += 1

    elif zn_perehod == 2:
        pg.hotkey("down")
        pg.hotkey("left")
        done_perehod += 1
        if done_perehod == kol_vo:
            done_perehod = 0
            kol_vo += 1
            zn_perehod += 1

    elif zn_perehod == 3:
        pg.hotkey("down")
        zn_perehod += 1

    elif zn_perehod == 4:
        pg.hotkey("up")
        pg.hotkey("right")
        done_perehod += 1
        if done_perehod == kol_vo:
            done_perehod = 0
            kol_vo += 1
            zn_perehod = 1


for i in range(1, kod+1):
    i = str(i)
    if was_space == 1:
        pg.write(" ")
        was_space = 0
        perehod()
    elif i == " ":
        was_space = 1
    else:
        if i.isupper():
            pg.write(i)
        else:
            pg.write(i)
        perehod()
kod.index()








































import pyautogui as pg
from time import sleep
kod = input("Код ")
pg.hotkey("alt", "tab")
for i in range(len(kod)):
    if kod[i] == "":
        kod[i] = " "

rus = "йцукенгшщзхъфывапролджэячсмитьбю?"
eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,.?"
up_rus = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ?"
up_eng = "QWERTYUIOP[]ASDFGHJKL;'ZXCVBNM,."
zn_perehod, kol_vo, done_perehod = 1, 1, 0
was_space = 0


def perehod():
    global zn_perehod, done_perehod, kol_vo
    if zn_perehod == 1:
        pg.hotkey("right")
        zn_perehod += 1

    elif zn_perehod == 2:
        pg.hotkey("down")
        pg.hotkey("left")
        done_perehod += 1
        if done_perehod == kol_vo:
            done_perehod = 0
            kol_vo += 1
            zn_perehod += 1

    elif zn_perehod == 3:
        pg.hotkey("down")
        zn_perehod += 1

    elif zn_perehod == 4:
        pg.hotkey("right")
        pg.hotkey("up")
        done_perehod += 1
        if done_perehod == kol_vo:
            done_perehod = 0
            kol_vo += 1
            zn_perehod = 1

def main():
    global kod, was_space, rus, eng, up_eng, up_rus
    for i in kod:
        if was_space == 1:
            pg.write(" ")
            was_space = 0
            perehod()
        elif i == " ":
            was_space = 1
        else:
            if i.isupper():
                pg.write(up_eng[up_rus.index(i)])
            else:
                pg.write(eng[rus.index(i)])
            perehod()
