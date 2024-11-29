from decimal import Decimal

def calculate_precision():
    # Введення чисел користувачем
    x1 = Decimal(input("Введіть значення для x1 (наприклад, 1.73): "))
    x2 = Decimal(input("Введіть значення для x2 (наприклад, 1.857): "))

    # Точні значення для √3 та 13/7
    print("\nКрок 1: Обчислюємо точні значення для √3 і 13/7:")
    X1 = Decimal("3").sqrt().quantize(Decimal("1.0000"))
    X2 = (Decimal("13") / Decimal("7")).quantize(Decimal("1.0000"))
    print(f"Точне значення √3: {X1}")
    print(f"Точне значення 13/7: {X2}")

    # Розрахунок абсолютних похибок
    print("\nКрок 2: Обчислюємо абсолютні похибки:")
    deltax1 = abs(x1 - X1).quantize(Decimal("1.0000")) + Decimal("0.0001")
    deltax2 = abs(x2 - X2).quantize(Decimal("1.0000")) + Decimal("0.0001")
    print(f"Абсолютна похибка для x1: {deltax1}")
    print(f"Абсолютна похибка для x2: {deltax2}")

    # Розрахунок відносних похибок
    print("\nКрок 3: Обчислюємо відносні похибки:")
    sigx1 = abs(deltax1 / x1).quantize(Decimal("1.00000"))
    sigx2 = abs(deltax2 / x2).quantize(Decimal("1.00000"))
    print(f"Відносна похибка для x1: {sigx1}")
    print(f"Відносна похибка для x2: {sigx2}")

    # Виведення результатів
    print("\nКрок 4: Порівнюємо точність:")
    if sigx1 < sigx2:
        print(f"\nЧисло {x1} точніше ніж {x2}")
    else:
        print(f"\nЧисло {x2} точніше ніж {x1}")

# Запуск програми
if __name__ == "__main__":
    calculate_precision()
