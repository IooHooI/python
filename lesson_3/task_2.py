

def task():
    # https://www.python.org/dev/peps/pep-0008/#method-names-and-instance-variables
    def print_user_info(**kwargs):
        print(("{} " * len(kwargs.items())).rstrip().format(*["{}: {}".format(k, v) for k, v in kwargs.items()]))

    print("Введите имя:")
    name = input()

    print("Введите фамилию:")
    last_name = input()

    print("Введите год рождения:")
    birth_year = input()

    print("Введите город проживания:")
    city = input()

    print("Введите email:")
    email = input()

    print("Введите номер телефона:")
    telephone = input()

    print_user_info(name=name, last_name=last_name, birth_year=birth_year, city=city, email=email, telephone=telephone)
