

def foo(original_arg):
    for item in original_arg:
        if original_arg.count(item) == 1:
            yield item


def task(original_arg):
    return [item for item in foo(original_arg)]


if __name__ == "__main__":
    print("Результат: {}".format(task([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11])))
