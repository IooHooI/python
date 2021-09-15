from auxiliary import check


def task():
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
