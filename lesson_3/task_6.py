

def task():
    def int_func(input_str):
        return input_str.capitalize()

    def int_func_several(input_str):
        return " ".join(int_func(item) for item in input_str.split())

    print("Введите слово из маленьких латинских букв:")

    a_word = input()

    print("Результат: {}".format(int_func(a_word)))

    print("Введите строку из слов, разделенных пробелом:")

    words = input()

    print("Результат: {}".format(int_func_several(words)))
