from auxiliary import isfloat


def task():
    def foo(n: float, m: float) -> float:
        return n / m

    print("Введите делитель:")
    n = input()

    print("Введите знаменатель")
    m = input()

    if isfloat(n) and isfloat(m):
        try:
            print("Результат: {}".format(foo(float(n), float(m))))
        except ZeroDivisionError:
            print("Это не мат.ан., на ноль делить нельзя")
    else:
        print("Что-то не так. Ушёл грустить.")
