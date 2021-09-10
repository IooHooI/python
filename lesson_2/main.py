def task_1():
    a_list = [
        12,
        242.2424,
        "wqefwfqewfwq",
        True,
        [
            12,
            3,
            12,
            3,
            1
        ],
        (1,
            2,
            3),
        {
            (1, 1): (1, 1),
            (2, 2): (2, 2),
            (3, 3): (3, 3),
            (4, 4): (4, 4)
        },
        {
            1,
            2,
            3
        },
        frozenset({
            1,
            2,
            3
        })
    ]

    for item in a_list:
        print(
            type(item)
        )


def task_2():
    print("Введите количество элементов в списке:")

    n = int(input())

    a_list = [None] * n

    print("Введите элементы списка:")

    for i in list(range(n)):
        curr = input()

        a_list[i] = curr

    print(a_list)

    if n > 1:
        for i in range(0, n - n % 2, 2):
            a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]

    print(a_list)


def task_3():
    seasons = {
        "Зима": [12, 1, 2],
        "Весна": [3, 4, 5],
        "Лето": [6, 7, 8],
        "Осень": [9, 10, 11]
    }

    print("Введите число от 1 до 12:")

    n = int(input())

    for k, v in seasons.items():
        if n in v:
            print("Время года: {}".format(k))
            return

    print("Время года найти не удалось")


def task_4():
    print("Введите строку из нескольких слов:")

    an_str = input()

    sub_strings = an_str.split()

    for i, sub_string in enumerate(sub_strings):
        print(i + 1, sub_string[:10])


def task_5():
    print("Введите количество элементов в рейтинге:")

    n = int(input())

    if n > 0:
        a_rating_list = []

        print("Введите элементы рейтинга:")

        a_rating_list.append(int(input()))

        print(a_rating_list, "Осталось ввести: {}".format(n - 1))

        for i in list(range(n - 1)):
            curr = int(input())

            for j in range(len(a_rating_list)):
                if curr > a_rating_list[j]:
                    a_rating_list.insert(j, curr)

                    break

            print(a_rating_list, "Осталось ввести: {}".format((n - 1) - (i + 1)))


def task_6():
    structure = []

    print("Введите количество товаров:")

    n = int(input())

    if n > 0:
        for i in range(n):
            print("Введите название товара:")

            name = input()

            print("Введите цену товара:")

            price = float(input())

            print("Введите количество экземпляров товара:")

            count = int(input())

            print("Введите единицу измерения:")

            unit_of_measure = input()

            curr_item_dict = {
                "название": name,
                "цена": price,
                "количество": count,
                "eд": unit_of_measure
            }

            print(curr_item_dict)
            print()

            structure.append((i + 1, curr_item_dict))

        for item in structure:
            print(
                item
            )

        print()

        analytics_results = {}

        for item in structure:
            for k, v in item[1].items():
                if k in analytics_results:
                    analytics_results[k].append(v)
                else:
                    analytics_results[k] = [v]

        for k, v in analytics_results.items():
            print(
                k,
                v
            )


if __name__ == "__main__":
    print("task_1")
    task_1()
    print("task_2")
    task_2()
    print("task_3")
    task_3()
    print("task_4")
    task_4()
    print("task_5")
    task_5()
    print("task_6")
    task_6()
