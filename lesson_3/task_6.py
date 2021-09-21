

def task():
    def int_func(input_str):
        return input_str.capitalize()

    def int_func_several(input_str):
        return " ".join(int_func(item) for item in input_str.split())

    a_word = input("Введите слово из маленьких латинских букв:")
    print("Результат: {}".format(int_func(a_word)))

    words = input("Введите строку из слов, разделенных пробелом:")
    print("Результат: {}".format(int_func_several(words)))
