def calculate_average(numbers):
    positive_numbers = [n for n in numbers if n > 0]
    if not positive_numbers:
        return None
    return sum(positive_numbers) / len(positive_numbers)

# Получение ввода от пользователя
user_input = input("Введите числа через запятую (например: 1, -2, 3): ")

# Преобразование строки в список чисел
try:
    number_list = [int(n.strip()) for n in user_input.split(',')]
except ValueError:
    print("Ошибка: Ввод должен содержать только числа, разделённые запятыми.")
    exit()

# Вычисление и логирование
result = calculate_average(number_list)

with open("interactive_log.txt", "w") as log_file:
    if result is not None:
        log_file.write(f"Среднее положительных чисел: {result}\n")
        print(f"✅ Среднее положительных чисел: {result}")
    else:
        log_file.write("❗ Нет положительных чисел для подсчёта.\n")
        print("❗ Нет положительных чисел для подсчёта.")

class Agent:
    def __init__(self):
        self.chat_history = []
        self.positive_inputs = 0  # Add a counter for positive inputs

    def add_to_chat_history(self, input, response, positive):
        self.chat_history.append((input, response, positive))
        if positive:  # Increment the counter if the input is positive
            self.positive_inputs += 1

    def get_chat_history(self):
        return self.chat_history

    def get_positive_inputs(self):
        return self.positive_inputs
def run_agent():
    while True:
        print("\nЧто вы хотите сделать?")
        print("1 - Ввести числа и вычислить среднее положительных")
        print("2 - Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            # Повторяем твой текущий ввод и расчёт
            user_input = input("Введите числа через запятую (например: 1, -2, 3): ")
            try:
                number_list = [int(n.strip()) for n in user_input.split(',')]
            except ValueError:
                print("Ошибка: Ввод должен содержать только числа, разделённые запятыми.")
                continue

            result = calculate_average(number_list)
            with open("interactive_log.txt", "a") as log_file:
                if result is not None:
                    log_file.write(f"✅ Среднее положительных чисел: {result}\n")
                    print(f"✅ Среднее положительных чисел: {result}")
                else:
                    log_file.write("❗ Нет положительных чисел для подсчёта.\n")
                    print("❗ Нет положительных чисел для подсчёта.")
        elif choice == "2":
            print("👋 До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
run_agent()





