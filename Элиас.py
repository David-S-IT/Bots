def razbivaiem(kod):
    kol_vo_0, razdelenie_1, text, new_kod = 0, False, "", []
    for i in kod:
        text += i
        if razdelenie_1:
            kol_vo_0 -= 1
            if not kol_vo_0:
                new_kod.append(int(text, 2))
                razdelenie_1, text = False, ""

        elif i == '1':
            if not kol_vo_0:
                new_kod.append(int(text, 2))
                text = ""
            else:
                razdelenie_1 = True

        else:
            kol_vo_0 += 1
    return new_kod


def chereduiem(kod):
    global bit
    new_kod = ""
    for i in kod:
        new_kod += str(bit) * int(i)
        bit = int(not bit)
    return new_kod


def delitel(sho, sk):
    text = ''
    for i in range(1, len(sho) + 1):
        if i % sk == 0:
            text += str(sho[i - sk:i] + " ")
    return text


def v_10_CC(kod):
    new_kod = []
    for i in kod:
        new_kod.append(int(i, 2))
    return new_kod


kod = input("Что: ").replace(" ", '')
bit = int(kod[0])
#print(*v_10_CC(delitel(chereduiem("121111253131125131211211112341615211521213112121116253213222131"), 8).split()), end='')
print(*v_10_CC(delitel(chereduiem(razbivaiem(kod[1:])), 8).split()), end='')
input()
