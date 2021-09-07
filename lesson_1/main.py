def check(var):
    if var.isdigit():
        return int(var)
    else:
        return None


def task_1():
    # 1. Поработайте с переменными, создайте несколько, выведите на экран,
    # запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
    int_var_1 = 1413
    str_var_1 = "wefwfeqgfq3"

    print("Число: {} (тип: {}), строка: {} (тип: {})".format(
        int_var_1,
        type(int_var_1),
        str_var_1,
        type(str_var_1)
    ))

    print("Введите 3 числа, пожалуйста (<number>+ENTER): ")

    int_var_2, int_var_3, int_var_4 = input(), input(), input()
    int_var_2, int_var_3, int_var_4 = check(int_var_2), check(int_var_3), check(int_var_4)

    if (int_var_2 is not None) and (int_var_3 is not None) and (int_var_4 is not None):
        print("Число: {} (тип: {})".format(int_var_2, type(int_var_2)))
        print("Число: {} (тип: {})".format(int_var_3, type(int_var_3)))
        print("Число: {} (тип: {})".format(int_var_4, type(int_var_4)))
    else:
        print("Что-то не так. Я пошел грустить.")
        exit(1)

    print("Введите строку пожалуйста: ")

    str_var_2 = input()

    print("Строка: {} (тип: {})".format(str_var_2, type(str_var_2)))


def task_2():
    # 2. Пользователь вводит время в секундах.
    # Переведите время в часы, минуты и секунды и выведите в формате чч: мм:сс.
    # Используйте форматирование строк.
    def foo(n):
        return "0{}".format(n) if n < 10 else str(n)

    print("Введите время в секундах:")

    total_seconds = input()
    total_seconds = check(total_seconds)

    if total_seconds is not None:
        hours = total_seconds // 3600

        minutes = total_seconds % 3600 // 60

        seconds = total_seconds % 60

        print("{}:{}:{}".format(foo(hours), foo(minutes), foo(seconds)))
    else:
        print("Что-то не так. Я пошел грустить.")
        exit(1)


def task_3():
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


def task_4():
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


def task_5():
    # 5. Запросите у пользователя значения выручки и издержек фирмы.
    # Определите, с каким финансовым результатом работает фирма
    # (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
    # Выведите соответствующее сообщение.
    # Если фирма отработала с прибылью, вычислите рентабельность выручки(соотношение прибыли к выручке).
    # Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
    print("Введите значение выручки фирмы n (0 < n):")

    n = input()
    n = check(n)

    print("Введите значение издержек фирмы m (0 < m):")

    m = input()
    m = check(m)

    if n is not None and 0 < n and m is not None and 0 < m:
        if n > m:
            print("Фирма работает в прибыль")

            r = (n - m) / float(n)

            print("Рентабельность: {}".format(r))

            print("Введите численность сотрудников фирмы k (0 < k):")

            k = input()
            k = check(k)

            if k is not None and 0 < k:
                print("Прибыль фирмы в расчете на одного сотрудника: {}".format(
                    (n - m) / float(k)
                ))
            else:
                print("Что-то не так. Я пошел грустить.")
                exit(1)
        else:
            print(
                "Фирма работает в убыток"
            )
    else:
        print("Что-то не так. Я пошел грустить.")
        exit(1)


def task_6():
    # 6. Спортсмен занимается ежедневными пробежками.
    # В первый день его результат составил a километров.
    # Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
    # Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
    # Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
    print("Введите значение параметра a (0 < a):")

    a = input()
    a = check(a)

    print("Введите значение параметра b (0 < b):")

    b = input()
    b = check(b)

    if a is not None and 0 < a and b is not None and 0 < b:
        days_count = 1
        curr_result = a

        while curr_result < b:
            print("{}-й день: {}".format(days_count, round(curr_result, 2)))

            days_count += 1

            curr_result += curr_result * 0.1

        print("{}-й день: {}".format(days_count, round(curr_result, 2)))
        print("Ответ: на {}-й день спортсмен достиг результата — не менее {} км.".format(days_count, b))
    else:
        print("Что-то не так. Я пошел грустить.")
        exit(1)


if __name__ == "__main__":
    print("task_1")
    task_1()
    print("task_2")
    task_2()
    print("task_3")
    task_3()
    print("task_4")
    task_4()
    print("task_5")
    task_5()
    print("task_6")
    task_6()
