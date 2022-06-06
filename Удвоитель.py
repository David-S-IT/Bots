a, l = map(int,input("����� �� � ��: ").split())
answer = a
do = 0
while answer < l:
    g = input()
    if g == "*":
        do += 1
        answer *= 2
        if answer > l:
            print("����� ������ ���", l, answer, "��������:", do)
        elif answer == l:
            print("�����!", "��������:", do)
        #elif g == "no" or g == "���" or g == "���" or g == "No":
         #   do -= 1
          #  print("�����!", "��������:", do)
        else:
            print("�����:", answer, "��������:", do)
    elif g == "" or g == "+":
        do += 1
        answer += 1
        if answer > l:
            print("����� ������ ���", l, answer, "��������:", do)
        elif answer == l:
            print("�����!", "��������:", do)
        else:
            print("�����:", answer, "��������:", do)
    elif g == "++":
        do += 31
        answer += 31
        if answer > l:
            print("����� ������ ���", l, answer, "��������:", do)
        elif answer == l:
            print("�����!", "��������:", do)
        else:
            print    ("�����:", answer, "��������:", do)
    else:
        print("���� ����� ������!", "��������:", do)