

def task(_from_, _to_, a, b):
    return [item for item in range(_from_, _to_) if item % a == 0 or item % b == 0]


if __name__ == "__main__":
    print("Результат: {}".format(task(20, 240, 20, 21)))
