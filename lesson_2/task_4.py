def task():
    print("Введите строку из нескольких слов:")
    an_str = input()
    sub_strings = an_str.split()

    for i, sub_string in enumerate(sub_strings):
        print(i + 1, sub_string[:10])