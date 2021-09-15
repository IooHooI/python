from auxiliary import isfloat


def task():
    terminal_symbol = "@"
    terminated = False
    total_sum = 0

    while not terminated:
        print("Введите числа, разделенные пробелом:")
        curr_iteration = input().split()
        for item in curr_iteration:
            if isfloat(item):
                total_sum += float(item)
            elif item == terminal_symbol:
                terminated = True
                break
            else:
                print("Что-то не так. Ушёл грустить.")
                terminated = True
                break
        print("Текущий результат: {}".format(total_sum))
    print("Итоговый результат: {}".format(total_sum))
