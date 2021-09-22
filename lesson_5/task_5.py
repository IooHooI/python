

def task():
    input_file_path = "./some_file"

    with open(input_file_path, "w") as f:
        input_str = input("Введите набор чисел, разделенных пробелами:")
        f.write(input_str)

    with open(input_file_path, "r") as f:
        numbers = f.read()
        numbers = [int(number) for number in numbers.strip().split()]

    return sum(numbers)


if __name__ == "__main__":
    print("Результат: {}".format(task()))
