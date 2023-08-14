import random

# Компуктор загадывает число
q = random.randint(0,10)
w = 0

while True:
    w += 1
    print("Попытка:", w)
    # Требуем от юзноа ввести число
    a = int(input("Введите число:"))
    if a > q:
        print("Меньше")
    elif a < q:
        print("Больше")
    else:
        print("Угадал")
        break
