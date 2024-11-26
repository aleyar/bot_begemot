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
        """Печатает сообщение с паузой."""
        sleep(self.timeout)
        print(message)

    def print_welcome_art(self):
        """Выводит символы приветствия."""
        self.sleep_message('''
─────────╔╗─╔╗╔═══╗╔╗───╔╗─────────────╔═══╗─────────
─────────║║─║║║╔══╝║║───║║─────────────║╔═╗║─────────
─────────║╚═╝║║╚══╗║║───║║─────────────║║─║║─────────
─────────║╔═╗║║╔══╝║║─╔╗║║─╔╗──────────║║─║║─────────
─────────║║─║║║╚══╗║╚═╝║║╚═╝║──────────║╚═╝║─────────
─────────╚╝─╚╝╚═══╝╚═══╝╚═══╝──────────╚═══╝─────────
        ''')

    def print_goodbye_art(self):
        """Выводит прощальный символ."""
        self.sleep_message('''
╔════╗╔═══╗     ╔══╗─╔═══╗     ╔═══╗╔═══╗╔═╗─╔╗╔════╗╔══╗╔═╗─╔╗╔╗─╔╗╔═══╗╔═══╗
║╔╗╔╗║║╔═╗║     ║╔╗║─║╔══╝     ║╔═╗║║╔═╗║║║╚╗║║║╔╗╔╗║╚╣─╝║║╚╗║║║║─║║║╔══╝╚╗╔╗║
╚╝║║╚╝║║─║║     ║╚╝╚╗║╚══╗     ║║─╚╝║║─║║║╔╗╚╝║╚╝║║╚╝─║║─║╔╗╚╝║║║─║║║╚══╗─║║║║
──║║──║║─║║     ║╔═╗║║╔══╝     ║║─╔╗║║─║║║║╚╗║║──║║───║║─║║╚╗║║║║─║║║╔══╝─║║║║
──║║──║╚═╝║     ║╚═╝║║╚══╗     ║╚═╝║║╚═╝║║║─║║║──║║──╔╣─╗║║─║║║║╚═╝║║╚══╗╔╝╚╝║
──╚╝──╚═══╝     ╚═══╝╚═══╝     ╚═══╝╚═══╝╚╝─╚═╝──╚╝──╚══╝╚╝─╚═╝╚═══╝╚═══╝╚═══╝
        ''')

    def validate_input(self, prompt, valid_options=None, input_type=str):
        """Запрашивает ввод с валидацией."""
        while True:
            try:
                user_input = input_type(input(prompt).strip())
                if valid_options and user_input not in valid_options:
                    raise ValueError
                return user_input
            except (ValueError, TypeError):
                print("Неверный ввод. Попробуй еще раз.")

    def intro(self):
        """Приветствие и ввод имени игрока."""
        self.print_welcome_art()
        self.sleep_message('Ммм.. Опять разбудили!\n')
        self.sleep_message('Что же, добро пожаловать в игру "Числовая угадайка".\n---')
        self.sleep_message('Меня зовут Бот-Бегемот! Хозяин создал меня, чтобы испытывать искушенные умы.\n---')
        self.validate_input('Чтобы узнать правила, введи "Далее":\n>>', valid_options=["Далее"])
        self.sleep_message('''
        Итак, правила игры просты.
        Твой стартовый игровой баланс: 1000 осколков души.
        Чтобы пройти испытание, тебе надо выиграть у меня 9000 осколков души.
        ''')
        self.sleep_message('Это будет непросто! Надеюсь ты любишь числа и алгоритмы!\n---')
        self.validate_input(
            'Ты готов начинать? Напиши "Да" или "Готов":\n>>', valid_options=["Да", "Готов", "готова"]
        )
        self.name = input('Представься, пожалуйста:\n>>').strip().title()
        self.sleep_message(f'Рад знакомству, {self.name}! Да начнется игра!\n')

    def play_round(self):
        """Одна игровая сессия."""
        print(f"Твой баланс: {self.balance}, Баланс Бота: {self.balance_bot}")
        self.sleep_message("Чтобы сделать ставку, введи сумму, коэффициент и диапазон через пробел.\n")
        # Логика ставки и игры.

    def game_loop(self):
        """Игровой цикл."""
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
            self.validate_input('Чтобы продолжить, введи "Далее":\n>>', valid_options=["Далее"])

    def start(self):
        """Запуск игры."""
        self.intro()
        self.game_loop()


if __name__ == "__main__":
    game = NumberGuessingGame()
    game.start()
