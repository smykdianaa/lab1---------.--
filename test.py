import unittest
from unittest.mock import patch
from app import Figure


# --- Функція з input(), яку потрібно протестувати ---
def get_user_figure_length():
    """
    Запитує у користувача довжину сторони квадрата 
    та повертає периметр створеної фігури.
    """
    side_str = input("Введіть довжину сторони квадрата: ")
    side = float(side_str)
    fig = Figure("square", side)
    return fig.get_figure_length()


# --- Клас з тестами ---
class TestFigureLifecycleAndAdvanced(unittest.TestCase):

    # 1. Життєвий цикл тесту (Lifecycle Methods)
    @classmethod
    def setUpClass(cls):
        print("\n--- [setUpClass] Запуск усього тестового набору ---")

    @classmethod
    def tearDownClass(cls):
        print("\n--- [tearDownClass] Завершення усього тестового набору ---")

    def setUp(self):
        print("  -> [setUp] Підготовка даних перед тестом")

    def tearDown(self):
        print("  -> [tearDown] Очищення даних після тесту")

    # 2. ⭐ Тест із subTest для всіх типів Figure
    def test_all_figure_types_with_subtest(self):
        # Набір тестових даних: (тип, сторони, очікувана довжина/периметр, очікувані кути)
        cases = [
            {"type": "square", "sides": (5,), "expected_length": 20, "expected_angles": 4},
            {"type": "rectangle", "sides": (4, 6), "expected_length": 20, "expected_angles": 4},
            {"type": "triangle", "sides": (3, 4, 5), "expected_length": 12, "expected_angles": 3},
        ]

        for case in cases:
            # subTest дозволяє перевірити кожен випадок окремо
            with self.subTest(figure_type=case["type"]):
                fig = Figure(case["type"], *case["sides"])
                
                # Перевіряємо тип
                self.assertEqual(fig.get_figure_type(), case["type"])
                # Перевіряємо довжину (периметр)
                self.assertEqual(fig.get_figure_length(), case["expected_length"])
                # Перевіряємо кількість кутів
                self.assertEqual(fig.get_angles(), case["expected_angles"])

    # 3. ⭐ Тест функції з input() за допомогою patch
    @patch("builtins.input", return_value="5")
    def test_get_user_figure_length(self, mock_input):
        # Викликаємо функцію, що всередині викликає input()
        result = get_user_figure_length()

        # 1. Перевіряємо, що результат обчислено вірно (для квадрата зі стороною 5: 5 * 4 = 20.0)
        self.assertEqual(result, 20.0)
        
        # 2. Перевіряємо, що input() викликався рівно 1 раз
        mock_input.assert_called_once_with("Введіть довжину сторони квадрата: ")


if __name__ == "__main__":
    unittest.main()