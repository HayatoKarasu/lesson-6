a = int(input("Введите первое любое число: "))
b = int(input("Введите второе любое число: "))

if a < b:
    for c in range(a, b+1):
        if c % 2 == 0:
            print(c, end = " ")
else:
    print("Не верно! Первое число должно быть меньше второго")
