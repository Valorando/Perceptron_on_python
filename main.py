import random

class Perceptron:
    def __init__(self):
        self.weights = [random.random() for _ in range(3)]  # Три входа
        self.bias = random.random()
        self.learning_rate = 0.1  # Швидкість навчання

    # Активаційна функція (сходинкова)
    def activation_function(self, input):
        return 1 if input >= 0 else 0

    # Функція передбачення (обчислення виходу)
    def predict(self, x1, x2, x3):
        total_input = x1 * self.weights[0] + x2 * self.weights[1] + x3 * self.weights[2] + self.bias
        return self.activation_function(total_input)

    # Навчання перцептрона на одному кроці
    def train(self, x1, x2, x3, expected):
        prediction = self.predict(x1, x2, x3)
        error = expected - prediction

        # Оновлення ваг та зсуву за правилом навчання
        self.weights[0] += self.learning_rate * error * x1
        self.weights[1] += self.learning_rate * error * x2
        self.weights[2] += self.learning_rate * error * x3
        self.bias += self.learning_rate * error

# Функция для проверки входных значений
def check_input(value):
    if value not in [0, 1]:
        print("Програма завершена.")
        return False
    return True

# Основна програма
if __name__ == "__main__":
    perceptron = Perceptron()

    # Навчальна вибірка для операції OR з трьома входами
    inputs = [
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 0),
        (1, 0, 0),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0),
        (1, 1, 1)
    ]

    # Очікувані результати для OR з трьома входами
    outputs = [0, 1, 1, 1, 1, 1, 1, 1]

    # Навчання перцептрона
    for epoch in range(1000):  # 1000 епох навчання
        for i in range(len(inputs)):
            perceptron.train(*inputs[i], outputs[i])

    # Тестування
    print("Тестування перцептрона для операції OR з трьома входами:")
    for user_input in inputs:
        result = perceptron.predict(*user_input)
        print(f"Вхід: {user_input} -> Вихід: {result}")

    while True:
        print("\nВведіть нові значення для прогнозу (0 або 1). Для виходу введіть будь-яке інше значення.")

        try:
            x1 = int(input("Введіть перше значення (x1): "))
            if not check_input(x1):
                break

            x2 = int(input("Введіть друге значення (x2): "))
            if not check_input(x2):
                break

            x3 = int(input("Введіть третє значення (x3): "))
            if not check_input(x3):
                break

            # Прогнозування для введених користувачем значень
            predicted_result = perceptron.predict(x1, x2, x3)
            print(f"Прогнозоване значення для [{x1}, {x2}, {x3}]: {predicted_result}")

        except ValueError:
            print("Програма завершена.")
            break