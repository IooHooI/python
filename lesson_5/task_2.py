

def task():
    input_file_path = "./some_file"
    result = {
        "lines count": None,
        "words count per line": None
    }

    with open(input_file_path, "r") as f:
        lines = f.readlines()
        result["lines count"] = len(lines)
        result["words count per line"] = [len(line.split()) for line in lines]

    return result


if __name__ == "__main__":
    print("Результат: {}".format(task()))
