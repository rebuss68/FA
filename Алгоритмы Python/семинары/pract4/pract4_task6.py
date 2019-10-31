"""
Создать словарь железнодорожных сообщений с учетом более одной но менее 4 пересадок, с рекомендацией оптимального маршрута по времени
Между переходами разница в 30 мин
"""

import datetime

#Время для пересадки между поездами
TIME_WAIT = 30

class UniversalCalss():

    @staticmethod
    def get_train_time(*time_ranges):
        """
        Метод для вычисления времени прибытия поезда
        Необходим для проверки на то, успевает ли человек на свой поезд
        """
        out_list = []
        for time_range in time_ranges:
            time = time_range[0]
            begin_time = time_range[1]

            train_begin_time = datetime.datetime.strptime(begin_time, "%d.%m.%Y %H:%M")
            train_arrive_time = train_begin_time + datetime.timedelta(minutes=time)

            out_list.append((train_begin_time,train_arrive_time))
        return out_list

    @staticmethod
    def detect_station_waiting_time(station_name, all_wait_list):
        for way in all_wait_list["ways"]:
            if station_name == way["point"]:
                return True, way["time"]
        return False, None


        
class Task6():

    def __init__(self):
        """
        Конструктор класса
        Формирует словарь железнодорожных сообщений + вызов всех методов
        """
        self.all_ways_list = []
        date = datetime.datetime.now().date().strftime("%d.%m.%Y ")
        self.d = {
            "Одинцово": [
                {"begin_time": date+"21:30", "time_range": 30, "name": "Белорусский вокзал"},
                {"begin_time": date+"14:40", "time_range": 3, "name": "Баковка"},
                {"begin_time": date+"10:30", "time_range": 15, "name": "Отрадное"},
            ],

            "Баковка": [
                {"begin_time": date+"07:45", "time_range": 3, "name": "Одинцово"},
                {"begin_time": date+"14:20", "time_range": 10, "name": "Курский Вокзал"},
                {"begin_time": date+"08:10", "time_range": 25, "name": "Савёловский Вокзал"},
            ],
            "Отрадное": [
                {"begin_time": date+"08:10", "time_range": 15, "name": "Одинцово"},
                {"begin_time": date+"09:40", "time_range": 60, "name": "Курский Вокзал"},
                {"begin_time": date+"18:21", "time_range": 38, "name": "Савёловский вокзал"},
            ],
            "Белорусский вокзал": [
                {"begin_time": date+"11:15", "time_range": 30, "name": "Одинцово"},
                {"begin_time": date+"13:50", "time_range": 10, "name": "Курский Вокзал"},
                {"begin_time": date+"20:52", "time_range": 5, "name": "Савёловский вокзал"},
            ],
            "Курский Вокзал": [
                {"begin_time": date+"17:02", "time_range": 10, "name": "Белорусский Вокзал"},
                {"begin_time": date+"17:10", "time_range": 10, "name": "Баковка"},
                {"begin_time": date+"15:58", "time_range": 60, "name": "Отрадное"},
            ],
            "Савёловский Вокзал": [
                {"begin_time": date+"11:18", "time_range": 5, "name": "Белорусский вокзал"},
                {"begin_time": date+"15:26", "time_range": 25, "name": "Баковка"},
                {"begin_time": date+"19:10", "time_range": 38, "name": "Отрадное"},
            ],
        }
        self.way_inputer()
        self.way_recognizer()
        if self.all_ways_list != []:
            self.waiting_time_detector()
            self.main_time_detector()
            self.result_outputer()

    def result_outputer(self):
        """
        Вывод результатов на экран
        """
        print("result_outputer")
        results = self.final_out_list
        for e in results:
            print(e["total_time"])

    def main_time_detector(self):
        
        """
        Метод вычисляет общее время, которое включает в себя:
         - Время поездки на поезда
         - Время ожидания между поездами
        Формуирет форматированный список рейсов, отсортированных по убыванию
        """

        all_ways_list = self.all_ways_list
        all_wait_list = self.all_wait_list

        out_list = []

        for i in range(len(all_ways_list)):
            
            final_way = {"total_time" : None, "ways":[]}

            print("\n\nОбнуление всего...")
            points = all_ways_list[i]["points"]
            print("points",points)
            times = all_ways_list[i]["times"]
            print("times",times)
            print("all_wait_list[i]",all_wait_list[i])
            total_time = None
            little_way_dict = []
            for j in range(len(times)):
                print(points[j]," -> ",points[j+1])
                train_time = times[j][1] - times[j][0]
                checked_value = UniversalCalss.detect_station_waiting_time(points[j+1], all_wait_list[i])
                print("train_time",train_time)

                if checked_value[0] == True:
                    print("Опа, добавлем время ожидания..",checked_value[1])
                    little_way_dict.append({"way_from":points[j],"way_to":points[j+1],"train_time":train_time,"waiting_time":checked_value[1]})
                    train_time += checked_value[1]
                else:
                    little_way_dict.append({"way_from":points[j],"way_to":points[j+1],"train_time":train_time,"waiting_time":None})
                
                
                if total_time == None:
                    total_time = train_time
                else:
                    total_time += train_time

            final_way["total_time"] = total_time
            final_way["ways"] = little_way_dict
            out_list.append(final_way)
            out_list.sort(key=lambda x: (x["total_time"]))
    
        self.final_out_list = out_list   



    def waiting_time_detector(self):
        """
        Метод для определения времени ожидания след поезда между станциями + TIME_WAIT мин на пересадку
        """

        all_ways_list = self.all_ways_list
        all_wait_list = []

        for way in all_ways_list:
            #Словарь для хранения маршрутов и времени для дальнейшего вывода
            wait_dict = {"ways":[]}
            #Список с парами прибытия предыдущего и отправления следующего поезда
            pairs_time = []
            #Т.к. есть прямой маршрут, то время одно от точки 0 до 1
            #Индивидуальный подход кароч, если маршрут прямой
            if len(way["times"]) == 1:
                pairs_time.append([way["times"][0][0],way["times"][0][1]])

                if pairs_time[0][0] > pairs_time[0][1]:
                    pairs_time[0][1] = pairs_time[0][1] + datetime.timedelta(days=1)
                    total_time = pairs_time[0][1]-pairs_time[0][0]
                else:
                    total_time = pairs_time[0][1] - pairs_time[0][0]
                wait_dict["ways"].append({ "point":way["points"], "time": total_time ,"type":0})  
            else:
                for i in range(1,len(way["times"])):
                    pairs_time.append([way["times"][i-1][1],way["times"][i][0]])

                for i in range(len(pairs_time)):
                    
                    #Если не успевает на след поезд от премени предыдущего поезда + 30 мин, то + 24 часа
                    if pairs_time[i][0] + datetime.timedelta(minutes=TIME_WAIT) > pairs_time[i][1]:
                        pairs_time[i][1] = pairs_time[i][1] + datetime.timedelta(days=1)
                        diff_time = pairs_time[i][1]-pairs_time[i][0]
                    
                    else:
                        diff_time = pairs_time[i][1] - pairs_time[i][0]
                    #ways_final_list[]
                    wait_dict["ways"].append({ "point":way["points"][i+1], "time": diff_time ,"type":1})
                    
            all_wait_list.append(wait_dict)
        self.all_wait_list = all_wait_list

    def way_inputer(self):
        """
        Ввод данных
        """

        self.point_a = input("Введите точку А -> ")
        self.point_b = input("Введите точку В -> ")

    def way_recognizer(self):
        """
        Метод для поиска маршрутов по словарю d
        Заносит результаты вычислений в all_ways_list
        """

        d = self.d
        point_a = self.point_a
        point_b = self.point_b

        all_ways_list = []

        if point_a in d:

            for first_element in d[point_a]:

                if first_element["name"] == point_b:
                    print("[Вложенность 0] " + point_a + " - > " + first_element["name"])

                    all_ways_list.append(
                        {
                            "points": [point_a, first_element["name"]],
                            "times": UniversalCalss.get_train_time((first_element["time_range"],first_element["begin_time"])),
                            "detector_number": 0,
                        })

                if first_element["name"] in d:
                    for second_element in d[first_element["name"]]:
                        if second_element["name"] == point_b:
                            print("[Вложенность 1] " + point_a + " - > " + first_element["name"] + " -> " +
                                  second_element["name"])
                            
                            all_ways_list.append(
                                {
                                    "points": [point_a, first_element["name"], second_element["name"]],
                                    "times": UniversalCalss.get_train_time(
                                        (first_element["time_range"], first_element["begin_time"]),
                                        (second_element["time_range"], second_element["begin_time"])
                                    ),
                                    "detector_number": 1,
                                })

                        if second_element["name"] in d:
                            for third_element in d[second_element["name"]]:
                                if third_element["name"] == point_b:
                                    print("[Вложенность 2] " + point_a + " - > " + first_element["name"] + " -> " +
                                          second_element["name"] + " -> " + third_element["name"])
                                    all_ways_list.append(
                                        {
                                            "points": [point_a, first_element["name"], second_element["name"],
                                                       third_element["name"]],
                                            "times": UniversalCalss.get_train_time(
                                                (first_element["time_range"], first_element["begin_time"]),
                                                (second_element["time_range"], second_element["begin_time"]),
                                                (third_element["time_range"], third_element["begin_time"]),
                                            ),
                                            "detector_number": 2,
                                        })

                                if third_element["name"] in d:
                                    for fourth_element in d[third_element["name"]]:
                                        if fourth_element["name"] == point_b:
                                            print("[Вложенность 3] " + point_a + " - > " + first_element[
                                                "name"] + " -> " + second_element["name"] + " -> " + third_element[
                                                      "name"] + " -> " + fourth_element["name"])
                                            all_ways_list.append(
                                                {
                                                    "points": [point_a, first_element["name"], second_element["name"],
                                                               third_element["name"], fourth_element["name"]],
                                                    "times": UniversalCalss.get_train_time(
                                                        (first_element["time_range"], first_element["begin_time"]),
                                                        (second_element["time_range"], second_element["begin_time"]),
                                                        (third_element["time_range"], third_element["begin_time"]),
                                                        (fourth_element["time_range"], fourth_element["begin_time"]),
                                                    ),
                                                    "detector_number": 3,
                                                })

            self.all_ways_list = all_ways_list

        else:
            print("Нет исходной точки в начале")

if __name__ == "__main__":
    Task6()
