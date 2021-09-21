

def foo(original_arg):
    if len(original_arg) > 1:
        past = original_arg[0]
        for curr in original_arg:
            if curr > past:
                yield curr
            past = curr
    else:
        return original_arg


def task(original_arg):
    return [item for item in foo(original_arg)]


if __name__ == "__main__":
    print("Результат: {}".format(task([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55])))
