from auxiliary import check


def task():
    # 4. Пользователь вводит целое положительное число.
    # Найдите самую большую цифру в числе.
    # Для решения используйте цикл while и арифметические операции.
    print("Введите целое число n (0 < n):")
    n = input()
    n = check(n)

    if n is not None and 0 < n:
        i = 1
        str_n = str(n)
        max_digit = int(str_n[i - 1])

        while i < len(str_n):
            if int(str_n[i]) > max_digit:
                max_digit = int(str_n[i])
            i += 1

        print("Результат: {}".format(max_digit))
    else:
        print("Что-то не так. Я пошел грустить.")
        exit(1)
