import unittest

# 1. Функція, яка рахує кількість голосних літер
def count_vowels(text: str) -> int:
    # Перевірка на тип даних
    if not isinstance(text, str):
        raise TypeError("Передане значення має бути рядком!")
    
    # Англійські та українські голосні літери (малі та великі)
    vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯaeiouAEIOU"
    
    return sum(1 for char in text if char in vowels)


# 2. Клас з юніт-тестами
class TestCountVowels(unittest.TestCase):

    # Тест для звичайного рядка
    def test_standard_string(self):
        self.assertEqual(count_vowels("hello"), 2)

    # Тест для порожнього рядка
    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

    # Тест для рядка з цифрами та символами (без голосних)
    def test_digits_and_symbols(self):
        self.assertEqual(count_vowels("12345!@#$"), 0)

    # Тест для рядка з українськими літерами
    def test_ukrainian_letters(self):
        self.assertEqual(count_vowels("Привіт Світ"), 3)  # и, і, і

    # Тест на помилку типу даних (якщо передано не рядок)
    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            count_vowels(123)


if __name__ == "__main__":
    unittest.main()