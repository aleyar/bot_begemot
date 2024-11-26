from random import randint, uniform
from time import sleep


class NumberGuessingGame:
    def __init__(self):
        self.balance = 1000
        self.balance_bot = 9000
        self.timeout = uniform(1.5, 3.6)
        self.name = ""
        self.list_coef = [2, 4, 10]
        self.list_bet = [100, 1000, 10000]
        self.list_try = {
            2: [6, 9, 13],
            4: [5, 8, 12],
            10: [4, 7, 11]
        }

    def sleep_message(self, message):
        sleep(self.timeout)
        print(message)

    def print_welcome_art(self):
        self.sleep_message('''
─────────╔╗─╔╗╔═══╗╔╗───╔╗─────────────╔═══╗─────────
─────────║║─║║║╔══╝║║───║║─────────────║╔═╗║─────────
─────────║╚═╝║║╚══╗║║───║║─────────────║║─║║─────────
─────────║╔═╗║║╔══╝║║─╔╗║║─╔╗──────────║║─║║─────────
─────────║║─║║║╚══╗║╚═╝║║╚═╝║──────────║╚═╝║─────────
─────────╚╝─╚╝╚═══╝╚═══╝╚═══╝──────────╚═══╝─────────
        ''')

    def print_goodbye_art(self):
        """Выводит прощальное сообщение с артами."""
        self.sleep_message('''
╔════╗╔═══╗     ╔══╗─╔═══╗     ╔═══╗╔═══╗╔═╗─╔╗╔════╗╔══╗╔═╗─╔╗╔╗─╔╗╔═══╗╔═══╗
║╔╗╔╗║║╔═╗║     ║╔╗║─║╔══╝     ║╔═╗║║╔═╗║║║╚╗║║║╔╗╔╗║╚╣─╝║║╚╗║║║║─║║║╔══╝╚╗╔╗║
╚╝║║╚╝║║─║║     ║╚╝╚╗║╚══╗     ║║─╚╝║║─║║║╔╗╚╝║╚╝║║╚╝─║║─║╔╗╚╝║║║─║║║╚══╗─║║║║
──║║──║║─║║     ║╔═╗║║╔══╝     ║║─╔╗║║─║║║║╚╗║║──║║───║║─║║╚╗║║║║─║║║╔══╝─║║║║
──║║──║╚═╝║     ║╚═╝║║╚══╗     ║╚═╝║║╚═╝║║║─║║║──║║──╔╣─╗║║─║║║║╚═╝║║╚══╗╔╝╚╝║
──╚╝──╚═══╝     ╚═══╝╚═══╝     ╚═══╝╚═══╝╚╝─╚═╝──╚╝──╚══╝╚╝─╚═╝╚═══╝╚═══╝╚═══╝
        ''')
        self.sleep_message(f'Игра окончена. Спасибо за игру, {self.name}!')

    def validate_input(self, prompt, valid_options=None):
        while True:
            user_input = input(prompt).strip()
            if valid_options and user_input not in valid_options:
                print("Ошибка: некорректный ввод. Попробуй ещё раз.")
            else:
                return user_input

    def validate_bet(self):
        while True:
            try:
                bet_input = input('Введи сумму, коэффициент и диапазон через пробел (например: 500 4 1000):\n>> ').strip()
                bet_parts = list(map(int, bet_input.split()))
                if len(bet_parts) != 3:
                    print("Ошибка: необходимо ввести ровно три значения. Попробуй ещё раз.")
                    continue
                bet_sum, bet_coef, bet_range = bet_parts
                if bet_sum < 100 or bet_sum > self.balance or bet_sum > self.balance_bot:
                    print(f"Ошибка: сумма ставки должна быть не менее 100 и не превышать ваш баланс ({self.balance}) "
                          f"и баланс Бота ({self.balance_bot}).")
                    continue
                if bet_coef not in self.list_coef:
                    print(f"Ошибка: коэффициент должен быть одним из {self.list_coef}.")
                    continue
                if bet_range not in self.list_bet:
                    print(f"Ошибка: диапазон должен быть одним из {self.list_bet}.")
                    continue
                return bet_sum, bet_coef, bet_range
            except ValueError:
                print("Ошибка: необходимо ввести три числа, разделенные пробелами. Попробуй еще раз.")

    def intro(self):
        self.print_welcome_art()
        self.sleep_message('Ммм.. Опять разбудили!\n')
        self.sleep_message('Что же, добро пожаловать в игру "Числовая угадайка".\n---')
        self.sleep_message('Меня зовут Бот-Бегемот! Ха-ха! Хозяин создал меня, чтобы испытывать искушенные умы.\n---')
        self.validate_input('Чтобы узнать правила, введи "Далее":\n>>', valid_options=["Далее"])
        self.sleep_message('''
        Итак, правила игры просты.
        Твой стартовый игровой баланс: 1000 осколков души.
        Чтобы пройти испытание, тебе надо выиграть у меня 9000 осколков души.
        ---''')
        self.sleep_message('Это будет непросто! Надеюсь ты любишь числа и алгоритмы!\n---')
        self.sleep_message(''' 
        Пример ставки: 
        Введи 500 4 1000 (это значит: ставишь 500 осколков, коэффициент 4, диапазон от 1 до 1000). 
        ---''')
        self.validate_input(
            'Ты готов начинать? Напиши "Да" или "Готов":\n>>', valid_options=["Да", "Готов", "готова"]
        )
        self.name = input('Представься, пожалуйста:\n>>').strip().title()
        self.sleep_message(f'Рад знакомству, {self.name}! Да начнется игра!\n')

    def play_round(self):
        print(f"Твой баланс: {self.balance}, Баланс Бота: {self.balance_bot}")
        self.sleep_message("Доступные коэффициенты: [2, 4, 10]. Доступные диапазоны: [100, 1000, 10000].")
        bet_sum, bet_coef, bet_range = self.validate_bet()

        self.balance -= bet_sum
        self.balance_bot += bet_sum
        number_to_guess = randint(1, bet_range)
        tries = self.list_try[bet_coef][self.list_bet.index(bet_range)]

        print(f"Я загадал число от 1 до {bet_range}. У тебя {tries} попыток, чтобы угадать!")

        while tries > 0:
            try:
                player_guess = int(input("Твое предположение: "))
                tries -= 1
                if player_guess == number_to_guess:
                    win_amount = bet_sum * bet_coef
                    self.balance += win_amount
                    self.balance_bot -= win_amount
                    print(f"Поздравляю, ты угадал число! Ты выиграл {win_amount} осколков души.")
                    return
                elif player_guess < number_to_guess:
                    print(f"Нет, мое число больше. Осталось {tries} попыток.")
                else:
                    print(f"Нет, мое число меньше. Осталось {tries} попыток.")
            except ValueError:
                print("Ошибка: введи целое число.")

        print(f"Ты проиграл ставку! Загаданное число было {number_to_guess}.")

    def game_loop(self):
        while self.balance > 0 and self.balance_bot > 0:
            self.play_round()
            if self.balance >= 10000:
                self.sleep_message(
                    f'Да ты везунчик, {self.name}! Ты смог одолеть Бота-Бегемота и вернуть свои осколки души.'
                )
                return
            elif self.balance <= 0:
                self.print_goodbye_art()
                self.sleep_message(f'Твоя игра окончена, {self.name}. Ты всегда можешь вызвать меня снова.')
                return

    def start(self):
        self.intro()
        self.game_loop()


if __name__ == "__main__":
    game = NumberGuessingGame()
    game.start()
