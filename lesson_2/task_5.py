def task():
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