

def foo(*args):
    income = int(args[0])
    costs = int(args[1])

    return income - costs


def task():
    input_file_path = "./some_file"

    with open(input_file_path, "w") as f:
        f.write("{}\n".format("firm_1 ООО 87658 2433."))
        f.write("{}\n".format("firm_2 ОО1 78468 3464."))
        f.write("{}\n".format("firm_3 ОО2 36455 6636."))
        f.write("{}\n".format("firm_4 ОО2 97598 445855."))
        f.write("{}\n".format("firm_5 ОО2 14535 45684574."))
        f.write("{}\n".format("firm_6 ОО2 56786 546745."))
        f.write("{}\n".format("firm_7 ООО 21412 3453."))
        f.write("{}\n".format("firm_8 ОО1 56786 6786."))
        f.write("{}\n".format("firm_9 ОО1 25425 2342."))

    with open(input_file_path, "r") as f:
        lines = f.readlines()
        result = {line.split()[0]: foo(*line.strip(".\n").split()[2:]) for line in lines}

    all_positive = [v for k, v in result.items() if v > 0]

    return [result, {"average_profit": sum(all_positive) / len(all_positive)}]


if __name__ == "__main__":
    print("Результат: {}".format(task()))
