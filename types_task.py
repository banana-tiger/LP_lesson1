try:
    v = float(input("Введите число от 1 до 10:"))
    if 0 < v <= 10.99:
        print(f"Результат: {v + 10}")
    else:
        print("Не соответствует условию (число от 1 до 10)")
except ValueError:
    print("Не число")
