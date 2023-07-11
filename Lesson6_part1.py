n = int(input("Введите любое число: "))

zero = 0

for a in range(1, n+1):
    z = int(input("Введите любое целое число: "))
    if z == 0:
        zero += 1
        print("Всего нулей: ", zero)
    else:
        print("Данное число не является нулем")

print("Итого", zero, "нулей")
