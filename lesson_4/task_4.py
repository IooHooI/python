

def task(original_arg):
    for curr in original_arg:
        yield curr


if __name__ == "__main__":
    result = []

    original = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    # TODO
    for item in task(original):
        if item not in result:
            result.append(item)

    print("Результат: {}".format(result))
