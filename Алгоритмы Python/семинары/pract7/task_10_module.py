import random
from collections.abc import MutableMapping

UNIC_NAMES_LIST = [
    "Комова Елизавета Олеговна",
    "Репенков Сергей Алексеевич",
    "Анисимов Ефим Сергеевич",
    "Борисов Никита Алексеевич",
    "Исмоилова Милена Витальевна",
    "Рогов Владимир Алексеевич",
    "Савочкин Артём Дмитриевич",
    "Кривошеина Елена Олеговна",
    "Пономарев Михаил Александрович",
    "Абдулмеджидов Мирза Мурадович",
    "Егшатян Артем Кирович",
    "Гарайшин Тамерлан Тагирович",
    "Брусова Полина Игоревна",
    "Крылова Елизавета Алексеевна",
    "Гераськина Надежда Станиславовна",
    "Гиниятуллина Эвита Маратовна",
    "Малахов Иван Петрович",
    "Жилина Алена Алексеевна",
    "Королев Илья Алексеевич",
    "Пойкалайнен Александра Максимовна",
    "Щербак Станислав Валентинович",
    "Буркина Елизавета Сергеевна",
    "Мосолова Ксения Дмитриевна",
    "Кротов Олег Валерьевич",
    "Шаповалов Сергей Александрович",
    "Прищепа Екатерина Михайловна",
    "Артемьева Дарья Сергеевна",
    "Попова Софья Александровна",
    "Башмакова Анастасия Алексеевна",
    "Корнева Татьяна Андреевна",
    "Олзошкина Янжина Владленовна",
    "Касьянов Максим Евгеньевич",
    "Олейник Анастасия Александровна",
    "Сивухов Артём Олегович",
    "Груздев Всеволод Алексеевич",
    "Буковец Данила Андреевич",
    "Зелянина Алёна Геннадьевна",
    "Мерзляков Данила Артемович",
    "Карасёв Артём Владимирович",
    "Пономаренко Александр Павлович",
    "Курносиков Кирилл Андреевич",
    "Гуриков Дмитрий Олегович",
    "Котова Екатерина Дмитриевна",
    "Лихачев Марк Игоревич",
    "Волкова Татьяна Алексеевна",
    "Марунько Анна Сергеевна",
    "Пашкевич Денис Вячеславович",
    "Маркова Ольга Алексеевна",
    "Термышева Полина Евгеньевна",
    "Василевская Лидия Игоревна",
]

class DEMKAdict(MutableMapping):
    """
    Кастомная коллекция от dict
    """

    def __init__(self, *args, **kwargs):
        self.store = dict()
        self.update(dict(*args, **kwargs))

    def __getitem__(self, key):
        return self.store[self.__keytransform__(key)]

    def __setitem__(self, key, value):
        self.store[self.__keytransform__(key)] = value

    def __delitem__(self, key):
        del self.store[self.__keytransform__(key)]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def __keytransform__(self, key):
        return key


class Task10_1():
    """
    Cоздать словарь телефонного справочника. Заполнить его 50 элементами. Реализовать поиск по телефону
    """

    def __init__(self):
        self.custom_generator()
        self.search()

    def locale_random(self, n):
        return str(random.randint(10 ** (n - 1), (10 ** n) - 1))

    def custom_generator(self):
        self.d = DEMKAdict()
        for e in UNIC_NAMES_LIST:
            key = "+7" + self.locale_random(10)
            self.d[key] = e
            print("Сгенерировали ключ " + key)

    def search(self):
        input_key = input("Введите номер телефона для поиска ->")
        if input_key in self.d:
            print("Значение для телефона " + input_key + " -> " + self.d[input_key])
        else:
            print("Введённого номера телефона нет в базе")

class Task10_2(Task10_1):
    """
    Реализовать проверку на существующие записи в предыдущих заданиях с возможностью дополнения
    """

    def __init__(self):
        self.dict_generator()
        self.search()

    def search(self):
        s = input("Введите адрес для поиска ->")
        if s in self.d:
            print("Адрес найден!\nПроживающие по адресу:")
            [print(x) for x in self.d[s]]
        else:
            print("Адрес не найден, но мы его добавим в систему")
            names = input("Введите ФИО людей, проживающих по этому адресу через заптую -> ")
            self.d[s] = names.split(",")
            print("Обновлённый словарь:")
            for k, v in self.d.items():
                print(k, v)

if __name__ == "__main__":
    Task10_1()