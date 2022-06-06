def delitel(sho, sk):
    text = ''
    for i in range(1, len(sho) + 1):
        if i % sk == 0:
            text += str(sho[i - sk:i] + " ")
    return text


print(delitel(input("Что "), int(input("По сколько "))), end='')

input()


def greeting(name: str) -> str:
    return 'Hello ' + name
