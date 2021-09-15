from auxiliary import isfloat


def task():
    def my_func(*args):
        return sum(sorted(args, reverse=True)[:2])

    print("Введите arg1:")
    n = input()

    print("Введите arg2")
    m = input()

    print("Введите arg3")
    o = input()

    if isfloat(n) and isfloat(m) and isfloat(o):
        print("Результат: {}".format(my_func(float(n), float(m), float(o))))
    else:
        print("Что-то не так. Ушёл грустить.")
