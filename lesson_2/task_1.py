def task():
    a_list = [
        12,
        242.2424,
        "wqefwfqewfwq",
        True,
        [12, 3, 12, 3, 1],
        (1, 2, 3),
        {(1, 1): (1, 1), (2, 2): (2, 2), (3, 3): (3, 3), (4, 4): (4, 4)},
        {1, 2, 3},
        frozenset({1, 2, 3})
    ]

    for item in a_list:
        print(type(item))
