from auxiliary import isfloat
from auxiliary import isint


def task():
    def my_func_1(x, y):
        return x ** y

    def my_func_2(x, y):
        res = 1

        for _ in range(abs(y)):
            res /= x

        return res

    print("Введите x:")
    x = input()

    print("Введите y")
    y = input()

    if isfloat(x) and isint(y) and float(x) > 0 > int(y):
        print("Результат V1: {}".format(my_func_1(float(x), int(y))))
        print("Результат V2: {}".format(my_func_2(float(x), int(y))))
    else:
        print("Что-то не так. Ушёл грустить.")
