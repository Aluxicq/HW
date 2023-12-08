import random

attempts = 3
print("Попробуй угадать число от 0 до 5!")
number = random.randint(0, 5)
while True:

    user_number = int(input("Введи число: "))
    if user_number == number:
        print("Это верно, я загадал число", number)
        break

    else:
        print('Не угадал')
        attempts -= 1
    if attempts == 0:
        print('Ты проиграл!')
