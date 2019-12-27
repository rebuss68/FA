"""
(15 баллов) Имеется строка, состоящая из целых чисел, перечисленных через запятую.
Напишите функцию, которая вычисляет количество положительных и отрицательных чисел в этой строке.
Строка является параметром функции. Функция возвращает кортеж из 2 вычисленных значений.
"""
def get_values(input_str):
    
    input_list = input_str.split(",")

    #Положительные числа
    plus = 0
    #Отрицательные числа
    minus = 0

    #Цикл по каждому элементу
    for e in input_list:

        #Если элемент меньше нуля, то увеличиваем количество отрицательных чисел на 1
        if int(e) < 0:
            minus += 1
        
        #Если элемент больше нуля, то увеличиваем количество положительных чисел на 1
        elif int(e) > 0:
            plus += 1
    
    #Возврат значения
    return (plus, minus)


if __name__ == "__main__":
    this_str = "1,2,35,-56,305"
    result = get_values(this_str)
    print(result)
    
   