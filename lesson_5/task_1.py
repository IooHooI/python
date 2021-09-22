

def task():
    input_file_path = "./some_file"
    input_str = None

    with open(input_file_path, "w") as f:
        while input_str != "":
            input_str = input("Введите строку:")
            if len(input_str) > 0:
                f.write("{}\n".format(input_str))

    return input_file_path


if __name__ == "__main__":
    print("Результат: {}".format(task()))
