

def foo(n):
    curr = 1
    for item in range(1, n + 1):
        curr *= item
        yield curr


def task(n):
    return [item for item in foo(n)]


if __name__ == "__main__":
    print("Результат: {}".format(task(10)))
