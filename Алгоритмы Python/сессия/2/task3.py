"""
(20 баллов) Строка представляет собой дату в формате день.месяц.год, 
например, «17.5.21», «18.06.56», «2.12.99». 
Напишите функцию, которая определяет время года, соответствующее этой дате. 
Проверьте, что день находится в диапазоне от 1 до 31, месяц – от 1 до 12.
Функция возвращает название времени года.
В случае ошибки возвращает «Ошибка в дате».
(10 баллов) Создайте с помощью присваивания строку вида «17.15.21, 18.06.56, 2.12.99».
Используя созданную функцию, вычислите сколько дат приходятся на каждое время года.
Выведите полученную информацию в виде таблицы с заголовками: время года, количество.
(10 баллов) Если параметр функции не является строкой, то функция генерирует собственное исключение. 
Добавьте в программу обработку исключений (как собственного, так и стандартных).
"""

def check_date(date_str):

    if type(date_str) != str:
        raise ValueError("Неверный параметр","Параметр функции не является строкой")

    #Разделение по точке строки
    day, month, year = date_str.split(".")
    
    #Перевод в целочисленный тип
    day = int(day)
    month = int(month)

    #Проверка на корректность даты
    if 1 <= day <= 31 and 1 <= month <= 12:

        
        if 3 <= month <= 5:
            return "Весна"

        if 6 <= month <= 8:
            return "Лето"

        if 9 <= month <= 11:
            return "Осень"

        #Если не Весна, не Лето и не Осень, то логично, что Зима
        return "Зима"

    #Если еще не вернули никакое значение, то значит не вошли в условие
    # Значит у нас ошибка в дате 
    return "Ошибка в дате"


if __name__ == "__main__":

    #Словарь с временами года:
    seasons_dict = {
        "Лето":  0,
        "Зима":  0,
        "Весна": 0,
        "Осень": 0,
    }

    #Список дат
    date_list = []
    
    for month in range(1,13):
        for day in range(1,32):

            #Текущая дата
            current_date = str(day)+"."+str(month)+".2019"

            #Добавляем в список
            date_list.append(current_date)

    #Цикл по каждой дате
    for date in date_list:
        
        print(date)
        #Получаем результат работы функции
        try:
            result = check_date(date)
        except ValueError as e:
            print("Ошибка ValueError:", e)
        except Exception as e:
            print("")

        #Прибавляем +1 к значению в словаре по ключу-результату
        seasons_dict[result] += 1
    
    #Вывод результатов из сформированного словаря
    print("Время года      Количество")
    for key, value in seasons_dict.items():
        print(key+"              "+str(value))