class Figure:
    def __init__(self, figure_type: str, *sides):
        self.figure_type = figure_type.lower()
        self.sides = sides
        
        # Перевірка на невідомий тип фігури
        allowed_types = ["square", "rectangle", "triangle"]
        if self.figure_type not in allowed_types:
            raise ValueError(f"Невідомий тип фігури: '{figure_type}'")

        # Перевірка на від'ємну або нульову довжину сторін
        for side in self.sides:
            if side <= 0:
                raise ValueError("Довжина сторони має бути більшою за нуль!")

        # Перевірка кількості сторін для кожного типу
        if self.figure_type == "square" and len(self.sides) != 1:
            raise ValueError("Для квадрата потрібно вказати 1 сторону.")
        elif self.figure_type == "rectangle" and len(self.sides) != 2:
            raise ValueError("Для прямокутника потрібно вказати 2 сторони.")
        elif self.figure_type == "triangle" and len(self.sides) != 3:
            raise ValueError("Для трикутника потрібно вказати 3 сторони.")

    def get_figure_type(self) -> str:
        return self.figure_type

    def get_figure_length(self) -> float:
        """Повертає периметр (довжину) фігури."""
        if self.figure_type == "square":
            return self.sides[0] * 4
        elif self.figure_type == "rectangle":
            # Виправлено помилку реалізації: формула 2 * (a + b)
            return 2 * (self.sides[0] + self.sides[1])
        elif self.figure_type == "triangle":
            return sum(self.sides)

    def get_angles(self) -> int:
        """Повертає кількість кутів фігури."""
        if self.figure_type in ["square", "rectangle"]:
            return 4
        elif self.figure_type == "triangle":
            return 3


if __name__ == "__main__":
    sq = Figure("square", 5)
    rect = Figure("rectangle", 4, 6)
    tri = Figure("triangle", 3, 4, 5)

    print(f"Фігура: {sq.get_figure_type()}, Периметр: {sq.get_figure_length()}, Кутів: {sq.get_angles()}")
    print(f"Фігура: {rect.get_figure_type()}, Периметр: {rect.get_figure_length()}, Кутів: {rect.get_angles()}")
    print(f"Фігура: {tri.get_figure_type()}, Периметр: {tri.get_figure_length()}, Кутів: {tri.get_angles()}")