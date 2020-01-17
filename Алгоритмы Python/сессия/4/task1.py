"""
(20 баллов) Имеется список строк вида «товар: количество» (товар может повторяться), 
например, [“ручки: 5”, “тетради: 30”, “ручки: 10”].

Напишите функцию, которая для этого списка вычисляет общее количество каждого товара.
Функция возвращает словарь вида {“ручки”: 15, “тетради”: 30}.
"""


def list2dict(list_str):
    # выходной словарь
    out_d = {}

    # Цикл по каждому элементу
    for e in list_str:

        # Разбиваем по ключу - значению
        key, count = e.split(" ")

        # Конверт кол-ва из строки в число
        count = int(count)

        # Выкидываем двоеточие
        key = key[: len(key) - 1]

        # Если ключа нет в словаре, то создаём его и мутим значние
        if key not in out_d:
            out_d[key] = count
        # Иначе он есть и прибавляем колво
        else:
            out_d[key] += count

    return out_d
