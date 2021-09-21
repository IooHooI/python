def task():
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