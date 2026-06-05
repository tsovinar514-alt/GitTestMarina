import random

print("Франкенштейн: Я загадал число от 1 до 10. Сможешь угадать его?")
secret_number = random.randint(1, 10)
attempts = 0

while True:
    try:
        user_guess = int(input("Введи свой вариант: "))
        attempts += 1
        
        if user_guess < secret_number:
            print("Франкенштейн: Моё число больше! Попробуй ещё раз.")
        elif user_guess > secret_number:
            print("Франкенштейн: Моё число меньше! Не сдавайся.")
        else:
            print(f"Франкенштейн: Потрясающе! Ты угадал число за {attempts} попыток!")
            break
    except ValueError:
        print("Франкенштейн: Пожалуйста, введи именно целое число.")
