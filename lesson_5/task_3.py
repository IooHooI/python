

def task():
    input_file_path = "./some_file"

    with open(input_file_path, "r") as f:
        lines = f.readlines()
        salaries_dict = {
            line.split(": ")[0]: int(line.split(": ")[1].strip()) for line in lines
        }
        small_salaries_dict = {
            k: v for k, v in salaries_dict.items() if v < 20000
        }

        print("Маленькие зарплаты: {}".format(small_salaries_dict))

    return "средняя зарплата: {}".format(sum(salaries_dict.values()) / len(salaries_dict.values()))


if __name__ == "__main__":
    print("Результат: {}".format(task()))
