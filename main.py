import random

random_number = random.randint(1, 100)

print('Добро пожаловать в числовую угадайку')


def is_valid(number):
    if 1 <= number <= 100:
        return True
    else:
        return False


attempts_counter = 0

while True:
    line = input()
    if line.isdigit():
        enter_number = int(line)
    else:
        print('А может быть все-таки введем целое число?')
        continue
    if is_valid(enter_number) == True:
        if enter_number < random_number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            attempts_counter += 1
            continue
        elif enter_number > random_number:
            print('Ваше число больше загаданного, попробуйте еще разок')
            attempts_counter += 1
            continue
        else:
            print('Да! Вы угадали!')
            print(f'Количевство ваших попыток: {attempts_counter}')
            print('Спасибо, что поиграли в мою "Числовую Угадайку", увидимся ещё!')
            break
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')