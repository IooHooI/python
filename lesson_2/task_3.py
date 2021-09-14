def task():
    print("Введите число от 1 до 12:")
    n = int(input())
    seasons = {
        "Зима": [12, 1, 2],
        "Весна": [3, 4, 5],
        "Лето": [6, 7, 8],
        "Осень": [9, 10, 11]
    }

    for k, v in seasons.items():
        if n in v:
            print("Время года: {}".format(k))
            return

    print("Время года найти не удалось")