

def foo(_from_, _to_, a, b):
    item = _from_
    while _from_ <= item <= _to_:
        if item % a == 0 or item % b == 0:
            yield item
        item += 1


def task(_from_, _to_, a, b):
    return [item for item in foo(_from_, _to_, a, b)]


if __name__ == "__main__":
    print("Результат: {}".format(task(20, 240, 20, 21)))
