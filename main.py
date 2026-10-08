def check_number(user_input):
    # 1. Перевірка на числовий тип
    try:
        number = float(user_input)
    except ValueError:
        raise ValueError("Помилка: введене значення не є числом!")

    # 2. Перевірка за допомогою raise (бізнес-логіка)
    if number <= 0:
        raise ValueError("Помилка: число має бути більшим за нуль!")

    # 3. Перевірка за допомогою assert (внутрішній контроль)
    assert number > 0, "Число має бути додатним"

    return number


# Тестуємо з різними значеннями (правильними та неправильними)
test_inputs = ["10", "-5", "0", "abc"]

print("=== РЕЗУЛЬТАТИ ПЕРЕВІРКИ ===\n")

for val in test_inputs:
    print(f"Введене значення: '{val}'")
    try:
        result = check_number(val)
        print(f"  --> [УСПІХ] Число {result} прийнято!")
    except ValueError as e:
        print(f"  --> [НЕПРАВИЛЬНО] {e}")
    print("-" * 35)