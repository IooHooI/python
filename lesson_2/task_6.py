def task():
    print("Введите количество товаров:")
    n = int(input())
    structure = []

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
            print(item)

        print()
        analytics_results = {}

        for item in structure:
            for k, v in item[1].items():
                if k in analytics_results:
                    analytics_results[k].append(v)
                else:
                    analytics_results[k] = [v]

        for k, v in analytics_results.items():
            print(k, v)