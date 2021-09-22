

def foo(input_str):
    sub_strings = input_str.split()

    return [int(sub_string.split("(")[0]) for sub_string in sub_strings if "(" in sub_string]


def task():
    input_file_path = "./some_file"

    with open(input_file_path, "w") as f:
        f.write("{}\n".format("Информатика: 100(л) 50(пр) 20(лаб)."))
        f.write("{}\n".format("Физика: 30(л) — 10(лаб)"))
        f.write("{}\n".format("Физкультура: — 30(пр) —"))

    with open(input_file_path, "r") as f:
        lines = f.readlines()
        result = {line.split(": ")[0]: sum(foo(line.split(": ")[1])) for line in lines}

    return result


if __name__ == "__main__":
    print("Результат: {}".format(task()))
