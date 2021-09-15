from auxiliary import check


def task():
    # 3. Узнайте у пользователя число n.
    # Найдите сумму чисел n + nn + nnn.
    # Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
    print("Введите положительное число n:")
    n = input()

    if check(n) is not None:
        result = int(n) + int(n + n) + int(n + n + n)

        print("Результат: {}".format(result))
    else:
        print("Что-то не так. Я пошел грустить.")
        exit(1)
