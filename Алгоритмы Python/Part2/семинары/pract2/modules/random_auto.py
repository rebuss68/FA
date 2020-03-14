from random import choice, randint

model_list = [
    "Audi",
    "BMW",
    "Ford",
    "Honda",
    "Hyundai",
    "Kia",
    "Lada (ВАЗ)",
    "Mazda",
    "Mercedes-Benz",
    "Mitsubishi",
    "Nissan",
    "Renault",
    "Skoda",
    "Toyota",
    "Volkswagen",
    "Acura",
    "Daihatsu",
    "Datsun",
    "Honda",
    "Infiniti",
    "Isuzu",
    "Lexus",
    "Mazda",
    "Mitsubishi",
    "Nissan",
    "Scion",
    "Subaru",
    "Suzuki",
    "Toyota",
    "Buick",
    "Cadillac",
    "Chevrolet",
    "Chrysler",
    "Dodge",
    "Ford",
    "GMC",
    "Hummer",
    "Jeep",
    "Lincoln",
    "Mercury",
    "Oldsmobile",
    "Pontiac",
    "Tesla",
    "Aurus",
    "Lada (ВАЗ)",
    "ГАЗ",
    "Москвич",
    "ТагАЗ",
    "УАЗ",
    "Audi",
    "BMW",
    "Mercedes-Benz",
    "Opel",
    "Porsche",
    "Volkswagen",
    "Daewoo",
    "Genesis",
    "Hyundai",
    "Kia",
    "SsangYong",
    "Alfa Romeo",
    "Aston Martin",
    "Bentley",
    "Bugatti",
    "Citroen",
    "DS",
    "Ferrari",
    "Fiat",
    "Jaguar",
    "Lamborghini",
    "Lancia",
    "Land Rover",
    "Maserati",
    "Maybach",
    "Mini",
    "Peugeot",
    "Ravon",
    "Renault",
    "Rolls-Royce",
    "Rover",
    "Saab",
    "SEAT",
    "Skoda",
    "Smart",
    "Volvo",
    "ZAZ",
    "Brilliance",
    "BYD",
    "Changan",
    "Chery",
    "DongFeng",
    "FAW",
    "Foton",
    "GAC",
    "Geely",
    "Great Wall",
    "Haima",
    "Haval",
    "JAC",
    "Lifan",
    "Luxgen",
    "Zotye",
]


def random_auto():
    return choice(model_list)


def random_number():
    rus_abs = "АВЕКМНОРСТУХ"
    return choice(rus_abs) + str(randint(100, 999)) + choice(rus_abs) + choice(rus_abs)
