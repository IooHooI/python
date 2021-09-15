from auxiliary import check


def task():
    # 3. Узнайте у пользователя число n.
    # Найдите сумму чисел n + nn + nnn.
    # Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
    print("Введите число n (0 <= n < 10):")
    n = input()
    n = check(n)

    if n is not None and 0 <= n < 10:
        m = 3
        result = sum([sum([n * 10**j for j in range(i + 1)]) for i in range(m)])

        print("Результат: {}".format(result))
    else:
        print("Что-то не так. Я пошел грустить.")
        exit(1)
