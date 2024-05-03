cars = ["BMW", "MB", "LADA", "KIA", "HONDA"]
cars_count = 0
for i in range(len(cars)):
    print("Я езжу на автомобиле марки ", cars[i])
    cars_count += 10
    print("Счетчик автомобилей: ",cars_count)
print("Всего автомобилей: ", cars_count)
