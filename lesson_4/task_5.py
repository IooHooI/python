from functools import reduce


def foo(_min_, _max_):
    for item in range(_min_, _max_ + 2, 2):
        yield item


def task(_min_, _max_):
    return reduce(lambda x, y: x * y, [item for item in foo(_min_, _max_)])


if __name__ == "__main__":
    print("Результат: {}".format(task(100, 1000)))
