from auxiliary import check


def task():
    # 1. Поработайте с переменными, создайте несколько, выведите на экран,
    # запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
    int_var_1 = 1413
    str_var_1 = "wefwfeqgfq3"

    print("Число: {} (тип: {}), строка: {} (тип: {})".format(int_var_1, type(int_var_1), str_var_1, type(str_var_1)))
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
