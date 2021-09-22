

def task():
    numbers_dict = {
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять"
    }
    input_file_path = "./some_file"
    new_input_file_path = "./some_file_new"

    with open(input_file_path, "w") as f:
        f.write("{}\n".format("One — 1"))
        f.write("{}\n".format("Two — 2"))
        f.write("{}\n".format("Three — 3"))
        f.write("{}\n".format("Four — 4"))

    with open(input_file_path, "r") as f:
        lines = f.readlines()
        numbers = [int(line.split(" — ")[1].strip()) for line in lines]

    with open(new_input_file_path, "w") as f:
        for number in numbers:
            f.write("{} - {}\n".format(numbers_dict[number], number))

    return new_input_file_path


if __name__ == "__main__":
    print("Результат: {}".format(task()))
