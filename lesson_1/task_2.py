from auxiliary import check


def task():
    # 2. Пользователь вводит время в секундах.
    # Переведите время в часы, минуты и секунды и выведите в формате чч: мм:сс.
    # Используйте форматирование строк.
    def foo(n):
        return "0{}".format(n) if n < 10 else str(n)

    print("Введите время в секундах:")
    total_seconds = input()
    total_seconds = check(total_seconds)

    if total_seconds is not None:
        hours = total_seconds // 3600
        minutes = total_seconds % 3600 // 60
        seconds = total_seconds % 60

        print("{}:{}:{}".format(foo(hours), foo(minutes), foo(seconds)))
    else:
        print("Что-то не так. Я пошел грустить.")
        exit(1)
